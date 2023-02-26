<script lang="ts">
    import Search from "$icons/Search.svelte";
    import Settings from "$icons/Settings.svelte";

    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

{#if !mobile}
    <episode class="flex justify-between mt-24">
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
                    <p class="font-bold text-white flex justify-center items-center">
                        <span class="text-3xl">23</span>
                        episodes
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
        <div class="flex w-full justify-end -translate-x-40">
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

        <episode-details class="flex flex-col text-white">
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
        </episode-details>
    </episode>
{/if}
