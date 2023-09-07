<script lang="ts">
    import { page } from "$app/stores";
    import { OpengraphGenerator } from "$functions/opengraph";
    import AnimeCore from "$icons/anime_core.svelte";

    const opengraph_html = new OpengraphGenerator({
        title: "CoreProject - A modern anime, manga, sound streaming site",
        site_name: "CoreProject",
        image_url: "", // Use Opengraph later
        url: $page.url.href,
        locale: "en_US",
        description: "The most modern anime, manga, sound streaming site"
    }).generate_opengraph();
</script>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

<div class="flex gap-3 md:gap-[0.75vw] w-full h-full items-center justify-center">
    <span class="text-3xl md:text-[1.75vw]">Visit</span>
    <a
        href="/anime"
        class="border-b-2 border-surface-50/50 transition-colors md:border-b-[0.15vw] hover:border-surface-50"
    >
        <AnimeCore class="w-48 md:w-[10vw]" />
    </a>
</div>
