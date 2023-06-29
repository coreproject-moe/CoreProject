<script lang="ts">
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import { latest_animes } from "$data/mock/latest_animes";
    import CoreProject from "$icons/core_project.svelte";
    import Refresh from "$icons/refresh.svelte";
    import { Timer as EasyTimer } from "easytimer.js";
    import { beforeUpdate, onDestroy } from "svelte";
    import { blur } from "svelte/transition";

    // Constants
    let CHOICE: number;

    let timer = new EasyTimer({
        target: {
            seconds: 20
        },
        precision: "secondTenths"
    });

    timer.on("targetAchieved", () => {
        change_index();
    });

    const change_index = () => {
        const index = globalThis.Math.floor(globalThis.Math.random() * latest_animes.length);
        CHOICE = index;
        timer.isRunning() ? timer.reset() : timer.start();
    };

    // Run it before the UI is updated to show current behaviour
    beforeUpdate(() => {
        change_index();
    });

    onDestroy(() => {
        timer.stop();
    });
</script>

<root class="relative inline-grid h-full w-full md:grid-cols-2">
    {#each latest_animes as item, index}
        {#if index === CHOICE}
            <div
                class="relative col-start-1 col-end-2 row-start-1 row-end-2"
                transition:blur={{ duration: 500 }}
            >
                <ImageLoader
                    src={item.cover ?? ""}
                    class="absolute h-full w-full object-cover"
                />

                <div class="absolute inset-0 bg-gradient-to-r from-surface-900 to-surface-900/60" />
                <div class="absolute inset-0 bg-gradient-to-t from-surface-900/50 to-surface-900/0" />

                <div class="absolute inset-0 bottom-[6vw] hidden flex-col items-center justify-center text-center md:flex">
                    <span class="text-[0.75vw] font-semibold uppercase leading-none text-surface-50">welcome to</span>
                    <div class="mt-[0.75vw] flex items-center leading-none">
                        <CoreProject />
                        {#each ".moe".split("") as letter}
                            <span class="inline-flex text-[1.5vw] font-bold text-surface-300">{letter}</span>
                        {/each}
                    </div>
                    <span class="mt-[2.875vw] max-w-[22vw] text-[1.25vw] font-semibold leading-[1.75vw]">Bridging the gap between streaming and torrenting sites with a modern and clean interface.</span>

                    <span class="mt-[4vw] text-[0.9vw] font-semibold leading-none">With a coreproject account, you can</span>
                    <span class="mt-[1vw] max-w-[20.375vw] text-[0.9vw] font-medium leading-[1vw] text-surface-200">continue on animecore, mangacore and soundcore with same account.</span>
                </div>

                <div class="absolute bottom-[1.85vw] left-10 md:left-[2vw] md:flex">
                    <div class="flex flex-col gap-2 md:gap-[0.75vw]">
                        <span class="text-[2.25vw] font-semibold uppercase leading-none tracking-widest text-surface-300/75 md:text-[0.75vw]">Background from anime</span>
                        <div class="flex items-center gap-[2vw] md:gap-[0.5vw]">
                            <span class="text-[3vw] font-bold uppercase leading-none tracking-widest text-warning-400 md:text-[1vw]">
                                {item.name}
                            </span>
                            <button
                                class="btn p-0"
                                on:click={change_index}
                            >
                                <Refresh class="hidden w-[2vw] md:flex md:w-[0.8vw]" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        {/if}
    {/each}
    <div class="z-0 col-start-1 col-end-1 row-start-1 row-end-1 flex items-center justify-center md:col-start-2 md:col-end-2 md:block md:items-end md:px-[8vw] md:py-[2.2vw]">
        <slot />
    </div>
</root>

<style lang="postcss">
    :global(#page) {
        @apply overflow-y-hidden;
    }
</style>
