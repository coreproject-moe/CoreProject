<script lang="ts">
    export let title_english: string;
    export let title_japanese: string;
    export let anime_source: string;
    export let episodes: number;
    export let status: "completed" | "airing";
    export let aired_from: string;

    import { formatDateString } from "$functions/covertDateToSeason";
    import BookOpen from "$icons/Book-Open.svelte";
    import Download from "$icons/Download.svelte";
    import Edit from "$icons/Edit.svelte";
    import PlayCircle from "$icons/PlayCircle.svelte";
    import Share from "$icons/Share.svelte";
    import Video from "$icons/Video.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

<anime-info-base class="flex w-3/5 flex-col gap-2 md:w-72">
    <h1 class="text-2xl font-bold text-white md:text-4xl">{title_english}</h1>
    <p class="text-sm text-neutral-400">
        <!-- Todo modify this to have anime synonyms  -->
        <span class="items">{title_japanese}</span>
    </p>
    <p class="text-xs text-white">
        {#if anime_source}
            <span class="items">{anime_source}</span>
        {/if}
        {#if episodes}
            <span class="items">{episodes}eps</span>
        {/if}
        <span class="items">{status}</span>
        {#if aired_from}
            <span class="items">{formatDateString(aired_from)}</span>
        {/if}
    </p>

    <!-- buttons  -->
    {#if !mobile}
        <div class="mt-7 flex items-center gap-4">
            <button
                aria-label="Play"
                class="btn-primary btn-lg btn h-[70px] w-[108px] rounded-lg normal-case"
            >
                <div class="flex justify-between gap-2 py-2">
                    <PlayCircle
                        width={30}
                        height={30}
                        color="white"
                        class="translate-y-1"
                    />
                    <div class="flex flex-col text-start">
                        <h2 class="text-sm font-bold">Watch</h2>
                        <p class="text-xs font-thin text-zinc-300">Ep 01</p>
                    </div>
                </div>
            </button>
            <button
                aria-label="Play"
                class="btn-info btn-square btn-lg btn rounded-lg normal-case"
            >
                <div class="flex flex-col items-center justify-center py-2">
                    <BookOpen
                        width="32"
                        height="31"
                        class="text-base-100"
                    />
                    <p>Read</p>
                </div>
            </button>
        </div>
    {/if}
    <!-- Share button groups  -->
    {#if !mobile}
        <div class="mt-5 flex gap-2">
            <button class="btn-warning btn-square btn-sm btn flex items-center justify-center">
                <Video
                    width="18"
                    height="18"
                    class="text-base-100"
                />
            </button>
            <button class="btn-warning btn-square btn-sm btn flex items-center justify-center">
                <Edit
                    variant="with_underline_around_pencil"
                    width="18"
                    height="18"
                    class="text-base-100"
                />
            </button>
            <button class="btn-warning btn-square btn-sm btn flex items-center justify-center">
                <Download
                    width="18"
                    height="18"
                    class="text-base-100"
                />
            </button>
            <button class="btn-warning btn-square btn-sm btn flex items-center justify-center">
                <Share
                    width="18"
                    height="18"
                    class="text-base-100"
                />
            </button>
        </div>
    {/if}
</anime-info-base>

<style lang="scss">
    .items {
        &:not(:last-child)::after {
            content: " ▪ ";
        }
    }
</style>
