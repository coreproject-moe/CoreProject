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

    export let episodes: Episodes;
</script>

<ScrollArea gradient_mask>
    {#each episodes as episode}
        <Episode {episode} />
    {/each}
</ScrollArea>
