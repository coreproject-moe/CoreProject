<script lang="ts">
    import { Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import continueWatching from "$data/mock/continue_watching.json";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";

    // Responsive switches
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    lastestEpisodeNameWordCount ??= 25;

    let mylistAnimeNameWordCount: number;
    mylistAnimeNameWordCount ??= 25;
</script>

<p class="font-bold text-3xl items-start flex pb-4">Continue Watching</p>
<div class="h-28 md:h-[200px] w-96 md:w-[60vw]">
    <Swiper
        speed={600}
        direction="horizontal"
        slidesPerView={"auto"}
        spaceBetween={24}
        modules={[Mousewheel]}
        mousewheel={{
            sensitivity: 0.001,
            forceToAxis: true
        }}
    >
        {#each continueWatching as item}
            <SwiperSlide>
                <div
                    class="h-28 md:h-[200px] w-96 md:w-[640px] flex flex-row gap-6 select-none cursor-grab carousel-item rounded-xl items-center justify-around"
                    style="
                    background-image:
                        linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                        linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                        url('{item.background_image}');
                    "
                >
                    <div class="md:self-start flex flex-col items-start gap-2 md:pt-5">
                        <p class="font-bold">{item.name}</p>
                        <p>
                            continue from Ep {voca
                                .chain(String(item.current_episode))
                                .padLeft(2, String(0))}
                        </p>
                        <p class="text-justify text-sm hidden md:block">
                            {voca.chain(item.about).truncate(60)}
                        </p>
                    </div>

                    <div class="md:self-end md:pb-5">
                        <button
                            class="btn btn-circle btn-md btn-warning"
                            aria-label="play"
                        >
                            <Play
                                width={20}
                                height={20}
                            />
                        </button>
                    </div>
                </div>
            </SwiperSlide>
        {/each}
    </Swiper>
</div>
