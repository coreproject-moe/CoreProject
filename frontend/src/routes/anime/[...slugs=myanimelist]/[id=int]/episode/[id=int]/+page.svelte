<script lang="ts">
    import { page } from "$app/stores";
    import EpisodePage from "$components/pages/episode/index.svelte";
    import { OpengraphGenerator } from "$functions/opengraph";
    import { derived } from "svelte/store";

    let episode_number = derived(page, (page) => page.params.id);

    const opengraph_html = new OpengraphGenerator({
        title: `Watch  on AnimeCore | Episode ${episode_number}`,
        url: $page.url.href,
        description: "",
        site_name: "CoreProject",
        locale: "en_US",
        image_url: ""
    }).generate_opengraph();
</script>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

<EpisodePage episode_number={Number($episode_number)} />
