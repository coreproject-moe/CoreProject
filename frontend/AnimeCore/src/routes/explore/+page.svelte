<script lang="ts">
    import { OpengraphGenerator } from "$functions/opengraph";
    import { page } from "$app/stores";
    import Search from "$icons/search.svelte";
    import Chevron from "$icons/chevron.svelte";
    import Preference from "$icons/preference.svelte";
    import Circle from "$icons/circle.svelte";
    import { trending_animes } from "$data/mock/trending";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import { blur } from "svelte/transition";

    /* Anime cards scroll */
    // no:of items to show on each scroll
    let SHOW_NEW_CARDS_COUNT = 2,
        trending_animes_scroll_element: HTMLElement,
        popular_animes_scroll_element: HTMLElement,
        last_scrolled: "trending" | "popular";

    const show_scroll_buttons: {
        [key in typeof last_scrolled]: {
            left: boolean;
            right: boolean;
        };
    } = {
        trending: {
            left: false,
            right: true
        },
        popular: {
            left: false,
            right: true
        }
    };

    function handle_scroll_direction(element: HTMLElement, direction: "left" | "right") {
        switch (direction) {
            case "left":
                element.scrollLeft -= SHOW_NEW_CARDS_COUNT * 200;
                break;
            case "right":
                element.scrollLeft += SHOW_NEW_CARDS_COUNT * 200;
                break;
            default:
                break;
        }
    }

    function handle_scroll(event: UIEvent) {
        const element = event.target as HTMLElement;
        const { scrollLeft, scrollWidth, clientWidth } = element;
        // check if scroll end is not reached
        show_scroll_buttons[last_scrolled].right = Math.abs(scrollLeft + clientWidth) !== scrollWidth;
        // check if its not scroll start pos
        show_scroll_buttons[last_scrolled].left = Math.abs(scrollLeft + clientWidth) !== clientWidth;
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

<section class="md:pl-[1.5vw] md:pr-[3.75vw] md:pb-[2.5vw]">
    <section-headings class="flex flex-col md:gap-[0.5vw]">
        <span class="font-bold leading-none md:text-[2vw]">
            Anime <span class="text-warning-400">Explore</span>
        </span>
        <span class="font-semibold leading-none text-surface-50 md:text-[1.1vw]">Unleash your inner Otaku: Explore anime wonders</span>
    </section-headings>

    <filter-options class=" flex items-end justify-between md:mt-[2vw]">
        <search class="flex flex-col md:gap-[0.5vw]">
            <span class="font-semibold leading-none text-surface-50 md:text-[1.1vw]">Search Animes</span>
            <div class="relative flex items-center">
                <Search class="pointer-events-none absolute text-surface-50 md:ml-[1vw] md:w-[1.25vw]" />
                <input
                    type="text"
                    placeholder="Looking for specific anime? start here..."
                    class="border-none bg-surface-400 leading-none placeholder:text-surface-50 focus:ring-0 md:w-[43.5vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[3vw] md:text-[1vw]"
                />
            </div>
        </search>
        <genres class="flex flex-col md:gap-[0.5vw]">
            <span class="font-semibold leading-none text-surface-50 md:text-[1.1vw]">Genres</span>
            <div class="relative flex items-center">
                <button class="btn absolute right-0 p-0 md:mr-[1vw] md:w-[1.25vw]">
                    <Chevron class="text-surface-50" />
                </button>
                <input
                    type="text"
                    placeholder="Any"
                    class="border-none bg-surface-400 leading-none placeholder:text-surface-50 focus:ring-0 md:w-[12.5vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                />
            </div>
        </genres>
        <year class="flex flex-col md:gap-[0.5vw]">
            <span class="font-semibold leading-none text-surface-50 md:text-[1.1vw]">Year</span>
            <div class="relative flex items-center">
                <button class="btn absolute right-0 p-0 md:mr-[1vw] md:w-[1.25vw]">
                    <Chevron class="text-surface-50" />
                </button>
                <input
                    type="text"
                    placeholder="Any"
                    class="border-none bg-surface-400 leading-none placeholder:text-surface-50 focus:ring-0 md:w-[12.5vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                />
            </div>
        </year>
        <season class="flex flex-col md:gap-[0.5vw]">
            <span class="font-semibold leading-none text-surface-50 md:text-[1.1vw]">Season</span>
            <div class="relative flex items-center">
                <button class="btn absolute right-0 p-0 md:mr-[1vw] md:w-[1.25vw]">
                    <Chevron class="text-surface-50" />
                </button>
                <input
                    type="text"
                    placeholder="Any"
                    class="border-none bg-surface-400 leading-none placeholder:text-surface-50 focus:ring-0 md:w-[12.5vw] md:rounded-[0.5vw] md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"
                />
            </div>
        </season>
        <more-filter-option>
            <button class="btn bg-surface-400 md:rounded-[0.5vw] md:p-[1vw]">
                <Preference class="md:w-[1vw]" />
            </button>
        </more-filter-option>
    </filter-options>

    <results-section class=" md:mt-[4vw] flex flex-col md:gap-[4vw]">
        <trending-now>
            <headings class="flex flex-col leading-none md:gap-[0.35vw]">
                <span class="font-semibold md:text-[1.25vw]">Trending Now</span>
                <span class="text-surface-50 md:text-[1vw]">Crowd Favorites: Anime Hits and Hype</span>
            </headings>

            <result-animes class="relative block md:mt-[1.25vw]">
                <div
                    class="flex snap-x overflow-x-scroll scroll-smooth scrollbar-none md:gap-[1.25vw]"
                    bind:this={trending_animes_scroll_element}
                    on:scroll={(event) => {
                        last_scrolled = "trending";
                        handle_scroll(event);
                    }}
                >
                    {#each trending_animes as anime}
                        <anime class="flex flex-shrink-0 snap-start flex-col leading-none md:w-[13.7vw] md:gap-[0.75vw]">
                            <ImageLoader
                                src={anime.cover}
                                class="w-full md:h-[20vw] md:rounded-[0.75vw]"
                            />
                            <div class="flex flex-col md:gap-[0.35vw]">
                                <anime_name class="line-clamp-1 font-semibold md:text-[1.1vw]">{anime.name}</anime_name>
                                <anime_info class="flex items-center text-surface-50 md:gap-[0.5vw] md:text-[0.9vw]">
                                    <genre>{anime.genre}</genre>
                                    <Circle class="md:w-[0.25vw]" />
                                    <year>{anime.year}</year>
                                    <Circle class="md:w-[0.25vw]" />
                                    <episodes_count>{anime.episodes_count} eps</episodes_count>
                                </anime_info>
                            </div>
                        </anime>
                    {/each}
                </div>

                <scroll-buttons>
                    {#if show_scroll_buttons.trending.left}
                        <left-scroll
                            transition:blur={{ duration: 300 }}
                            class="absolute -left-[1.5vw] top-[8.5vw] z-10"
                        >
                            <button
                                class="btn rounded-full bg-surface-400 md:p-[1vw]"
                                on:click={() => handle_scroll_direction(trending_animes_scroll_element, "left")}
                            >
                                <Chevron class="rotate-90 md:w-[1.5vw]" />
                            </button>
                        </left-scroll>
                    {/if}
                    {#if show_scroll_buttons.trending.right}
                        <right-scroll
                            transition:blur={{ duration: 300 }}
                            class="absolute -right-[1.5vw] top-[8.5vw] z-10"
                        >
                            <button
                                class="btn rounded-full bg-surface-400 md:p-[1vw]"
                                on:click={() => handle_scroll_direction(trending_animes_scroll_element, "right")}
                            >
                                <Chevron class="-rotate-90 md:w-[1.5vw]" />
                            </button>
                        </right-scroll>
                    {/if}
                </scroll-buttons>
            </result-animes>
        </trending-now>

        <popular-animes>
            <headings class="flex flex-col leading-none md:gap-[0.35vw]">
                <span class="font-semibold md:text-[1.25vw]">Popular this season</span>
                <span class="text-surface-50 md:text-[1vw]">Seasonal Gems: Discovering the Best of the Moment</span>
            </headings>

            <result-animes class="relative block md:mt-[1.25vw]">
                <div
                    class="flex snap-x overflow-x-scroll scroll-smooth scrollbar-none md:gap-[1.25vw]"
                    bind:this={popular_animes_scroll_element}
                    on:scroll={(event) => {
                        last_scrolled = "popular";
                        handle_scroll(event);
                    }}
                >
                    {#each trending_animes.reverse() as anime}
                        <anime class="flex flex-shrink-0 snap-start flex-col leading-none md:w-[13.7vw] md:gap-[0.75vw]">
                            <ImageLoader
                                src={anime.cover}
                                class="w-full md:h-[20vw] md:rounded-[0.75vw]"
                            />
                            <div class="flex flex-col md:gap-[0.35vw]">
                                <anime_name class="line-clamp-1 font-semibold md:text-[1.1vw]">{anime.name}</anime_name>
                                <anime_info class="flex items-center text-surface-50 md:gap-[0.5vw] md:text-[0.9vw]">
                                    <genre>{anime.genre}</genre>
                                    <Circle class="md:w-[0.25vw]" />
                                    <year>{anime.year}</year>
                                    <Circle class="md:w-[0.25vw]" />
                                    <episodes_count>{anime.episodes_count} eps</episodes_count>
                                </anime_info>
                            </div>
                        </anime>
                    {/each}
                </div>

                <scroll-buttons>
                    {#if show_scroll_buttons.popular.left}
                        <left-scroll
                            transition:blur={{ duration: 300 }}
                            class="absolute -left-[1.5vw] top-[8.5vw] z-10"
                        >
                            <button
                                class="btn rounded-full bg-surface-400 md:p-[1vw]"
                                on:click={() => handle_scroll_direction(popular_animes_scroll_element, "left")}
                            >
                                <Chevron class="rotate-90 md:w-[1.5vw]" />
                            </button>
                        </left-scroll>
                    {/if}
                    {#if show_scroll_buttons.popular.right}
                        <right-scroll
                            transition:blur={{ duration: 300 }}
                            class="absolute -right-[1.5vw] top-[8.5vw] z-10"
                        >
                            <button
                                class="btn rounded-full bg-surface-400 md:p-[1vw]"
                                on:click={() => handle_scroll_direction(popular_animes_scroll_element, "right")}
                            >
                                <Chevron class="-rotate-90 md:w-[1.5vw]" />
                            </button>
                        </right-scroll>
                    {/if}
                </scroll-buttons>
            </result-animes>
        </popular-animes>
    </results-section>
</section>
