<script lang="ts">
    import { FreeMode, Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import latestEpisodes from "$data/mock/latest_episode.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";

    // Responsive switches
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    lastestEpisodeNameWordCount ??= 25;
</script>

<p class="flex text-3xl font-bold">Latest Episode</p>
<p class="mt-6 mb-3 flex gap-2 md:my-0">
    show from my list only
    <ChevronDown
        height={25}
        width={25}
    />
</p>
<div class="h-28 w-96 md:h-[530px] md:w-80">
    <Swiper
        direction={mobile ? "horizontal" : "vertical"}
        modules={[Mousewheel, FreeMode]}
        slidesPerView={mobile ? 1 : 4}
        spaceBetween={24}
        mousewheel={{
            forceToAxis: true
        }}
        freeMode={{
            enabled: true,
            sticky: true
        }}
    >
        {#each latestEpisodes as item}
            <SwiperSlide>
                <div
                    class="carousel-item flex w-10/12 items-center justify-between rounded-xl bg-cover bg-center bg-no-repeat p-8 md:w-64"
                    style="
                        background-image:
                            linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                            linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                            url('{item.background_image.trim()}');
                    "
                >
                    <div class="flex flex-col items-start">
                        <p
                            class="font-bold"
                            style="display: block ruby"
                        >
                            {voca
                                .chain(item.name)
                                .trim()
                                .truncate(lastestEpisodeNameWordCount + 3, " ...")}
                        </p>
                        <p>
                            Ep {voca.chain(String(item.episode)).padLeft(2, String(0))}
                        </p>
                    </div>

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
            </SwiperSlide>
        {/each}
    </Swiper>
</div>
