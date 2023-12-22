<script lang="ts">
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

    export let episodes: string;
    // parse string to JSON
    let episodes_data: Episodes = JSON.parse(episodes);
</script>

<ScrollArea
    gradient_mask="true"
    offset_scrollbar="true"
    parent_class="mt-[1vw] w-full max-h-[23vw] snap-y smooth-scroll snap-mandatory"
    class="flex w-full flex-col gap-[1vw]"
>
    {#each episodes_data as episode}
        <Episode {episode} />
    {/each}
</ScrollArea>
