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

<p class="mt-10 mb-6 flex items-start pb-4 text-3xl font-bold md:my-0">Continue Watching</p>
<div class="h-28 w-96 md:h-[200px] md:w-[60vw]">
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
                    class="carousel-item flex h-28 w-96 cursor-grab select-none flex-row items-center justify-around gap-6 rounded-xl md:h-[200px] md:w-[640px]"
                    style="
                        background-image:
                            linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                            linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                            url('{item.background_image}');
                    "
                >
                    <div class="flex flex-col items-start gap-2 md:self-start md:pt-5">
                        <p class="font-bold">{item.name}</p>
                        <p>
                            continue from Ep {voca
                                .chain(String(item.current_episode))
                                .padLeft(2, String(0))}
                        </p>
                        <p class="hidden text-justify text-sm md:block">
                            {voca.chain(item.about).truncate(60)}
                        </p>
                    </div>

                    <div class="md:self-end md:pb-5">
                        <button
                            class="btn-warning btn-md btn-circle btn"
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
