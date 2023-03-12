<!-- https://www.figma.com/file/tNUUtsk20ltOrQICdEoggG/Core-Project?node-id=1875%3A2336&t=ZryTYMGAVmoLyR72-0 -->
<script lang="ts">
    export let data: Partial<{
        id: number;
        mal_id: number;
        title_english: string;
        title_japanese: string;
        anime_source: string;
        anime_aired_from: string;
        anime_aired_to: string;
        anime_banner: string; // image
        anime_cover: string; // Image
        anime_synopsis: string;
        anime_background: string;
        anime_rating: string;
        genres: string;
        episodes: string;
        episodes_count: number;
    }>;

    import { UrlMaps } from "$data/urls";
    import Navbar from "$components/shared/Navbar.svelte";
    import ScrollArea from "$components/shared/ScrollArea.svelte";
    import Bookmark from "$icons/Bookmark.svelte";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Circle from "$icons/Circle.svelte";
    import Edit from "$icons/Edit.svelte";
    import External from "$icons/External.svelte";
    import Heart from "$icons/Heart.svelte";

    import TrendingUp from "$icons/Trending-Up.svelte";
    import { responsiveMode } from "$store/Responsive";

    import AnimeInfo from "./AnimeInfo.svelte";
    import ImageCard from "./ImageCard.svelte";
    import Episode from "./Episode.svelte";
    import EpisodeSkeleton from "./Episode.skeleton.svelte";
    import StarRating from "svelte-star-rating";
    import Settings from "$icons/Settings.svelte";

    const urls = new UrlMaps();
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    const anime_card_image = urls.DOMAIN + String(data?.anime_banner);
    const anime_background_image = urls.DOMAIN + String(data?.anime_cover);

    const genres = async (url: string) => {
        const res = await fetch(urls.DOMAIN + url);
        if (!res.ok) {
            throw new Error("Failed to fetch genres" + res.status);
        }
        const res_json = await res.json();
        const data: Array<{
            id: number;
            mal_id: number;
            name: string;
            type: string;
        }> = res_json;
        return data;
    };

    const episodes = async (url: string) => {
        const res = await fetch(urls.DOMAIN + url);
        if (!res.ok) {
            throw new Error("Failed to fetch episodes" + res.status);
        }
        const res_json = await res.json();
        const data: Array<{
            id: number;
            episode_number: number;
            episode_name: string;
            episode_thumbnail: string;
            episode_length: number;
            episode_summary: string;
            providers: Array<object>;
        }> = res_json;
        return data;
    };

    const details_mapping = [
        { Episodes: 22 },
        { "Episode Duration": 0 },
        { Status: "Finished" },
        { "Start Date": "" },
        { "End Date": "" },
        { Season: "" },
        { Studios: "" },
        { Producers: [] },
        { Source: [] },
        { Tags: [] }
    ];
</script>

<div class="grid h-screen relative overflow-x-hidden">
    <!-- Background Image Container -->
    <div
        class="bg-black h-[80vw] md:h-screen absolute top-0"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div
            class="h-[80vw] md:h-screen w-screen bg-no-repeat bg-center bg-cover brightness-50"
            style="background-image:url('{anime_background_image}')"
        />
        <div
            class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
        />
    </div>

    <div class="h-screen grid w-screen absolute inset-0">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 md:pr-[72px] pl-6 md:pl-20 pb-0">
                    <Navbar />
                </div>
                <div class="flex flex-col mt-12 md:mt-20 mx-6 md:mx-20">
                    <anime-info
                        class="flex justify-between items-center md:items-start gap-3 flex-col md:flex-row"
                    >
                        <div class="flex gap-7 self-start">
                            <!-- Anime image card  -->
                            <ImageCard
                                src={anime_card_image}
                                alt={`${data?.title_english} image`}
                            />

                            <!-- Anime info  -->
                            <AnimeInfo
                                title_english={data?.title_english ?? ""}
                                title_japanese={data?.title_japanese ?? ""}
                                anime_source={data?.anime_source ?? ""}
                                episodes={Number(data?.episodes_count)}
                                status={data?.anime_aired_to ? "completed" : "airing"}
                                aired_from={data?.anime_aired_to ?? ""}
                            />
                        </div>

                        {#if mobile}
                            <div class="flex self-start gap-2 mt-10 md:mt-0">
                                <button class="btn btn-sm btn-info normal-case">
                                    <div class="flex justify-center align-center gap-3">
                                        <span class="w-2 translate-y-1">
                                            <Circle color="#6FCF97" />
                                        </span>
                                        <span class="font-bold">Watching</span>
                                        <span class="w-2">
                                            <ChevronDown
                                                width="16"
                                                height="16"
                                                class="text-base-100"
                                            />
                                        </span>
                                    </div>
                                </button>
                                <button class="btn btn-sm btn-info btn-square">
                                    <Bookmark
                                        width="16"
                                        height="16"
                                    />
                                </button>
                                <button class="btn btn-sm btn-info btn-square">
                                    <Heart
                                        color="#FF8796"
                                        width="16"
                                        height="16"
                                    />
                                </button>
                            </div>
                        {/if}

                        <anime-synopsys class="md:mt-0 mt-10">
                            <ScrollArea
                                class="h-56 text-white"
                                offsetScrollbar={true}
                            >
                                <p class="nowrap">
                                    {data?.anime_synopsis}
                                </p>
                            </ScrollArea>
                            <div class="hidden md:flex gap-2 flex-row pt-5">
                                {#await genres(String(data?.genres))}
                                    <div class="animate-pulse flex space-x-4">
                                        {#each Array(5) as _}
                                            <div
                                                class="w-14 badge text-white bg-base-100 badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                            />
                                        {/each}
                                    </div>
                                {:then value}
                                    {#if value}
                                        {#each value as item}
                                            <span
                                                class="badge text-white bg-base-100 badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                            >
                                                {item.name}
                                            </span>
                                        {/each}
                                    {/if}
                                {:catch}
                                    <nothing />
                                {/await}
                            </div>
                            <button
                                class="btn btn-sm  text-sm normal-case glass btn-disabled mt-5 gap-4 text-white flex-nowrap hidden md:flex"
                                style="--glass-blur:20px;--glass-reflex-degree:90deg;--glass-reflex-opacity:0;--glass-opacity:10%"
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
                                    <span class="text-warning">
                                        0/{data?.episodes_count}
                                    </span>
                                </div>
                                <div>
                                    <span>Your Score :</span>
                                    <span class="text-warning">Not Rated</span>
                                </div>
                            </button>
                        </anime-synopsys>
                        {#if !mobile}
                            <anime-ratings class="flex flex-col !w-[240px]">
                                <h1 class="text-white text-2xl font-bold mb-4">Ratings</h1>
                                <p>
                                    <span class="text-white text-3xl font-bold">79%</span>
                                    <span class="text-sm text-neutral-400">| 2.8k ratings</span>
                                </p>
                                <div class="divider w-[71px] color-[#D9D9D9]" />
                                <p class="my-1">
                                    <span class="text-white text-xl">#86</span>
                                    <span class="text-sm text-neutral-400">
                                        Most Popular All Time
                                    </span>
                                </p>
                                <p class="my-1">
                                    <span class="text-white text-xl">#260</span>
                                    <span class="text-sm text-neutral-400">
                                        Highest Rated Of All Time
                                    </span>
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
                                <star-container class="flex mt-2 items-center gap-2 flex-nowrap">
                                    <stars class="flex translate-y-1">
                                        <StarRating
                                            rating={Number(data?.anime_rating ?? 0)}
                                            config={{ fullColor: "white" }}
                                        />
                                    </stars>
                                    <p class="font-bold nowrap text-lg w-12">
                                        {(100 / 5) * Number(data?.anime_rating ?? 0)} %
                                    </p>
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
                        {/if}
                    </anime-info>
                    <div
                        class="flex justify-between items-center md:items-start gap-3 flex-col md:flex-row mt-24"
                    >
                        {#await episodes(String(data?.episodes))}
                            {#if !mobile}
                                <EpisodeSkeleton />
                            {/if}
                        {:then episodes}
                            <Episode
                                backend_anime_number={Number(data?.id)}
                                {episodes}
                            />
                        {:catch}
                            <div class="flex" />
                        {/await}
                        {#if !mobile}
                            <episode-details
                                class="flex flex-col text-white justify-center items-start !w-[221px] gap-6"
                            >
                                <p class="flex gap-2">
                                    <span class="font-bold text-xl">Details</span>
                                    <button class="btn btn-square btn-sm">
                                        <Settings
                                            class="translate-y-0.5"
                                            color="white"
                                            height="22"
                                            width="22"
                                        />
                                    </button>
                                </p>
                                {#each details_mapping as item}
                                    <div class="flex flex-col">
                                        <span class="font-bold">{Object.keys(item)}</span>
                                        <span>{Object.values(item)}</span>
                                    </div>
                                {/each}
                            </episode-details>
                        {/if}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
