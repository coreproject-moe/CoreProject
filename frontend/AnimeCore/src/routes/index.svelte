<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { Controller, EffectFade, Navigation, Pagination } from "swiper";
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

<Swiper modules={[EffectFade, Controller]} effect="fade" on:swiper={onSwiper}>
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
