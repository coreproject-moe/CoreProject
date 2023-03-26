<script lang="ts">
    export let episodes: Array<{
        id: number;
        episode_number: number;
        episode_name: string;
        episode_thumbnail: string;
        episode_length: number;
        episode_summary: string;
        providers: Array<object>;
    }>;
    export let backend_anime_number: number;
    import { UrlMaps } from "$data/urls";
    import { formatTime } from "$functions/formatTime";

    import List from "$icons/List.svelte";
    import MoreVertical from "$icons/MoreVertical.svelte";
    import Search from "$icons/Search.svelte";
    import Settings from "$icons/Settings.svelte";
    import { responsiveMode } from "$store/Responsive";

    import EpisodeCard from "./EpisodeCard.svelte";

    const backend_urls = new UrlMaps();
</script>

<!-- Mobile version  -->
<div class="mt-10 flex w-full flex-col text-white md:mt-0 md:hidden">
    <span class="text-2xl font-bold">Episodes</span>
    <div class="divider before:bg-white after:bg-white" />
    <div class="flex justify-between">
        <div class="flex text-xl font-bold">
            {episodes.length} Episodes
        </div>
        <div class="flex gap-4">
            <div>
                <List
                    width="30"
                    height="30"
                    color="white"
                />
            </div>
            <div>
                <Search
                    width="20"
                    height="20"
                    color="white"
                />
            </div>
        </div>
    </div>
    {#each episodes as episode}
        {@const url = backend_urls.DOMAIN + episode.episode_thumbnail}
        {@const formated_date = new formatTime(episode.episode_length)}
        <a href="../backend/{backend_anime_number}/episode/{episode.episode_number}">
            <div class="relative my-4 flex h-16 w-[90vw] items-center rounded-lg bg-[#1E2036]">
                <img
                    class="mask mask-squircle mx-4 h-10 w-10"
                    src={url}
                    alt={episode.episode_name}
                />
                <div class="flex flex-col">
                    <span class="font-bold">Episode {episode.episode_number}</span>
                    <span>{formated_date.formatSecondsToTimeStampDuration}</span>
                </div>
                <MoreVertical
                    class="absolute right-5"
                    width="30"
                    height="30"
                />
            </div>
        </a>
    {/each}
</div>
<!-- Desktop version  -->
<div class="hidden w-4/5 flex-col md:flex">
    <div class="flex">
        <div>
            <div class="flex gap-1">
                <h1 class="font-bond text-lg text-white">Episodes</h1>
                <button class="btn-square btn-sm btn">
                    <Settings
                        class="translate-y-0.5"
                        color="white"
                        height="22"
                        width="22"
                    />
                </button>
            </div>
            <episode-and-dub-container class="mt-12 flex gap-4">
                <div class="flex gap-3">
                    <p class="flex items-center justify-center gap-2 font-bold text-white">
                        <span class="text-3xl">{episodes.length}</span>
                        <span>episodes</span>
                    </p>
                    <div class="flex items-center justify-center text-white">▪</div>

                    <div class="flex items-center justify-center">
                        <div class="flex flex-col gap-2">
                            <span class="text-white">
                                available in <span
                                    style="display: inline-block; width: 60px; border-top: 1px solid; border-radius: 10px;"
                                />
                            </span>
                            <span class="flex gap-3">
                                <span
                                    class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6 text-white"
                                >
                                    Sub
                                </span>
                                <span
                                    class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6 text-white"
                                >
                                    Dub
                                </span>
                            </span>
                        </div>
                    </div>
                    <div class="flex items-center justify-center text-white">▪</div>
                    <div class="flex items-center justify-center gap-3">
                        <span
                            class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6 text-white"
                        >
                            1080
                        </span>
                        <span
                            class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6 text-white"
                        >
                            720
                        </span>
                        <span
                            class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6 text-white"
                        >
                            480
                        </span>
                    </div>
                </div>
            </episode-and-dub-container>
        </div>
        <div class="flex w-full justify-end">
            <div class="flex justify-center gap-5 text-white">
                <div class="flex w-[135px] flex-col">
                    <span>Type</span>
                    <select class="select mt-2 w-full bg-neutral">
                        <option value="Subbed">Subbed</option>
                    </select>
                </div>
                <div class="flex w-[135px] flex-col">
                    <span>Display</span>
                    <select class="select mt-2 w-full bg-neutral">
                        <option value="Thumbnails">Thumbnails</option>
                    </select>
                </div>
                <div class="flex translate-y-8">
                    <button class="btn-square btn">
                        <Search
                            width="16"
                            height="16"
                            class="text-white"
                        />
                    </button>
                </div>
            </div>
        </div>
    </div>
    <div class="mt-10 grid grid-cols-3 gap-x-20 gap-y-10">
        {#each episodes as episode}
            {@const url = backend_urls.DOMAIN + episode.episode_thumbnail}
            {@const name = episode.episode_name}
            {@const number = episode.episode_number}
            {@const duration = episode.episode_length}
            <EpisodeCard
                {backend_anime_number}
                episode_card_background_image={url}
                episode_name={name}
                episode_duration={duration}
                episode_number={number}
            />
        {/each}
    </div>
</div>
