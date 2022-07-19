<script lang="ts">
    import Navbar from "$components/common/Navbar.svelte";
    import ScrollArea from "$components/common/ScrollArea.svelte";
    import type { Swiper as SwiperType } from "swiper";
    import Progress from "./Progress.svelte";
    import type Timer from "easytimer.js";
    import type { SvelteComponent } from "svelte";

    export let rootSwiper: SwiperType;
    export let mainHeroSwiper:SwiperType;
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

    interface IProgress extends SvelteComponent,Partial<Timer>{}
    let progress :IProgress;

    const disableScroll = () => {
        rootSwiper.mousewheel.disable();
        rootSwiper.allowTouchMove = false;
        progress.pause?.()
    };
    const enableScroll = () => {
        rootSwiper.mousewheel.enable();
        rootSwiper.allowTouchMove = true;

        progress.start?.()
    };

    const timerEnded = () => {
        mainHeroSwiper.slideNext()
    }
</script>

<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url('{backgroundImage}');"
>
    <div class="hero-overlay grid">
        <div class="pt-8 pr-[72px] pl-16 pb-0">
            <Navbar />
        </div>
        <div class="grid grid-flow-col auto-cols-max justify-between min-w-full content-end pb-8">
            <div class='hidden md:flex'></div>
            <div class='flex items-center gap-4'>
                {#if isActive}
                    <Progress bind:this={progress} on:targetAchieved={timerEnded}/>
                {:else}
                    <!-- Placeholder to prevent layout shift -->
                    <progress class="progress progress-secondary w-40" value=0 max=100/>
                {/if}

                <div class="swiper__mainhero__pagination w-40" />
            </div>
            <div class='hidden md:flex'>03</div>
        </div>
    </div>

    <div class="pl-10 md:pl-24 hero-content flex-col text-neutral-content text-white justify-self-start">
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
                class="text-6xl font-bold">{animeTitle}</ScrollArea
            >

            <h1 class="font-bold py-8 hidden md:flex">
                <span class="items pr-2">TV</span><span class="items pr-2"
                    >{animeEpisodeCount} eps</span
                ><span class="items pr-2">Completed</span><span class="items pr-2"
                    >{animeAirTime}</span
                ><span>{animeStudio}</span>
            </h1>
            <ScrollArea
                parentClass="mb-5"
                class="max-h-24 font-normal text-gray-400"
                on:mouseenter={disableScroll}
                on:mouseleave={enableScroll}
                offsetScrollbar
            >
                {animeSummary}
            </ScrollArea>
            <div class="flex gap-4 pt-3">
                {#each tags as tag}
                    <span class="badge bg-base-100 badge-lg rounded-md text-white uppercase border-transparent"
                        >{tag}</span
                    >
                {/each}
            </div>
            <div class="mt-6 flex gap-4">
                <button class="btn btn-lg btn-secondary rounded-[16px] px-5 "
                    ><img alt="" src="/icons/play.svg" width="24" height="24" /></button
                >
                <button class="btn btn-secondary btn-lg btn-outline border-4 rounded-[16px]">
                    <div class="text-lg font-bold flex gap-2">
                        Details
                        <span class="flex items-center">
                            <img
                                alt=""
                                src="/icons/chevrons-right.svg"
                                width="24"
                                height="24"
                            />
                        </span>
                    </div>
                </button>
            </div>
        </div>

    </div>
</div>

<style lang="scss">
    .hero-overlay {
        box-shadow: inset 0px -30px 12px -2px rgba(7, 5, 25, 0.85),
                inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.8),
                inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2);

        @media screen and (min-width:768px){
                    box-shadow:
inset 0 4px calc(10vh + 1800px) rgb(7, 5, 25),
            inset 0 -40vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.2);

        }
    }

    .items {
        &::after {
            content: " ▪ ";
        }
    }
</style>
