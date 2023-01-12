<script lang="ts">
    import exploreData from "$data/mock/explore.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import FourBoxSquares from "$icons/FourBoxSquares.svelte";
    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
    import AnimeCard from "./AnimeCard.svelte";

    let selectionChoice = "popular";
</script>

<div class="hero min-h-[60vh] md:min-h-screen w-screen flex flex-col">
    <div class="flex gap-3 md:gap-32 pt-8 ml-8 md:ml-0 my-7 md:my-0">
        {#each ["popular", "trending", "top rated", "upcoming"] as item}
            <button
                class="btn {item.toLowerCase() === selectionChoice.toLowerCase() &&
                    'btn-active'} btn-ghost text-white capitalize font-bold text-lg"
                on:click|capture={() => {
                    selectionChoice = item.toLowerCase();
                }}
            >
                {item}
            </button>
        {/each}
    </div>
    {#if mobile}
        <div class="flex w-screen">
            <div class="self-start pl-8">
                All Time
                <ChevronDown
                    class="inline-block"
                    color="white"
                    height={18}
                    width={18}
                />
            </div>
        </div>
    {:else}
        <div class="flex gap-7 mt-8">
            <div class="flex flex-col w-[135px]">
                <span>Time Range</span>
                <select class="mt-2 select w-full bg-neutral">
                    <option selected>All-Time</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
                Genre
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
                Year
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
                Season
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
                Format
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
                Airing Status
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Any</option>
                </select>
            </div>
            <div class="flex flex-col w-[135px]">
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
                        class="input bg-neutral w-[135px] pl-9"
                        autocomplete="off"
                    />
                </div>
            </div>
            <div class="flex flex-col w-[135px]">
                Sort by
                <select class="mt-2 select w-full max-w-[135px] bg-neutral">
                    <option selected>Popularity</option>
                </select>
            </div>
            <div class="flex self-end">
                <button class="btn btn-square">
                    <FourBoxSquares
                        height={24}
                        width={24}
                        color="#D9D9D9"
                    />
                </button>
            </div>
        </div>
        <div class="mt-[40px] grid gap-x-20 gap-y-10 grid-cols-3">
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
