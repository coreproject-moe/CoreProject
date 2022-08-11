<script lang="ts">
    import { blur } from "svelte/transition";

    import GenreSlide from "$components/pages/Home/Genre/Slide.svelte";
    import LibrarySlide from "$components/pages/Home/Library/Slide.svelte";
    import MainHeroSlide from "$components/pages/Home/MainHero/Slide.svelte";
    import data from "$data/mock/main_hero_data.json";

    let mainHeroSlideActiveIndex = 0;
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div
    class="h-screen w-screen carousel carousel-vertical text-white"
    style="overscroll-behavior-block: contain"
>
    <div class="carousel-item h-auto w-auto inline-grid">
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
    <div class="carousel-item h-auto w-auto">
        <GenreSlide />
    </div>
    <div class="carousel-item h-auto w-auto">
        <LibrarySlide />
    </div>
</div>
