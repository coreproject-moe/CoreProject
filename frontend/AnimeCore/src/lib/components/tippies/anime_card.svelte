<script lang="ts">
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import { FormatDate } from "$functions/format_date";
    import { round_to_nearest_zero_point_five } from "$functions/math";
    import Circle from "$icons/circle.svelte";
    import Info from "$icons/info.svelte";
    import PlayCircle from "$icons/play_circle.svelte";
    import Star from "$icons/star.svelte";
    import { Ratings } from "@skeletonlabs/skeleton";

    export let anime_id: number;
    export let anime_name: string;
    export let anime_episodes_count: number;
    export let anime_type: string;
    export let anime_genres: string[];
    export let anime_studios: string[];
    export let anime_synopsis: string;
    export let anime_release_date: string;
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
                <span class="text-surface-50 md:text-[0.8vw] leading-none">4.5 rating</span>
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

        <options class="md:mt-[0.25vw] border-t-[0.1vw] md:pt-[0.75vw] border-white/10 flex items-center md:gap-[0.5vw]">
            <a href="/mal/{anime_id}/episode/1" class="btn leading-none bg-primary-500 md:rounded-[0.5vw] flex-1 h-[2.3vw]">
                <PlayCircle class="md:w-[1vw]" />
                <span class="md:text-[0.9vw] font-semibold">Watch Ep 1</span>
            </a>
            <a href="/mal/{anime_id}" class="btn leading-none bg-primary-500/25 md:rounded-[0.5vw] p-0 h-[2.3vw] aspect-square">
                <Info class="md:w-[1.2vw]" />
            </a>
        </options>
    </div>
</popup-container>