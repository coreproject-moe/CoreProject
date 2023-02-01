<script lang="ts">
    import AnimeInfo from "$components/pages/AnimeInfo/AnimeInfo.svelte";

    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<svelte:head>
    <title>{data.animeData?.title_english} | CoreProject | MyAnimelist</title>
</svelte:head>

<AnimeInfo data={data.animeData} />
