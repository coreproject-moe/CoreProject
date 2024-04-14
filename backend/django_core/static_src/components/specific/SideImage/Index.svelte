<script lang="ts">
    import Refresh from "$icons/Refresh/Index.svelte";
    import CoreProject from "$icons/CoreProjectText/Index.svelte";

    import { afterUpdate, beforeUpdate } from "svelte";
    import JSON5 from "json5";
    import { blur } from "svelte/transition";
    import * as _ from "lodash-es";
    
    export let animes: string | null = null;

    type Anime = {
        name: string;
        cover: string;
    };

    let _anime: Anime[], picked_anime: Anime;

    beforeUpdate(() => {
        if (animes !== null && typeof animes === "string") {
            _anime = JSON5.parse(animes) satisfies typeof _anime;
        } else {
            throw new Error("`animes` not provided for `side-image`");
        }
    });
    afterUpdate(() => {
        get_random_anime();
    });

    const get_random_anime = () => {
        const array_without_element = picked_anime === undefined ? _anime : _anime.filter((item) => item !== picked_anime);
        const sample = _.sample(array_without_element);
        if (sample == undefined) {
            get_random_anime();
        } else {
            picked_anime = sample;
        }
    };
</script>

{#if picked_anime}
    <div class="h-dvh">
        {#key picked_anime}
            <img
                transition:blur
                src={picked_anime.cover}
                alt="{picked_anime.name} image"
                class="absolute h-full w-full object-cover transition-all"
            />
        {/key}
        <div class="absolute inset-0 bg-gradient-to-r from-secondary/75 to-secondary/50"></div>
        <backdrop class="absolute inset-0 bg-transparent duration-300"></backdrop>

        <div class="absolute inset-0 bottom-[6vw] hidden flex-col items-center justify-center text-center text-white md:flex">
            <span class="text-[0.9vw] font-semibold uppercase leading-none">welcome to</span>
            <CoreProject class="!mt-[0.5vw] !leading-none md:!text-[1.5vw]" />
            <span class="mt-[2.875vw] max-w-[22vw] text-[1.25vw] font-semibold leading-[1.75vw]">Bridging the gap between streaming and torrenting sites with a modern and clean interface.</span>
            <span class="mt-[4vw] text-[1vw] font-semibold leading-none">With a coreproject account, you can</span>
            <span class="text-surface-200 mt-[0.5vw] max-w-[22vw] text-[1vw] font-medium leading-[1vw]">continue on animecore, mangacore and soundcore with same account.</span>
        </div>
        <div class="absolute left-7 top-7 md:bottom-[1.85vw] md:left-[2vw] md:top-auto md:flex">
            <div class="flex flex-col gap-2 md:gap-[0.75vw]">
                <span class="text-[2.25vw] font-semibold uppercase leading-none tracking-widest text-white/75 md:text-[0.75vw]">Background from anime</span>
                <div class="grid">
                    {#key picked_anime}
                        <div
                            transition:blur
                            class="col-start-1 row-start-1 text-[3vw] font-bold uppercase leading-none tracking-widest text-warning md:text-[1vw]"
                        >
                            {picked_anime.name}
                            <button
                                on:click|preventDefault={() => {
                                    get_random_anime();
                                }}
                            >
                                <Refresh class="w-4 md:w-[1vw]" />
                            </button>
                        </div>
                    {/key}
                </div>
            </div>
        </div>
    </div>
{/if}
