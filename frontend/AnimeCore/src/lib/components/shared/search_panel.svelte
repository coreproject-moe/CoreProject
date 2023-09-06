<script lang="ts">
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import Circle from "$icons/circle.svelte";
    import Cross from "$icons/cross.svelte";
    import Search from "$icons/search.svelte";
    import ImageLoader from "./image/image_loader.svelte";

    // search input
    let search_query: string;
</script>

<search-panel>
    <div class="mt-[3.5vw] flex flex-col items-center">
        <form class="relative flex h-[3.7vw] w-[37.5vw] items-center">
            <button
                class="btn absolute left-[1.25vw] p-0"
                aria-label="Search"
            >
                <Search style="width: 1.25vw;" />
            </button>
            <input
                bind:value={search_query}
                type="text"
                placeholder="Search for animes, mangas and musics"
                class="h-full w-full rounded-[0.625vw] border-none bg-surface-400 pl-[3.50vw] text-[1.1vw] font-semibold text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-50"
            />

            <button
                type="button"
                aria-label="Clear"
                class="btn absolute right-[1.25vw] p-0"
                on:click={() => (search_query = "")}
            >
                <Cross style="width: 1.5vw; opacity: 0.7;" />
            </button>
        </form>

        <div class="mt-[1.5vw] flex gap-[4vw]">
            <div>
                <span class="text-[1.2vw] font-semibold text-surface-50">anime</span>
                <div class="mt-[0.2vw] h-[28.25vw] w-[21.875vw] rounded-[0.75vw] bg-surface-400 p-[1vw] shadow-lg">
                    <ScrollArea
                        offsetScrollbar
                        gradientMask
                        class="md:pb-[2vw]"
                    >
                        {#each Array(6) as _}
                            <a
                                href="/mal/"
                                class="flex items-center gap-[1vw] rounded-[0.7vw] p-[0.8vw] transition duration-200 hover:bg-white/10"
                            >
                                <ImageLoader
                                    src="/images/DemonSlayer-bg.avif"
                                    alt={search_query}
                                    class="h-[3.5vw] w-[3.5vw] rounded-[0.5vw] object-cover"
                                />
                                <div class="flex flex-col">
                                    <span class="text-[1.1vw] font-semibold leading-none text-white">Kimetsu no Yaiba</span>
                                    <span class="text-[0.7vw] font-medium uppercase leading-[1.5vw] text-surface-200">Demon slayer</span>
                                    <div class="flex items-center gap-[0.3vw] text-[0.7vw] leading-[1vw] text-surface-200">
                                        <span>2006</span>
                                        <span>TV</span>
                                        <Circle style="width: 0.2vw;" />
                                        <span>26 eps</span>
                                    </div>
                                </div>
                            </a>
                        {/each}
                    </ScrollArea>
                </div>
            </div>

            <div>
                <span class="text-[1.2vw] font-semibold text-surface-50">manga</span>
                <div class="mt-[0.2vw] h-[28.25vw] w-[21.875vw] rounded-[0.75vw] bg-surface-400 shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">mangacore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>

            <div>
                <span class="text-[1.2vw] font-semibold text-surface-50">music</span>
                <div class="mt-[0.2vw] h-[28.25vw] w-[21.875vw] rounded-[0.75vw] bg-surface-400 shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">soundcore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>
        </div>

        <p class="mt-[2vw] text-[0.8vw] text-surface-50">
            Want even advanced searching with genres, time-ranges, tags and more? Try the
            <a
                href="/explore"
                class="text-surface-50 underline"
            >
                Explore
            </a>
            page
        </p>
    </div>
</search-panel>
