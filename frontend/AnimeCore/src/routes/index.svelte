<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";


    import {
        Autoplay,
        Mousewheel,
        Navigation,
        Pagination,
        EffectFade,
        EffectCoverflow
    } from "swiper";

    import MainHero from "$components/swiper/MainHero.svelte";
    import TrendingHero from "$components/swiper/TrendingHero.svelte";
    import { responsiveMode } from "$store/responsive";
    import FromYourList from "$components/swiper/FromYourList.svelte";

    let mainSlide = 0;
    let trendingSlide = 0;

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
    const onTrendingSlideChange = (e: any) => {
        const [swiper] = e.detail[0];
        trendingSlide = swiper?.activeIndex;
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
            modules={[EffectFade, Autoplay, Navigation]}
            navigation={{
                nextEl: ".mainhero__next__el",
                prevEl: ".mainhero__previous__el"
            }}
            effect="fade"
            on:swiper={onMainSwiper}
        >
            {#each Array(100) as f, i}
                <MainHero
                    backgroundImageUrl={"/images/Hyouka-poster.png"}
                    animeName="Hyouka {i}"
                    on:backClick={onMainSwiperBackward}
                    on:forwardClick={onMainSwiperForward}
                />
            {/each}
        </Swiper>
    </SwiperSlide>
    <SwiperSlide>
        <section class="hero {$responsiveMode === 'mobile' ? 'is-small' : 'is-fullheight'}">
            <div class="hero-head">
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
            </div>

            <div class="hero-body">
                <Swiper
                    slidesPerView={$responsiveMode === "mobile" ? 3 : 1}
                    spaceBetween={$responsiveMode === "mobile" ? 10 : 40}
                    on:slideChange={onTrendingSlideChange}
                    pagination={{
                        el: ".trending__pagination__element"
                    }}
                    modules={$responsiveMode === "mobile"
                        ? [Navigation]
                        : [Navigation, EffectFade, Pagination]}
                    navigation={{
                        nextEl: ".trending__next__el",
                        prevEl: ".trending__previous__el"
                    }}
                    effect={$responsiveMode === "mobile" ? "slide" : "fade"}
                >
                    {#each Array(11) as _, i}
                        <TrendingHero slideNumber={String(i).padStart(2, "0")} />
                    {/each}
                </Swiper>
            </div>

            <div class="hero-foot is-hidden-mobile">
                <div class="py-6">
                    <div class="field is-grouped is-justify-content-center">
                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 trending__previous__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-left.svg" height={24} width={24} />
                            </span>
                        </button>

                        <button
                            class="button is-medium is-warning has-text-white mx-0 has-text-weight-medium"
                        >
                            {trendingSlide}
                        </button>

                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 trending__next__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-right.svg" height={24} width={24} />
                            </span>
                        </button>
                    </div>
                </div>
            </div>
        </section>
    </SwiperSlide>
    <SwiperSlide>
        <section class="hero {$responsiveMode === 'mobile' ? 'is-small' : 'is-fullheight'}">
            <!-- Hero head: will stick at the top -->
            <div class="hero-head">
                <div class="container pt-6 px-4" style="max-width:95vw">
                    <div class="title is-size-2 has-text-white">
                        <div class="columns is-mobile">
                            <div class="column is-narrow">
                                <span class="is-align-self-center"> FROM YOUR LIST </span>
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
            </div>

            <!-- Hero content: will be in the middle -->
            <div class="hero-body">
                <Swiper
                    modules={[EffectCoverflow]}
                    grabCursor={true}
                    slidesPerView={$responsiveMode === "mobile" ? 3 : 5}
                    spaceBetween={$responsiveMode === "mobile" ? 10 : 40}
                    coverflowEffect={{
                        rotate: 50,
                        stretch: 0,
                        depth: 100,
                        modifier: 1,
                        slideShadows: true
                    }}
                >
                    {#each Array(12) as _, i}
                        <FromYourList />
                    {/each}
                </Swiper>
            </div>

            <!-- Hero footer: will stick at the bottom -->
            <div class="hero-foot is-hidden-mobile">
                <div class="py-6">
                    <div class="field is-grouped is-justify-content-center">
                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 trending__previous__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-left.svg" height={24} width={24} />
                            </span>
                        </button>

                        <button
                            class="button is-medium is-warning has-text-white mx-0 has-text-weight-medium"
                        >
                            {trendingSlide}
                        </button>

                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 trending__next__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-right.svg" height={24} width={24} />
                            </span>
                        </button>
                    </div>
                </div>
            </div>
        </section>
    </SwiperSlide>
</Swiper>

<style lang="scss">
    .button {
        border-radius: 16px;
        border-width: 5px;
        height: 32px;
    }
</style>
