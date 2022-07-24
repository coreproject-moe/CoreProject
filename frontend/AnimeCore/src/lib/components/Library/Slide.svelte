<script lang="ts">
    export let rootSwiper: SwiperType;

    import type { Swiper as SwiperType } from "swiper";
    import { Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    const disableRootSwiperScroll = () => {
        rootSwiper?.mousewheel?.disable();
        rootSwiper.allowTouchMove = false;
    };
    const enableRootSwiperScroll = () => {
        rootSwiper?.mousewheel?.enable();
        rootSwiper.allowTouchMove = true;
    };
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3">
            <p class="text-xl font-bold flex">Latest Episode</p>
            <p class="flex gap-2">show from my list only <ChevronDown height={25} width={25} /></p>
            <div
                class="h-28 md:h-[530px] w-96 md:w-80"
                on:mouseenter={disableRootSwiperScroll}
                on:touchstart={disableRootSwiperScroll}
                on:mouseleave={enableRootSwiperScroll}
                on:touchend={enableRootSwiperScroll}
            >
                <Swiper
                    speed={600}
                    direction={mobile ? "horizontal" : "vertical"}
                    modules={[Mousewheel]}
                    slidesPerView={mobile ? 1 : 5}
                    spaceBetween={14}
                    mousewheel={{
                        sensitivity:.001
                    }}

                >
                    {#each Array(10) as item, index}
                        <SwiperSlide>
                            <div
                                class="w-96 md:w-80 h-28 md:h-24 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-500 flex items-center justify-around"
                            >
                                <div class="flex flex-col items-start">
                                    <p class="font-bold">Spy x Family -{index}</p>
                                    <p>Ep 06</p>
                                </div>

                                <button class="btn btn-circle btn-md btn-warning" aria-label='play'>
                                    <Play width={20} height={20} />
                                </button>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </div>
            <div class="btn-group justify-center">
                <button class="btn">1</button>
                <button class="btn">2</button>
                <button class="btn btn-disabled">...</button>
                <button class="btn">99</button>
                <button class="btn">100</button>
            </div>
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex" />
        <div class="flex flex-col">
            <p class="font-bold text-3xl">Continue Watching</p>
            <Swiper>
                <SwiperSlide>

                </SwiperSlide>
            </Swiper>
            <div class="flex flex-col">
                <p class="font-bold text-3xl">Continue Watching</p>
                <div class="carousel carousel-center rounded-box">
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://placeimg.com/400/300/arch" alt="Pizza" />
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>
