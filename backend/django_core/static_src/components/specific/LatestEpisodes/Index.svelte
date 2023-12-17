<script lang="ts">
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Episode from "./Episode.svelte";
    import type { Episode as EpisodeType } from "../../../types/episode";

    export let episodes: string;
    // parse string to JSON
    let episodes_data: EpisodeType[] = JSON.parse(episodes);
</script>

<ScrollArea
    gradient_mask
    offset_scrollbar
    parent_class="mt-[1vw] w-full max-h-[23vw] snap-y smooth-scroll snap-mandatory"
    class="flex w-full flex-col gap-[1vw]"
>
    {#each episodes_data as episode}
        <Episode {episode} />
    {/each}
</ScrollArea>
