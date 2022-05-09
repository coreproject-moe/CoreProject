<script lang="ts">
    import {
        Autoplay,
        EffectCoverflow,
        EffectFade,
        Mousewheel,
        Navigation,
        Pagination
    } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import FromYourList from "$components/swiper/FromYourList.svelte";
    import MainHero from "$components/swiper/MainHero.svelte";
    import TrendingHero from "$components/swiper/TrendingHero.svelte";
    import { responsiveMode } from "$store/responsive";

    let trendingSlide = 0;
    let fromyourlistSlide = 0;

    const onTrendingSlideChange = (e: any) => {
        const [swiper] = e.detail[0];
        trendingSlide = swiper?.activeIndex;
    };
    const onFromYourListSlideChange = (e: any) => {
        const [swiper] = e.detail[0];
        fromyourlistSlide = swiper?.activeIndex;
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
    <!-- <SwiperSlide>
        <Swiper
            modules={[EffectFade, Autoplay, Navigation]}
            navigation={{
                nextEl: ".mainhero__next__el",
                prevEl: ".mainhero__previous__el"
            }}
            effect="fade"
        >
            {#each Array(100) as f, i}
                <MainHero backgroundImageUrl={"/images/Hyouka-poster.png"} animeName="Hyouka {i}" />
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

            <div class="hero-body py-0">
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
                <div class="columns is-mobile is-centered mb-0">
                    <div class="column is-narrow py-0">
                        <div class="trending__pagination__element" />
                    </div>
                </div>
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
                            {String(trendingSlide).padStart(2, "0")}
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
    </SwiperSlide> -->
    <SwiperSlide>
        <section class="hero {$responsiveMode === 'mobile' ? 'is-small' : 'is-fullheight'}">
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

            <div class="hero-body is-flex-direction-column is-justify-content-center">
                <nav class="level is-mobile" style="min-width:90vw">
                    <p
                        class="level-item has-text-centered is-hidden-mobile has-text-white has-text-weight-bold is-justify-content-flex-start"
                    >
                        <span class="pr-2"> Watching 13 anime. AniList </span>
                        <span class="icon is-small">
                            <img
                                class="is-align-self-flex-start"
                                src="/icons/external-link.svg"
                                alt=""
                                height={24}
                                width={24}
                            />
                        </span>
                    </p>

                    <div class="level-item has-text-centered">
                        <div class="dropdown is-active">
                            <div class="dropdown-trigger">
                                <button class="button is-warning mx-4 is-flex">
                                    <span class="has-text-weight-semibold has-text-white"
                                        >Watching</span
                                    >
                                    <span class="icon">
                                        <img
                                            class="is-align-self-flex-start"
                                            src="/icons/chevron-down.svg"
                                            alt=""
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                </button>
                            </div>
                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item"> Dropdown item </a>
                                    <a class="dropdown-item"> Other dropdown item </a>
                                    <a href="#" class="dropdown-item is-active">
                                        Active dropdown item
                                    </a>
                                    <a href="#" class="dropdown-item"> Other dropdown item </a>
                                    <hr class="dropdown-divider" />
                                    <a href="#" class="dropdown-item"> With a divider </a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="level-item has-text-centered is-justify-content-flex-end">
                        <div class="dropdown is-active">
                            <div class="dropdown-trigger">
                                <button class="button is-info mx-4 is-flex">
                                    <span class="icon">
                                        <img
                                            class="is-align-self-flex-start"
                                            src="/icons/settings.svg"
                                            alt=""
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                    <span class="has-text-weight-semibold">Options</span>
                                </button>
                            </div>
                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item"> Dropdown item </a>
                                    <a class="dropdown-item"> Other dropdown item </a>
                                    <a href="#" class="dropdown-item is-active">
                                        Active dropdown item
                                    </a>
                                    <a href="#" class="dropdown-item"> Other dropdown item </a>
                                    <hr class="dropdown-divider" />
                                    <a href="#" class="dropdown-item"> With a divider </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>

                <Swiper
                    navigation={{
                        nextEl: ".fromyourlist__next__el",
                        prevEl: ".fromyourlist__previous__el"
                    }}
                    modules={[EffectCoverflow, Navigation]}
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
                    on:slideChange={onFromYourListSlideChange}
                >
                    {#each Array(12) as _, i}
                        <FromYourList />
                    {/each}
                </Swiper>
            </div>

            <div class="hero-foot is-hidden-mobile">
                <div class="py-6">
                    <div class="field is-grouped is-justify-content-center">
                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 fromyourlist__previous__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-left.svg" height={24} width={24} />
                            </span>
                        </button>

                        <button
                            class="button is-medium is-warning has-text-white mx-0 has-text-weight-medium"
                        >
                            {String(fromyourlistSlide)?.padStart(2, "0")}
                        </button>

                        <button
                            class="button is-medium has-border-warning-light is-warning is-outlined mx-5 fromyourlist__next__el"
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
    }
</style>
