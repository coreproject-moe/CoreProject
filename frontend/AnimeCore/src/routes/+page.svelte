<script lang="ts">
    import { detect } from "detect-browser";
    import { blur } from "svelte/transition";
    import { swipe } from "svelte-gestures";

    import ExploreSlide from "$components/pages/Home/Explore/Slide.svelte";
    import GenreSlide from "$components/pages/Home/Genre/Slide.svelte";
    import LibrarySlide from "$components/pages/Home/Library/Slide.svelte";
    import MainHeroSlide from "$components/pages/Home/MainHero/Slide.svelte";
    import data from "$data/mock/main_hero_data.json";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { timer as timerStore } from "$store/Timer";
    const browser = detect();

    let mainHeroSlideActiveIndex = 0;
    let mainHeroRootElement: HTMLElement;

    const addOneToMainHeroSlideActiveIndex = () => {
        // Remove the previous image
        $navbar_variant = "";

        if (mainHeroSlideActiveIndex + 1 === data.length) {
            mainHeroSlideActiveIndex = 0;
            return;
        }
        mainHeroSlideActiveIndex += 1;
    };

    const minusOneToMainHeroSlideActiveIndex = () => {
        // Remove the previous image
        $navbar_variant = "";

        if (mainHeroSlideActiveIndex === 0) {
            mainHeroSlideActiveIndex = data.length - 1;
            return;
        }
        mainHeroSlideActiveIndex -= 1;
    };

    const swipeHandler = (event: CustomEvent) => {
        const direction = event.detail.direction;
        if (direction === "left") {
            addOneToMainHeroSlideActiveIndex();
        } else if (direction === "right") {
            minusOneToMainHeroSlideActiveIndex();
        }
    };
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<!-- svelte-ignore redundant-event-modifier -->
<div
    class="h-screen w-screen carousel carousel-vertical snap-none md:snap-y md:snap-mandatory text-white overflow-x-hidden"
    on:scroll|passive={() => {
        if (
            Math.abs(Number(mainHeroRootElement?.getBoundingClientRect().top)) >=
            Number(mainHeroRootElement?.getBoundingClientRect().height)
        ) {
            $timerStore = "reset";
        } else if (Math.abs(Number(mainHeroRootElement?.getBoundingClientRect().top)) > 0) {
            $timerStore = "pause";
        } else {
            $timerStore = "start";
        }
    }}
>
    <div class="carousel-item snap-always min-h-[60vh] md:min-h-screen w-screen">
        <div
            class="inline-grid"
            bind:this={mainHeroRootElement}
            use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: "pan-y" }}
            on:swipe={swipeHandler}
        >
            {#each data as item, index}
                {#if index === mainHeroSlideActiveIndex}
                    <div
                        transition:blur|local
                        style="grid-area: 1 / 1 / 2 / 2"
                    >
                        <MainHeroSlide
                            bind:mainHeroSlideActiveIndex
                            {data}
                            {addOneToMainHeroSlideActiveIndex}
                            {minusOneToMainHeroSlideActiveIndex}
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
    <div class="carousel-item snap-always">
        <GenreSlide />
    </div>
    <div class="carousel-item snap-always">
        <LibrarySlide />
    </div>
    <div class="carousel-item snap-always">
        <ExploreSlide />
    </div>
    <!-- Show a footer for  android users -->
    {#if ["Android OS", "iOS", null].includes(browser && browser.os)}
        {#if browser?.name === "firefox"}
            <div class="py-10" />
        {:else if browser?.name.includes("chrom")}
            <!-- Could be 'chrome','chromium','edge-chromium' -->
            <div class="py-8" />
        {/if}
    {/if}
</div>
