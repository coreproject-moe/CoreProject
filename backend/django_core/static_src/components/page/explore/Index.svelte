<script lang="ts">
    import * as _ from "lodash-es";
    import { cn } from "$functions/classname";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import MoreBox from "$icons/MoreBox/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Chevron from "$icons/Chevron/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Expand from "$icons/Expand/Index.svelte";
    import SixGrids from "$icons/SixGrids/Index.svelte";
    import { scale } from "svelte/transition";
    import { FormatDate } from "$functions/format_date";
    import HoverExpand from "$components/minor/HoverExpand/Index.svelte";
    import AnimeCard from "./AnimeCard.svelte";
    import { string_to_boolean } from "$functions/string_to_bool";
    import { reverse } from "$functions/urls";
    import { Anime } from "../../../types/anime";
    import { onMount } from "svelte";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";

    // Binding
    let result_animes_element: HTMLDivElement;
    let search_query = "",
        active_filters: Array<string> = [],
        thumbnail_mode: "card_with_dropdown" | "detailed_card" = "card_with_dropdown";

    let search_promise: Promise<Anime[]> | null = null;

    onMount(async () => {
        search_promise = get_anime_with_serach_parameters();
    });

    // Mapping
    let filter_options_mapping: {
        [key: string]: {
            title: string;
            class: string;
            value: string;
            items: Array<string | number>;
            selected_items: string[] | null;
        };
    } = {
        time_range: {
            title: "Time Range",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            items: [],
            selected_items: []
        },
        genres: {
            title: "Genres",
            class: "md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: ["action", "adventure", "hentai", "romance"],
            selected_items: []
        },
        year: {
            title: "Year",
            class: "hidden md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: [2020, 2021, 2022, 2023],
            selected_items: []
        },
        season: {
            title: "Season",
            class: "md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: ["winter", "spring", "summer", "fall"],
            selected_items: []
        },
        format: {
            title: "Format",
            class: "hidden md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: ["tv show", "movie"],
            selected_items: []
        },
        airing_status: {
            title: "Airing Status",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            items: [],
            selected_items: []
        },
        sort_by: {
            title: "Sort by",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            items: [],
            selected_items: []
        }
    };

    // Functions
    const handle_input = async () => {
            search_promise = get_anime_with_serach_parameters();
        },
        update_selected_items = (key: string, selected_item: string) => {
            let filter_option = filter_options_mapping[key];
            let is_selected = filter_option.selected_items!.some((item) => item === selected_item);

            if (is_selected) {
                // if selected: remove from seleted list
                filter_option.selected_items = filter_option.selected_items!.filter((item) => item !== selected_item);
                // remove from active filters
                active_filters = active_filters.filter((filter) => filter !== selected_item);
            } else {
                // else: add to selected list
                filter_option.selected_items = [...filter_option.selected_items!, selected_item];
                // add to active filters
                active_filters = [...active_filters, selected_item];
            }

            // update filer_options_mapping
            filter_options_mapping[key] = filter_option;
            // run fetch
            handle_input();
        },
        clear_selected_items = (key: string) => {
            filter_options_mapping[key].selected_items = [];
            // run fetch
            handle_input();
        },
        change_thumbnail_mode = (mode: typeof thumbnail_mode) => {
            thumbnail_mode = mode;
        };

    const get_anime_with_serach_parameters = async (): Promise<Anime[]> => {
        let url = new URL(window.location.protocol + "//" + window.location.hostname + ":" + window.location.port + reverse(`anime-list`));

        const search_map = {
            name: search_query,
            genres: filter_options_mapping["genres"].selected_items
                ?.map((item) => {
                    return item.toLowerCase();
                })
                .join()
        };
        for (const [key, val] of Object.entries(search_map)) {
            if (!_.isEmpty(val) && !_.isUndefined(val)) {
                url.searchParams.set(key, val);
            }
        }

        const res = await fetch(url, {
            method: "GET",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": get_csrf_token()
            },
            signal: AbortSignal.timeout(FETCH_TIMEOUT)
        });
        const json = await res.json();

        if (res.ok) {
            return _.uniqBy(json["results"], "mal_id") as Array<Anime>;
        } else {
            throw new Error("Something is wrong from the backend");
        }
    };
</script>

<section class="mt-20 flex flex-col p-5 md:mt-0 md:gap-[1.5vw] md:pb-[2.5vw] md:pl-[1.5vw] md:pr-[3.75vw] md:pt-0">
    <div class="flex flex-col gap-2 md:gap-[0.5vw]">
        <div class="text-3xl font-bold leading-none md:text-[2vw]">
            Anime <span class="text-warning">Explore</span>
        </div>
        <span class="text-base font-normal leading-none md:text-[1.1vw]">Unleash your inner Otaku: Explore anime wonders</span>
    </div>

    <div class="mt-7 flex flex-col gap-1 md:hidden">
        <span class="text-base font-semibold leading-none">Search Animes</span>
        <div class="relative flex items-center">
            <Search class="pointer-events-none absolute ml-4 w-4" />
            <input
                type="text"
                placeholder="Looking for specific anime? Start from here..."
                class="w-full rounded-lg border-none bg-neutral py-3 pl-12 leading-none focus:ring-0 md:bg-neutral"
            />
        </div>
    </div>

    <div class="mt-2 flex items-end justify-between gap-3 md:mt-0 md:gap-0">
        <div class="flex items-center gap-3 md:gap-[1.5vw]">
            <div class="hidden flex-col gap-[0.35vw] md:flex">
                <span class="text-[1vw] font-semibold leading-none">Search Animes</span>
                <div class="relative flex items-center">
                    <div class="absolute md:ml-[1vw]">
                        <Search class="md:w-[1.1vw]" />
                    </div>
                    <input
                        bind:value={search_query}
                        on:input={handle_input}
                        type="text"
                        placeholder="Looking for specific anime? Start from here..."
                        class="w-[30vw] rounded-[0.5vw] border-none bg-neutral py-[0.8vw] pl-[3vw] text-[1vw] font-semibold leading-none text-neutral-content placeholder:font-medium placeholder:text-neutral-content/75 focus:ring-0 md:bg-neutral"
                    />
                </div>
            </div>
            {#each Object.entries(filter_options_mapping) as option}
                {@const title = option[1].title}
                {@const klass = option[1].class}
                {@const selected_items = option[1].selected_items}
                {@const filter_items = option[1].items}

                <div class={cn(klass, "group dropdown dropdown-bottom")}>
                    <span class="font-semibold leading-none md:text-[1vw]">{title}</span>
                    <div class="relative flex items-center">
                        <span class="absolute flex cursor-pointer items-center md:gap-[0.25vw]">
                            {#if selected_items}
                                {#if !_.isEmpty(selected_items)}
                                    <span class="badge badge-primary ml-3 rounded p-1 text-sm font-semibold capitalize md:ml-[0.75vw] md:h-[1.5vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
                                        <!-- show first item -->
                                        {selected_items[0]}
                                    </span>
                                {:else}
                                    <span class="ml-3 text-base duration-300 group-focus-within:opacity-0 md:ml-[1vw] md:text-[0.9vw]">Any</span>
                                {/if}
                                <!-- show count of remaining items if exists -->
                                {#if selected_items.length > 1}
                                    <span class="badge ml-1 rounded p-1 text-sm font-semibold md:ml-[0.15vw] md:h-[1.5vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
                                        +{selected_items.filter((item) => item !== selected_items[0]).length}
                                    </span>
                                {/if}
                            {/if}
                        </span>
                        <input
                            bind:value={option[1].value}
                            on:blur={() => (option[1].value = "")}
                            type="text"
                            tabindex="0"
                            role="button"
                            class="peer placeholder w-full rounded-lg border-none bg-neutral py-3 text-base font-semibold leading-none text-neutral-content placeholder:font-medium focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:bg-neutral md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                        />
                        {#if selected_items}
                            {#if !_.isEmpty(selected_items)}
                                <button
                                    on:click|preventDefault={() => clear_selected_items(option[0])}
                                    class="btn absolute right-0 mr-3 w-4 border-none !bg-transparent p-0 md:mr-[1vw] md:w-[1vw]"
                                >
                                    <Cross class="md:w-[1vw]" />
                                </button>
                            {/if}
                        {:else}
                            <button class="btn absolute right-0 mr-3 w-4 border-none !bg-transparent p-0 md:mr-[1vw] md:w-[1vw]">
                                <Chevron class="md:w-[1vw]" />
                            </button>
                        {/if}
                    </div>

                    {#if filter_items}
                        <div class="dropdown-content z-10 mt-2 w-full overflow-x-hidden rounded-lg md:mt-[1vw] md:rounded-[0.5vw]">
                            <ScrollArea
                                gradient_mask={false}
                                class="flex w-full flex-col md:p-[0.35vw]"
                                parent_class="md:max-h-[30vw] bg-neutral w-full"
                            >
                                {#each Object.entries(filter_items) as [key, value]}
                                    {@const is_selected = selected_items?.some((item) => item === value)}

                                    <button
                                        on:click|preventDefault={() => {
                                            const val = String(value);
                                            update_selected_items(option[0], val);
                                        }}
                                        class="btn btn-neutral relative flex h-max min-h-max items-center justify-start rounded-none p-3 py-3 text-sm leading-none md:rounded-[0.35vw] md:px-[1vw] md:py-[0.75vw] md:text-[0.9vw]"
                                    >
                                        <span class="capitalize">{value}</span>

                                        {#if is_selected}
                                            <div class="absolute right-3 rounded-full bg-primary p-1 text-white md:right-[0.75vw] md:p-[0.25vw]">
                                                <Tick class="w-2 text-white md:w-[0.75vw]" />
                                            </div>
                                        {/if}
                                    </button>
                                {/each}
                            </ScrollArea>
                        </div>
                    {/if}
                </div>
            {/each}
        </div>

        <button class="btn btn-neutral h-max min-h-max rounded-lg p-[0.85rem] md:rounded-[0.5vw] md:p-[0.8vw]">
            <MoreBox class="w-4 md:w-[1.1vw]" />
        </button>
    </div>

    <div class="mt-16 md:mt-[1.5vw]">
        <div class="flex items-center justify-between">
            <div class="flex flex-col gap-2 md:gap-[0.35vw]">
                <span class="text-xl font-semibold leading-none text-accent md:text-[1.35vw]">Trending Now</span>
                <span class="text-sm leading-none md:text-[1vw]">Crowd Favorites: Anime Hits and Hype</span>
            </div>
            <div class="flex gap-3 md:gap-[1vw]">
                <button class="btn h-max min-h-max border-none !bg-transparent p-0">
                    <Expand class="w-5 md:w-[1.25vw]" />
                    <span class="font-semibold md:text-[1vw]">Trending</span>
                </button>
                <div class="divider divider-horizontal m-0"></div>
                <button
                    class="btn h-max min-h-max border-none !bg-transparent p-0"
                    on:click={() => change_thumbnail_mode("card_with_dropdown")}
                >
                    <SixGrids class="w-5 md:w-[1.15vw]" />
                </button>
                <button
                    class="btn h-max min-h-max border-none !bg-transparent p-0"
                    on:click={() => change_thumbnail_mode("detailed_card")}
                >
                    <MoreBox class="w-[1.1rem] md:w-[1vw]" />
                </button>
            </div>
        </div>

        {#if search_promise}
            {#await search_promise}
                <div class="grid h-full place-items-center">
                    <span class="loading loading-ring loading-lg"></span>
                </div>
            {:then results}
                {#if !_.isEmpty(results)}
                    {#if thumbnail_mode === "detailed_card"}
                        <div
                            bind:this={result_animes_element}
                            class="mt-5 grid grid-cols-2 gap-3 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1.5vw]"
                        >
                            {#each results as anime}
                                <a
                                    in:scale={{ start: 0.95 }}
                                    href="/mal/{anime.mal_id}"
                                    class="relative col-span-1 grid grid-cols-1 md:grid-cols-2"
                                >
                                    <div class="relative">
                                        <img
                                            src={anime.cover}
                                            alt={anime.name}
                                            class="h-44 w-full rounded-t-lg object-cover object-center md:h-[20vw] md:rounded-l-[0.35vw] md:rounded-r-none"
                                        />
                                        <div class="absolute inset-x-0 bottom-0 rounded-b-lg backdrop-blur md:rounded-l-[0.35vw]">
                                            <div class="flex w-full flex-col bg-secondary/95 p-3 md:gap-[0.35vw] md:p-[1vw]">
                                                <HoverExpand
                                                    class="w-full text-sm font-semibold text-accent md:text-[1vw] md:leading-[1.35vw]"
                                                    height="md:max-h-[1.35vw] md:hover:max-h-[10vw]"
                                                >
                                                    {anime.name}
                                                </HoverExpand>
                                                <span class="line-clamp-1 text-xs md:line-clamp-none md:text-[0.8vw]">
                                                    {anime?.studios?.[0].name ?? ""}
                                                </span>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="rounded-rt-none flex flex-col justify-between rounded-b-lg bg-neutral/25 md:rounded-l-none md:rounded-r-[0.35vw]">
                                        <div class="flex flex-col gap-1 p-3 leading-none md:gap-[0.5vw] md:p-[1vw]">
                                            <span class="text-xs font-semibold capitalize md:text-[1vw]">
                                                {new FormatDate(anime.aired_from ?? "").format_to_season}
                                            </span>
                                            <div class="flex items-center gap-1 md:gap-[0.5vw]">
                                                <span class="text-xs md:text-[0.8vw]">{anime.source}</span>
                                                <Circle class="w-1 opacity-50 md:w-[0.25vw]" />
                                                <span class="text-xs md:text-[0.8vw]">{anime.episode_count} eps</span>
                                            </div>
                                            <ScrollArea
                                                offset_scrollbar
                                                gradient_mask
                                                parent_class="max-h-12 md:max-h-[11vw] md:mt-[0.5vw]"
                                                class="text-surface-300 text-xs leading-snug md:text-justify md:text-[0.85vw] md:leading-[1vw]"
                                            >
                                                {anime.synopsis}
                                            </ScrollArea>
                                        </div>

                                        <div class="flex items-center gap-2 overflow-x-scroll p-3 pt-0 scrollbar-none md:gap-[0.5vw] md:p-[1vw]">
                                            {#each anime?.genres ?? [] as genre}
                                                <span
                                                    class="whitespace-nowrap rounded-sm bg-warning p-1 text-xs font-semibold capitalize leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]"
                                                >
                                                    {genre.name}
                                                </span>
                                            {/each}
                                        </div>
                                    </div>
                                </a>
                            {/each}
                        </div>
                    {:else if thumbnail_mode === "card_with_dropdown"}
                        <div
                            class="mt-5 grid grid-cols-3 gap-3 md:mt-[1.25vw] md:grid-cols-6 md:gap-[1.5vw]"
                            bind:this={result_animes_element}
                        >
                            {#each results as item}
                                <AnimeCard
                                    anime_mal_id={item?.mal_id ?? 0}
                                    anime_name={item.name ?? "N/A"}
                                    anime_studios={item.studios ?? []}
                                    anime_image={item.cover ?? ""}
                                    anime_genres={item.genres ?? []}
                                    anime_synopsis={item.synopsis ?? ""}
                                    anime_total_episodes={item.episode_count ?? null}
                                    anime_rating={item.rating ?? "N/A"}
                                />
                            {/each}
                        </div>
                    {/if}
                {:else}
                    <div class="flex h-full flex-col items-center justify-center gap-[0.5vw] text-[1.1vw]">
                        <span class="font-medium leading-none">No match found!</span>
                        <span class="text-center font-semibold leading-none text-error">
                            Couldn't find animes with: "{search_query}"
                            <br />
                            <span class="text-accent/75">Filters: {active_filters.join(" - ")}</span>
                        </span>
                    </div>
                {/if}
            {:catch error}
                <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                    <span class="font-medium leading-none">Oh no, something is wrong!</span>
                    <span class="text-center font-semibold leading-none text-error">{@html error}</span>
                </div>
            {/await}
        {/if}
    </div>
</section>
