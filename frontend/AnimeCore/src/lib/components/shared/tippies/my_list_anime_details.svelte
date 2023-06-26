<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Circle from "$icons/circle.svelte";

    export let anime_cover: string;
    export let anime_name: string;
    export let anime_type: string;
    export let anime_release_date: string;
    export let anime_episodes_count: number;
    export let anime_genres: string[];
    export let anime_studios: string[];
    export let anime_synopsis: string;
    export let anime_current_episode: number;
</script>

<div class="z-20 h-[18vw] w-[20vw] rounded-[1vw]">
    <div
        class="relative flex h-full w-full items-center overflow-hidden rounded-[1vw] bg-cover bg-center"
        style="background-image: url({anime_cover});"
    >
        <gradient-overlay class="gradient absolute h-full w-full bg-gradient-to-t from-surface-900 to-surface-900/25 transition duration-300 group-hover:to-surface-900/50" />
        <gradient-overlay class="gradient absolute h-full w-full bg-gradient-to-r from-surface-900/75 to-surface-900/25 transition duration-300 group-hover:to-surface-900/50" />

        <div class="absolute flex h-full flex-col justify-end rounded-[1vw] border-[0.25vw] border-b-0 border-surface-50/50 px-[1.5625vw] pb-[3vw]">
            <span class="line-clamp-1 text-[1vw] font-semibold leading-[1.25vw] text-white">
                {anime_name}
            </span>
            <span class="line-clamp-1 text-[0.75vw] font-semibold uppercase leading-[1.25vw] tracking-wider text-surface-50">
                {anime_name}
            </span>

            <div class="mt-[0.25vw] flex items-center gap-[0.5vw] text-[0.75vw]">
                <span>{anime_type}</span>
                <Circle class="w-[0.2vw] text-surface-50" />
                <span class="capitalize">
                    {new FormatDate(anime_release_date).format_to_season}
                </span>
                <Circle class="w-[0.2vw] text-surface-50" />
                <span>{anime_episodes_count} episodes</span>
            </div>

            <div class="mt-[0.5vw] flex gap-[0.5vw]">
                {#each anime_genres as genre}
                    <span class="rounded-[0.25vw] bg-surface-900 px-[0.625vw] py-[0.35vw] text-[0.75vw] leading-[0.75vw]">
                        {genre}
                    </span>
                {/each}
            </div>

            <div class="mt-[0.5vw] flex items-center gap-[0.5vw] text-[0.75vw]">
                <span>
                    69% <span class="text-surface-200">[7852 ratings]</span>
                </span>
                <Circle class="w-[0.2vw] text-surface-50" />
                <span>{anime_studios[0]}</span>
            </div>

            <span class="mt-[0.75vw] line-clamp-3 text-[0.75vw] font-medium leading-[1vw] text-surface-50">
                {anime_synopsis}
            </span>
        </div>

        <div class="absolute bottom-0 flex h-[1.75vw] w-full items-center justify-center gap-[0.5vw] bg-primary-500 text-[0.9vw] font-semibold">
            <span class="font-medium">Watching</span>
            <Circle class="w-[0.2vw]" />
            <span>
                {anime_current_episode}/{anime_episodes_count}
            </span>
        </div>
    </div>
</div>
