<script lang="ts">
    import { page } from "$app/stores";
    import { OpengraphGenerator } from "$functions/opengraph";

    import Login from "./login.svelte";
    import UploadPage from "./upload_page.svelte";

    let token: string | null = null; // check if token is valid

    function on_submit(values: CustomEvent) {
        token = values.detail;
    }

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

{#if token}
    <UploadPage />
{:else}
    <!-- logic for testing -->
    <Login on:submit={on_submit} />
{/if}
