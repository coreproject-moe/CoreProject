<script lang="ts">
    import emblaCarouselSvelte, { type EmblaOptionsType } from "embla-carousel-svelte";
    import voca from "voca";

    import continueWatching from "$data/mock/continue_watching.json";
    import latestEpisodes from "$data/mock/latest_episode.json";
    import myList from "$data/mock/my_list.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Heart from "$icons/Heart.svelte";
    import Play from "$icons/Play.svelte";
    import Settings from "$icons/Settings.svelte";
    import { responsiveMode } from "$store/Responsive";
    import Pagination from "./Pagination.svelte";

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    $: {
        switch (true) {
            case $responsiveMode === "mobile":
                lastestEpisodeNameWordCount = 25;
                break;
            case $responsiveMode === "tablet":
                lastestEpisodeNameWordCount = 16;
                break;
            case $responsiveMode === "desktop":
                lastestEpisodeNameWordCount = 19;
                break;
            case $responsiveMode === "widescreen":
                lastestEpisodeNameWordCount = 21;
                break;
            case $responsiveMode === "fullhd":
                lastestEpisodeNameWordCount = 22;
                break;
        }
    }

    let mylistAnimeNameWordCount: number;
    mylistAnimeNameWordCount ??= 25;

    // Embla Config
    const latestEpisodes_emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            breakpoints: {
                "(max-width: 768px)": { axis: "x", align: "center" },
                "(min-width: 769px)": { axis: "y", align: "start" }
            }
        },
        plugins: []
    };

    const continueWatching__emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            axis: "x",
            align: "start"
        },
        plugins: []
    };

    const myList__emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            axis: "x",
            align: "start"
        },
        plugins: []
    };
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3 self-start">
            <p class="text-3xl font-bold flex">Latest Episode</p>
            <p class="flex gap-2">
                show from my list only
                <ChevronDown
                    height={25}
                    width={25}
                />
            </p>

            <embla
                class="overflow-hidden overscroll-auto lg:overscroll-contain overflow-y-hidden"
                use:emblaCarouselSvelte={latestEpisodes_emblaConfig}
            >
                <embla-container
                    class="h-28 md:h-[530px] w-96 md:w-80 gap-6 flex flex-row md:flex-col"
                >
                    {#each latestEpisodes as item}
                        <embla-slide
                            class="cursor-grab select-none w-10/12 md:w-64 carousel-item bg-center rounded-xl bg-no-repeat bg-cover flex items-center justify-between p-8"
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
                                class="btn btn-circle btn-md btn-warning"
                                aria-label="play"
                            >
                                <Play
                                    width={20}
                                    height={20}
                                />
                            </button>
                        </embla-slide>
                    {/each}
                </embla-container>
            </embla>
            <div class="hidden md:flex justify-center">
                <Pagination />
            </div>
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex before:bg-white after:bg-white" />
        <div class="flex flex-col mb-4 md:mb-0">
            <p class="font-bold text-3xl items-start flex pb-4">Continue Watching</p>
            <embla
                class="overflow-hidden overscroll-auto lg:overscroll-contain overflow-y-hidden"
                use:emblaCarouselSvelte={continueWatching__emblaConfig}
            >
                <embla-container class="h-28 md:h-[200px] w-96 md:w-[640px] flex flex-row gap-6">
                    {#each continueWatching as item}
                        <embla-slide
                            class="select-none cursor-grab carousel-item w-96 md:w-[640px] rounded-xl flex items-center justify-around"
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
                        </embla-slide>
                    {/each}
                </embla-container>
            </embla>

            <div class="divider hidden md:flex before:bg-white after:bg-white" />
            <div class="flex justify-between pb-3 gap-2 my-4 md:my-0">
                <div class="flex items-center">
                    <p class="font-bold text-3xl items-start">My List</p>
                    <p class="text-3xl">•</p>
                    <p class="text-xl">Watching</p>
                    <ChevronDown
                        color="white"
                        height="24"
                        width="24"
                    />
                </div>
                <div class="flex items-center">
                    <Settings
                        color="white"
                        height="24"
                        width="24"
                    />
                </div>
            </div>

            <embla
                class="overflow-hidden"
                use:emblaCarouselSvelte={myList__emblaConfig}
            >
                <embla-container
                    class="w-96 md:w-[60vw] gap-6 overscroll-auto lg:overscroll-contain flex flex-row"
                >
                    {#each myList as item}
                        <embla-slide
                            class="select-none cursor-grab carousel-item card w-36 h-52 bg-base-100 image-full before:!opacity-60"
                        >
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
                        </embla-slide>
                    {/each}
                </embla-container>
            </embla>

            <div class="gap-8 mt-16 hidden md:flex">
                <div
                    class="flex flex-col items-center w-32 h-20 justify-center rounded-lg bg-[#42424240]"
                >
                    <rectangle
                        style="width: 20px;height: 20px;background: #DCD9F7;border-radius: 2px;"
                    />
                    <div class="w-32 mt-2.5">Placeholder</div>
                </div>

                <div class="text-start">
                    <p class="font-bold text-xl">Characters, Seiyuus, Studios and lots more!</p>
                    <p>
                        Did you know that you can search for characters, voice actors/actresses,
                        studios and anime staff here? You can also
                        <Heart
                            height={12}
                            width={12}
                            class="inline-block"
                            color="#FFABB6"
                        />
                        your favorite ones. If you have a tracker account added, they will also be synced
                        to your profile.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
