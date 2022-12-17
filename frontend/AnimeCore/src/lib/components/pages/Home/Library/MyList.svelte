<script lang="ts">
    import { Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import myList from "$data/mock/my_list.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
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

<div class="flex items-center pb-3 gap-2">
    <p class="font-bold text-3xl items-start">My List</p>
    <p class="text-3xl">•</p>
    <p class="text-xl">Watching</p>
    <ChevronDown
        color="white"
        height="24"
        width="24"
    />
</div>

<div class="w-96 md:w-[60vw]">
    <Swiper
        speed={600}
        direction="horizontal"
        slidesPerView={"auto"}
        spaceBetween={30}
        modules={[Mousewheel]}
        mousewheel={{
            sensitivity: 0.001,
            forceToAxis: true
        }}
    >
        {#each myList as item}
            <SwiperSlide>
                <div class="card w-36 h-52 bg-base-100 image-full before:!opacity-60">
                    <figure>
                        <img
                            src={item.background_image}
                            alt={item.name}
                        />
                    </figure>
                    <div class="card-body justify-between items-center !text-white">
                        <h2 class="card-title">
                            {voca.chain(item.name).truncate(mylistAnimeNameWordCount + 3)}
                        </h2>
                        <div class="card-actions">{item.current}/{item.total}</div>
                    </div>
                </div>
            </SwiperSlide>
        {/each}
    </Swiper>
</div>
