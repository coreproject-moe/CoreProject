<script lang="ts">
    import { onMount } from "svelte";

    import Navbar from "$components/shared/Navbar.svelte";
    import ScrollArea from "$components/shared/ScrollArea.svelte";
    import { fetchImageAndConvertToBlob } from "$functions/fetchImage";
    import { getImageBrightness } from "$functions/getImageBrightness";
    import ChevronLeft from "$icons/Chevron-Left.svelte";
    import ChevronRight from "$icons/Chevron-Right.svelte";
    import ChevronsRight from "$icons/Chevrons-Right.svelte";
    import Mouse from "$icons/Mouse.svelte";
    import Play from "$icons/Play.svelte";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { responsiveMode } from "$store/Responsive";
    import { timer as timerStore } from "$store/Timer";

    import Progress from "./Progress.svelte";

    export let data: Array<{
        animeEpisodeCount: number;
        animeStudio: string;
        animeAirTime: string;
        animeTitle: string;
        animeSummary: string;
        backgroundImage: string;
        backgroundBanner: string;
        tags: string[];
    }>;
    export let mainHeroSlideActiveIndex: number;
    export let animeTitle: string;
    export let animeSummary: string;
    export let animeEpisodeCount: string | number;
    export let animeStudio: string;
    export let animeAirTime: string;
    export let backgroundImage: string;
    export let backgroundBanner: string;
    export let tags: string[];

    export let addOneToMainHeroSlideActiveIndex: () => void;
    export let minusOneToMainHeroSlideActiveIndex: () => void;

    let background: string;

    let mobile: boolean;
    // let tablet: boolean;
    // let fullhd: boolean;

    $: mobile = $responsiveMode === "mobile";
    // $: fullhd = $responsiveMode === "fullhd";
    // $: tablet = $responsiveMode === "tablet";

    const timerEnded = () => {
        addOneToMainHeroSlideActiveIndex();
    };

    const checkViewPortAndMountChangeBackgroundImage = async () => {
        if (mobile) {
            background = await fetchImageAndConvertToBlob(backgroundBanner);
        } else {
            background = await fetchImageAndConvertToBlob(backgroundImage);
        }
    };

    onMount(async () => {
        await checkViewPortAndMountChangeBackgroundImage();

        getImageBrightness(background, (brightness) => {
            if (brightness == undefined || brightness > 120) {
                $navbar_variant = "black";
            } else {
                $navbar_variant = "white";
            }
        });
    });
</script>

<svelte:window
    on:resize={async () => {
        await checkViewPortAndMountChangeBackgroundImage();
    }}
    on:focus={() => {
        $timerStore = "start";
    }}
    on:blur={() => {
        $timerStore = "pause";
    }}
/>

<div class="inline-grid h-full w-screen">
    <div style="grid-area: 1 / 1 / 2 / 2">
        <div
            class="hero h-full w-full bg-center bg-no-repeat"
            style="background-image:url('{background ?? ''}')"
        >
            <div
                class="hero-overlay from-base-100 via-base-100/[.8] md:via-base-100/[.0001] grid"
                style="--tw-bg-opacity:0"
            >
                <div class="pt-8 md:pr-[72px] pl-6 md:pl-20 pb-0">
                    <Navbar />
                </div>
                <div
                    class="grid grid-flow-col auto-cols-max min-w-full content-end pb-8  justify-center md:justify-between"
                >
                    <div class="hidden md:flex" />
                    <div class="flex items-center gap-3">
                        <Progress
                            class="w-32 md:w-48"
                            on:targetAchieved={timerEnded}
                        />

                        <div
                            class="w-56 flex justify-center swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal"
                        >
                            <div class="flex flex-row gap-3">
                                {#each Array(data.length) as _, index}
                                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                                    <svg
                                        height="10"
                                        width="10"
                                        class="cursor-pointer"
                                        on:click={() => {
                                            mainHeroSlideActiveIndex = index;
                                        }}
                                    >
                                        <circle
                                            cx="5"
                                            cy="5"
                                            r="5"
                                            style="
                                            fill:{index === mainHeroSlideActiveIndex
                                                ? 'var(--swiper-pagination-color)'
                                                : 'var(--swiper-pagination-bullet-inactive-color)'};
                                            opacity:{index === mainHeroSlideActiveIndex
                                                ? '1'
                                                : 'var(--swiper-pagination-bullet-inactive-opacity)'}
                                            "
                                        />
                                    </svg>
                                {/each}
                            </div>
                        </div>
                        <div class="gap-4 hidden md:flex">
                            <button
                                class="btn btn-secondary btn-sm btn-square"
                                on:click={() => {
                                    minusOneToMainHeroSlideActiveIndex();
                                }}
                            >
                                <ChevronLeft
                                    height={24}
                                    width={24}
                                    color="black"
                                />
                            </button>
                            <button
                                class="btn btn-secondary btn-sm btn-square"
                                on:click={() => {
                                    addOneToMainHeroSlideActiveIndex();
                                }}
                            >
                                <ChevronRight
                                    height={24}
                                    width={24}
                                    color="black"
                                />
                            </button>
                        </div>
                    </div>
                    <div class="hidden md:flex items-center animate-bounce">
                        <Mouse
                            width={24}
                            height={24}
                            color="white"
                        />
                        <div class="px-3">scroll below</div>
                    </div>
                </div>
            </div>

            <div class="pl-10 md:pl-24 hero-content flex-col justify-self-start">
                <div class="max-w-[80vw]">
                    <div class="text-secondary text-lg font-bold pb-3 flex gap-2">
                        Featured
                        <span class="flex items-center">
                            <span
                                style="display: inline-block; width: 60px; border-top: 4px solid; border-radius: 10px;"
                            />
                        </span>
                    </div>
                    <ScrollArea
                        style="height:72px"
                        class="font-bold leading-8 md:leading-[4.25rem] text-3xl md:text-6xl"
                        on:mouseenter={() => {
                            $timerStore = "pause";
                        }}
                        on:mouseleave={() => {
                            $timerStore = "start";
                        }}
                        on:touchstart={() => {
                            $timerStore = "pause";
                        }}
                        on:touchend={() => {
                            $timerStore = "start";
                        }}
                    >
                        {animeTitle}
                    </ScrollArea>

                    <h1 class="font-bold py-8 hidden md:flex">
                        <span class="items">TV</span>
                        <span class="items">{String(animeEpisodeCount)} eps</span>
                        <span class="items">Completed</span>
                        <span class="items">{String(animeAirTime)}</span>
                        <span class="items">{animeStudio}</span>
                    </h1>
                    <ScrollArea
                        parentClass="mb-5"
                        style="min-height:110px"
                        class="max-h-24 font-normal text-gray-400 prose [text-shadow:-1px_-1px_0_#0000009e,1px_-1px_0_#0000008c,0px_1px_0_#0000009e,1px_0px_0_#00000061]"
                        offsetScrollbar
                        on:mouseenter={() => {
                            $timerStore = "pause";
                        }}
                        on:mouseleave={() => {
                            $timerStore = "start";
                        }}
                        on:touchstart={() => {
                            $timerStore = "pause";
                        }}
                        on:touchend={() => {
                            $timerStore = "start";
                        }}
                    >
                        {animeSummary}
                    </ScrollArea>
                    <div class="gap-4 pt-3 hidden md:flex">
                        {#each tags as tag}
                            <span
                                class="badge text-white bg-base-100 badge-lg rounded-md uppercase border-transparent leading-6 text-sm font-bold"
                            >
                                {tag}
                            </span>
                        {/each}
                    </div>
                    <div class="mt-6 flex gap-4">
                        <button
                            aria-label="Play"
                            class="btn btn-md md:btn-lg btn-secondary rounded-[16px] px-5 "
                        >
                            <Play
                                width={24}
                                height={24}
                            />
                        </button>
                        <button
                            class="btn btn-secondary btn-md md:btn-lg btn-outline border-4 rounded-[16px]"
                        >
                            <div class="text-lg font-bold flex gap-2">
                                Details
                                <span class="flex items-center">
                                    <ChevronsRight
                                        height={24}
                                        width={24}
                                    />
                                </span>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style lang="scss">
    .hero-overlay {
        background-image: linear-gradient(to top, var(--tw-gradient-stops));

        @media screen and (min-width: 768px) {
            background-image: linear-gradient(to top, var(--tw-gradient-stops)),
                linear-gradient(to left, var(--tw-gradient-stops)),
                linear-gradient(to right, var(--tw-gradient-stops));
        }
    }
    .items {
        &:not(:last-child)::after {
            @apply pr-2;
            content: " ▪ ";
        }
    }
</style>
