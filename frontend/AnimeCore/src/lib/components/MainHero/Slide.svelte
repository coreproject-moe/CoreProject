<script lang="ts">
    import type { SvelteComponent } from "svelte";
    import type { Swiper as SwiperType } from "swiper";

    import Navbar from "$components/common/Navbar.svelte";
    import ScrollArea from "$components/common/ScrollArea.svelte";
    import ChevronLeft from "$icons/Chevron-Left.svelte";
    import ChevronRight from "$icons/Chevron-Right.svelte";
    import ChevronsRight from "$icons/Chevrons-Right.svelte";
    import Mouse from "$icons/Mouse.svelte";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";

    import Progress from "./Progress.svelte";

    export let rootSwiper: Partial<SwiperType>;
    export let mainHeroSwiper: Partial<SwiperType>;

    export let isPrev: boolean;
    export let isNext: boolean;
    export let isVisible: boolean;
    export let isDuplicate: boolean;
    export let isActive: boolean;

    export let animeTitle: string;
    export let animeSummary: string;
    export let animeEpisodeCount: number;
    export let animeStudio: string;
    export let animeAirTime: string;
    export let backgroundImage: string;
    export let backgroundBanner: string;
    export let tags: string[];

    // Event listener to reset the timer on slide change
    $: rootSwiper?.on?.("slideChange", () => {
        if (rootSwiper?.realIndex === 0) {
            progress?.reset?.();
            progress?.start?.();
        } else {
            progress?.pause?.();
        }
    });

    interface IProgress extends SvelteComponent {
        start: () => void;
        reset: () => void;
        pause: () => void;
    }

    let progress: IProgress;

    let mobile: boolean;
    let tablet: boolean;
    let fullhd: boolean;

    $: fullhd = $responsiveMode === "fullhd";
    $: tablet = $responsiveMode === "tablet";
    $: mobile = $responsiveMode === "mobile";

    let background: string;

    $: {
        if (mobile) {
            background = backgroundBanner;
        } else if (tablet) {
            background = backgroundImage;
        } else if (fullhd) {
            background = backgroundImage;
        } else {
            background = backgroundImage; // This is the default one
        }
    }

    const disableScroll = () => {
        rootSwiper.mousewheel?.disable();
        rootSwiper.allowTouchMove = false;
        progress.pause?.();
    };
    const enableScroll = () => {
        rootSwiper.mousewheel?.enable();
        rootSwiper.allowTouchMove = true;

        progress.start?.();
    };

    const timerEnded = () => {
        mainHeroSwiper.slideNext?.();
    };
</script>

<svelte:window
    on:focus={()=>{
        progress?.start?.()
    }}
    on:blur={()=>{
        progress?.pause?.()
    }}
/>

<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url('{background}');"
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
                {#if isActive}
                    <Progress bind:this={progress} on:targetAchieved={timerEnded} />
                {:else}
                    <!-- Placeholder to prevent layout shift -->
                    <progress class="progress progress-secondary w-40" value={0} max={100} />
                {/if}

                <div
                    class="w-40 flex justify-center swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal"
                >
                    {#each Array(10) as _, index}
                        <span
                            class="swiper-pagination-bullet {mainHeroSwiper?.realIndex === index
                                ? 'swiper-pagination-bullet-active'
                                : ''}"
                            on:click={() => {
                                mainHeroSwiper?.slideTo?.(index + 1);
                            }}
                        />
                    {/each}
                </div>
                <div class="gap-4 hidden md:flex">
                    <button
                        class="btn btn-secondary btn-sm btn-square"
                        on:click={() => {
                            mainHeroSwiper?.slidePrev?.();
                        }}
                    >
                        <ChevronLeft height={24} width={24} color="black" />
                    </button>
                    <button
                        class="btn btn-secondary btn-sm btn-square"
                        on:click={() => {
                            mainHeroSwiper?.slideNext?.();
                        }}
                    >
                        <ChevronRight height={24} width={24} color="black" />
                    </button>
                </div>
            </div>
            <div class="hidden md:flex items-center animate-bounce">
                <Mouse width={24} height={24} color="white" />
                <div class="px-3">scroll below</div>
            </div>
        </div>
    </div>

    <div
        class="pl-10 md:pl-24 hero-content flex-col text-neutral-content text-white justify-self-start"
    >
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
                on:mouseenter={disableScroll}
                on:mouseleave={enableScroll}
            >
                {animeTitle}
            </ScrollArea>

            <h1 class="font-bold py-8 hidden md:flex">
                <span class="items pr-2">TV</span>
                <span class="items pr-2">{animeEpisodeCount} eps</span>
                <span class="items pr-2">Completed</span>
                <span class="items pr-2">{animeAirTime}</span>
                <span class="items">{animeStudio}</span>
            </h1>
            <ScrollArea
                parentClass="mb-5"
                style="min-height:110px"
                class="max-h-24 font-normal text-gray-400 prose [text-shadow:-1px_-1px_0_#0000009e,1px_-1px_0_#0000008c,0px_1px_0_#0000009e,1px_0px_0_#00000061]"
                on:mouseenter={disableScroll}
                on:mouseleave={enableScroll}
                offsetScrollbar
            >
                {animeSummary}
            </ScrollArea>
            <div class="gap-4 pt-3 hidden md:flex">
                {#each tags as tag}
                    <span
                        class="badge bg-base-100 badge-lg rounded-md text-white uppercase border-transparent leading-6 text-sm font-bold"
                    >
                        {tag}
                    </span>
                {/each}
            </div>
            <div class="mt-6 flex gap-4">
                <button class="btn btn-md md:btn-lg btn-secondary rounded-[16px] px-5 ">
                    <Play width={24} height={24} />
                </button>
                <button
                    class="btn btn-secondary btn-md md:btn-lg btn-outline border-4 rounded-[16px]"
                >
                    <div class="text-lg font-bold flex gap-2">
                        Details
                        <span class="flex items-center">
                            <ChevronsRight height={24} width={24} />
                        </span>
                    </div>
                </button>
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
            content: " ▪ ";
        }
    }
</style>
