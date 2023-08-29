import { c as create_ssr_component, b as spread, d as escape_object, j as subscribe, v as validate_component, l as each, a as add_attribute, e as escape } from "../../../chunks/ssr.js";
import { O as OpengraphGenerator } from "../../../chunks/opengraph.js";
import { p as page } from "../../../chunks/stores.js";
import { S as Search } from "../../../chunks/search.js";
import { C as Chevron } from "../../../chunks/chevron.js";
import { I as Image_loader } from "../../../chunks/image_loader.js";
import { S as Scroll_area, C as Circle } from "../../../chunks/circle.js";
import { C as Cross } from "../../../chunks/cross.js";
import "dayjs";
import "dayjs/plugin/localeData.js";
import "dayjs/plugin/relativeTime.js";
import "dayjs/plugin/utc.js";
import "../../../chunks/ProgressBar.svelte_svelte_type_style_lang.js";
const More_box = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><rect width="8" height="8" rx="2" fill="currentColor"></rect><rect x="12" width="8" height="8" rx="2" fill="currentColor"></rect><rect x="12" y="12" width="8" height="8" rx="2" fill="currentColor"></rect><rect y="12" width="8" height="8" rx="2" fill="currentColor"></rect></svg>`;
});
const trending_animes = [
  {
    id: 1,
    name: "One piece",
    cover: "/images/cover/one_piece.webp",
    synopsis: `Azur Lane, a combination of all the different Camps in the world, was once successful in repelling the underwater menace, the Siren. Now splintered, they must face a new threat in Red Axis, former allies who crave to wield this otherworldly Siren technology for their own nefarious desires! Who will be victorious in the never-ending war between these battleship girls!? Akagami no Shirayuki-hime depicts Shirayuki's journey toward a new life at the royal palace of Clarines, as well as Zen's endeavor to become a prince worthy of his title. As loyal friendships are forged and deadly enemies formed, Shirayuki and Zen slowly learn to support each other as they walk their own paths.`,
    current_episode: 4,
    episodes_count: 1071,
    genres: ["Action", "Ecchi", "sci-Fi"],
    type: "TV",
    release_date: "2023-04-22T10:30:00.000Z",
    studios: ["Bibury Animation Studios"]
  },
  {
    id: 2,
    name: "Horimiya: The Missing Piece",
    cover: "/images/cover/horimiya.jpg",
    synopsis: `Brutal murders, petty thefts, and senseless violence pollute the human world. In contrast, the realm of death gods is a humdrum, unchanging gambling den. The ingenious 17-year-old Japanese student Light Yagami and sadistic god of death Ryuk share one belief: their worlds are rotten.`,
    current_episode: 8,
    episodes_count: 28,
    genres: ["Action", "Drama", "Triller"],
    type: "TV",
    release_date: "2018-10-22T10:30:00.000Z",
    studios: ["Animation XXX"]
  },
  {
    id: 3,
    name: "Rurouni Kenshin: Meji na tokito",
    cover: "/images/cover/rurouni.webp",
    synopsis: `Kintarou Ooe is a specialist in part-time work, riding all over the highways and byways of Japan on his trusty steed, the Mikazuki 5, and finding employment wherever he can. His adventures bring him knowledge and experience that can't be taught in a classroom, from political corruption to the delicacy of a young woman's heart. With nothing but the open road before him—not to mention the many beautiful women along the way—Kintarou `,
    current_episode: 1,
    episodes_count: 6,
    genres: ["Action", "Ecchi", "sci-Fi"],
    type: "TV",
    release_date: "2020-12-22T10:30:00.000Z",
    studios: ["WI Studios"]
  },
  {
    id: 4,
    name: "7SEEDS",
    cover: "/images/7Seeds.avif",
    synopsis: `Imagine this: you are living a normal day in your life. Maybe you are out with friends, eating your family's home-cooked meal or spending time with your girlfriend. When you next wake up, you are suddenly thrust into a strange, new world, surrounded by five strangers on a rapidly sinking boat in the middle of a storm.`,
    current_episode: 5,
    episodes_count: 12,
    genres: ["Action", "Horror", "sci-Fi"],
    type: "TV",
    release_date: "2010-01-22T10:30:00.000Z",
    studios: ["Bibury Animation Studios"]
  },
  {
    id: 5,
    name: "Demon Slayer: Kimetsu yo yaiba",
    cover: "/images/cover/ds.jpeg",
    genre: "Shounen",
    year: 2023,
    synopsis: `The world has become a slaughtering ground for the Crimson Denizens, mysterious beings from a parallel universe who thrive on the life energy of humans. These merciless murderers only leave behind scant remainders of souls called "Torches," which are mere residues that will eventually be destroyed, along with the very fact of the victims' existence from the minds of the living. In an ambitious endeavor to put an end to this invisible, hungry massacre, warriors called Flame Hazes relentlessly fight these monsters.`,
    current_episode: 19,
    episodes_count: 24,
    genres: ["Action", "Ecchi", "sci-Fi"],
    type: "TV",
    release_date: "2016-06-22T10:30:00.000Z",
    studios: ["Kyoto Studios"]
  },
  {
    id: 6,
    name: "Shakugan no Shana",
    cover: "/images/ShakuganNoShana.avif",
    synopsis: `The world has become a slaughtering ground for the Crimson Denizens, mysterious beings from a parallel universe who thrive on the life energy of humans. These merciless murderers only leave behind scant remainders of souls called "Torches," which are mere residues that will eventually be destroyed, along with the very fact of the victims' existence from the minds of the living. In an ambitious endeavor to put an end to this invisible, hungry massacre, warriors called Flame Hazes relentlessly fight these monsters.`,
    current_episode: 19,
    episodes_count: 24,
    genres: ["Action", "Ecchi", "sci-Fi"],
    type: "TV",
    release_date: "2016-06-22T10:30:00.000Z",
    studios: ["Kyoto Studios"]
  },
  {
    id: 7,
    name: "Jujutsu Kaisen 2nd season",
    cover: "/images/cover/jjk.webp",
    synopsis: `Although her name means "snow white," Shirayuki is a cheerful, red-haired girl living in the country of Tanbarun who works diligently as an apothecary at her herbal shop. Her life changes drastically when she is noticed by the silly prince of Tanbarun, Prince Raji, who then tries to force her to become his concubine.`,
    current_episode: 11,
    episodes_count: 12,
    genres: ["Love", "Drama", "Action"],
    type: "TV",
    release_date: "2013-08-22T10:30:00.000Z",
    studios: ["Kyoto Animations"]
  },
  {
    id: 8,
    name: "To LOVE-Ru",
    cover: "/images/ToLOVERu.avif",
    synopsis: `Rito Yuuki never gets a break—he's always finding himself in lewd accidents with girls around him. Although his heart still yearns for Haruna, his childhood love, Rito can't help but question his feelings for Lala, the alien princess who appeared in front of him and declared she would marry him. But now, it's not just Lala he has to deal with: her younger twin sisters, Momo and Nana, have also traveled to Earth, wanting to meet their older sister's fiancé, and just as luck would have it, they end up staying at Rito's home.`,
    current_episode: 9,
    episodes_count: 26,
    genres: ["Romantic", "Ecchi", "School"],
    type: "TV",
    release_date: "2021-7-22T10:30:00.000Z",
    studios: ["Bibury Animation Studios"]
  },
  {
    id: 9,
    name: "The girl I like to forgot her name",
    cover: "/images/cover/fish.png",
    genre: "Shounen",
    year: 2023,
    synopsis: `Brutal murders, petty thefts, and senseless violence pollute the human world. In contrast, the realm of death gods is a humdrum, unchanging gambling den. The ingenious 17-year-old Japanese student Light Yagami and sadistic god of death Ryuk share one belief: their worlds are rotten.`,
    current_episode: 8,
    episodes_count: 28,
    genres: ["Action", "Drama", "Triller"],
    type: "TV",
    release_date: "2018-10-22T10:30:00.000Z",
    studios: ["Animation XXX"]
  }
];
const Expand = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 24 24" }
    ],
    {}
  )}><path fill="currentColor" d="m18 9l-6-6l-6 6h12Zm0 6l-6 6l-6-6h12Z"></path></svg>`;
});
const Six_grids = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 16 16" }
    ],
    {}
  )}><path fill="currentColor" d="M1 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2zM1 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V7zM1 12a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-2z"></path></svg>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  let result_animes_element;
  let filter_options_mapping = {
    time_range: {
      title: "Time Range",
      class: "hidden flex-col md:gap-[0.35vw]",
      value: "",
      selected_items: []
    },
    genres: {
      title: "Genres",
      class: "md:flex flex-col md:gap-[0.35vw]",
      value: "",
      items: {
        action: "Action",
        adventure: "Adventure",
        hentai: "Hentai",
        romance: "Romance"
      },
      selected_items: []
    },
    year: {
      title: "Year",
      class: "md:flex flex-col md:gap-[0.35vw]",
      value: "",
      items: {
        2023: "2023",
        2022: "2022",
        2021: "2021",
        2020: "2020"
      },
      selected_items: []
    },
    season: {
      title: "Season",
      class: "md:flex flex-col md:gap-[0.35vw]",
      value: "",
      items: {
        winter: "Winter",
        spring: "Spring",
        summer: "Summer",
        fall: "Fall"
      },
      selected_items: []
    },
    format: {
      title: "Format",
      class: "hidden md:flex flex-col md:gap-[0.35vw]",
      value: "",
      items: { tv_show: "TV Show", movie: "Movie" },
      selected_items: []
    },
    airing_status: {
      title: "Airing Status",
      class: "hidden flex-col md:gap-[0.35vw]",
      value: "",
      selected_items: []
    },
    sort_by: {
      title: "Sort by",
      class: "hidden flex-col md:gap-[0.35vw]",
      value: "",
      selected_items: []
    }
  };
  const opengraph_html = new OpengraphGenerator({
    title: "Explore the Anime Universe: Your Gateway to Otaku Delights!",
    site_name: "CoreProject",
    image_url: "",
    // Use Opengraph later
    url: $page.url.href,
    locale: "en_US",
    description: "The most modern anime streaming site"
  }).generate_opengraph();
  $$unsubscribe_page();
  return `${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} <section class="mt-20 flex flex-col p-5 md:mt-0 md:gap-[1.5vw] md:pb-[2.5vw] md:pl-[1.5vw] md:pr-[3.75vw] md:pt-0"><section-headings class="flex flex-col gap-2 md:gap-[0.5vw]" data-svelte-h="svelte-1aoywkr"><span class="text-2xl font-bold leading-none md:text-[2vw]">Anime <span class="text-warning-400">Explore</span></span> <span class="text-base font-normal leading-none text-surface-50 md:text-[1.1vw]">Unleash your inner Otaku: Explore anime wonders</span></section-headings> <search class="mt-10 flex flex-col gap-1 md:hidden"><span class="text-base font-semibold leading-none text-surface-50" data-svelte-h="svelte-3nqshk">Search Animes</span> <div class="relative flex items-center">${validate_component(Search, "Search").$$render(
    $$result,
    {
      class: "pointer-events-none absolute ml-4 w-4 text-surface-300"
    },
    {},
    {}
  )} <input type="text" placeholder="Looking for specific anime? Start from here..." class="w-full rounded-lg border-none bg-surface-400 py-3 pl-12 leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:bg-surface-400/75"></div></search> <filter-options class="mt-3 flex items-end justify-between gap-3 md:mt-0 md:gap-0"><div class="flex items-center gap-3 md:gap-[1.5vw]"><search class="hidden flex-col gap-[0.35vw] md:flex"><span class="text-[1vw] font-semibold leading-none text-surface-50" data-svelte-h="svelte-i83h8b">Search Animes</span> <div class="relative flex items-center">${validate_component(Search, "Search").$$render(
    $$result,
    {
      class: "pointer-events-none absolute ml-[1vw] w-[1vw] text-surface-300"
    },
    {},
    {}
  )} <input type="text" placeholder="Looking for specific anime? Start from here..." class="w-[30vw] rounded-[0.5vw] border-none bg-surface-400 py-[0.8vw] pl-[3vw] text-[1vw] leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:bg-surface-400/75"></div></search> ${each(Object.entries(filter_options_mapping), (option) => {
    let title = option[1].title, klass = option[1].class, selected_items = option[1].selected_items;
    option[1].items;
    return `    <div class="${escape(klass, true) + " group"}"><span class="font-semibold leading-none text-surface-50 md:text-[1vw]">${escape(title)}</span> <div class="relative flex items-center"><span class="absolute cursor-pointer text-surface-50 opacity-100 duration-300 group-focus-within:opacity-0">${selected_items.length > 0 ? `<span class="ml-3 rounded bg-primary-500 p-1 text-sm font-semibold md:ml-[0.75vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]"> ${escape(selected_items[0][1])}</span>  ${selected_items.length > 1 ? `<span class="ml-1 rounded bg-primary-500/50 p-1 text-sm font-semibold md:ml-[0.15vw] md:rounded-[0.25vw] md:p-[0.35vw] md:text-[0.85vw]">+${escape(selected_items.filter((item) => item !== selected_items[0]).length)} </span>` : ``}` : `<span class="ml-3 text-base md:ml-[1vw] md:text-[0.9vw]" data-svelte-h="svelte-qb61bp">Any</span>`}</span> <input type="text" class="peer w-full rounded-lg border-none bg-surface-400 py-3 text-base leading-none text-surface-50 placeholder:text-surface-50 focus:ring-0 md:w-[11vw] md:rounded-[0.5vw] md:bg-surface-400/75 md:py-[0.8vw] md:pl-[1vw] md:text-[1vw]"${add_attribute("value", option[1].value, 0)}> ${selected_items.length > 0 ? `<button class="btn absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]">${validate_component(Cross, "Cross").$$render($$result, { class: "text-surface-300" }, {}, {})} </button>` : `<button class="btn absolute right-0 mr-3 w-4 p-0 md:mr-[1vw] md:w-[1vw]">${validate_component(Chevron, "Chevron").$$render($$result, { class: "text-surface-300" }, {}, {})} </button>`}</div> </div>`;
  })}</div> <more-filter-option><button class="btn rounded-lg bg-surface-400 p-[0.85rem] md:rounded-[0.5vw] md:bg-surface-400/75 md:p-[0.9vw]">${validate_component(More_box, "MoreBox").$$render($$result, { class: "w-4 text-surface-50 md:w-[1vw]" }, {}, {})}</button></more-filter-option></filter-options> <div class="mt-16 md:mt-[1.5vw]"><div class="flex items-center justify-between"><headings class="flex flex-col gap-2 md:gap-[0.35vw]" data-svelte-h="svelte-14481af"><span class="text-xl font-semibold leading-none md:text-[1.35vw]">Trending Now</span> <span class="text-base leading-none text-surface-50 md:text-[1vw]">Crowd Favorites: Anime Hits and Hype</span></headings> <div class="flex gap-3 md:gap-[1vw]"><button class="btn p-0 text-surface-50">${validate_component(Expand, "Expand").$$render($$result, { class: "w-5 md:w-[1.25vw]" }, {}, {})} <span class="font-semibold md:text-[1vw]" data-svelte-h="svelte-1o3ct5c">Trending</span></button> <span class="divider-vertical h-7 !border-surface-50/25 md:h-[2vw]"></span> <button class="btn p-0 text-surface-50">${validate_component(Six_grids, "SixGrids").$$render($$result, { class: "w-5 md:w-[1.15vw]" }, {}, {})}</button> <button class="btn p-0 text-surface-50">${validate_component(More_box, "MoreBox").$$render($$result, { class: "w-[1.1rem] md:w-[1vw]" }, {}, {})}</button></div></div> ${`${`<result-animes class="mt-5 grid grid-cols-3 gap-3 md:mt-[1.25vw] md:grid-cols-6 md:gap-[1.5vw]"${add_attribute("this", result_animes_element, 0)}>${each(trending_animes, (anime) => {
    return `<a href="${"/mal/" + escape(anime.id, true)}" class="relative col-span-1 flex flex-col gap-2 md:gap-[0.5vw]"><div class="relative">${validate_component(Image_loader, "ImageLoader").$$render(
      $$result,
      {
        src: anime.cover,
        alt: anime.name,
        class: "h-60 w-full rounded-md object-cover object-center md:h-[20vw] md:rounded-[0.35vw]"
      },
      {},
      {}
    )} <anime-info class="absolute inset-x-0 bottom-0 rounded-b-lg backdrop-blur md:rounded-b-[0.5vw]"><div class="flex flex-col gap-1 bg-surface-900/90 p-3 md:gap-[0.35vw] md:p-[1vw]">${validate_component(Scroll_area, "ScrollArea").$$render(
      $$result,
      {
        class: "flex overflow-hidden text-sm font-semibold duration-300 ease-in-out scrollbar-none hover:max-h-[10vw] hover:overflow-y-scroll md:max-h-[1.35vw] md:text-[1vw] md:leading-[1.35vw]"
      },
      {},
      {
        default: () => {
          return `<span class="line-clamp-1 md:line-clamp-none">${escape(anime.name)}</span> `;
        }
      }
    )} <anime_info class="flex items-center gap-2 text-xs leading-none text-surface-50 md:gap-[0.5vw] md:text-[0.8vw]"><genre>${escape(anime.genres[0])}</genre> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-75 md:w-[0.25vw]" }, {}, {})} <episodes_count>${escape(anime.episodes_count)} eps</episodes_count> </anime_info></div> </anime-info></div> </a>`;
  })}</result-animes>`}`}</div></section>`;
});
export {
  Page as default
};
