<script lang="ts">
    export let pk: string | null = null,
        anime_name: string | null = null,
        anime_japanese_name: string | null = null,
        anime_genres: string | null = null,
        anime_episodes_count: string | null = null, // Is number
        anime_synopsis: string | null = null,
        anime_episodes: string | null = null;

    import { reverse } from "$functions/urls";
    import JSON5 from "json5";
    import * as _ from "lodash-es";

    // Components
    import CommentBox from "$components/specific/CommentBox/Index.svelte";
    import Comment from "$components/minor/Comment/Index.svelte";
    import HoverExpand from "$components/minor/HoverExpand/Index.svelte";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Rating from "$components/minor/Rating/Index.svelte";

    //Icons
    import Dot from "$icons/Dot/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Edit from "$icons/Edit/Index.svelte";
    import Book from "$icons/Book/Index.svelte";
    import Headphone from "$icons/Headphone/Index.svelte";
    import Download from "$icons/Download/Index.svelte";
    import Share from "$icons/Share/Index.svelte";
    import Settings from "$icons/Settings/Index.svelte";
    import Chevron from "$icons/Chevron/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
    import Filter from "$icons/Filter/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";
    import TrendingArrow from "$icons/TrendingArrow/Index.svelte";
    import { string_to_number } from "$functions/string_to_number";

    // Internal logics
    const sencond_mapping = [
        // anime.source
        { item: "TV", show_dots_after: true },
        // anime.episode
        { item: `${string_to_number(anime_episodes_count)} eps`, show_dots_after: true },
        // anime.status
        { item: `completed`, show_dots_after: true },
        // anime.aired_from
        { item: `spring 2023`, show_dots_after: true },
        // anime.aired_to
        { item: `Kuschio animation`, show_dots_after: false }
    ];

    // Parse anime_episode to Compatible JSON
    const parse_anime_episode: () => { banner: string; name: string; japanese_name: string; duration: string; formats: string[]; resolutions: string[] }[] = () => {
        if (!_.isNull(anime_episodes) && _.isString(anime_episodes)) {
            return JSON5.parse(anime_episodes);
        } else {
            throw new Error(`${`anime_episode`} is not castable to JSON`);
        }
    };
</script>

<div class="relative mt-16 block h-screen bg-cover md:mt-0">
    <img
        src="https://files.otakustudy.com/wp-content/uploads/2020/10/10153058/your-lie-in-april-cover.jpg"
        class="absolute hidden h-full w-full select-none rounded-tl-[1.5vw] object-cover object-center md:flex"
        alt={anime_name}
    />
    <div class="gradient absolute inset-0 bg-gradient-to-t from-secondary to-secondary/80"></div>
    <div class="absolute inset-0 grid grid-cols-12 items-start p-5 pt-10 md:p-[5vw]">
        <div class="col-span-12 md:col-span-10 md:pr-[4vw]">
            <div class="grid grid-cols-12 items-end justify-between">
                <div class="relative col-span-12 grid grid-cols-12 gap-5 md:col-span-7 md:flex md:w-full md:items-end md:gap-[2vw] md:pr-[2vw]">
                    <div class="relative col-span-12 h-96 md:h-[18.25vw] md:w-[13vw] md:flex-shrink-0">
                        <div
                            class="pointer-events-none absolute inset-0 z-10 h-[150%] w-[125%] -translate-x-8 -translate-y-28 [background-image:radial-gradient(circle_at_center,rgba(255,255,255,0.1)0%,transparent_100%)] [mask-image:linear-gradient(to_bottom,rgba(7,5,25,0.95)80%,rgba(0,0,0,0)100%)] md:hidden"
                        ></div>
                        <img
                            alt=""
                            src="https://files.otakustudy.com/wp-content/uploads/2020/10/10153058/your-lie-in-april-cover.jpg"
                            class="h-full w-full rounded-xl object-cover object-center md:rounded-[1vw]"
                        />
                        <div class="gradient from-surface-900/75 to-surface-900/25 absolute inset-0 bg-gradient-to-t md:hidden"></div>
                    </div>
                    <div class="absolute bottom-0 col-span-12 p-5 md:static md:p-0">
                        <HoverExpand
                            class="w-full text-2xl font-bold text-white md:text-[2vw] md:leading-[2.7vw]"
                            height="max-h-48 md:max-h-[10vw]"
                        >
                            {anime_name}
                        </HoverExpand>
                        <HoverExpand class="flex flex-wrap gap-x-2 pt-2 text-xs font-semibold uppercase tracking-wider md:gap-x-[0.25vw] md:pt-[0.625vw] md:text-[0.75vw] md:leading-[0.9vw]">
                            {anime_japanese_name}
                        </HoverExpand>
                        <div class="mt-1 flex flex-wrap items-center gap-2 text-xs font-semibold md:mt-[0.25vw] md:gap-[0.5vw] md:pt-[0.5vw] md:text-[0.75vw] md:leading-[0.75vw]">
                            {#each sencond_mapping as map}
                                <span>{map.item}</span>
                                {#if map.show_dots_after}
                                    <Dot class="w-[0.35rem] opacity-75" />
                                {/if}
                            {/each}
                        </div>
                        <div class="mt-3 flex items-center gap-3 md:mt-[1.5vw] md:gap-[0.75vw]">
                            <button
                                type="button"
                                class="btn btn-primary h-14 w-[6.5rem] rounded-lg font-bold text-white md:h-[4vw] md:w-[7vw] md:rounded-[0.625vw]"
                            >
                                <div class="flex gap-3 md:gap-[0.7vw]">
                                    <Play class="w-5 md:w-[1.5vw]" />

                                    <div class="flex flex-col items-start gap-1">
                                        <span class="text-sm leading-none md:text-[0.9vw]">Watch</span>
                                        <span class="text-surface-50 text-xs font-semibold leading-none md:text-[0.75vw]">Ep 01</span>
                                    </div>
                                </div>
                            </button>
                            {#each [Book, Headphone] as item}
                                <button
                                    type="button"
                                    class="bg-secondary-100 text-surface-500 btn h-14 w-14 rounded-lg capitalize md:h-[4vw] md:w-[4vw] md:rounded-[0.625vw] md:text-[0.87vw] md:font-semibold"
                                    disabled
                                >
                                    <div class="flex flex-col items-center gap-2 md:gap-[0.68vw]">
                                        <svelte:component
                                            this={item}
                                            class="text-surface-500 w-4 md:w-[1.5vw]"
                                        ></svelte:component>
                                        <span class="leading-none">read</span>
                                    </div>
                                </button>
                            {/each}
                        </div>
                        <div class="mt-3 flex gap-2 md:mt-[0.75vw] md:gap-[0.75vw]">
                            <!-- <button
                                type="button"
                                aria-label="video"
                                class="btn btn-warning h-7 min-h-full w-7 rounded p-0 md:h-[2vw] md:w-[2vw] md:rounded-[0.25vw]"
                            >
                                <coreproject-icon-record class="w-4 md:w-[1.125vw]"></coreproject-icon-record>
                            </button> -->
                            <button
                                type="button"
                                aria-label="video"
                                class="btn btn-warning h-7 min-h-full w-7 rounded p-0 md:h-[2vw] md:w-[2vw] md:rounded-[0.25vw]"
                            >
                                <Edit class="w-4 md:w-[1.125vw]" />
                            </button>
                            <button
                                type="button"
                                aria-label="video"
                                class="btn btn-warning h-7 min-h-full w-7 rounded p-0 md:h-[2vw] md:w-[2vw] md:rounded-[0.25vw]"
                            >
                                <Download class="w-4 md:w-[1.125vw]" />
                            </button>
                            <button
                                type="button"
                                aria-label="video"
                                class="btn btn-warning h-7 min-h-full w-7 rounded p-0 md:h-[2vw] md:w-[2vw] md:rounded-[0.25vw]"
                            >
                                <Share class="w-4 md:w-[1.125vw]" />
                            </button>
                        </div>
                    </div>
                </div>
                <div class="col-span-12 mt-10 flex flex-col gap-[0.75vw] md:col-span-5 md:mt-0">
                    <div class="flex gap-[0.75vw]">
                        <div class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Synopsis</div>
                        <button class="btn btn-secondary hidden min-h-full rounded-[0.1875vw] p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                            <Settings class="w-[0.9vw] opacity-75" />
                        </button>
                    </div>
                    <ScrollArea
                        class="text-justify text-xs md:text-[0.8vw] md:leading-[1vw]"
                        parent_class="max-h-40 md:max-h-[10vw]"
                        offset_scrollbar="true"
                        gradient_mask="true"
                    >
                        {anime_synopsis}
                    </ScrollArea>
                    <div class="hidden gap-[0.5vw] text-white md:flex md:text-[0.75vw] md:leading-[0.9vw]">
                        {#if !_.isNull(anime_genres) && _.isString(anime_genres)}
                            {#each JSON5.parse(anime_genres) as item}
                                <span class="rounded-[0.25vw] bg-warning font-semibold text-black md:px-[0.75vw] md:py-[0.4vw]">{item}</span>
                            {/each}
                        {/if}
                    </div>
                    <div class="hidden w-max gap-[0.75vw] rounded-[0.25vw] bg-secondary md:flex md:px-[0.75vw] md:py-[0.5vw] md:text-[0.75vw] md:leading-[0.75vw]">
                        <div class="flex gap-[0.25vw]">
                            <span>Score:</span>
                            <span class="text-warning-400 font-semibold">79</span>
                        </div>
                        <div class="flex gap-[0.25vw]">
                            <span>Status:</span>
                            <button class="btn h-min min-h-min border-none !bg-transparent p-0 leading-none md:text-[0.75vw]">
                                <span class="font-semibold text-warning">Watching</span>
                                <Chevron class="text-warning-400 w-[0.625vw]" />
                            </button>
                        </div>
                        <div class="flex gap-[0.25vw]">
                            <span>Episode:</span>
                            <span class="text-warning-400 font-semibold">0/9</span>
                        </div>
                        <div class="flex gap-[0.25vw]">
                            <span>Your Score:</span>
                            <button class="btn h-min min-h-min border-none !bg-transparent p-0 leading-none md:text-[0.75vw]">
                                <span class="font-semibold text-warning">Not Rated</span>
                                <Chevron class="text-warning-400 w-[0.625vw]" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="my-7 block md:my-[6vw]">
                <div class="border-surface-50/10 flex border-b-2 pb-1 md:gap-x-[0.75vw] md:border-none md:pb-0">
                    <div class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Episodes</div>
                    <button class="bg-surface-400 btn btn-secondary hidden min-h-full rounded p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                        <Settings class="w-[0.9vw] opacity-75" />
                    </button>
                </div>
                <div class="mt-2 flex flex-col justify-between gap-y-5 md:mt-0 md:flex-row md:gap-y-0">
                    <div class="hidden items-end gap-2 md:flex md:gap-[1vw]">
                        <p class="flex items-center gap-1 md:gap-[0.75vw]">
                            <span class="text-base font-bold leading-none md:text-[2vw] md:leading-[1.9vw]">23</span>
                            <span class="text-xs font-semibold md:text-[1vw]">episodes</span>
                            <Dot class="w-[0.4vw] opacity-50" />
                        </p>
                        <div>
                            <div class="flex w-full items-center gap-2 leading-4 md:gap-[1vw] md:leading-[1.5vw]">
                                <span class="flex-shrink-0 text-[0.5rem] font-medium md:text-[0.75vw]">Available in</span>
                                <div class="h-[0.1rem] w-full bg-accent opacity-25 md:h-[0.1vw]"></div>
                            </div>
                            <div class="flex h-5 gap-2 text-[0.5rem] font-bold md:h-[1.8vw] md:gap-[0.5vw] md:text-[0.75vw]">
                                <span class="flex h-full place-items-center rounded bg-secondary px-2 uppercase leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">sub</span>
                                <span class="flex h-full place-items-center rounded bg-secondary px-2 uppercase leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">dub</span>
                                <Dot class="w-[0.4vw] opacity-50" />
                                <span class="flex h-full place-items-center rounded bg-secondary px-2 leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">1080p</span>
                                <span class="flex h-full place-items-center rounded bg-secondary px-2 leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">720p</span>
                                <span class="flex h-full place-items-center rounded bg-secondary px-2 leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">480p</span>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center justify-between gap-2 md:items-end md:gap-[0.75vw]">
                        <p class="flex items-center gap-1 md:hidden">
                            <span class="text-base font-bold leading-none">23</span>
                            <span class="text-surface-50 text-sm font-semibold">episodes</span>
                        </p>
                        <div class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]">
                            <span class="text-surface-50 text-[0.65rem] leading-[0.9vw] transition-colors duration-300 group-hover:text-white md:text-[0.75vw]">Type</span>
                            <button class="btn btn-secondary h-7 min-h-full rounded px-3 text-[0.65rem] font-semibold md:h-[2.5vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw] md:leading-[0.9vw]">
                                <span>Subbed</span>
                                <Chevron class="w-3 md:w-[1vw]"></Chevron>
                            </button>
                        </div>
                        <div class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]">
                            <span class="text-surface-50 text-[0.65rem] leading-[0.9vw] transition-colors duration-300 group-hover:text-white md:text-[0.75vw]">Display Mode</span>
                            <button class="btn btn-secondary h-7 min-h-full rounded px-3 text-[0.65rem] font-semibold leading-[0.9vw] md:h-[2.5vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw]">
                                <span>Thumbnails</span>
                                <Chevron class="w-3 md:w-[1vw]"></Chevron>
                            </button>
                        </div>
                        <button
                            class="bg-surface-400 btn btn-secondary h-7 min-h-max w-auto rounded p-0 font-semibold md:ml-0 md:h-[2.5vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                            aria-label="Search"
                        >
                            <Search class="w-3 md:w-[1vw]"></Search>
                        </button>
                    </div>
                </div>
                <div class="mt-4 grid grid-cols-12 gap-5 md:mt-[2.5vw] md:gap-[2.5vw]">
                    {#each parse_anime_episode() as episode}
                        <a
                            href="/anime/mal/1/episode/1"
                            class="relative col-span-12 grid grid-cols-12 gap-4 md:col-span-4"
                        >
                            <div class="relative col-span-5 h-full w-full md:col-span-12 md:h-[18vw]">
                                <div class="block h-24 md:h-[12vw] md:w-full">
                                    <img
                                        src={episode.banner}
                                        alt=""
                                        class="h-full w-full shrink-0 rounded-lg bg-cover bg-center md:rounded-t-[0.625vw]"
                                    />
                                </div>
                                <div class="absolute inset-0 hidden bg-gradient-to-t from-secondary/75 to-transparent md:flex md:h-[12vw]"></div>
                            </div>
                            <div
                                class="col-span-7 flex h-full w-full flex-col items-start justify-between md:absolute md:bottom-0 md:col-span-12 md:h-auto md:rounded-b-[0.625vw] md:bg-secondary md:p-[1vw]"
                            >
                                <div class="absolute inset-x-0 bottom-0 flex justify-between md:-top-[2.5vw] md:px-[1vw]">
                                    <p
                                        class="text-surface-50 rounded bg-secondary/75 p-1 text-xs font-bold tracking-wider md:h-max md:rounded-[0.4vw] md:bg-secondary md:px-[0.55vw] md:py-[0.55vw] md:text-[0.8vw] md:leading-none"
                                    >
                                        EP 01
                                    </p>
                                    <p
                                        class="text-surface-50 rounded bg-secondary/75 p-1 py-0 text-[0.7rem] font-semibold md:h-max md:rounded-[0.4vw] md:bg-secondary md:px-[0.5vw] md:py-[0.55vw] md:text-[0.8vw] md:leading-none"
                                    >
                                        {episode.duration}
                                    </p>
                                </div>
                                <div class="relative flex h-full w-full flex-col items-start md:gap-[0.25vw]">
                                    <coreproject-hover-expand
                                        class="text-xs font-medium leading-4 text-white md:text-[0.9vw] md:leading-[1.1vw]"
                                        height="md:max-h-[1.15vw] md:hover:max-h-[9vw]"
                                    >
                                        {episode.name}
                                    </coreproject-hover-expand>
                                    <coreproject-hover-expand
                                        class="text-xs font-medium leading-4 text-white md:text-[0.9vw] md:leading-[1.1vw]"
                                        height="md:max-h-[1.15vw] md:hover:max-h-[9vw]"
                                    >
                                        {episode.japanese_name}
                                    </coreproject-hover-expand>
                                </div>

                                <div class="bg-surface-900 relative flex w-full items-center gap-2 md:gap-[0.5vw] md:pt-[0.75vw]">
                                    <div class="flex gap-2 leading-none md:gap-[0.65vw]">
                                        {#each episode.formats as format}
                                            <span class="text-surface-50 md:bg-surface-400/50 rounded text-[0.6rem] font-semibold uppercase tracking-wider md:text-[0.8vw]">
                                                {format}
                                            </span>
                                        {/each}
                                    </div>
                                    <coreproject-icon-dot class="w-1 opacity-50 md:w-[0.25vw]"></coreproject-icon-dot>
                                    <div class="flex gap-2 leading-none md:gap-[0.65vw]">
                                        {#each episode.resolutions as res}
                                            <span class="text-surface-50 md:bg-surface-400/25 text-[0.6rem] font-semibold uppercase tracking-wider md:rounded md:text-[0.8vw]">
                                                {res}
                                            </span>
                                        {/each}
                                    </div>
                                </div>
                            </div>
                        </a>
                    {/each}
                </div>
                <div class="mt-10 flex grid-cols-5 flex-col gap-10 md:mt-[3vw] md:grid md:gap-[4.375vw]">
                    <div class="md:col-span-3">
                        <div class="border-surface-50/10 flex gap-2 border-b-2 pb-1 md:gap-[0.75vw] md:border-none md:pb-0">
                            <div class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Comments</div>
                            <button class="bg-surface-400 btn btn-secondary hidden min-h-full rounded p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                <Settings class="w-[0.9vw] opacity-75"></Settings>
                            </button>
                        </div>
                        <div class="mt-2 flex items-center justify-between md:hidden">
                            <p class="flex items-center gap-1 md:hidden">
                                <span class="text-base font-bold leading-none">69</span>
                                <span class="text-surface-50 text-sm font-semibold">div</span>
                            </p>
                            <button
                                class="btn-icon bg-surface-400 btn h-7 w-auto rounded p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                                aria-label="Filter"
                            >
                                <Filter class="w-3 md:w-[1vw]"></Filter>
                            </button>
                        </div>
                        <div class="md:mt-[1vw]">
                            <CommentBox submit_url={reverse("anime-commment-endpoint", Number(pk))}></CommentBox>
                        </div>
                        <div class="mt-10 flex w-full md:mt-[2vw]">
                            <Comment api_url={reverse("anime-commment-endpoint", Number(pk))}></Comment>
                        </div>
                    </div>
                    <div class="md:col-span-2">
                        <div class="border-surface-50/10 flex gap-2 border-b-2 pb-1 md:gap-[0.75vw] md:border-none md:pb-0">
                            <div class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Forum div</div>
                            <button class="bg-surface-400 btn btn-secondary hidden min-h-full rounded p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                <Settings class="w-[0.9vw] opacity-75"></Settings>
                            </button>
                        </div>
                        <div class="mt-2 flex items-center justify-between md:mt-[0.75vw]">
                            <p class="flex items-center gap-1 md:hidden">
                                <span class="text-base font-bold leading-none">106</span>
                                <span class="text-surface-50 text-sm font-semibold">div</span>
                            </p>
                            <div class="flex items-center gap-2 md:w-full md:justify-between">
                                <button
                                    class="bg-surface-400 btn btn-secondary h-7 min-h-full gap-2 rounded px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]"
                                >
                                    <Cross class="w-4 rotate-45 md:w-[1vw]"></Cross>
                                    Create New
                                </button>
                                <button
                                    class="bg-surface-400 btn btn-secondary h-7 min-h-full w-auto rounded p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                                    aria-label="Filter"
                                >
                                    <Filter class="w-3 md:w-[1vw]"></Filter>
                                </button>
                            </div>
                        </div>
                        <div class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1.25vw] md:flex md:gap-[1vw]">
                            <a
                                href="/"
                                class="card w-full grid-cols-7 overflow-hidden rounded-lg !bg-neutral/50 md:grid md:rounded-[0.625vw]"
                            >
                                <div class="col-span-2 block h-16 md:h-full md:w-full">
                                    <img
                                        alt=""
                                        src="https://timelinecovers.pro/facebook-cover/download/anime-your-lie-in-april-kaori-and-arima-facebook-cover.jpg"
                                        class="h-full w-full object-cover object-center"
                                    />
                                </div>
                                <div class="flex h-36 flex-col justify-between p-3 md:col-span-5 md:h-full md:gap-[0.375vw] md:p-[1vw]">
                                    <div>
                                        <div class="line-clamp-2 text-xs font-extrabold md:text-[0.875vw] md:leading-[1.25vw]">Celebrating 10 years of Hyouka!</div>
                                        <div class="text-surface-50 mt-2 line-clamp-3 text-[0.6rem] font-medium leading-snug md:mt-[0.5vw] md:line-clamp-2 md:text-[0.75vw] md:leading-[1.125vw]">
                                            Ousei Arima is a child prodigy known as the "Human Metronome" for playing the piano with precision and perfection. Guided by a strict mother and rigorous
                                            training, Kousei dominates every competition he enters
                                        </div>
                                    </div>
                                    <div class="flex items-end justify-between text-[0.6rem] leading-none md:mt-[0.75vw] md:items-center md:text-[0.75vw]">
                                        <div class="flex flex-col gap-1 md:flex-row md:items-center md:gap-[0.25vw]">
                                            <div>
                                                Posted by <span class="text-[0.65rem] font-semibold md:text-[0.85vw]">Eiennlaio</span>
                                            </div>
                                            <div class="text-surface-50">7 months ago</div>
                                        </div>
                                        <div class="flex items-center gap-1 md:gap-[0.25vw]">
                                            <Chat class="w-3 md:w-[1vw]"></Chat>
                                            <div>69</div>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="hidden flex-col gap-[1vw] md:col-span-2 md:flex">
            <div class="flex gap-[0.75vw]">
                <div class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Ratings</div>
                <button class="bg-surface-400 btn btn-secondary min-h-full rounded-[0.1875vw] p-0 md:h-[1.5vw] md:w-[1.5vw]">
                    <Settings class="w-[0.9vw] opacity-75"></Settings>
                </button>
            </div>
            <div class="flex flex-col gap-[0.75vw]">
                <div class="flex items-center gap-[0.5vw]">
                    <span class="border-surface-50/50 border-b-2 pb-[0.5vw] font-bold md:text-[2vw] md:leading-[1.5vw]">92%</span>
                    <span class="!border-surface-50/50 text-surface-50 divider-vertical m-0 font-semibold md:pl-1 md:text-[0.75vw] md:leading-[0.8vw]">2.8k ratings</span>
                </div>
                <div class="block">
                    <div class="flex items-center md:gap-[0.25vw]">
                        <span class="font-semibold md:text-[1vw] md:leading-[1.5vw]">#80</span>
                        <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Trending of all time</span>
                    </div>
                    <div class="flex items-center md:gap-[0.25vw]">
                        <span class="font-semibold md:text-[1vw] md:leading-[1.5vw]">#108</span>
                        <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Most popular anime</span>
                    </div>
                </div>
                <button class="btn btn-accent min-h-full md:h-[1.5vw] md:w-max md:rounded-[0.25vw] md:text-[0.75vw]">
                    <TrendingArrow class="w-[1.25vw]"></TrendingArrow>
                    <span>Detailed Distribution</span>
                </button>
                <div class="flex flex-col gap-[0.5vw] leading-none">
                    <span class="font-semibold md:text-[0.9vw] md:leading-[0.9vw]">Your rating</span>
                    <div class="flex items-center gap-[0.75vw]">
                        <Rating />
                        <span class="font-bold leading-none md:text-[0.95vw]">92%</span>
                        <button class="text-surface-500 btn btn-secondary min-h-full p-[0.3vw] md:h-[1.375vw] md:w-[1.375vw] md:rounded-[0.19vw]">
                            <Edit class="w-[0.75vw]"></Edit>
                        </button>
                    </div>
                </div>
                <button class="btn flex h-min min-h-full w-max items-center gap-[0.5vw] border-none !bg-transparent p-0 md:text-[0.8vw]">
                    Add a review
                    <Edit class="w-[0.8vw]"></Edit>
                </button>
            </div>
            <div class="flex gap-[0.75vw] md:mt-[6vw]">
                <div class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Details</div>
                <button class="btn btn-secondary min-h-full rounded p-0 md:h-[1.5vw] md:w-[1.5vw]">
                    <Settings class="w-[0.9vw] opacity-75"></Settings>
                </button>
            </div>
            <div class="md:mb-[2vw] md:mt-[1.25vw]">
                <div class="flex flex-col gap-[1.125vw] capitalize">
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">format</p>
                        <p>TV</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">episodes</p>
                        <p>22</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">episode Duration</p>
                        <p>26 Minutes</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">status</p>
                        <p>finished</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">start date</p>
                        <p>Apr 23, 2012</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">end date</p>
                        <p>Sep 16, 2012</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">season</p>
                        <p>spring 2012</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">studios</p>
                        <p>Kyoto Animation</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.75vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">producers</p>
                        <p>Animation Do</p>
                        <p>Kadokawa Shoten</p>
                        <p>Klock Worx</p>
                        <p>Lantis</p>
                        <p>chara-ani.com</p>
                    </div>
                    <div class="text-surface-50 flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none">
                        <p class="font-semibold text-white">source</p>
                        <p>Night Novel</p>
                    </div>
                </div>
                <div class="mt-[2.5vw] block">
                    <div class="flex gap-[0.75vw]">
                        <div class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Voiceover Cast</div>
                        <button class="bg-surface-400 btn btn-secondary min-h-full rounded p-0 md:h-[1.5vw] md:w-[1.5vw]">
                            <Settings class="w-[0.9vw] opacity-75"></Settings>
                        </button>
                    </div>
                    <div class="mt-[1vw] flex flex-col">
                        <span class="text-surface-50 text-[0.9375vw]">VAs</span>
                        <button class="bg-surface-400 btn btn-secondary mt-[0.3vw] h-[2.25vw] min-h-full w-[6.625vw] gap-1 rounded-[0.375vw] p-0 text-[0.875vw]">
                            Japanese
                            <Chevron class="w-[1vw]"></Chevron>
                        </button>
                    </div>
                    <div class="mt-[1vw] block">
                        <div class="relative grid h-[9vw] w-full grid-cols-2 gap-[2px] overflow-hidden rounded-[0.75vw]">
                            <div class="relative col-span-1 w-full bg-cover">
                                <img
                                    alt=""
                                    src="https://i.pinimg.com/550x/ed/47/64/ed4764a0074e785738f2797641aeb411.jpg"
                                    class="absolute h-full w-full object-cover object-center"
                                />
                                <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1vw] text-white md:px-[1vw]">Houtarou Oreki</span>
                            </div>
                            <div class="relative col-span-1 w-full bg-cover">
                                <img
                                    alt=""
                                    src="https://animeanime.global/wp-content/uploads/2020/10/360236.jpg"
                                    class="absolute h-full w-full object-cover object-center"
                                />
                                <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1vw] text-white md:px-[1vw]">Yuuichi Nakamura</span>
                            </div>
                            <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-secondary/75 to-secondary/5"></div>
                        </div>
                        <div class="mt-[1vw] flex flex-col">
                            <div class="btn-group">
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">
                                    <Chevron class="w-[1vw] rotate-180"></Chevron>
                                </button>
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">01</button>
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">
                                    <Chevron class="w-[1vw]"></Chevron>
                                </button>
                            </div>
                            <span class="text-surface-50 mt-[0.5vw] text-[0.75vw] leading-none">Showing 1-5, out of 58 Voiceover div</span>
                        </div>
                    </div>
                </div>
                <div class="mt-[2.5vw] block">
                    <div class="flex gap-3">
                        <div class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">div</div>
                        <button class="bg-surface-400 btn btn-secondary min-h-full rounded p-0 md:h-[1.5vw] md:w-[1.5vw]">
                            <Settings class="w-[0.9vw] opacity-75"></Settings>
                        </button>
                    </div>
                    <div class="mt-[1vw] block">
                        <div class="grid grid-cols-2 gap-[0.75vw]">
                            <a
                                href="/myanimelist/1"
                                class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover bg-center"
                            >
                                <img
                                    alt=""
                                    src="https://cdn.myanimelist.net/images/anime/1958/107912.jpg"
                                    class="absolute h-full w-full object-cover object-center"
                                />
                                <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw] text-white">
                                    Yahari Ore no Seishun Love Come wa Machigatteiru.
                                </span>
                                <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-secondary/75 to-secondary/5"></div>
                            </a>
                            <a
                                href="/myanimelist/1"
                                class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover"
                            >
                                <img
                                    alt=""
                                    src="https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx849-uXOftsjBDz2T.png"
                                    class="absolute h-full w-full object-cover object-center"
                                />
                                <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw] text-white">
                                    Suzumiya Haruhi no Yuuutsu
                                </span>
                                <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-secondary/75 to-secondary/5"></div>
                            </a>
                        </div>
                        <div class="mt-[1vw] flex flex-col">
                            <div class="btn-group">
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">
                                    <Chevron class="w-[1vw] rotate-180"></Chevron>
                                </button>
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">01</button>
                                <button class="btn btn-secondary min-h-full p-0 md:h-[2vw] md:w-[2vw]">
                                    <Chevron class="w-[1vw]"></Chevron>
                                </button>
                            </div>
                            <span class="text-surface-50 mt-[0.5vw] text-[0.75vw] leading-none">Showing 1-8, out of 47 div</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
