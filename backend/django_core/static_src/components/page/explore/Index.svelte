<script lang="ts">
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

    // Mock
    const trending_animes = [
        {
            id: 1,
            name: "One piece",
            cover: "https://i.pinimg.com/originals/04/65/2b/04652b44ea7c1275d1022d98d59ecc97.jpg",
            synopsis: `Azur Lane, a combination of all the different Camps in the world, was once successful in repelling the underwater menace, the Siren. Now splintered, they must face a new threat in Red Axis, former allies who crave to wield this otherworldly Siren technology for their own nefarious desires! Who will be victorious in the never-ending war between these battleship girls!? Akagami no Shirayuki-hime depicts Shirayuki's journey toward a new life at the royal palace of Clarines, as well as Zen's endeavor to become a prince worthy of his title. As loyal friendships are forged and deadly enemies formed, Shirayuki and Zen slowly learn to support each other as they walk their own paths.`,
            current_episode: 4,
            episodes_count: 1071,
            genres: ["Action", "Ecchi", "sci-Fi"],
            type: "TV",
            release_date: "2023-04-22T10:30:00.000Z",
            studios: ["Bibury Animation Studios"]
        },
    ];

    // Binding
    let result_animes_element: HTMLDivElement;

    // Mapping
    let filter_options_mapping: {
        [key: string]: {
            title: string;
            class: string;
            value: string;
            items: Record<string, string> | null;
            selected_items: Array<[string, string]> | null;
        };
    } = {
        time_range: {
            title: "Time Range",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            items: {},
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
            items: {},
            selected_items: []
        },
        sort_by: {
            title: "Sort by",
            class: "hidden flex-col md:gap-[0.35vw]",
            value: "",
            items: {},
            selected_items: []
        }
    };

    // Functions
    const update_selected_items = (key: string, selected_item: [string, string]) => {
        let filter_option = filter_options_mapping[key];
        let is_selected = filter_option.selected_items!.some((item) => item[0] === selected_item[0]);

        if (is_selected) {
            filter_option.selected_items = filter_option.selected_items!.filter((item) => item[0] !== selected_item[0]);
        } else {
            filter_option.selected_items = [...filter_option.selected_items!, selected_item];
        }

        // update filer_options_mapping
        filter_options_mapping[key] = filter_option;
    },
    clear_selected_items = (key: string) => {
        // update filter_options_mapping
        filter_options_mapping[key].selected_items = [];
    },
    change_thumbnail_mode = (mode: typeof thumbnail_mode) => {
        thumbnail_mode = mode;
    };

    // Thumbnail modes
    let thumbnail_mode: "card_with_dropdown" | "detailed_card" = "card_with_dropdown";
</script>

<section class="mt-20 flex flex-col p-5 md:mt-0 md:gap-[1.5vw] md:pb-[2.5vw] md:pl-[1.5vw] md:pr-[3.75vw] md:pt-0">
    <div class="flex flex-col gap-2 md:gap-[0.5vw]">
        <div class="text-2xl font-bold leading-none md:text-[2vw]">
            Anime <span class="text-warning">Explore</span>
        </div>
        <span class="text-base font-normal leading-none md:text-[1.1vw]">Unleash your inner Otaku: Explore anime wonders</span>
    </div>

    <div class="mt-10 flex flex-col gap-1 md:hidden">
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

    <div class="mt-3 flex items-end justify-between gap-3 md:mt-0 md:gap-0">
        <div class="flex items-center gap-3 md:gap-[1.5vw]">
            <div class="hidden flex-col gap-[0.35vw] md:flex">
                <span class="text-[1vw] font-semibold leading-none">Search Animes</span>
                <div class="relative flex items-center">
                    <div class="absolute md:ml-[1vw]">
                        <Search class="md:w-[1.1vw]" />
                    </div>
                    <input
                        type="text"
                        placeholder="Looking for specific anime? Start from here..."
                        class="w-[30vw] rounded-[0.5vw] border-none bg-neutral py-[0.8vw] pl-[3vw] text-[1vw] leading-none focus:ring-0 md:bg-neutral text-neutral-content font-semibold placeholder:text-neutral-content/75 placeholder:font-medium"
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
                        <span class="absolute flex items-center md:gap-[0.25vw] cursor-pointer">
                            {#if selected_items}
                                {#if selected_items.length > 0}
                                    <span class="ml-3 badge badge-primary rounded p-1 text-sm font-semibold md:ml-[0.75vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw] md:h-[1.5vw]">
                                        <!-- show first item -->
                                        {selected_items[0][1]}
                                    </span>
                                {:else}
                                    <span class="ml-3 text-base md:ml-[1vw] md:text-[0.9vw] group-focus-within:opacity-0 duration-300">Any</span>
                                {/if}
                                <!-- show count of remaining items if exists -->
                                {#if selected_items.length > 1}
                                    <span class="ml-1 rounded badge md:h-[1.5vw] p-1 text-sm font-semibold md:ml-[0.15vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
                                        +{selected_items.filter((item) => item !== selected_items[0]).length}
                                    </span>
                                {/if}
                            {/if}
                        </span>
                        <input
                            bind:value={option[1].value}
                            on:blur={() => (option[1].value = "")}
                            type="text"
                            tabindex="0" role="button"
                            class="peer w-full rounded-lg border-none bg-neutral py-3 text-base leading-none placeholder focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:bg-neutral text-neutral-content md:py-[0.8vw] md:pl-[1vw] md:text-[1vw] placeholder:font-medium font-semibold"
                        />
                        {#if selected_items}
                            {#if selected_items.length > 0}
                                <button
                                    on:click|preventDefault={() => clear_selected_items(option[0])}
                                    class="btn !bg-transparent border-none absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]"
                                >
                                    <Cross class="md:w-[1vw]" />
                                </button>
                            {/if}
                        {:else}
                            <button class="btn !bg-transparent border-none absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]">
                                <Chevron class="md:w-[1vw]" />
                            </button>
                        {/if}
                    </div>
                    <button
                        tabindex="0"
                        class="dropdown-content z-10 md:mt-[1vw] w-[8.5rem] rounded-lg md:w-[11vw] md:rounded-[0.5vw] overflow-x-hidden"
                    >
                        {#if filter_items}
                            <ScrollArea
                                class="md:p-[0.35vw] flex flex-col w-full"
                                parent_class="md:max-h-[30vw] bg-neutral w-full"
                            >
                                {#each Object.entries(filter_items) as item}
                                    {@const key = item[0]}
                                    {@const value = item[1]}

                                    {@const is_selected = selected_items?.some(selected_item => selected_item[0] === key)}

                                    <button
                                        on:click|preventDefault={() => update_selected_items(option[0], item)}
                                        class="relative btn btn-neutral h-max min-h-max leading-none flex items-center justify-start md:rounded-[0.35vw] p-3 text-sm md:px-[1vw] md:py-[0.75vw] md:text-[0.9vw]">
                                        {value}

                                        {#if is_selected}
                                            <div class="absolute right-[0.75vw] rounded-full bg-primary text-white p-1 md:p-[0.25vw]">
                                                <Tick class="w-2 md:w-[0.75vw] text-white" />
                                            </div>
                                        {/if}
                                    </button>
                                {/each}
                            </ScrollArea>
                        {/if}
                    </button>
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
                <span class="text-xl font-semibold text-accent leading-none md:text-[1.35vw]">Trending Now</span>
                <span class="text-base leading-none md:text-[1vw]">Crowd Favorites: Anime Hits and Hype</span>
            </div>
            <div class="flex gap-3 md:gap-[1vw]">
                <button class="btn p-0 !bg-transparent border-none min-h-max h-max">
                    <Expand class="w-5 md:w-[1.25vw]" />
                    <span class="font-semibold md:text-[1vw]">Trending</span>
                </button>
                <div class="divider divider-horizontal"></div>
                <button
                    class="btn p-0 !bg-transparent border-none min-h-max h-max"
                    on:click={() => change_thumbnail_mode("card_with_dropdown")}
                >
                    <SixGrids class="w-5 md:w-[1.15vw]" />
                </button>
                <button
                    class="btn p-0 !bg-transparent border-none min-h-max h-max"
                    on:click={() => change_thumbnail_mode("detailed_card")}
                >
                    <MoreBox class="w-[1.1rem] md:w-[1vw]" />
                </button>
            </div>
        </div>

        {#if thumbnail_mode === "detailed_card"}
            <div
                bind:this={result_animes_element}
                class="mt-5 grid grid-cols-2 gap-3 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1.5vw]"
            >
                {#each trending_animes as anime}
                    <a
                        in:scale={{ start: 0.95 }}
                        href="/mal/{anime.id}"
                        class="relative col-span-1 grid grid-cols-1 md:grid-cols-2"
                    >
                        <div class="relative">
                            <img
                                src={anime.cover}
                                alt={anime.name}
                                class="h-56 w-full rounded-t-lg object-cover object-center md:h-[20vw] md:rounded-l-[0.35vw] md:rounded-r-none"
                            />
                            <anime-info class="absolute inset-x-0 bottom-0 rounded-b-lg backdrop-blur md:rounded-l-[0.35vw]">
                                <div class="w-full flex flex-col bg-secondary/90 p-3 md:gap-[0.35vw] md:p-[1vw]">
                                    <HoverExpand
                                        class="text-sm font-semibold md:text-[1vw] md:leading-[1.35vw] w-full text-accent"
                                        height="md:max-h-[1.35vw] md:hover:max-h-[10vw]"
                                    >
                                        {anime.name}
                                    </HoverExpand>
                                    <studio-name class="line-clamp-1 text-xs md:line-clamp-none md:text-[0.8vw]">
                                        {anime.studios}
                                    </studio-name>
                                </div>
                            </anime-info>
                        </div>

                        <anime-details class="flex flex-col justify-between rounded-r-lg bg-neutral/25 md:rounded-r-[0.35vw]">
                            <div class="flex flex-col gap-1 p-3 leading-none md:gap-[0.5vw] md:p-[1vw]">
                                <release-time class="text-xs font-semibold capitalize md:text-[1vw]">
                                    {new FormatDate(anime.release_date).format_to_season}
                                </release-time>
                                <div class="flex items-center gap-1 md:gap-[0.5vw]">
                                    <type class="text-xs md:text-[0.8vw]">{anime.type}</type>
                                    <Circle class="w-1 opacity-50 md:w-[0.25vw]" />
                                    <episodes class="text-xs md:text-[0.8vw]">{anime.episodes_count} episodes</episodes>
                                </div>
                                <ScrollArea
                                    offset_scrollbar
                                    gradient_mask
                                    parent_class="max-h-24 md:max-h-[11vw] md:mt-[0.5vw]"
                                    class="text-xs leading-snug text-surface-300 md:text-justify md:text-[0.85vw] md:leading-[1vw]"
                                >
                                    {anime.synopsis}
                                </ScrollArea>
                            </div>

                            <genres class="flex items-center gap-2 overflow-x-scroll p-3 scrollbar-none md:gap-[0.5vw] md:p-[1vw]">
                                {#each anime.genres as genre}
                                    <genre class="whitespace-nowrap rounded bg-warning p-1 text-xs font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">
                                        {genre}
                                    </genre>
                                {/each}
                            </genres>
                        </anime-details>
                    </a>
                {/each}
            </div>
        {:else if thumbnail_mode === "card_with_dropdown"}
            <div
                class="mt-5 grid grid-cols-3 gap-3 md:mt-[1.25vw] md:grid-cols-6 md:gap-[1.5vw]"
                bind:this={result_animes_element}
            >
                {#each trending_animes as anime}
                    <a
                        in:scale={{ start: 0.95 }}
                        href="/mal/{anime.id}"
                        class="relative col-span-1 flex flex-col gap-2 md:gap-[0.5vw]"
                    >
                        <div class="relative">
                            <img
                                src={anime.cover}
                                alt={anime.name}
                                class="h-60 w-full rounded-md object-cover object-center md:h-[20vw] md:rounded-[0.35vw]"
                            />
                            <anime-info class="absolute inset-x-0 bottom-0 rounded-b-lg backdrop-blur md:rounded-b-[0.5vw]">
                                <div class="flex flex-col w-full gap-1 bg-secondary/90 p-3 md:gap-[0.35vw] md:p-[1vw]">
                                    <HoverExpand
                                        class="w-full text-sm font-semibold md:text-[1vw] md:leading-[1.35vw] text-accent"
                                        height="md:max-h-[1.35vw] md:hover:max-h-[10vw]"
                                    >
                                        {anime.name}
                                    </HoverExpand>
                                    <anime_info class="flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                                        <genre>{anime.genres[0]}</genre>
                                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                        <episodes_count>{anime.episodes_count} eps</episodes_count>
                                    </anime_info>
                                </div>
                            </anime-info>
                        </div>
                    </a>
                {/each}
            </div>
        {/if}
    </div>
</section>
