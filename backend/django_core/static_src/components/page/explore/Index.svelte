<script lang="ts">
    import { cn } from "$functions/classname";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import MoreBox from "$icons/MoreBox/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Chevron from "$icons/Chevron/Index.svelte";

    // Mapping
    let filter_options_mapping: {
        [key: string]: {
            title: string;
            class: string;
            value: string;
            items?: Record<string, string> | undefined;
            selected_items?: Array<[string, string]>;
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

    // Functions
    const update_selected_items = (key: string, selected_item: [string, string]) => {
        let filter_option = filter_options_mapping[key];
        let is_selected = filter_option.selected_items?.some((item) => item[0] === selected_item[0]);

        if (is_selected) {
            filter_option.selected_items = filter_option.selected_items?.filter((item) => item[0] !== selected_item[0]);
        } else {
            filter_option.selected_items = [...filter_option.selected_items, selected_item];
        }

        // update filer_options_mapping
        filter_options_mapping[key] = filter_option;
    },
    clear_selected_items = (key: string) => {
        // update filter_options_mapping
        filter_options_mapping[key].selected_items = [];
    };
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
                        <span class="absolute flex items-center md:gap-[0.25vw] cursor-pointer opacity-100 duration-300 group-focus-within:opacity-0">
                            {#if selected_items.length > 0}
                                <span class="ml-3 badge badge-primary rounded p-1 text-sm font-semibold md:ml-[0.75vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw] md:h-[1.5vw]">
                                    <!-- show first item -->
                                    {selected_items[0][1]}
                                </span>
                                <!-- show count of remaining items if exists -->
                                {#if selected_items.length > 1}
                                    <span class="ml-1 rounded badge md:h-[1.5vw] p-1 text-sm font-semibold md:ml-[0.15vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">
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
                            tabindex="0" role="button"
                            class="peer w-full rounded-lg border-none bg-neutral py-3 text-base leading-none placeholder focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:bg-neutral text-neutral-content md:py-[0.8vw] md:pl-[1vw] md:text-[1vw] placeholder:font-medium font-semibold"
                        />
                        {#if selected_items.length > 0}
                            <button
                                on:click|preventDefault={() => clear_selected_items(option[0])}
                                class="btn !bg-transparent border-none absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]"
                            >
                                <Cross class="md:w-[1vw]" />
                            </button>
                        {:else}
                            <button class="btn !bg-transparent border-none absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]">
                                <Chevron class="md:w-[1vw]" />
                            </button>
                        {/if}
                    </div>
                    <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                    <div
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

                                    {@const is_selected = selected_items.some(selected_item => selected_item[0] === key)}

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
                    </div>
                </div>
            {/each}
        </div>

        <button class="btn btn-neutral h-max min-h-max rounded-lg p-[0.85rem] md:rounded-[0.5vw] md:p-[0.8vw]">
            <MoreBox class="w-4 md:w-[1.1vw]" />
        </button>
    </div>
</section>
