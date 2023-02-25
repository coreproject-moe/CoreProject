<!-- https://www.figma.com/file/tNUUtsk20ltOrQICdEoggG/Core-Project?node-id=1875%3A2336&t=ZryTYMGAVmoLyR72-0 -->
<script lang="ts">
    export let data: Partial<{
        mal_id: number;
        episodes: [
            {
                episode_number: number;
            }
        ];
        title_english: string;
        title_japanese: string;
        anime_source: string;
        anime_aired_from: Date;
        anime_aired_to: Date;
        anime_cover: string; // Image
        anime_synopsis: string;
        anime_background: string;
        anime_rating: string;
        updated: Date;
    }>;
    import Navbar from "$components/shared/Navbar.svelte";
    import ScrollArea from "$components/shared/ScrollArea.svelte";
    import BookOpen from "$icons/Book-Open.svelte";
    import Download from "$icons/Download.svelte";
    import Edit from "$icons/Edit.svelte";
    import External from "$icons/External.svelte";
    import PlayCircle from "$icons/PlayCircle.svelte";
    import Settings from "$icons/Settings.svelte";
    import Share from "$icons/Share.svelte";
    import Star from "$icons/Star.svelte";
    import TrendingUp from "$icons/Trending-Up.svelte";
    import Video from "$icons/Video.svelte";
</script>

<div class="grid h-screen relative">
    <!-- Background Image Container -->
    <div
        class="bg-black h-[80vw] md:h-screen absolute top-0"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div
            class="h-[80vw] md:h-screen w-screen bg-no-repeat bg-center bg-cover brightness-50"
            style="background-image:url('{data?.anime_cover ?? ''}')"
        />
        <div
            class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
        />
    </div>

    <div class="h-screen grid absolute inset-0">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 md:pr-[72px] pl-6 md:pl-20 pb-0">
                    <Navbar />
                </div>
                <anime-info
                    class="flex justify-center items-center md:items-start gap-11 flex-col md:flex-row mt-12 md:mt-20"
                >
                    <div class="flex gap-7">
                        <!-- Anime image card  -->
                        <anime-image-card class="card w-36 md:w-52 h-48 md:h-72">
                            <img
                                class="rounded-lg"
                                src="https://media.kitsu.io/anime/poster_images/42420/large.jpg"
                                alt="Azure Lane"
                            />
                        </anime-image-card>

                        <!-- Anime info  -->
                        <anime-info class="flex flex-col gap-2">
                            <h1 class="text-white text-4xl font-bold">{data?.title_english}</h1>
                            <p class="text-neutral-400 text-sm">
                                <!-- Todo modify this to have anime synonyms  -->
                                <span class="items">{data?.title_japanese}</span>
                                <span class="items">Hyouka: Forbidden Secrets</span>
                            </p>
                            <p class="text-white text-xs">
                                <span class="items">TV</span>
                                <span class="items">22eps</span>
                                <span class="items">completed</span>
                                <span class="items">spring 2021</span>
                                <span class="items">kyoto</span>
                            </p>

                            <!-- buttons  -->
                            <div class="mt-7 hidden md:flex items-center gap-4">
                                <button
                                    aria-label="Play"
                                    class="btn btn-lg btn-primary rounded-lg w-[108px] h-[70px] normal-case"
                                >
                                    <div class="flex justify-between gap-2 py-2">
                                        <PlayCircle
                                            width={30}
                                            height={30}
                                            color="white"
                                            class="translate-y-1"
                                        />
                                        <div class="flex flex-col text-start">
                                            <h2 class="font-bold text-sm">Watch</h2>
                                            <p class="text-xs font-thin text-zinc-300">Ep 01</p>
                                        </div>
                                    </div>
                                </button>
                                <button
                                    aria-label="Play"
                                    class="btn btn-info btn-lg rounded-lg normal-case btn-square"
                                >
                                    <div class="flex flex-col justify-center items-center py-2">
                                        <BookOpen
                                            width="32"
                                            height="31"
                                            class="text-base-100"
                                        />
                                        <p>Read</p>
                                    </div>
                                </button>
                            </div>
                            <!-- Share button groups  -->
                            <div class="mt-5 gap-2 hidden md:flex">
                                <button
                                    class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                                >
                                    <Video
                                        width="18"
                                        height="18"
                                        class="text-base-100"
                                    />
                                </button>
                                <button
                                    class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                                >
                                    <Edit
                                        variant="with_underline_around_pencil"
                                        width="18"
                                        height="18"
                                        class="text-base-100"
                                    />
                                </button>
                                <button
                                    class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                                >
                                    <Download
                                        width="18"
                                        height="18"
                                        class="text-base-100"
                                    />
                                </button>
                                <button
                                    class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                                >
                                    <Share
                                        width="18"
                                        height="18"
                                        class="text-base-100"
                                    />
                                </button>
                            </div>
                        </anime-info>
                    </div>

                    <anime-synopsys>
                        <ScrollArea class="w-[410px] h-56 text-white">
                            <p class="nowrap">
                                {data?.anime_synopsis}
                            </p>
                        </ScrollArea>
                        <div class="flex gap-2 mt-3">
                            {#each ["mystery", "slice of life"] as tag}
                                <span
                                    class="badge text-white bg-base-100 badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                >
                                    {tag}
                                </span>
                            {/each}
                        </div>
                        <button
                            class="btn btn-sm  text-sm normal-case glass btn-disabled mt-5 gap-4 text-white flex-nowrap"
                            style="--glass-blur:20px;--glass-reflex-degree:360deg;--glass-reflex-opacity:0;--glass-opacity:10%"
                        >
                            <div>
                                <span>Score :</span>
                                <span class="text-warning">78</span>
                            </div>
                            <div>
                                <span>Status :</span>
                                <span class="text-warning">watching</span>
                            </div>
                            <div>
                                <span>Episode :</span>
                                <span class="text-warning">0/22</span>
                            </div>
                            <div>
                                <span>Your Score :</span>
                                <span class="text-warning">Not Rated</span>
                            </div>
                        </button>
                    </anime-synopsys>
                    <anime-ratings class="hidden md:flex flex-col">
                        <h1 class="text-white text-2xl font-bold mb-4">Ratings</h1>
                        <p>
                            <span class="text-white text-3xl font-bold">79%</span>
                            <span class="text-sm text-neutral-400">| 2.8k ratings</span>
                        </p>
                        <div class="divider w-[71px] color-[#D9D9D9]" />
                        <p class="my-1">
                            <span class="text-white text-xl">#86</span>
                            <span class="text-sm text-neutral-400">Most Popular All Time</span>
                        </p>
                        <p class="my-1">
                            <span class="text-white text-xl">#260</span>
                            <span class="text-sm text-neutral-400">Highest Rated Of All Time</span>
                        </p>

                        <button
                            class="btn bg-white hover:bg-white my-2 h-[26px] w-[170px] px-0 leading-none min-h-fit"
                        >
                            <div class="flex gap-2 justify-center items-center">
                                <div class="flex justify-center items-center">
                                    <TrendingUp
                                        class="translate-y-1 text-base-100"
                                        width="20"
                                        height="18"
                                    />
                                </div>
                                <p class="text-black normal-case whitespace-nowrap">
                                    Detailed Distribution
                                </p>
                            </div>
                        </button>

                        <p class="text-white mt-2">Your rating</p>
                        <star-container class="flex mt-2 items-center gap-2">
                            <stars class="flex">
                                <!-- Todo fix this star rating system -->
                                {#each Array(5) as _}
                                    <Star
                                        class="translate-y-1"
                                        width="25"
                                        height="25"
                                    />
                                {/each}
                            </stars>
                            <span class="font-bold nowrap text-lg">90 %</span>
                            <button class="btn btn-square btn-sm btn-info">
                                <Edit
                                    variant="without_underline_around_pencil"
                                    height="15"
                                    width="15"
                                />
                            </button>
                        </star-container>

                        <p class="mt-4 flex items-center text-white">
                            Add a review
                            <External
                                class="translate-y-1 ml-1"
                                width="18"
                                height="19"
                            />
                        </p>
                    </anime-ratings>
                </anime-info>
                <episode>
                    <div class="flex gap-1">
                        <h1 class="font-bond text-lg text-white">Episodes</h1>
                        <button class="btn btn-square btn-sm">
                            <Settings
                                class="translate-y-1"
                                color="white"
                                height="22"
                                width="22"
                            />
                        </button>
                    </div>

                    <episode-and-dub-container>available in</episode-and-dub-container>
                </episode>
            </div>
        </div>
    </div>
</div>

<style lang="scss">
    .items {
        &:not(:last-child)::after {
            content: " ▪ ";
        }
    }
</style>
