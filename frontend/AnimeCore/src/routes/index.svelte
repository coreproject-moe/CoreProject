<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { EffectFade, Mousewheel } from "swiper";
    import MainHero from "$components/swiper/MainHero.svelte";
    import TrendingHero from "$components/swiper/TrendingHero.svelte";
    import { responsiveMode } from "$store/responsive";

    let mainSlide = 0;

    let mainSwiper: Swiper;

    const onMainSwiper = (e: CustomEvent<any>) => {
        const [__swiper] = e.detail;
        mainSwiper = __swiper;
    };

    const onMainSwiperBackward = () => {
        mainSlide = mainSlide - 1;
        mainSwiper?.slideTo(mainSlide);
    };

    const onMainSwiperForward = () => {
        mainSlide = mainSlide + 1;
        mainSwiper?.slideTo(mainSlide);
    };

    let trendingSwiper: Swiper;

    let trendingSlide = 0;

    const onTrendingSwiper = (e: CustomEvent<any>) => {
        const [__swiper] = e.detail;
        trendingSwiper = __swiper;
    };
    const onTrendingSwiperBackward = () => {
        trendingSlide = trendingSlide - 1;
        trendingSwiper?.slideTo(trendingSlide);
    };

    const onTrendingSwiperForward = () => {
        trendingSlide = trendingSlide + 1;
        console.log(trendingSwiper);
        trendingSwiper?.slideTo(trendingSlide);
    };
</script>

<Swiper
    speed={600}
    spaceBetween={0}
    direction="vertical"
    slidesPerView="auto"
    modules={[Mousewheel]}
    mousewheel={{ sensitivity: 0.001 }}
>
    <SwiperSlide>
        <Swiper modules={[EffectFade]} effect="fade" on:swiper={onMainSwiper}>
            {#each Array(100) as f, i}
                <SwiperSlide>
                    <MainHero
                        backgroundImageUrl={"/images/Hyouka-poster.png"}
                        animeName="Hyouka {i}"
                        on:backClick={onMainSwiperBackward}
                        on:forwardClick={onMainSwiperForward}
                    />
                </SwiperSlide>
            {/each}
        </Swiper>
    </SwiperSlide>
    <SwiperSlide>
        <Swiper
            slidesPerView={$responsiveMode === "mobile" ? 3 : 1}
            on:swiper={onTrendingSwiper}
            modules={$responsiveMode === "mobile" ? [] : [EffectFade]}
            effect={$responsiveMode === "mobile" ? "" : "fade"}
        >
            {#each Array(10) as _, i}
                <SwiperSlide>
                    <TrendingHero
                        slideNumber={JSON.stringify(i)}
                        on:backClick={onTrendingSwiperBackward}
                        on:forwardClick={onTrendingSwiperForward}
                    />
                </SwiperSlide>
            {/each}
        </Swiper>
    </SwiperSlide>
</Swiper>
