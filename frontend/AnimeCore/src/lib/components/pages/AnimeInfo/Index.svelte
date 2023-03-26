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
        average_episode_length: number;
    }>;

    import StarRating from "svelte-star-rating";
    import isEmpty from "lodash.isempty";

    import Navbar from "$components/shared/Navbar.svelte";
    import ScrollArea from "$components/shared/ScrollArea.svelte";
    import { UrlMaps } from "$data/urls";
    import Bookmark from "$icons/Bookmark.svelte";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Circle from "$icons/Circle.svelte";
    import Edit from "$icons/Edit.svelte";
    import External from "$icons/External.svelte";
    import Heart from "$icons/Heart.svelte";
    import Settings from "$icons/Settings.svelte";
    import TrendingUp from "$icons/Trending-Up.svelte";

    import AnimeInfo from "./AnimeInfo/AnimeInfo.svelte";
    import EpisodeSkeleton from "./Skeletons/Episode.svelte";
    import Episode from "./Episodes/Episode.svelte";
    import { formatTime } from "$functions/formatTime";
    import { formatDate } from "$functions/formatDate";

    const urls = new UrlMaps();

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

    const formated_aired_from = new formatDate(String(data?.anime_aired_from));
    const formated_aired_to = new formatDate(String(data?.anime_aired_to));

    const details_mapping = [
        data?.episodes_count ?? { Episodes: data?.episodes_count },
        data?.average_episode_length ?? {
            // Average episode duration
            "Episode Duration": `${
                new formatTime(Number(data?.average_episode_length)).formatSecondsToMinutes
            } minutes`
        },
        { Status: "Finished" },
        data?.anime_aired_from
            ? { "Start Date": formated_aired_from.formatToHumanReadableForm }
            : {},
        data?.anime_aired_to ? { "End Date": formated_aired_to.formatToHumanReadableForm } : {},
        data?.anime_aired_from ? { Season: formated_aired_from.formatToSeason } : {},
        { Studios: "" },
        { Producers: [] },
        { Source: [] },
        { Tags: [] }
    ];
</script>

<div class="relative grid h-screen overflow-x-hidden">
    <!-- Background Image Container -->
    <div
        class="absolute top-0 h-[80vw] bg-black md:h-screen"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div
            class="h-[80vw] w-screen bg-cover bg-center bg-no-repeat brightness-50 md:h-screen"
            style="background-image:url('{anime_background_image}')"
        />
        <div
            class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
        />
    </div>

    <div class="absolute inset-0 grid h-screen w-screen">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 pl-6 pb-0 md:pr-[72px] md:pl-20">
                    <Navbar />
                </div>
                <div class="mx-6 mt-12 flex flex-col md:mx-20 md:mt-20">
                    <anime-info
                        class="flex flex-col items-center justify-between gap-3 md:flex-row md:items-start"
                    >
                        <div class="flex gap-7 self-start">
                            <!-- Anime image card  -->
                            <anime-image-card
                                class="card flex h-[150px] w-[100px] md:h-[300px] md:w-[200px]"
                            >
                                <img
                                    class="rounded-lg object-contain"
                                    width={200}
                                    height={300}
                                    src={anime_card_image}
                                    alt="${data?.title_english} banner image"
                                />
                            </anime-image-card>

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

                        <div class="mt-10 flex gap-2 self-start md:mt-0 md:hidden">
                            <button class="btn-info btn-sm btn normal-case">
                                <div class="align-center flex justify-center gap-3">
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
                            <button class="btn-info btn-square btn-sm btn">
                                <Bookmark
                                    width="16"
                                    height="16"
                                />
                            </button>
                            <button class="btn-info btn-square btn-sm btn">
                                <Heart
                                    color="#FF8796"
                                    width="16"
                                    height="16"
                                />
                            </button>
                        </div>

                        <anime-synopsys class="mt-10 md:mt-0">
                            <ScrollArea
                                class="h-56 text-white"
                                offsetScrollbar={true}
                            >
                                <p class="nowrap">
                                    {data?.anime_synopsis}
                                </p>
                            </ScrollArea>
                            <div class="hidden flex-row gap-2 pt-5 md:flex">
                                {#await genres(String(data?.genres))}
                                    <div class="flex animate-pulse space-x-4">
                                        {#each Array(5) as _}
                                            <div
                                                class="badge badge-lg w-14 rounded-md border-transparent bg-base-100 text-sm font-bold capitalize leading-6 text-white"
                                            />
                                        {/each}
                                    </div>
                                {:then value}
                                    {#if value}
                                        {#each value as item}
                                            <span
                                                class="badge badge-lg rounded-md border-transparent bg-base-100 text-sm font-bold capitalize leading-6 text-white"
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
                                class="btn-disabled glass  btn-sm btn mt-5 hidden flex-nowrap gap-4 text-sm normal-case text-white md:flex"
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
                        <anime-ratings class="hidden !w-[240px] flex-col md:flex">
                            <h1 class="mb-4 text-2xl font-bold text-white">Ratings</h1>
                            <p>
                                <span class="text-3xl font-bold text-white">79%</span>
                                <span class="text-sm text-neutral-400">| 2.8k ratings</span>
                            </p>
                            <div class="divider w-[71px]" />
                            <p class="my-1">
                                <span class="text-xl text-white">#86</span>
                                <span class="text-sm text-neutral-400">Most Popular All Time</span>
                            </p>
                            <p class="my-1">
                                <span class="text-xl text-white">#260</span>
                                <span class="text-sm text-neutral-400">
                                    Highest Rated Of All Time
                                </span>
                            </p>

                            <button
                                class="btn my-2 h-[26px] min-h-fit w-[170px] bg-white px-0 leading-none hover:bg-white"
                            >
                                <div class="flex items-center justify-center gap-2">
                                    <div class="flex items-center justify-center">
                                        <TrendingUp
                                            class="translate-y-1 text-base-100"
                                            width="20"
                                            height="18"
                                        />
                                    </div>
                                    <p class="whitespace-nowrap normal-case text-black">
                                        Detailed Distribution
                                    </p>
                                </div>
                            </button>

                            <p class="mt-2 text-white">Your rating</p>
                            <star-container class="mt-2 flex flex-nowrap items-center gap-2">
                                <stars class="flex translate-y-1">
                                    <StarRating
                                        rating={Number(data?.anime_rating ?? 0)}
                                        config={{ fullColor: "white" }}
                                    />
                                </stars>
                                <p class="nowrap w-12 text-lg font-bold">
                                    {(100 / 5) * Number(data?.anime_rating ?? 0)} %
                                </p>
                                <button class="btn-info btn-square btn-sm btn">
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
                                    class="ml-1 translate-y-1"
                                    width="18"
                                    height="19"
                                />
                            </p>
                        </anime-ratings>
                    </anime-info>
                    <div
                        class="mt-24 flex flex-col items-center justify-between gap-3 md:flex-row md:items-start"
                    >
                        {#await episodes(String(data?.episodes))}
                            <EpisodeSkeleton />
                        {:then episodes}
                            <Episode
                                backend_anime_number={Number(data?.id)}
                                {episodes}
                            />
                        {:catch}
                            <div class="flex" />
                        {/await}

                        <episode-details
                            class="hidden !w-[221px] flex-col items-start justify-center gap-6 text-white md:flex"
                        >
                            <p class="flex gap-2">
                                <span class="text-xl font-bold">Details</span>
                                <button class="btn-square btn-sm btn">
                                    <Settings
                                        class="translate-y-0.5"
                                        color="white"
                                        height="22"
                                        width="22"
                                    />
                                </button>
                            </p>
                            {#each details_mapping as item}
                                {#if !isEmpty(item)}
                                    <div class="flex flex-col">
                                        <span class="font-bold capitalize">
                                            {Object.keys(item)}
                                        </span>
                                        <span class="capitalize">{Object.values(item)}</span>
                                    </div>
                                {/if}
                            {/each}
                        </episode-details>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
