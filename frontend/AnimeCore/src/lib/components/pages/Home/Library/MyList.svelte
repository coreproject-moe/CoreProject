<script lang="ts">
    import { Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import myList from "$data/mock/my_list.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import { responsiveMode } from "$store/Responsive";
    import Settings from "$icons/Settings.svelte";

    // Responsive switches
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    lastestEpisodeNameWordCount ??= 25;

    let mylistAnimeNameWordCount: number;
    mylistAnimeNameWordCount ??= 25;
</script>

<div class="flex justify-between pb-3 gap-2 mt-10 mb-3 md:my-0">
    <div class="flex items-center flex-col md:flex-row gap-5 md:gap-0">
        <p class="font-bold text-3xl items-start">My List</p>
        <p class="text-3xl hidden md:block">•</p>
        <p class="text-sm md:text-xl">
            Watching
            <ChevronDown
                class="inline-block"
                color="white"
                height="24"
                width="24"
            />
        </p>
    </div>
    <div class="flex items-center">
        <Settings
            color="white"
            height="24"
            width="24"
        />
    </div>
</div>

<div class="w-96 md:w-[60vw]">
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
                        <h2 class="card-title text-sm">
                            {voca.chain(item.name).truncate(mylistAnimeNameWordCount + 3)}
                        </h2>
                        <div class="card-actions">{item.current}/{item.total}</div>
                    </div>
                </div>
            </SwiperSlide>
        {/each}
    </Swiper>
</div>
