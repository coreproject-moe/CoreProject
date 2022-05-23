<script lang="ts">
    import { Autoplay, EffectFade, Mousewheel, Navigation, Pagination } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import FromYourList from "$components/swiper/FromYourList.svelte";
    import MainHero from "$components/swiper/MainHero.svelte";
    import TrendingHero from "$components/swiper/TrendingHero.svelte";
    import { responsiveMode } from "$store/responsive";

    let slidesPerView: number;
    let trendingSlide = 0;
    let fromyourlistSlide = 0;


    // Dropdown Bool
    let dropdownPickStateOpen = false;

    const onTrendingSlideChange = (e: any) => {
        const [swiper] = e.detail[0];
        trendingSlide = swiper?.activeIndex;
    };
    const onFromYourListSlideChange = (e: any) => {
        const [swiper] = e.detail[0];
        fromyourlistSlide = swiper?.activeIndex;
    };

    $: {
        switch ($responsiveMode) {
            case "mobile":
                slidesPerView = 3;
                break;

            case "tablet":
                slidesPerView = 4;
                break;
            case "desktop":
            case "widescreen":
                slidesPerView = 5;
                break;
            case "fullhd":
                slidesPerView = 6;
                break;
            default:
                break;
        }
    }
</script>

<Swiper
    speed={600}
    spaceBetween={0}
    direction="vertical"
    slidesPerView="auto"
    modules={[Mousewheel]}
    mousewheel={{ sensitivity: 0.001 }}
    simulateTouch={false}
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

            <div class="hero-body is-flex-direction-column">
                <nav class="level is-mobile pb-6" style="min-width:90vw">
                    <p
                        class="level-item has-text-centered is-hidden-touch has-text-white has-text-weight-bold is-justify-content-flex-start"
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

                    <div
                        class="level-item has-text-centered {$responsiveMode === 'mobile'
                            ? 'is-justify-content-flex-start'
                            : ''}"
                    >
                        <div class="dropdown {dropdownPickStateOpen ? 'is-active' : ''}">
                            <div class="dropdown-trigger">
                                <button
                                    class="button is-warning mx-4 is-flex {$responsiveMode ===
                                    'mobile'
                                        ? 'is-small'
                                        : 'is-medium'}"
                                    on:click={() => {
                                        dropdownPickStateOpen = !dropdownPickStateOpen;
                                    }}
                                >
                                    <span class="has-text-weight-semibold has-text-white"
                                        >Watching</span
                                    >
                                    <span class="icon">
                                        <img
                                            src={dropdownPickStateOpen
                                                ? "/icons/chevron-up.svg"
                                                : "/icons/chevron-down.svg"}
                                            alt=""
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                </button>
                            </div>
                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content has-background-warning-light" />
                            </div>
                        </div>
                    </div>

                    <div class="level-item has-text-centered is-justify-content-flex-end">
                        <button
                            data-target="option-modal"
                            class="button is-info mx-4 is-flex modal-button {$responsiveMode ===
                            'mobile'
                                ? 'is-small'
                                : 'is-medium'}"
                        >
                            <span class="icon">
                                <img src="/icons/settings.svg" alt="" height={24} width={24} />
                            </span>
                            <span class="has-text-weight-semibold">Options</span>
                        </button>
                    </div>
                </nav>

                <Swiper
                    navigation={{
                        nextEl: ".fromyourlist__next__el",
                        prevEl: ".fromyourlist__previous__el"
                    }}
                    modules={[Navigation]}
                    grabCursor={true}
                    {slidesPerView}
                    slidesPerGroup={slidesPerView}
                    spaceBetween={$responsiveMode === "mobile" ? 10 : 40}
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
                            {String(fromyourlistSlide / slidesPerView)?.padStart(2, "0")}
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
        border-radius: 10px !important;
        border-width: 5px;
    }
</style>
