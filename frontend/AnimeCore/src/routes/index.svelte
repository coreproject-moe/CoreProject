<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { EffectFade, Mousewheel } from "swiper";
    import MainHero from "$components/swiper/MainHero.svelte";

    let mainSlide = 0;
    let swiper: Swiper;

    const onSwiper = (e: any) => {
        const [__swiper] = e.detail;
        swiper = __swiper;
    };

    const onSwiperBackward = () => {
        mainSlide = mainSlide - 1;
        swiper?.slideTo(mainSlide);
    };

    const onSwiperForward = () => {
        mainSlide = mainSlide + 1;
        swiper?.slideTo(mainSlide);
    };
</script>

<Swiper speed={600} direction="vertical" modules={[Mousewheel]} mousewheel={{ sensitivity: 0.001 }}>
    <SwiperSlide>
        <Swiper modules={[EffectFade]} effect="fade" on:swiper={onSwiper}>
            {#each Array(100) as f, i}
                <SwiperSlide>
                    <MainHero
                        backgroundImageUrl={"/images/Hyouka-poster.png"}
                        animeName="Hyouka {i}"
                        onBackClick={onSwiperBackward}
                        onForwardClick={onSwiperForward}
                    />
                </SwiperSlide>
            {/each}
        </Swiper>
    </SwiperSlide>
    <SwiperSlide>Hello world</SwiperSlide>
</Swiper>


