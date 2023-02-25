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
    import Download from "$icons/Download.svelte";
    import Edit from "$icons/Edit.svelte";
    import External from "$icons/External.svelte";
    import Play from "$icons/Play.svelte";
    import PlayCircle from "$icons/PlayCircle.svelte";
    import Share from "$icons/Share.svelte";
    import Star from "$icons/Star.svelte";
    import TrendingUp from "$icons/Trending-Up.svelte";
    import Video from "$icons/Video.svelte";
</script>

<div class="grid h-screen relative">
    <!-- Background Image Container -->
    <div
        class="bg-black h-screen absolute top-0"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div
            class="h-screen w-screen bg-no-repeat bg-center bg-cover brightness-50"
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
                <div class="flex justify-center gap-11">
                    <!-- Anime image card  -->
                    <anime-image-card class="card w-52 h-72">
                        <img
                            class="rounded-lg"
                            src="https://media.kitsu.io/anime/poster_images/42420/large.jpg"
                            alt="Azure Lane"
                        />
                    </anime-image-card>

                    <!-- Anime info  -->
                    <anime-info class="flex flex-col gap-2">
                        <h1 class="text-white text-4xl font-bold">Hyouka</h1>
                        <p class="text-neutral-400 text-sm">
                            <span class="items">氷菓</span>
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
                        <div class="mt-7 btn-group">
                            <button
                                aria-label="Play"
                                class="btn btn-md md:btn-lg btn-primary rounded-[16px]"
                            >
                                <div class="flex justify-between gap-2 py-2">
                                    <PlayCircle
                                        width={30}
                                        height={30}
                                        color="white"
                                    />
                                    <div class="flex flex-col text-start gap-1 ">
                                        <h2 class="font-bold">Watch</h2>
                                        <p class="text-xs normal-case">Ep 01</p>
                                    </div>
                                </div>
                            </button>
                        </div>
                        <!-- Share button groups  -->
                        <div class="mt-5 flex gap-2 ">
                            <button
                                class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                            >
                                <Video
                                    width="18"
                                    height="18"
                                    color="black"
                                />
                            </button>
                            <button
                                class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                            >
                                <Edit
                                    variant="with_underline_around_pencil"
                                    width="18"
                                    height="18"
                                    color="black"
                                />
                            </button>
                            <button
                                class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                            >
                                <Download
                                    width="18"
                                    height="18"
                                    color="black"
                                />
                            </button>
                            <button
                                class="btn btn-sm btn-square btn-warning flex justify-center items-center"
                            >
                                <Share
                                    width="18"
                                    height="18"
                                    color="black"
                                />
                            </button>
                        </div>
                    </anime-info>

                    <anime-synopsys>
                        <p class="w-80">
                            Energy-conservative high school student Houtarou Oreki ends up with more
                            than he bargained for when he signs up for the Classics Club at his
                            sister's behest—especially when he realizes how deep-rooted the club's
                            history really is. Begrudgingly, Oreki is dragged into an investigation
                            concerning the 45-year-old mystery that surrounds the club room.
                            Accompanied by his fellow club members, the knowledgeable Satoshi
                            Fukube, the stern but benign Mayaka Ibara, and the ever-curious Eru
                            Chitanda, Oreki must combat deadlines and lack of information with
                            resourcefulness and hidden talent, in order to not only find the truth
                            buried beneath the dust of works created years before them, but of other
                            small side cases as well. Based on the award-winning Koten-bu light
                            novel series, and directed by Yasuhiro Takemoto of Suzumiya Haruhi no
                            Shoushitsu, Hyouka shows that normal life can be full of small
                            mysteries, be it family history, a student film, or even the withered
                            flowers that make up a ghost story. Energy-conservative high school
                            student Houtarou Oreki ends up with more than he bargained for when he
                            signs up for the Classics Club at his sister's behest—especially when he
                            realizes how deep-rooted the club's history really is. Begrudgingly,
                            Oreki is dragged into an investigation concerning the 45-year-old
                            mystery that surrounds the club room. Accompanied by his fellow club
                            members, the knowledgeable Satoshi Fukube, the stern but benign Mayaka
                            Ibara, and the ever-curious Eru Chitanda, Oreki must combat deadlines
                            and lack of information with resourcefulness and hidden talent, in order
                            to not only find the truth buried beneath the dust of works created
                            years before them, but of other small side cases as well. Based on the
                            award-winning Koten-bu light novel series, and directed by Yasuhiro
                            Takemoto of Suzumiya Haruhi no Shoushitsu, Hyouka shows that normal life
                            can be full of small mysteries, be it family history, a student film, or
                            even the withered flowers that make up a ghost story.
                        </p>
                    </anime-synopsys>
                    <anime-ratings class="flex flex-col">
                        <h1 class="text-white text-2xl font-bold mb-4">Ratings</h1>
                        <p>
                            <span class="text-white text-3xl font-bold">79%</span>
                            <span class="text-sm">| 2.8k ratings</span>
                        </p>
                        <div class="divider w-[71px] color-[#D9D9D9]" />
                        <p class="my-1">
                            <span class="text-white text-xl">#86</span>
                            <span class="text-sm">Most Popular All Time</span>
                        </p>
                        <p class="my-1">
                            <span class="text-white text-xl">#260</span>
                            <span class="text-sm">Highest Rated Of All Time</span>
                        </p>

                        <button
                            class="btn bg-white hover:bg-white my-2 h-[26px] w-[170px] px-0 leading-none min-h-fit"
                        >
                            <div class="flex gap-2 justify-center items-center">
                                <div class="flex justify-center items-center">
                                    <TrendingUp
                                        class="translate-y-1"
                                        width="20"
                                        height="18"
                                        color="black"
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
                </div>
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
