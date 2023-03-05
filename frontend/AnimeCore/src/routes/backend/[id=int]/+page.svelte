<script lang="ts">
    import AnimeInfo from "$components/pages/AnimeInfo/Index.svelte";

    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<svelte:head>
    <title>{data.animeData?.title_english} | CoreProject</title>
</svelte:head>

<AnimeInfo data={data.animeData} />
