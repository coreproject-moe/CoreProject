<script lang="ts">
    import type { Swiper as SwiperType } from "swiper";
    import { EffectFade, Lazy } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import GenreSlide from "$components/pages/Home/Genre/Slide.svelte";
    import LibrarySlide from "$components/pages/Home/Library/Slide.svelte";
    import MainHeroSlide from "$components/pages/Home/MainHero/Slide.svelte";
    import data from "$data/mock/main_hero_data.json";

    let mainHeroSwiper: Partial<SwiperType>;

    const onMainHeroSwiper = (e: CustomEvent) => {
        const [swiper] = e.detail;
        mainHeroSwiper = swiper;
    };
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div class="h-screen carousel carousel-vertical overscroll-auto">
    <div class="carousel-item h-auto w-auto">
        <Swiper
            modules={[EffectFade, Lazy]}
            effect="fade"
            direction="horizontal"
            slidesPerView={1}
            on:swiper={onMainHeroSwiper}
            loop
            lazy
        >
            {#each data as item}
                <SwiperSlide let:data={{ isActive, isDuplicate, isVisible, isPrev, isNext }}>
                    <MainHeroSlide
                        {isPrev}
                        {isNext}
                        {isActive}
                        {isDuplicate}
                        {isVisible}
                        {mainHeroSwiper}
                        animeTitle={item.animeTitle}
                        animeSummary={item.animeSummary}
                        animeEpisodeCount={item.animeEpisodeCount}
                        animeStudio={item.animeStudio}
                        animeAirTime={item.animeAirTime}
                        backgroundImage={item.backgroundImage}
                        backgroundBanner={item.backgroundBanner}
                        tags={item.tags}
                    />
                </SwiperSlide>
            {/each}
        </Swiper>
    </div>
    <div class="carousel-item h-auto w-auto">
        <GenreSlide />
    </div>
    <!--
    <div class="carousel-item h-auto w-auto">
        <LibrarySlide />
    </div>
</div>
