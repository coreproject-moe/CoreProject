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

<svelte:window on:focus={()=>{
    console.log('start')
    progress.start?.()
}} on:blur={()=>{
    console.log('stop')
    progress.stop?.()
}} />

<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url('{backgroundImage}');"
>
    <div class="hero-overlay bg-opacity-60 bg-gradient-to-t from-base-100 via-base-100/[.45] grid">
        <div class="pt-8 pr-[72px] pl-16 pb-0">
            <Navbar />
        </div>
        <div class="grid grid-flow-col auto-cols-max justify-between min-w-full content-end pb-8">
            <div class='hidden md:flex'></div>
            <div class='flex items-center gap-4'>
                {#if isActive}
                    <Progress bind:this={progress} on:targetAchieved={timerEnded}/>
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
                    <span class="badge bg-base-100 badge-lg rounded-md text-white uppercase"
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
    .items {
        &::after {
            content: " ▪ ";
        }
    }
</style>
