<script lang="ts">
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import Circle from "$icons/circle.svelte";
    import Info from "$icons/info.svelte";
    import PlayCircle from "$icons/play_circle.svelte";
    import Star from "$icons/star.svelte";

    export let anime_id: number, anime_name: string, anime_episodes_count: number, anime_current_episode: number, anime_type: string, anime_genres: string[], anime_studios: string[], anime_synopsis: string, anime_release_date: string;
</script>

<popup-container class="hidden flex-col overflow-hidden bg-surface-400 leading-none md:flex md:w-[20vw] md:rounded-[0.75vw]">
    <div class="flex flex-col md:gap-[0.35vw] md:p-[1vw]">
        <anime-name class="font-semibold md:text-[1vw] md:leading-[1.25vw]">{anime_name}</anime-name>

        <div class="flex items-center text-surface-50 md:gap-[0.35vw] md:text-[0.8vw]">
            <rating class="flex items-center md:gap-[0.5vw]">
                <Star
                    color="yellow"
                    variant="full"
                    fill_color="yellow"
                    class="h-[1.1vw] w-[1.1vw]"
                />
                <span class="leading-none text-surface-50 md:text-[0.8vw]">4.5 rating</span>
            </rating>
            <Circle class="opacity-50 md:w-[0.25vw]" />
            <anime-type>{anime_type}</anime-type>
            <Circle class="opacity-50 md:w-[0.25vw]" />
            <episodes-count>{anime_episodes_count} episdoes</episodes-count>
        </div>
        <studio class="text-surface-50 md:text-[0.75vw]">
            {#each anime_studios as studio}
                <span>{studio}</span>
            {/each}
        </studio>
        <genres class="flex items-center md:my-[0.35vw] md:gap-[0.5vw]">
            {#each anime_genres as genre}
                <genre class="bg-surface-50 font-semibold leading-none text-black md:rounded-[0.35vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">
                    {genre}
                </genre>
            {/each}
        </genres>
        <ScrollArea
            parentClass="md:max-h-[4vw]"
            offsetScrollbar
            class="text-surface-50 md:text-[0.8vw] md:leading-[1vw]"
        >
            {anime_synopsis}
        </ScrollArea>

        <options class="flex items-center border-t-[0.1vw] border-white/10 md:mt-[0.25vw] md:gap-[0.5vw] md:pt-[0.75vw]">
            <a
                href="/mal/{anime_id}/episode/{anime_current_episode}"
                class="btn h-[2.3vw] flex-1 bg-primary-500 leading-none md:rounded-[0.5vw]"
            >
                <PlayCircle class="md:w-[0.9vw]" />
                <span class="font-semibold md:text-[0.9vw]">Continue Ep {anime_current_episode}</span>
            </a>
            <a
                href="/mal/{anime_id}"
                class="btn aspect-square h-[2.3vw] bg-primary-500/25 p-0 leading-none md:rounded-[0.5vw]"
            >
                <Info class="md:w-[1.2vw]" />
            </a>
        </options>
    </div>
</popup-container>
