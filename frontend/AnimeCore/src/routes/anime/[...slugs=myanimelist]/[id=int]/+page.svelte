<script lang="ts">
    import AnimeInfo from "$components/pages/AnimeInfo/Index.svelte";

    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<svelte:head>
    {#if data.animeData.id}
        <title>{data.animeData?.title_english} | CoreProject | MyAnimelist</title>
    {:else}
        <title>Not Found | CoreProject | MyAnimeList</title>
    {/if}
</svelte:head>

{#if data.animeData.id}
    <AnimeInfo data={data.animeData} />
{:else}
    <div class="flex h-screen flex-1 items-center justify-center text-2xl font-bold text-white">
        404 | Not found
    </div>
{/if}
