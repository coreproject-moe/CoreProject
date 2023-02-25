<script lang="ts">
    import AnimeInfo from "$components/pages/AnimeInfo/Index.svelte";

    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<AnimeInfo {data} />
