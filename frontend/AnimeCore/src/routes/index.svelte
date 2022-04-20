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

<Swiper
    speed={600}
    spaceBetween={0}
    direction="vertical"
    modules={[Mousewheel]}
    mousewheel={{ sensitivity: 0.001 }}
>
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
    <SwiperSlide>
        <section class="hero is-fullheight">
            <div class="hero-body is-align-self-center">
                <div>
                    <div class="title pb-5 is-size-2 has-text-white">
                        <div class="is-flex">
                            <span class="pr-5 is-align-self-center"> TRENDING </span>
                            <div
                                class="is-align-self-center"
                                style="display: inline-block;width: 26em;border-top: 10px solid;"
                            />
                        </div>
                    </div>
                    <figure class="image is-16by9">
                        <img
                            alt=""
                            style="border-radius:18px"
                            src="https://bulma.io/images/placeholders/256x256.png"
                        />
                    </figure>
                </div>
            </div>
        </section>
    </SwiperSlide>
</Swiper>
