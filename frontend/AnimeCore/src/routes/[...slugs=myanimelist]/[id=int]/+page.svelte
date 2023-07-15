<script lang="ts">
    import { page } from "$app/stores";
    import AnimeInfoErrorPage from "$components/pages/anime_info/error.svelte";
    import AnimeInfoPage from "$components/pages/anime_info/index.svelte";
    import { anime_episodes } from "$data/mock/anime_episodes";
    import { anime_list } from "$data/mock/anime_list";
    import { OpengraphGenerator } from "$functions/opengraph";
    import TopRounded from "$icons/top_rounded.svelte";

    let anime_id = Number($page.params.id);

    let anime = anime_list?.find((anime) => anime.id === anime_id);

    const opengraph_html = new OpengraphGenerator({
        title: anime ? `Watch ${anime?.name} on AnimeCore` : "404 - Page not found!",
        url: $page.url.href,
        description: anime?.synopsis ?? "",
        site_name: "CoreProject",
        locale: "en_US",
        image_url: anime?.banner ?? ""
    }).generate_opengraph();
</script>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

{#if anime}
    <!--
        TopRounded is due to how skeleton works with it's AppRail.
        We are essentially monkeypatching border-top-left-radius
    -->
    <TopRounded class="fixed z-10 hidden w-[1.5vw] text-surface-900 md:flex" />
    <AnimeInfoPage
        anime_name={anime.name}
        japanese_name={anime.japanese_name}
        anime_episodes_count={anime.episodes_count}
        anime_date={anime.updated}
        anime_synopsis={anime.synopsis}
        anime_banner={anime.banner}
        anime_cover={anime.cover}
        {anime_episodes}
    />
{:else}
    <AnimeInfoErrorPage />
{/if}
