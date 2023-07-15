<script lang="ts">
    import { page } from "$app/stores";
    import { OpengraphGenerator } from "$functions/opengraph";

    let upload_page = import("./upload_page.svelte");

    let current_page = upload_page;
    const opengraph_html = new OpengraphGenerator({
        title: `Upload on AnimeCore`,
        url: $page.url.href,
        description: "Upload on animecore",
        site_name: "CoreProject",
        locale: "en_US",
        image_url: ""
    }).generate_opengraph();
</script>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

{#await current_page then page}
    <svelte:component this={page.default} />
{/await}
