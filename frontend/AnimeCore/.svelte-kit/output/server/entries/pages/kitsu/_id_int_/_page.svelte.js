import { c as create_ssr_component, j as subscribe, v as validate_component } from "../../../../chunks/ssr.js";
import { p as page } from "../../../../chunks/stores.js";
import { a as anime_list, b as anime_episodes, A as Anime_info, E as Error } from "../../../../chunks/anime_list.js";
import { O as OpengraphGenerator } from "../../../../chunks/opengraph.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  let anime_id = Number($page.params.id);
  let anime = anime_list?.find((anime2) => anime2.id === anime_id);
  const opengraph_html = new OpengraphGenerator({
    title: `Watch ${anime?.name} on AnimeCore`,
    url: $page.url.href,
    description: anime?.synopsis ?? "",
    site_name: "CoreProject",
    locale: "en_US",
    image_url: anime?.banner ?? ""
  }).generate_opengraph();
  $$unsubscribe_page();
  return `${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} ${anime ? `${validate_component(Anime_info, "AnimeInfoPage").$$render(
    $$result,
    {
      anime_name: anime.name,
      anime_alternative_name: anime.alternative_name,
      anime_episodes_count: anime.episodes_count,
      anime_date: anime.updated,
      anime_synopsis: anime.synopsis,
      anime_banner: anime.banner,
      anime_cover: anime.cover,
      anime_episodes
    },
    {},
    {}
  )}` : `${validate_component(Error, "AnimeInfoErrorPage").$$render($$result, {}, {}, {})}`}`;
});
export {
  Page as default
};
