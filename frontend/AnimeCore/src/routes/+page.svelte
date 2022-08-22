<script lang="ts">
    import { blur } from "svelte/transition";

    import GenreSlide from "$components/pages/Home/Genre/Slide.svelte";
    import LibrarySlide from "$components/pages/Home/Library/Slide.svelte";
    import MainHeroSlide from "$components/pages/Home/MainHero/Slide.svelte";
    import data from "$data/mock/main_hero_data.json";
    import { timer as timerStore } from "$store/Timer";

    let mainHeroSlideActiveIndex = 0;
    let mainHeroRootElement: HTMLElement;
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div
    class="h-screen w-screen carousel carousel-vertical snap-none md:snap-y md:snap-mandatory text-white"
    on:scroll={() => {
        console.log(mainHeroRootElement);
        if (
            Number(mainHeroRootElement?.getBoundingClientRect().top) < -140
            // Number(mainHeroRootElement?.getBoundingClientRect().
        ) {
            $timerStore = "pause";
        } else {
            $timerStore = "reset";
        }
    }}
>
    <div class="carousel-item h-auto w-auto">
        <div class="inline-grid" bind:this={mainHeroRootElement}>
            {#each data as item, index}
                {#if index === mainHeroSlideActiveIndex}
                    <div transition:blur|local style="grid-area: 1 / 1 / 2 / 2">
                        <MainHeroSlide
                            bind:mainHeroSlideActiveIndex
                            {data}
                            animeTitle={item.animeTitle}
                            animeSummary={item.animeSummary}
                            animeEpisodeCount={item.animeEpisodeCount}
                            animeStudio={item.animeStudio}
                            animeAirTime={item.animeAirTime}
                            backgroundImage={item.backgroundImage}
                            backgroundBanner={item.backgroundBanner}
                            tags={item.tags}
                        />
                    </div>
                {/if}
            {/each}
        </div>
    </div>
    <div class="carousel-item h-auto w-auto">
        <GenreSlide />
    </div>
    <div class="carousel-item h-auto">
        <LibrarySlide />
    </div>
</div>
