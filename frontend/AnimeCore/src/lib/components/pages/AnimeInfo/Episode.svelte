<script lang="ts">
    export let episodes: Array<{
        id: number;
        episode_number: number;
        episode_name: string;
        episode_thumbnail: string;
        episode_summary: string;
        providers: Array<object>;
    }>;
    import { UrlMaps } from "$data/urls";
    import Search from "$icons/Search.svelte";
    import Settings from "$icons/Settings.svelte";
    import EpisodeCard from "./EpisodeCard.svelte";
    import { responsiveMode } from "$store/Responsive";

    const backend_urls = new UrlMaps();
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    const details_mapping = [
        { Episodes: 22 },
        { "Episode Duration": "26 mins" },
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

{#if !mobile}
    <div class="flex justify-between items-center md:items-start gap-3 flex-col md:flex-row mt-24">
        <div class="flex w-4/5 flex-col">
            <div class="flex">
                <div>
                    <div class="flex gap-1">
                        <h1 class="font-bond text-lg text-white">Episodes</h1>
                        <button class="btn btn-square btn-sm">
                            <Settings
                                class="translate-y-0.5"
                                color="white"
                                height="22"
                                width="22"
                            />
                        </button>
                    </div>
                    <episode-and-dub-container class="flex gap-4 mt-12">
                        <div class="flex gap-3">
                            <p class="font-bold text-white flex gap-2 justify-center items-center">
                                <span class="text-3xl">{episodes.length}</span>
                                <span>episodes</span>
                            </p>
                            <div class="text-white flex justify-center items-center">▪</div>

                            <div class="flex justify-center items-center">
                                <div class="flex flex-col gap-2">
                                    <span class="text-white">
                                        available in <span
                                            style="display: inline-block; width: 60px; border-top: 1px solid; border-radius: 10px;"
                                        />
                                    </span>
                                    <span class="flex gap-3">
                                        <span
                                            class="badge text-white bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                        >
                                            Sub
                                        </span>
                                        <span
                                            class="badge text-white bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                        >
                                            Dub
                                        </span>
                                    </span>
                                </div>
                            </div>
                            <div class="text-white flex justify-center items-center">▪</div>
                            <div class="flex justify-center items-center gap-3">
                                <span
                                    class="badge text-white bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                >
                                    1080
                                </span>
                                <span
                                    class="badge text-white bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                >
                                    720
                                </span>
                                <span
                                    class="badge text-white bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                >
                                    480
                                </span>
                            </div>
                        </div>
                    </episode-and-dub-container>
                </div>
                <div class="flex w-full justify-end">
                    <div class="flex justify-center text-white gap-5">
                        <div class="flex flex-col w-[135px]">
                            <span>Type</span>
                            <select class="mt-2 select w-full bg-neutral">
                                <option value="Subbed">Subbed</option>
                            </select>
                        </div>
                        <div class="flex flex-col w-[135px]">
                            <span>Display</span>
                            <select class="mt-2 select w-full bg-neutral">
                                <option value="Thumbnails">Thumbnails</option>
                            </select>
                        </div>
                        <div class="flex translate-y-8">
                            <button class="btn btn-square">
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
            <div class="grid gap-x-20 gap-y-10 grid-cols-3 mt-10">
                {#each episodes as episode}
                    {@const url = backend_urls.DOMAIN + episode.episode_thumbnail}
                    {@const name = episode.episode_name}
                    {@const number = episode.episode_number}
                    <EpisodeCard
                        episode_card_background_image={url}
                        episode_name={name}
                        episode_number={number}
                    />
                {/each}
            </div>
        </div>
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
    </div>
{/if}
