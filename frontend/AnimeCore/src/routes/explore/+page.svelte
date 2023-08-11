<script lang="ts">
    import { OpengraphGenerator } from "$functions/opengraph";
    import { page } from "$app/stores";
    import Search from "$icons/search.svelte";
    import Chevron from "$icons/chevron.svelte";
    import Preference from "$icons/preference.svelte";
    import Circle from "$icons/circle.svelte";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import MoreBox from "$icons/more_box.svelte";
    import { trending_animes } from "$data/mock/trending";
    import VercelHover from "$components/shared/vercel_hover.svelte";

    /* Filter pages */
    let filter_pages_mapping: {
        [key in typeof active_filter_page]: {
            title: string;
            description: string;
        };
    } = {
        trending: {
            title: "Trending Now",
            description: "Crowd Favorites: Anime Hits and Hype"
        },
        popular: {
            title: "Popular this Season",
            description: "Seasonal Gems: Discovering the Best of the Moment"
        },
        upcoming: {
            title: "Upcoming",
            description: "Crowd Favorites: Anime Hits and Hype"
        },
        alltime: {
            title: "All-time Popular",
            description: "Seasonal Gems: Discovering the Best of the Moment"
        }
    };
    let active_filter_page: "trending" | "popular" | "upcoming" | "alltime" = "trending";

    function change_filter_page(page: string) {
        active_filter_page = page as typeof active_filter_page;
    }

    let filter_options_mapping: {
        [key: string]: {
            title: string;
            value: string;
            class: string;
        };
    } = {
        time_range: {
            title: "Time Range",
            value: "All-Time",
            class: "hidden md:flex flex-col md:gap-[0.35vw]"
        },
        genres: {
            title: "Genres",
            value: "Any",
            class: "md:flex flex-col md:gap-[0.35vw]"
        },
        year: {
            title: "Year",
            value: "Any",
            class: "hidden md:flex flex-col md:gap-[0.35vw]"
        },
        season: {
            title: "Season",
            value: "Any",
            class: "md:flex flex-col md:gap-[0.35vw]"
        },
        format: {
            title: "Format",
            value: "Any",
            class: "hidden md:flex flex-col md:gap-[0.35vw]"
        },
        airing_status: {
            title: "Airing Status",
            value: "Any",
            class: "hidden md:flex flex-col md:gap-[0.35vw]"
        },
        sort_by: {
            title: "Sort by",
            value: "Popularity",
            class: "md:flex flex-col md:gap-[0.35vw]"
        }
    };

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

    <explore-options class="mt-7 flex flex-col justify-between gap-5 md:mt-[2vw] md:flex-row md:items-end md:gap-0">
        <search class="flex flex-col gap-1 md:gap-[0.35vw]">
            <span class="text-base leading-none text-surface-50 md:text-[1vw]">Search Animes</span>
            <div class="relative flex items-center">
                <Search class="pointer-events-none absolute ml-4 w-5 text-surface-50 md:ml-[1vw] md:w-[1.25vw]" />
                <input
                    type="text"
                    placeholder="Looking for specific anime? Start from here..."
                    class="w-full rounded-lg border-none bg-surface-400 py-3 pl-14 leading-none placeholder:text-surface-50 focus:ring-0 md:w-[45vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[3vw] md:text-[1vw]"
                />
            </div>
        </search>
        <VercelHover
            direction="horizontal"
            glider_container_class="flex items-center justify-between md:gap-[0.5vw]"
            active_element_class="rounded-[0.75vw] bg-surface-400/50"
            let:handle_mouseenter
            let:handle_mouseleave
        >
            {#each Object.entries(filter_pages_mapping) as page}
                {@const page_key = page[0]}
                {@const page_title = page[1].title}

                {@const is_active = active_filter_page === page_key}

                <button
                    class="h-14 cursor-pointer rounded-lg px-3 py-2 text-base font-semibold leading-tight transition-colors hover:text-white md:h-auto md:rounded-[0.5vw] md:px-[1.25vw] md:py-[0.9vw] md:text-[1vw]"
                    class:bg-surface-400={is_active}
                    class:text-surface-50={!is_active}
                    on:mouseenter={handle_mouseenter}
                    on:mouseleave={handle_mouseleave}
                    on:click={() => change_filter_page(page_key)}
                >
                    {page_title}
                </button>
            {/each}
        </VercelHover>
    </explore-options>

    <filter-options class="mt-5 flex items-end justify-between gap-3 md:mt-0 md:gap-0">
        {#each Object.entries(filter_options_mapping) as option}
            {@const title = option[1].title}
            {@const value = option[1].value}
            {@const klass = option[1].class}

            <filter-component class={klass}>
                <span class="leading-none text-surface-50 md:text-[1vw]">{title}</span>
                <div class="relative flex items-center">
                    <button class="btn absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1.25vw]">
                        <Chevron class="text-surface-50" />
                    </button>
                    <input
                        type="text"
                        class="w-full rounded-lg border-none bg-surface-400 py-3 text-base leading-none placeholder:text-surface-50 focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                        {value}
                    />
                </div>
            </filter-component>
        {/each}

        <more-filter-option>
            <button class="btn bg-surface-400 p-3 md:rounded-[0.5vw] md:p-[0.79vw]">
                <MoreBox class="w-5 md:w-[1.25vw]" />
            </button>
        </more-filter-option>
    </filter-options>

    <active-filter-page class="mt-20 md:mt-[2vw]">
        <headings class="flex flex-col md:gap-[0.35vw]">
            <span class="text-xl font-semibold leading-none md:text-[1.25vw]">
                {filter_pages_mapping[active_filter_page].title}
            </span>
            <span class="text-base leading-none text-surface-50 md:text-[1vw]">
                {filter_pages_mapping[active_filter_page].description}
            </span>
        </headings>

        <result-animes class="mt-5 grid grid-cols-2 gap-5 md:mt-[1.25vw] md:grid-cols-6 md:gap-[1.25vw] md:gap-y-[3vw]">
            {#each trending_animes as anime}
                <anime class="flex flex-col gap-2 leading-none md:gap-[0.75vw]">
                    <ImageLoader
                        src={anime.cover}
                        class="h-80 w-full rounded-lg object-cover md:h-[20vw] md:rounded-[0.75vw]"
                    />
                    <div class="flex flex-col md:gap-[0.35vw]">
                        <anime_name class="line-clamp-1 text-base font-semibold md:text-[1.1vw]">{anime.name}</anime_name>
                        <anime_info class="flex items-center gap-2 text-sm text-surface-50 md:gap-[0.5vw] md:text-[0.9vw]">
                            <genre>{anime.genre}</genre>
                            <Circle class="w-1 md:w-[0.25vw]" />
                            <year>{anime.year}</year>
                            <Circle class="w-1 md:w-[0.25vw]" />
                            <episodes_count>{anime.episodes_count} eps</episodes_count>
                        </anime_info>
                    </div>
                </anime>
            {/each}
        </result-animes>
    </active-filter-page>
</section>
