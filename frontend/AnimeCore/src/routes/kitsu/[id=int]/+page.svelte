<script lang="ts">
    import { page } from "$app/stores";
    import AnimeInfoPage from "$components/pages/anime_info/index.svelte";
    import { anime_episodes } from "$data/mock/anime_episodes";
    import { anime_list } from "$data/mock/anime_list";
    import { OpengraphGenerator } from "$functions/opengraph";

    let anime_id = Number($page.params.id);

    let anime = anime_list?.find((anime) => anime.id === anime_id);

    const opengraph_html = new OpengraphGenerator({
        title: `Watch ${anime?.name} on AnimeCore`,
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
    <AnimeInfoPage
        anime_name={anime.name}
        anime_alternative_name={anime.alternative_name}
        anime_episodes_count={anime.episodes_count}
        anime_date={anime.updated}
        anime_synopsis={anime.synopsis}
        anime_banner={anime.banner}
        anime_cover={anime.cover}
        {anime_episodes}
    />
{/if}
