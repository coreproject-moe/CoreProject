<script lang="ts">
    import JSON5 from "json5";

    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Episode from "./Episode.svelte";

    type Episodes = {
        id: number;
        cover: string;
        name: string;
        episode_number: string;
        release_date: string;
        synopsis: string;
    }[];

    export let latest_episodes: string;
    // parse to JSON
    const latest_episodes_data = JSON5.parse(latest_episodes) satisfies Episodes;
</script>

<ScrollArea
    gradient_mask
    offset_scrollbar
    parent_class="mt-[1vw] w-full max-h-[23vw] snap-y smooth-scroll snap-mandatory"
    class="flex w-full flex-col gap-[1vw]"
>
    {#each latest_episodes_data as episode}
        <Episode {episode} />
    {/each}
</ScrollArea>
