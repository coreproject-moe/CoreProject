<script lang="ts">
    export let rootSwiper: SwiperType;
    import type { Swiper as SwiperType } from "swiper";
    import { Mousewheel, Pagination } from "swiper";
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

    const latestEpisodes = [
        {
            name: "Spy X Family",
            episode: 6,
            backgroundImage:
                "https://media.kitsu.io/manga/54448/cover_image/1c96f626f68456220ba41096a1942eee.png"
        }
    ];
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3">
            <p class="text-xl font-bold flex text-white">Latest Episode</p>
            <p class="flex gap-2 text-white">
                show from my list only <ChevronDown height={25} width={25} />
            </p>
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
                    modules={[Mousewheel, Pagination]}
                    pagination={{
                        el: ".latestEpisodesPaginationElement",
                        clickable: true
                    }}
                    slidesPerView={mobile ? 1 : 5}
                    spaceBetween={14}
                    mousewheel={{
                        sensitivity: 0.001
                    }}
                >
                    {#each latestEpisodes as item}
                        <SwiperSlide>
                            <div
                                class="w-96 md:w-80 h-28 md:h-24 rounded-xl flex items-center justify-around bg-center bg-no-repeat bg-cover"
                                style="background-image:url('{item.backgroundImage}')"
                            >
                                <div class="flex flex-col items-start text-white">
                                    <p class="font-bold">{item.name}</p>
                                    <p>Ep {item.episode}</p>
                                </div>

                                <button class="btn btn-circle btn-md btn-warning" aria-label="play">
                                    <Play width={20} height={20} />
                                </button>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </div>
            <div class="latestEpisodesPaginationElement flex justify-around pt-5" />
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex before:bg-white after:bg-white" />
        <div class="flex flex-col">
            <p class="font-bold text-3xl items-start flex pb-4 text-white">Continue Watching</p>
            <div
                class="h-28 md:h-[200px] w-96 md:w-[70vw]"
                on:mouseenter={disableRootSwiperScroll}
                on:touchstart={disableRootSwiperScroll}
                on:mouseleave={enableRootSwiperScroll}
                on:touchend={enableRootSwiperScroll}
            >
                <Swiper
                    speed={600}
                    direction="horizontal"
                    slidesPerView={"auto"}
                    spaceBetween={30}
                    modules={[Mousewheel]}
                    mousewheel={{
                        sensitivity: 0.001
                    }}
                    rewind
                >
                    {#each Array(10) as item}
                        <SwiperSlide>
                            <div
                                class="h-28 md:h-full w-96 md:w-[50vw] rounded-xl bg-gradient-to-r from-cyan-500 to-blue-500 flex items-center justify-around"
                            >
                                <div class="flex flex-col items-start">
                                    <p class="font-bold">Spy x Family</p>
                                    <p>Ep 06</p>
                                </div>

                                <button class="btn btn-circle btn-md btn-warning" aria-label="play">
                                    <Play width={20} height={20} />
                                </button>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </div>
            <div class="divider hidden md:flex before:bg-white after:bg-white" />

            <div class="flex flex-col">
                <div class="pb-3">
                    <p class="font-bold text-3xl flex items-start text-white">My List</p>
                </div>
            </div>
        </div>
    </div>
</div>
