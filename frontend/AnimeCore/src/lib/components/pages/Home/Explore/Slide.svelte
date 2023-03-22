<script lang="ts">
    import { Swiper, SwiperSlide } from "swiper/svelte";

    import exploreData from "$data/mock/explore.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import FourBoxSquares from "$icons/FourBoxSquares.svelte";
    import Funnel from "$icons/Funnel.svelte";
    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
    import AnimeCard from "./AnimeCard.svelte";

    let selectionChoice = "popular";
</script>

<div class="hero flex min-h-[80vh] w-screen flex-col md:min-h-screen">
    <div
        class="my-7 flex w-screen gap-3 overflow-y-scroll pt-8 scrollbar-hide md:my-0 md:w-auto md:gap-32"
    >
        {#each ["popular", "trending", "top rated", "upcoming"] as item}
            <button
                class="btn {selectionChoice.toLowerCase() === item.toLowerCase() &&
                    'btn-active'} btn-ghost text-lg font-bold capitalize text-white first:ml-4 last:mr-4 first:md:ml-0 last:md:mr-0 "
                on:click|capture={() => {
                    selectionChoice = item.toLowerCase();
                }}
            >
                {item}
            </button>
        {/each}
    </div>
    {#if mobile}
        <div class="flex w-screen items-center justify-between">
            <!-- All time button -->
            <div class="pl-8">
                All Time
                <ChevronDown
                    class="inline-block"
                    color="white"
                    height={18}
                    width={18}
                />
            </div>

            <!-- Filter and square Button  -->
            <div class="flex gap-6 pr-6">
                <button class="btn">
                    <div class="flex items-center gap-1">
                        <span>
                            <Funnel
                                width={18}
                                height={18}
                                color="white"
                            />
                        </span>
                        <span class="text-white">Filter</span>
                    </div>
                </button>
                <button class="btn-square btn">
                    <FourBoxSquares
                        height={24}
                        width={24}
                        color="#D9D9D9"
                    />
                </button>
            </div>
        </div>
        <div class="mt-10 h-96">
            <Swiper
                slidesPerView={2}
                direction="vertical"
            >
                {#each exploreData as item}
                    <SwiperSlide>
                        <AnimeCard
                            animeName={item.animeTitle}
                            animeCoverBackgroundImage={item.animeBackgroundCoverImage}
                            animeCardBackgroundImage={item.animeCardBackgroundImage}
                            animeTags={item.tags}
                            animeEpisodeCount={item.animeEpisodeCount}
                            animeAirTime={item.animeAirTime}
                            animeSummary={item.animeSummary}
                        />
                    </SwiperSlide>
                {/each}
            </Swiper>
        </div>
    {:else}
        <div class="mt-8 flex gap-7">
            <div class="flex w-[135px] flex-col">
                <span>Time Range</span>
                <select class="select mt-2 w-full bg-neutral">
                    <option selected>All-Time</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Genre
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Year
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Season
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Format
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Airing Status
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex w-[135px] flex-col">
                Search
                <div class="relative mt-2">
                    <span class="absolute inset-y-0 left-0 flex items-center pl-2">
                        <Search
                            class="ml-1"
                            color="white"
                            height="18"
                            width="18"
                        />
                    </span>
                    <input
                        type="text"
                        class="input w-[135px] bg-neutral pl-9"
                        autocomplete="off"
                    />
                </div>
            </div>
            <div class="flex w-[135px] flex-col">
                Sort by
                <select class="select mt-2 w-full max-w-[135px] bg-neutral">
                    <option selected>Popularity</option>
                </select>
            </div>
            <div class="flex self-end">
                <button class="btn-square btn">
                    <FourBoxSquares
                        height={24}
                        width={24}
                        color="#D9D9D9"
                    />
                </button>
            </div>
        </div>
        <div class="mt-[40px] grid grid-cols-3 gap-x-20 gap-y-10">
            {#each exploreData as item}
                <AnimeCard
                    animeName={item.animeTitle}
                    animeCoverBackgroundImage={item.animeBackgroundCoverImage}
                    animeCardBackgroundImage={item.animeCardBackgroundImage}
                    animeTags={item.tags}
                    animeEpisodeCount={item.animeEpisodeCount}
                    animeAirTime={item.animeAirTime}
                    animeSummary={item.animeSummary}
                />
            {/each}
        </div>
    {/if}
</div>
