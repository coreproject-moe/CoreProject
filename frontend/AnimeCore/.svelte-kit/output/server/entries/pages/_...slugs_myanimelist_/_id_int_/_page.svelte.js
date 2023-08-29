import { c as create_ssr_component, b as spread, d as escape_object, j as subscribe, v as validate_component } from "../../../../chunks/ssr.js";
import { p as page } from "../../../../chunks/stores.js";
import { a as anime_list, b as anime_episodes, A as Anime_info, E as Error } from "../../../../chunks/anime_list.js";
import { O as OpengraphGenerator } from "../../../../chunks/opengraph.js";
import { d as derived } from "../../../../chunks/index.js";
const Top_rounded = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 24 24" },
      { fill: "currentColor" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path fill-rule="evenodd" clip-rule="evenodd" d="M24 0H0V24C0 10.7451 10.7461 0 24 0Z" fill="currentColor"></path></svg>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  let $anime_id, $$unsubscribe_anime_id;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  let anime_id = derived(page, (page2) => page2.params.id);
  $$unsubscribe_anime_id = subscribe(anime_id, (value) => $anime_id = value);
  let anime = anime_list?.find((anime2) => anime2.id === Number($anime_id));
  const opengraph_html = new OpengraphGenerator({
    title: anime ? `Watch ${anime?.name} on AnimeCore` : "404 - Page not found!",
    url: $page.url.href,
    description: anime?.synopsis ?? "",
    site_name: "CoreProject",
    locale: "en_US",
    image_url: anime?.banner ?? ""
  }).generate_opengraph();
  $$unsubscribe_page();
  $$unsubscribe_anime_id();
  return `${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} ${anime ? ` ${validate_component(Top_rounded, "TopRounded").$$render(
    $$result,
    {
      class: "fixed z-10 hidden w-[1.5vw] text-surface-900 md:flex"
    },
    {},
    {}
  )} ${validate_component(Anime_info, "AnimeInfoPage").$$render(
    $$result,
    {
      anime_id: anime.id,
      anime_name: anime.name,
      japanese_name: anime.japanese_name,
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
