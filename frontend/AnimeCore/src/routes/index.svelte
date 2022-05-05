<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { EffectFade, Mousewheel } from "swiper";
    import MainHero from "$components/swiper/MainHero.svelte";
    import TrendingHero from "$components/swiper/TrendingHero.svelte";

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
            speed={600}
            spaceBetween={0}
            slidesPerView="auto"
            direction="horizontal"
            effect="fade"
            modules={[Mousewheel, EffectFade]}
            mousewheel={{ sensitivity: 0.001 }}
            autoplay={true}
        >
            {#each Array(10) as _, i}
                <TrendingHero slideNumber={JSON.stringify(i)} />
            {/each}
        </Swiper>
    </SwiperSlide>
</Swiper>
