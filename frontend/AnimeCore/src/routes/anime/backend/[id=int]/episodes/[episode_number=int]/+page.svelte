<script lang="ts">
    import voca from "voca";
    
    import Episode from "$components/pages/Episode/Index.svelte";
    import { UrlMaps } from "$data/urls";
    
    import type { PageData } from "./$types";

    export let data: PageData;

    const backend_mapping = new UrlMaps();
</script>

<svelte:head>
    <title>
        {data?.anime?.name} : {data?.episode?.episode_number} | {data?.episode?.episode_name} | CoreProject
    </title>
    <meta
        property="og:title"
        content={data?.episode?.episode_name}
    />
    <meta
        property="og:type"
        content="video.movie"
    />
    <meta
        property="og:image"
        content={backend_mapping.DOMAIN + data?.episode?.episode_thumbnail}
    />
    <meta
        property="og:description"
        content={voca.truncate(data?.episode?.episode_summary ?? "", 60)}
    />
</svelte:head>

<Episode data={data?.episode} />
