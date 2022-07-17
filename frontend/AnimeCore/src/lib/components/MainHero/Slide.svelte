<script lang="ts">
    import Navbar from "$components/common/Navbar.svelte";
    import type { Swiper as SwiperType } from 'swiper';

    export let isVisible:boolean;
    export let isDuplicate:boolean;
    export let isActive:boolean;

    export let rootSwiper : SwiperType;
    export let animeTitle: string;
    export let animeSummary: string;
    export let animeEpisodeCount: number;
    export let animeStudio: string;
    export let animeAirTime: string;
    export let backgroundImage: string;
    export let backgroundBanner: string;
    export let tags: string[];

    const disableScroll = () => {
        rootSwiper.mousewheel.disable();
        rootSwiper.allowTouchMove = false;
    }
    const enableScroll = () => {
        rootSwiper.mousewheel.enable()
        rootSwiper.allowTouchMove = true;

    }
</script>
<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url('{backgroundImage}');"
>
    <div class="hero-overlay bg-opacity-60 bg-gradient-to-t from-base-100">
        <div class="pt-8 pr-[72px] pl-16 pb-0">
            <Navbar />
        </div>
    </div>
    {#if rootSwiper?.activeIndex === 0}
        <div class="pl-10 md:pl-24 hero-content text-neutral-content text-white justify-self-start">
            <div class="max-w-prose">
                <div class="text-secondary text-lg font-bold pb-3 flex gap-2">
                    Featured
                    <span class='flex items-center' >
                        <span
                        style="display: inline-block; width: 60px; border-top: 4px solid; border-radius: 10px;"
                    />
                    </span>
                </div>
                <h1 class="mb-4 text-6xl font-bold max-h-16 h-20 overflow-y-scroll hover:scrollbar-thumb-gray-100 scrollbar scrollbar-thumb-gray-200 scrollbar-thumb-neutral-900">{animeTitle}</h1>
                <h1 class='font-bold py-8 hidden md:flex'>
                    <span class="items pr-2">TV</span><span
                        class="items pr-2">{animeEpisodeCount} eps</span
                    ><span class="items pr-2">Completed</span><span
                        class="items pr-2">{animeAirTime}</span
                    ><span>{animeStudio}</span>

                </h1>
                <div class="mb-5 max-h-24 text-ellipsis overflow-y-scroll hover:scrollbar-thumb-gray-100 scrollbar scrollbar-thumb-gray-200 scrollbar-thumb-neutral-900" on:mouseenter={disableScroll} on:mouseleave={enableScroll}  >
                    <div class="pr-3 font-normal text-gray-400">{animeSummary}</div>
                </div>
                <div class='flex gap-4 pt-3'>
                    {#each tags as tag}
                        <span class="badge bg-base-100 badge-lg rounded-md text-white">{tag}</span>
                    {/each}
                </div>
                <div class='mt-6 flex gap-4'>
                    <button class="btn btn-lg btn-secondary rounded-[16px] px-5 "><img alt="" src="/icons/play.svg" width="24" height="24"></button>
                    <button class="btn btn-secondary btn-lg btn-outline border-4 rounded-[16px]">
                        <div class="text-lg font-bold flex gap-2">
                            Details
                            <span class='flex items-center' >
                                <img alt="" src="/icons/chevrons-right.svg" width="24" height="24"/>
                            </span>
                        </div>

                    </button>
                </div>
            </div>
        </div>
    {:else}
        <div></div>
    {/if}
</div>

<style lang="scss">
    .items {
        &::after {
            content:" ▪ "
        }
    }

</style>
