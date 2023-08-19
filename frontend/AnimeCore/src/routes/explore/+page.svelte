<script lang="ts">
    import { OpengraphGenerator } from "$functions/opengraph";
    import { page } from "$app/stores";
    import Search from "$icons/search.svelte";
    import Chevron from "$icons/chevron.svelte";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import MoreBox from "$icons/more_box.svelte";
    import { trending_animes } from "$data/mock/trending";
    import tippy from "tippy.js";
    import Caption from "$icons/caption.svelte";
    import Mic from "$icons/mic.svelte";
    import FilterOptions from "$components/tippies/filter_options.svelte";
    import Cross from "$icons/cross.svelte";
    import { FormatDate } from "$functions/format_date";
    import Circle from "$icons/circle.svelte";
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import AnimeCard from "$components/tippies/anime_card.svelte";
    import Expand from "$icons/expand.svelte";
    import SixGrids from "$icons/six_grids.svelte";
    import { scale } from "svelte/transition";

    let filter_options_mapping: {
        [key: string]: {
            title: string;
            class: string;
            value: string;
            items?: Record<string, string> | undefined;
            selected_items: Array<[string, string]>;
        };
    } = {
        time_range: {
            title: "Time Range",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            selected_items: []
        },
        genres: {
            title: "Genres",
            class: "md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: {
                action: "Action",
                adventure: "Adventure",
                hentai: "Hentai",
                romance: "Romance"
            },
            selected_items: []
        },
        year: {
            title: "Year",
            class: "md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: {
                2023: "2023",
                2022: "2022",
                2021: "2021",
                2020: "2020"
            },
            selected_items: []
        },
        season: {
            title: "Season",
            class: "md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: {
                winter: "Winter",
                spring: "Spring",
                summer: "Summer",
                fall: "Fall"
            },
            selected_items: []
        },
        format: {
            title: "Format",
            class: "hidden md:flex flex-col md:gap-[0.35vw]",
            value: "",
            items: {
                tv_show: "TV Show",
                movie: "Movie"
            },
            selected_items: []
        },
        airing_status: {
            title: "Airing Status",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            selected_items: []
        },
        sort_by: {
            title: "Sort by",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            selected_items: []
        }
    };

    function update_selected_items(key: string, selected_item: [string, string]) {
        let filter_option = filter_options_mapping[key];
        let is_selected = filter_option.selected_items?.some((item) => item[0] === selected_item[0]);

        if (is_selected) {
            filter_option.selected_items = filter_option.selected_items?.filter((item) => item[0] !== selected_item[0]);
        } else {
            filter_option.selected_items = [...filter_option.selected_items, selected_item];
        }

        // update filer_options_mapping
        filter_options_mapping[key] = filter_option;
    }

    function clear_selected_items(key: string) {
        // update filter_options_mapping
        filter_options_mapping[key].selected_items = [];
    }

    /* Thumbnail modes */
    let thumbnail_mode: "card_with_tippy" | "detailed_card" = "detailed_card";

    function change_thumbnail_mode(mode: typeof thumbnail_mode) {
        thumbnail_mode = mode;
    }

    const opengraph_html = new OpengraphGenerator({
        title: "Explore the Anime Universe: Your Gateway to Otaku Delights!",
        site_name: "CoreProject",
        image_url: "", // Use Opengraph later
        url: $page.url.href,
        locale: "en_US",
        description: "The most modern anime streaming site"
    }).generate_opengraph();
</script>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

<section class="mt-20 flex flex-col p-5 md:mt-0 md:gap-[1.5vw] md:pb-[2.5vw] md:pl-[1.5vw] md:pr-[3.75vw] md:pt-0">
    <section-headings class="flex flex-col gap-2 md:gap-[0.5vw]">
        <span class="text-2xl font-bold leading-none md:text-[2vw]">
            Anime <span class="text-warning-400">Explore</span>
        </span>
        <span class="text-base font-normal leading-none text-surface-50 md:text-[1.1vw]">Unleash your inner Otaku: Explore anime wonders</span>
    </section-headings>

    <search class="mt-10 flex flex-col gap-1 md:hidden">
        <span class="text-base font-semibold leading-none text-surface-50">Search Animes</span>
        <div class="relative flex items-center">
            <Search class="pointer-events-none absolute ml-4 w-4 text-surface-300" />
            <input
                type="text"
                placeholder="Looking for specific anime? Start from here..."
                class="w-full rounded-lg border-none bg-surface-400 py-3 pl-12 leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:bg-surface-400/75"
            />
        </div>
    </search>
    <filter-options class="mt-3 flex items-end justify-between gap-3 md:mt-0 md:gap-0">
        <div class="flex items-center gap-3 md:gap-[1.5vw]">
            <search class="hidden flex-col gap-[0.35vw] md:flex">
                <span class="text-[1vw] font-semibold leading-none text-surface-50">Search Animes</span>
                <div class="relative flex items-center">
                    <Search class="pointer-events-none absolute ml-[1vw] w-[1vw] text-surface-300" />
                    <input
                        type="text"
                        placeholder="Looking for specific anime? Start from here..."
                        class="w-[30vw] rounded-[0.5vw] border-none bg-surface-400 py-[0.8vw] pl-[3vw] text-[1vw] leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:bg-surface-400/75"
                    />
                </div>
            </search>
            {#each Object.entries(filter_options_mapping) as option, index}
                {@const title = option[1].title}
                {@const klass = option[1].class}
                {@const selected_items = option[1].selected_items}
                {@const filter_items = option[1].items}

                <div
                    class="{klass} group"
                    use:tippy={{
                        trigger: "click",
                        arrow: false,
                        allowHTML: true,
                        placement: "bottom",
                        animation: "shift-away",
                        duration: [150, 150],
                        interactive: true,
                        appendTo: document.body,
                        onTrigger: async (instance) => {
                            const node = document.createElement("div");
                            const FilterOptionsComponent = new FilterOptions({
                                target: node,
                                props: {
                                    items: filter_items,
                                    selected_items: selected_items
                                }
                            });
                            // dispathced event from component
                            FilterOptionsComponent.$on("select", (e) => {
                                update_selected_items(option[0], e.detail);
                                // hide tippy
                                instance.hide();
                            });

                            instance.setContent(node);
                        }
                    }}
                >
                    <span class="font-semibold leading-none text-surface-50 md:text-[1vw]">{title}</span>
                    <div class="relative flex items-center">
                        <span class="absolute cursor-pointer text-surface-50 opacity-100 duration-300 group-focus-within:opacity-0">
                            {#if selected_items.length > 0}
                                <span class="ml-3 rounded bg-primary-500 p-1 text-sm font-semibold md:ml-[0.75vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
                                    <!-- show first item -->
                                    {selected_items[0][1]}
                                </span>
                                <!-- show count of remaining items if exists -->
                                {#if selected_items.length > 1}
                                    <span class="ml-1 rounded bg-primary-500/50 p-1 text-sm font-semibold md:ml-[0.15vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
                                        +{selected_items.filter((item) => item !== selected_items[0]).length}
                                    </span>
                                {/if}
                            {:else}
                                <span class="ml-3 text-base md:ml-[1vw] md:text-[0.9vw]">Any</span>
                            {/if}
                        </span>
                        <input
                            bind:value={option[1].value}
                            on:blur={() => (option[1].value = "")}
                            type="text"
                            class="peer w-full rounded-lg border-none bg-surface-400 py-3 text-base leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:bg-surface-400/75 md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                        />
                        {#if selected_items.length > 0}
                            <button
                                on:click={() => clear_selected_items(option[0])}
                                class="btn absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]"
                            >
                                <Cross class="text-surface-300" />
                            </button>
                        {:else}
                            <button class="btn absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]">
                                <Chevron class="text-surface-300" />
                            </button>
                        {/if}
                    </div>
                </div>
            {/each}
        </div>

        <more-filter-option>
            <button class="btn rounded-lg bg-surface-400 p-[0.85rem] md:rounded-[0.5vw] md:bg-surface-400/75 md:p-[0.9vw]">
                <MoreBox class="w-4 text-surface-50 md:w-[1vw]" />
            </button>
        </more-filter-option>
    </filter-options>

    <div class="mt-16 md:mt-[1.5vw]">
        <div class="flex items-center justify-between">
            <headings class="flex flex-col gap-2 md:gap-[0.35vw]">
                <span class="text-xl font-semibold leading-none md:text-[1.35vw]">Trending Now</span>
                <span class="text-base leading-none text-surface-50 md:text-[1vw]">Crowd Favorites: Anime Hits and Hype</span>
            </headings>
            <div class="flex md:gap-[1vw]">
                <button class="btn p-0 text-surface-50">
                    <Expand class="md:w-[1.25vw]" />
                    <span class="font-semibold md:text-[1vw]">Trending</span>
                </button>
                <span class="divider-vertical h-[2vw] !border-surface-50/25" />
                <button
                    class="btn p-0 text-surface-50"
                    on:click={() => change_thumbnail_mode("card_with_tippy")}
                >
                    <SixGrids class="md:w-[1.15vw]" />
                </button>
                <button
                    class="btn p-0 text-surface-50"
                    on:click={() => change_thumbnail_mode("detailed_card")}
                >
                    <MoreBox class="md:w-[1vw]" />
                </button>
            </div>
        </div>

        {#if thumbnail_mode === "detailed_card"}
            <result-animes class="mt-5 grid grid-cols-3 gap-3 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1.5vw]">
                {#each trending_animes as anime}
                    <a
                        in:scale={{ start: 0.95 }}
                        href="/mal/{anime.id}"
                        class="relative col-span-1 grid grid-cols-2"
                    >
                        <div class="relative">
                            <ImageLoader
                                src={anime.cover}
                                alt={anime.name}
                                class="h-52 w-full rounded-l-lg object-cover object-center md:h-[20vw] md:rounded-l-[0.35vw]"
                            />
                            <anime-info class="absolute inset-x-0 bottom-0 rounded-l-lg backdrop-blur md:rounded-l-[0.35vw]">
                                <div class="flex flex-col bg-surface-900/90 p-[1vw] md:gap-[0.35vw]">
                                    <ScrollArea class="flex max-h-[1.5vw] overflow-hidden font-semibold duration-300 ease-in-out scrollbar-none hover:max-h-[10vw] hover:overflow-y-scroll md:text-[1vw] md:leading-[1.35vw]">
                                        {anime.name}
                                    </ScrollArea>
                                    <studio-name class="text-surface-50 md:text-[0.8vw]">
                                        {anime.studios}
                                    </studio-name>
                                </div>
                            </anime-info>
                        </div>

                        <anime-details class="flex flex-col justify-between rounded-r-lg bg-surface-400/25 md:rounded-r-[0.35vw]">
                            <div class="flex flex-col gap-2 leading-none text-surface-50 md:gap-[0.5vw] md:p-[1vw]">
                                <release-time class="font-semibold capitalize md:text-[1vw]">
                                    {new FormatDate(anime.release_date).format_to_season}
                                </release-time>
                                <div class="flex items-center md:gap-[0.5vw]">
                                    <type class="md:text-[0.8vw]">{anime.type}</type>
                                    <Circle class="opacity-50 md:w-[0.25vw]" />
                                    <episodes class="md:text-[0.8vw]">{anime.episodes_count} episodes</episodes>
                                </div>
                                <ScrollArea
                                    offsetScrollbar
                                    parentClass="md:max-h-[11vw] md:mt-[0.5vw]"
                                    class="text-justify text-surface-300 md:text-[0.85vw] md:leading-[1vw]"
                                >
                                    {anime.synopsis}
                                </ScrollArea>
                            </div>

                            <genres class="flex items-center md:gap-[0.5vw] md:p-[1vw]">
                                {#each anime.genres as genre}
                                    <genre class="bg-warning-400 font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">
                                        {genre}
                                    </genre>
                                {/each}
                            </genres>
                        </anime-details>
                    </a>
                {/each}
            </result-animes>
        {:else if thumbnail_mode === "card_with_tippy"}
            <result-animes class="mt-5 grid grid-cols-3 gap-3 md:mt-[1.25vw] md:grid-cols-6 md:gap-[1.5vw]">
                {#each trending_animes as anime}
                    <a
                        in:scale={{ start: 0.95 }}
                        href="/mal/{anime.id}"
                        class="relative col-span-1 flex flex-col gap-2 md:gap-[0.5vw]"
                    >
                        <div
                            class="relative"
                            use:tippy={{
                                arrow: false,
                                allowHTML: true,
                                placement: "right-start",
                                animation: "scale",
                                duration: [150, 10],
                                interactive: true,
                                appendTo: document.body,
                                onTrigger: async (instance) => {
                                    const node = document.createElement("div");
                                    new AnimeCard({
                                        target: node,
                                        props: {
                                            anime_id: anime.id,
                                            anime_name: anime.name,
                                            anime_type: anime.type,
                                            anime_genres: anime.genres,
                                            anime_studios: anime.studios,
                                            anime_episodes_count: anime.episodes_count,
                                            anime_synopsis: anime.synopsis,
                                            anime_release_date: anime.release_date
                                        }
                                    });

                                    instance.setContent(node);
                                }
                            }}
                        >
                            <ImageLoader
                                src={anime.cover}
                                alt={anime.name}
                                class="h-52 w-full rounded-md object-cover object-center md:h-[20vw] md:rounded-[0.35vw]"
                            />
                            <overlay class="absolute inset-0 flex items-end bg-gradient-to-t from-surface-900/75 to-transparent p-2 leading-none md:p-[0.5vw]">
                                <div class="flex gap-1 overflow-hidden rounded md:gap-[0.2vw] md:rounded-[0.3vw]">
                                    <subs class="flex items-center gap-1 bg-warning-400 p-1 text-black md:gap-[0.25vw] md:px-[0.35vw] md:py-[0.25vw]">
                                        <Caption class="h-4 md:h-[1.25vw]" />
                                        <span class="text-xs font-semibold md:text-[0.8vw]">{anime.episodes_count}</span>
                                    </subs>
                                    <dubs class="flex items-center gap-1 bg-white/25 p-1 backdrop-blur md:gap-[0.25vw] md:px-[0.45vw] md:py-[0.25vw]">
                                        <Mic class="h-3 md:h-[0.8vw]" />
                                        <span class="text-xs font-semibold md:text-[0.8vw]">{anime.episodes_count}</span>
                                    </dubs>
                                </div>
                            </overlay>
                        </div>

                        <anime-details class="flex flex-col gap-2 text-surface-50 md:gap-[0.5vw]">
                            <anime_name class="line-clamp-1 text-xs font-semibold leading-none md:text-[1vw]">
                                {anime.name}
                            </anime_name>
                            <anime_info class="flex items-center gap-2 text-xs leading-none text-surface-50 md:gap-[0.5vw] md:text-[0.9vw]">
                                <genre>{anime.genres[0]}</genre>
                                <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                <episodes_count>{anime.episodes_count} eps</episodes_count>
                            </anime_info>
                        </anime-details>
                    </a>
                {/each}
            </result-animes>
        {/if}
    </div>
</section>
