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
                class="hero-overlay grid from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
                style="--tw-bg-opacity:0"
            >
                <div
                    class="grid min-w-full auto-cols-max grid-flow-col content-end justify-center  pb-8 md:justify-between"
                >
                    <div class="hidden md:flex" />
                    <div class="flex items-center gap-3">
                        <Progress
                            class="w-32 md:w-48"
                            on:targetAchieved={timerEnded}
                        />

                        <div
                            class="swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal flex w-56 justify-center"
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
                        <div class="hidden gap-4 md:flex">
                            <button
                                class="btn-secondary btn-square btn-sm btn"
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
                                class="btn-secondary btn-square btn-sm btn"
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
                    <div class="hidden animate-bounce items-center md:flex">
                        <Mouse
                            width={24}
                            height={24}
                            color="white"
                        />
                        <div class="px-3">scroll below</div>
                    </div>
                </div>
            </div>

            <div class="hero-content flex-col justify-self-start pl-10 md:pl-24">
                <div class="max-w-[80vw]">
                    <div class="flex gap-2 pb-3 text-lg font-bold text-secondary">
                        Featured
                        <span class="flex items-center">
                            <span
                                style="display: inline-block; width: 60px; border-top: 4px solid; border-radius: 10px;"
                            />
                        </span>
                    </div>
                    <ScrollArea
                        style="height:72px"
                        class="text-3xl font-bold leading-8 md:text-6xl md:leading-[4.25rem]"
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

                    <h1 class="hidden py-8 font-bold md:flex">
                        <span class="items">TV</span>
                        <span class="items">{String(animeEpisodeCount)} eps</span>
                        <span class="items">Completed</span>
                        <span class="items">{String(animeAirTime)}</span>
                        <span class="items">{animeStudio}</span>
                    </h1>
                    <ScrollArea
                        parentClass="mb-5"
                        style="min-height:110px"
                        class="prose max-h-24 font-normal text-gray-400 [text-shadow:-1px_-1px_0_#0000009e,1px_-1px_0_#0000008c,0px_1px_0_#0000009e,1px_0px_0_#00000061]"
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
                    <div class="hidden gap-4 pt-3 md:flex">
                        {#each tags as tag}
                            <span
                                class="badge badge-lg rounded-md border-transparent bg-base-100 text-sm font-bold uppercase leading-6 text-white"
                            >
                                {tag}
                            </span>
                        {/each}
                    </div>
                    <div class="mt-6 flex gap-4">
                        <button
                            aria-label="Play"
                            class="btn-secondary btn-md btn rounded-[16px] px-5 md:btn-lg "
                        >
                            <Play
                                width={24}
                                height={24}
                            />
                        </button>
                        <button
                            class="btn-outline btn-secondary btn-md btn rounded-[16px] border-4 md:btn-lg"
                        >
                            <div class="flex gap-2 text-lg font-bold">
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
