<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { Autoplay, EffectFade, Mousewheel, Navigation, Pagination } from "swiper";
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
        <Swiper
            autoplay={true}
            modules={[EffectFade, Autoplay]}
            effect="fade"
            on:swiper={onMainSwiper}
        >
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
        <div class="container pt-6 px-4" style="max-width:95vw">
            <div class="title is-size-2 has-text-white">
                <div class="columns is-mobile">
                    <div class="column is-narrow">
                        <span class="is-align-self-center"> TRENDING </span>
                    </div>
                    <div class="column is-flex">
                        <div
                            class="is-align-self-center"
                            style="
                            width: 100%;
                            display: inline-block;
                            border-top: 10px solid;
                        "
                        />
                    </div>
                </div>
            </div>
        </div>
        <Swiper
            slidesPerView={$responsiveMode === "mobile" ? 3 : 1}
            on:swiper={onTrendingSwiper}
            pagination={{
                el: ".trending__pagination__element"
            }}
            modules={$responsiveMode === "mobile" ? [] : [EffectFade, Pagination]}
            effect={$responsiveMode === "mobile" ? "slide" : "fade"}
        >
            {#each Array(11) as _, i}
                <SwiperSlide>
                    <TrendingHero
                        slideNumber={String(i).padStart(2, "0")}
                        on:backClick={onTrendingSwiperBackward}
                        on:forwardClick={onTrendingSwiperForward}
                    />
                </SwiperSlide>
            {/each}
        </Swiper>
    </SwiperSlide>
</Swiper>
