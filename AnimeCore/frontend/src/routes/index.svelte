<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import { EffectFade, Navigation, Pagination } from "swiper";
</script>

<Swiper spaceBetween={30} effect={"fade"} modules={[EffectFade, Navigation, Pagination]}>
    <SwiperSlide>
        <section
            class="hero is-fullheight has-background-black"
            style="
        background-image: url('/images/Hyouka-poster.png');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        box-shadow: 
            inset 0 4px 1800px #070519,
            inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)
        
    "
        >
            <div class="hero-head">
                <nav class="navbar">
                    <div class="container">
                        <div class="navbar-brand">
                            <div class="navbar-item">
                                <img alt="" src="/animecore_logo.svg" width={164} height={25} />
                            </div>
                            <span class="navbar-burger" data-target="navbarMenuHeroA">
                                <span />
                                <span />
                                <span />
                            </span>
                        </div>
                        <div id="navbarMenuHeroA" class="navbar-menu">
                            <div class="navbar-end">
                                <span class="navbar-item">
                                    <div class="button is-ghost">
                                        <img
                                            alt=""
                                            src="/icons/search.svg"
                                            width={32}
                                            height={32}
                                        />
                                    </div>
                                </span>
                                <span class="navbar-item px-0">
                                    <img
                                        alt=""
                                        style="max-height: 100%"
                                        src="/images/placeholder.png"
                                        width={60}
                                        height={60}
                                    />
                                </span>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>

            <div class="hero-body is-align-items-self-end">
                <div class="container">
                    <div class="title has-text-warning is-size-4">
                        Featured <span class="is-bold">——</span>
                    </div>
                    <div class="title is-size-1 has-text-white is-bold">Hyouka</div>
                    <div class="subtitle is-size-6 has-text-white pt-5" style="width: 60%;">
                        Energy-conservative high school student Houtarou Oreki ends up with more
                        than he bargained for when he signs up for the Classic Literature Club at
                        his sister&apos;s behest—especially when he realizes how deep-rooted the
                        club&apos;s history really is. Begrudgingly, Oreki is dragged into an...
                    </div>
                    <div class="subtitle">
                        <span class="tag is-size-6 mx-1 is-bold is-black"> Mystery </span>
                        <span class="tag is-size-6 mx-1 is-bold is-black"> Slice of Life </span>
                    </div>
                    <div class="subtitle">
                        <div class="buttons">
                            <button
                                class="button is-warning has-border-transparent mx-3"
                                style="border-radius: 12"
                            >
                                <span class="icon is-small">
                                    <img alt="" src="/icons/play.svg" height={24} width={24} />
                                </span>
                            </button>
                            <button
                                class="button is-warning is-outlined"
                                style="border-radius: 16px; border-width: 3px"
                            >
                                <span class="is-bold">Detailes</span>
                                <img
                                    alt=""
                                    src="/icons/chevrons-right.svg"
                                    height={24}
                                    width={24}
                                />
                            </button>
                            <button
                                class="button is-warning is-outlined"
                                style="border-radius: 16px; border-width: 3px"
                            >
                                <span class="icon is-small">
                                    <img
                                        alt=""
                                        src="/icons/chevron-left.svg"
                                        height={24}
                                        width={24}
                                    />
                                </span>
                            </button>
                            <button
                                class="button is-warning is-outlined"
                                style="border-radius: 16px;border-width: 3px"
                            >
                                <span class="icon is-small">
                                    <img
                                        alt=""
                                        src="/icons/chevron-right.svg"
                                        height={24}
                                        width={24}
                                    />
                                </span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="hero-foot">
                <nav class="tabs">
                    <div class="container has-text-white">
                        <div class="columns is-mobile is-centered">
                            <div class="column is-narrow px-1">
                                <img src="/icons/arrow-down.svg" alt="" height={24} width={24} />
                            </div>
                            <div class="column is-narrow px-1">scroll below</div>
                        </div>
                    </div>
                </nav>
            </div>
        </section>
    </SwiperSlide>
</Swiper>
