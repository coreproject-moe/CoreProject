<script lang="ts">
    import { Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import continueWatching from "$data/mock/continue_watching.json";
    import latestEpisodes from "$data/mock/latest_episode.json";
    import myList from "$data/mock/my_list.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
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

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3">
            <p class="text-3xl font-bold flex">Latest Episode</p>
            <p class="flex gap-2">
                show from my list only <ChevronDown height={25} width={25} />
            </p>
            <div
                class="h-28 md:h-[530px] w-96 md:w-80 carousel gap-6 carousel-center md:carousel-vertical"
            >
                {#each latestEpisodes as item}
                    <div
                        class="w-10/12 md:w-64 carousel-item bg-center rounded-xl bg-no-repeat bg-cover flex items-center justify-between p-8"
                        style="background-image:
                            linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                            linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                            url('{item.background_image.trim()}');
                        "
                    >
                        <div class="flex flex-col items-start">
                            <p class="font-bold" style="display: block ruby">
                                {voca
                                    .chain(item.name)
                                    .trim()
                                    .truncate(lastestEpisodeNameWordCount + 3, " ...")}
                            </p>
                            <p>
                                Ep {voca.chain(String(item.episode)).padLeft(2, String(0))}
                            </p>
                        </div>

                        <button class="btn btn-circle btn-md btn-warning" aria-label="play">
                            <Play width={20} height={20} />
                        </button>
                    </div>
                {/each}
            </div>
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex before:bg-white after:bg-white" />
        <div class="flex flex-col">
            <p class="font-bold text-3xl items-start flex pb-4">Continue Watching</p>
            <div class="h-28 md:h-[200px] w-96 md:w-[70vw] carousel gap-3">
                {#each continueWatching as item}
                    <div
                        class="carousel-item w-96 md:w-[30vw] rounded-xl flex items-center justify-around"
                        style="background-image:
                                linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                                linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                                url('{item.background_image}');"
                    >
                        <div class="flex flex-col items-start">
                            <p class="font-bold">{item.name}</p>
                            <p>
                                Ep {voca.chain(String(item.current_episode)).padLeft(2, String(0))}
                            </p>
                        </div>

                        <button class="btn btn-circle btn-md btn-warning" aria-label="play">
                            <Play width={20} height={20} />
                        </button>
                    </div>
                {/each}
            </div>
            <div class="divider hidden md:flex before:bg-white after:bg-white" />
            <div class="flex items-center pb-3 gap-2">
                <p class="font-bold text-3xl items-start">My List</p>
                <p class="text-3xl">•</p>
                <p class="text-xl">Watching</p>
                <ChevronDown color="white" height="24" width="24" />
            </div>

            <div class="w-96 md:w-[70vw]">
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
                                    <img src={item.background_image} alt={item.name} />
                                </figure>
                                <div class="card-body justify-between items-center !text-white">
                                    <h2 class="card-title">
                                        {voca
                                            .chain(item.name)
                                            .truncate(mylistAnimeNameWordCount + 3)}
                                    </h2>
                                    <div class="card-actions">{item.current}/{item.total}</div>
                                </div>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </div>
        </div>
    </div>
</div>
