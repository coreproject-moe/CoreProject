import { c as create_ssr_component, k as createEventDispatcher, e as escape, l as each, b as spread, d as escape_object, a as add_attribute, i as escape_attribute_value, v as validate_component, m as missing_component } from "./ssr.js";
import "lodash/sample.js";
import { F as Filter, T as Text_editor, W as Warning, C as Comment, e as episode_comments, b as Forum_posts, f as forum_posts, D as Download, S as Share } from "./comment.js";
import { I as Image_loader } from "./image_loader.js";
import { S as Scroll_area, C as Circle } from "./circle.js";
import { F as FormatDate, P as Play_circle } from "./play_circle.js";
import dayjs from "dayjs";
import duration from "dayjs/plugin/duration.js";
import utc from "dayjs/plugin/utc.js";
import { C as Chevron } from "./chevron.js";
import { C as Cross } from "./cross.js";
import { S as Settings_outline, E as Edit } from "./edit.js";
import { S as Search } from "./search.js";
import "./ProgressBar.svelte_svelte_type_style_lang.js";
const cBase = "w-full flex";
function isFull(value2, index) {
  return Math.floor(value2) >= index + 1;
}
function isHalf(value2, index) {
  return value2 === index + 0.5;
}
const Ratings = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let classesBase;
  let { value = 0 } = $$props;
  let { max = 5 } = $$props;
  let { interactive = false } = $$props;
  let { text = "text-token" } = $$props;
  let { fill = "fill-token" } = $$props;
  let { justify = "justify-center" } = $$props;
  let { spacing = "space-x-2" } = $$props;
  let { regionIcon = "" } = $$props;
  createEventDispatcher();
  if ($$props.value === void 0 && $$bindings.value && value !== void 0)
    $$bindings.value(value);
  if ($$props.max === void 0 && $$bindings.max && max !== void 0)
    $$bindings.max(max);
  if ($$props.interactive === void 0 && $$bindings.interactive && interactive !== void 0)
    $$bindings.interactive(interactive);
  if ($$props.text === void 0 && $$bindings.text && text !== void 0)
    $$bindings.text(text);
  if ($$props.fill === void 0 && $$bindings.fill && fill !== void 0)
    $$bindings.fill(fill);
  if ($$props.justify === void 0 && $$bindings.justify && justify !== void 0)
    $$bindings.justify(justify);
  if ($$props.spacing === void 0 && $$bindings.spacing && spacing !== void 0)
    $$bindings.spacing(spacing);
  if ($$props.regionIcon === void 0 && $$bindings.regionIcon && regionIcon !== void 0)
    $$bindings.regionIcon(regionIcon);
  classesBase = `${cBase} ${text} ${fill} ${justify} ${spacing} ${$$props.class ?? ""}`;
  return `<div class="${"ratings " + escape(classesBase, true)}" data-testid="rating-bar"> ${each({ length: max }, (_, i) => {
    return `${interactive ? `<button class="${"rating-icon " + escape(regionIcon, true)}" type="button">${isFull(value, i) ? `${slots.full ? slots.full({}) : ``}` : `${isHalf(value, i) ? `${slots.half ? slots.half({}) : ``}` : `${slots.empty ? slots.empty({}) : ``}`}`} </button>` : `<span class="${"rating-icon " + escape(regionIcon, true)}">${isFull(value, i) ? `${slots.full ? slots.full({}) : ``}` : `${isHalf(value, i) ? `${slots.half ? slots.half({}) : ``}` : `${slots.empty ? slots.empty({}) : ``}`}`} </span>`}`;
  })}</div>`;
});
const round_to_nearest_zero_point_five = (rating) => {
  return Number((Math.round(rating * 2) / 2).toFixed(1));
};
const Star = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const { variant, fill_color, ...props } = $$props;
  return `${variant === "empty" ? `<svg${spread(
    [
      { width: "30" },
      { height: "30" },
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object(props)
    ],
    {}
  )}><path d="M15 2.5L18.8625 10.325L27.5 11.5875L21.25 17.675L22.725 26.275L15 22.2125L7.275 26.275L8.75 17.675L2.5 11.5875L11.1375 10.325L15 2.5Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>` : `${variant === "half" ? `<svg${spread(
    [
      { width: "30" },
      { height: "30" },
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object(props)
    ],
    {}
  )}><defs><linearGradient id="grad"><stop offset="50%"${add_attribute("stop-color", fill_color, 0)}></stop><stop offset="50%" stop-color="transparent"></stop></linearGradient></defs><path fill="url(#grad)" d="M15 2.5L18.8625 10.325L27.5 11.5875L21.25 17.675L22.725 26.275L15 22.2125L7.275 26.275L8.75 17.675L2.5 11.5875L11.1375 10.325L15 2.5Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>` : `${variant === "full" ? `<svg${spread(
    [
      { width: "30" },
      { height: "30" },
      { viewBox: "0 0 30 30" },
      { fill: escape_attribute_value(fill_color) },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object(props)
    ],
    {}
  )}><path d="M15 2.5L18.8625 10.325L27.5 11.5875L21.25 17.675L22.725 26.275L15 22.2125L7.275 26.275L8.75 17.675L2.5 11.5875L11.1375 10.325L15 2.5Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>` : ``}`}`}`;
});
const Error = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let mapping;
  return `${$$result.head += `<!-- HEAD_svelte-16z1l2s_START --><link${add_attribute("href", mapping?.image.src, 0)} rel="preload" as="image"><style data-svelte-h="svelte-tu1ggt">#page {
            overflow: hidden;
        }</style><!-- HEAD_svelte-16z1l2s_END -->`, ""} ${``}`;
});
class FormatTime {
  #duration;
  constructor(time) {
    dayjs.extend(utc);
    dayjs.extend(duration);
    this.#duration = dayjs.duration(time, "seconds");
  }
  get format_seconds_to_time_stamp_duration() {
    const timeString = dayjs.utc(this.#duration.asMilliseconds()).format("mm:ss");
    return timeString;
  }
  get format_seconds_to_minutes() {
    const timeString = dayjs.utc(this.#duration.asMilliseconds()).format("m");
    return timeString;
  }
}
const External_link = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M22.5 16.25V23.75C22.5 24.413 22.2366 25.0489 21.7678 25.5178C21.2989 25.9866 20.663 26.25 20 26.25H6.25C5.58696 26.25 4.95107 25.9866 4.48223 25.5178C4.01339 25.0489 3.75 24.413 3.75 23.75V10C3.75 9.33696 4.01339 8.70107 4.48223 8.23223C4.95107 7.76339 5.58696 7.5 6.25 7.5H13.75" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18.75 3.75H26.25V11.25" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12.5 17.5L26.25 3.75" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Listen = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M3.75 22.5V15C3.75 12.0163 4.93526 9.15483 7.04505 7.04505C9.15483 4.93526 12.0163 3.75 15 3.75C17.9837 3.75 20.8452 4.93526 22.955 7.04505C25.0647 9.15483 26.25 12.0163 26.25 15V22.5" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M26.25 23.75C26.25 24.413 25.9866 25.0489 25.5178 25.5178C25.0489 25.9866 24.413 26.25 23.75 26.25H22.5C21.837 26.25 21.2011 25.9866 20.7322 25.5178C20.2634 25.0489 20 24.413 20 23.75V20C20 19.337 20.2634 18.7011 20.7322 18.2322C21.2011 17.7634 21.837 17.5 22.5 17.5H26.25V23.75ZM3.75 23.75C3.75 24.413 4.01339 25.0489 4.48223 25.5178C4.95107 25.9866 5.58696 26.25 6.25 26.25H7.5C8.16304 26.25 8.79893 25.9866 9.26777 25.5178C9.73661 25.0489 10 24.413 10 23.75V20C10 19.337 9.73661 18.7011 9.26777 18.2322C8.79893 17.7634 8.16304 17.5 7.5 17.5H3.75V23.75Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Read = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M2.5 3.75H10C11.3261 3.75 12.5979 4.27678 13.5355 5.21447C14.4732 6.15215 15 7.42392 15 8.75V26.25C15 25.2554 14.6049 24.3016 13.9017 23.5983C13.1984 22.8951 12.2446 22.5 11.25 22.5H2.5V3.75Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M27.5 3.75H20C18.6739 3.75 17.4021 4.27678 16.4645 5.21447C15.5268 6.15215 15 7.42392 15 8.75V26.25C15 25.2554 15.3951 24.3016 16.0983 23.5983C16.8016 22.8951 17.7554 22.5 18.75 22.5H27.5V3.75Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Trending_up = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { viewBox: "0 0 20 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props)
    ],
    {}
  )}><g filter="url(#filter0_d_1911_2848)"><path d="M15.5 3L10.75 7.75L8.25 5.25L4.5 9" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12.5 3H15.5V6" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><filter id="filter0_d_1911_2848" x="0" y="0" width="20" height="20" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></feColorMatrix><feOffset dy="4"></feOffset><feGaussianBlur stdDeviation="2"></feGaussianBlur><feComposite in2="hardAlpha" operator="out"></feComposite><feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"></feColorMatrix><feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_1911_2848"></feBlend><feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_1911_2848" result="shape"></feBlend></filter></defs></svg>`;
});
const Video = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { viewBox: "0 0 18 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props)
    ],
    {}
  )}><g clip-path="url(#clip0_1917_2470)"><path d="M17.25 5.25L12 9L17.25 12.75V5.25Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10.5 3.75H2.25C1.42157 3.75 0.75 4.42157 0.75 5.25V12.75C0.75 13.5784 1.42157 14.25 2.25 14.25H10.5C11.3284 14.25 12 13.5784 12 12.75V5.25C12 4.42157 11.3284 3.75 10.5 3.75Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clipPath id="clip0_1917_2470"><rect width="18" height="18" fill="white"></rect></clipPath></defs></svg>`;
});
const index_svelte_svelte_type_style_lang = "";
const css = {
  code: "episode-japanese-name.svelte-keg09q:not(:hover),episode-name.svelte-keg09q:not(:hover){-webkit-mask-image:linear-gradient(90deg, rgba(7, 5, 25, 0.95) 90%, rgba(0, 0, 0, 0) 100%);mask-image:linear-gradient(90deg, rgba(7, 5, 25, 0.95) 90%, rgba(0, 0, 0, 0) 100%);-webkit-mask-position:right;mask-position:right}",
  map: null
};
const Anime_info = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { anime_id } = $$props;
  let { anime_name } = $$props;
  let { japanese_name } = $$props;
  let { anime_episodes_count } = $$props;
  let { anime_date } = $$props;
  let { anime_synopsis } = $$props;
  let { anime_banner } = $$props;
  let { anime_cover } = $$props;
  let { anime_episodes: anime_episodes2 } = $$props;
  const anime_details = {
    format: "TV",
    episodes: "22",
    "episode Duration": "26 Minutes",
    status: "finished",
    "start date": new FormatDate("2012-04-23").format_to_human_readable_form,
    "end date": new FormatDate("2012-09-16").format_to_human_readable_form,
    season: new FormatDate("2012-4").format_to_season,
    studios: "Kyoto Animation",
    producers: ["Lantis", "Kadokawa Shoten", "Klock Worx", "chara-ani.com", "Animation Do"],
    source: "Night Novel"
  };
  const icon_mapping = {
    anime_options: {
      read: {
        icon: {
          component: Read,
          class: "w-4 md:w-[1.5vw] text-surface-500"
        }
      },
      listen: {
        icon: {
          component: Listen,
          class: "w-4 md:w-[1.5vw] text-surface-500"
        }
      }
    },
    user_options_icons: {
      video: {
        icon: {
          component: Video,
          variant: false,
          class: "w-4 md:w-[1.125vw]"
        }
      },
      edit: {
        icon: {
          component: Edit,
          variant: "with_underline_around_pencil",
          class: "w-4 md:w-[1.125vw]"
        }
      },
      download: {
        icon: {
          component: Download,
          class: "w-4 md:w-[1.125vw]"
        }
      },
      share: {
        icon: {
          component: Share,
          class: "w-4 md:w-[1.125vw]"
        }
      }
    }
  };
  if ($$props.anime_id === void 0 && $$bindings.anime_id && anime_id !== void 0)
    $$bindings.anime_id(anime_id);
  if ($$props.anime_name === void 0 && $$bindings.anime_name && anime_name !== void 0)
    $$bindings.anime_name(anime_name);
  if ($$props.japanese_name === void 0 && $$bindings.japanese_name && japanese_name !== void 0)
    $$bindings.japanese_name(japanese_name);
  if ($$props.anime_episodes_count === void 0 && $$bindings.anime_episodes_count && anime_episodes_count !== void 0)
    $$bindings.anime_episodes_count(anime_episodes_count);
  if ($$props.anime_date === void 0 && $$bindings.anime_date && anime_date !== void 0)
    $$bindings.anime_date(anime_date);
  if ($$props.anime_synopsis === void 0 && $$bindings.anime_synopsis && anime_synopsis !== void 0)
    $$bindings.anime_synopsis(anime_synopsis);
  if ($$props.anime_banner === void 0 && $$bindings.anime_banner && anime_banner !== void 0)
    $$bindings.anime_banner(anime_banner);
  if ($$props.anime_cover === void 0 && $$bindings.anime_cover && anime_cover !== void 0)
    $$bindings.anime_cover(anime_cover);
  if ($$props.anime_episodes === void 0 && $$bindings.anime_episodes && anime_episodes2 !== void 0)
    $$bindings.anime_episodes(anime_episodes2);
  $$result.css.add(css);
  return `<anime-info-container class="relative mt-16 block h-screen bg-cover md:mt-0">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: anime_cover ?? "",
      class: "absolute hidden h-full w-full select-none rounded-tl-[1.5vw] object-cover object-center md:flex"
    },
    {},
    {}
  )} <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-t from-surface-900 to-surface-900/50"></gradient-overlay> <anime-info-section class="absolute inset-0 grid grid-cols-12 items-start p-5 pt-10 md:p-[5vw]"><anime-info-episodes class="col-span-12 md:col-span-10 md:pr-[4vw]"><anime-main-infos class="grid grid-cols-12 items-end justify-between"><anime-titles class="relative col-span-12 grid grid-cols-12 gap-5 md:col-span-7 md:flex md:w-full md:items-end md:gap-[2vw] md:pr-[2vw]"><anime-banner class="relative col-span-12 h-96 md:h-[18.25vw] md:w-[13vw] md:flex-shrink-0"><radial-gradient class="pointer-events-none absolute inset-0 z-10 h-[150%] w-[125%] -translate-x-8 -translate-y-28 md:hidden" style="background-image: radial-gradient(circle at center, rgba(255, 255, 255, 0.1) 0%, transparent 100%); mask-image: linear-gradient(to bottom, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);"></radial-gradient> ${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      class: "h-full w-full rounded-xl object-cover object-center md:rounded-[1vw]",
      src: anime_banner,
      alt: anime_name
    },
    {},
    {}
  )} <overlay-gradient class="gradient absolute inset-0 bg-gradient-to-t from-surface-900/75 to-surface-900/25 md:hidden"></overlay-gradient></anime-banner> <anime-details class="absolute bottom-0 col-span-12 p-5 md:static md:p-0">${validate_component(Scroll_area, "ScrollArea").$$render($$result, { class: "max-h-48 md:max-h-[10vw]" }, {}, {
    default: () => {
      return `<anime-name class="text-2xl font-bold md:text-[2vw] md:leading-[2.7vw]">${escape(anime_name)}</anime-name>`;
    }
  })} <anime-japanese-name class="flex flex-wrap gap-x-2 pt-2 text-xs font-semibold uppercase tracking-wider text-surface-50 md:gap-x-[0.25vw] md:pt-[0.625vw] md:text-[0.75vw] md:leading-[0.9vw]">${escape(japanese_name)}</anime-japanese-name> <anime-other-infos class="mt-1 flex flex-wrap items-center gap-2 text-xs font-semibold md:mt-[0.25vw] md:gap-[0.5vw] md:pt-[0.5vw] md:text-[0.75vw] md:leading-[0.75vw]"><span data-svelte-h="svelte-u9rmgs">TV</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.35rem] opacity-50" }, {}, {})} <span>${escape(anime_episodes_count)} eps</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.35rem] opacity-50" }, {}, {})} <span data-svelte-h="svelte-3p0uht">Completed</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.35rem] opacity-50" }, {}, {})} <span class="capitalize">${escape(new FormatDate(anime_date).format_to_season)}</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.35rem] opacity-50" }, {}, {})} <span class="uppercase tracking-wider" data-svelte-h="svelte-39rb5w">Kuschio animation</span></anime-other-infos> <watch-options class="mt-3 flex items-center gap-3 md:mt-[1.5vw] md:gap-[0.75vw]"><button type="button" class="btn h-14 w-[6.5rem] rounded-lg bg-primary-500 font-bold text-white md:h-[4.3vw] md:w-[7vw] md:rounded-[0.625vw]"><div class="flex gap-3 md:gap-[0.7vw]">${validate_component(Play_circle, "PlayCircle").$$render($$result, { class: "w-5 md:w-[1.5vw]" }, {}, {})} <div class="flex flex-col items-start gap-1" data-svelte-h="svelte-15n7j5p"><span class="text-sm leading-none md:text-[0.87vw]">Watch</span> <span class="text-xs font-bold leading-none text-surface-50 md:text-[0.625vw]">Ep 01</span></div></div></button> ${each(Object.entries(icon_mapping.anime_options), (item) => {
    let item_name = item[0], item_icon = item[1].icon, component = item_icon.component, component_class = item_icon.class;
    return `    <button type="button" class="btn h-14 w-14 rounded-lg bg-secondary-100 capitalize text-surface-500 md:h-[4.3vw] md:w-[4.3vw] md:rounded-[0.625vw] md:text-[0.87vw] md:font-semibold" disabled><div class="flex flex-col items-center gap-2 md:gap-[0.68vw]">${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: component_class }, {}, {})} <span class="leading-none">${escape(item_name)}</span></div> </button>`;
  })}</watch-options> <user-options class="mt-3 flex gap-2 md:mt-[0.75vw] md:gap-[0.75vw]">${each(Object.entries(icon_mapping.user_options_icons), (item) => {
    let item_label = item[0], item_icon = item[1].icon, component = item_icon.component, component_class = item_icon.class, component_variant = item_icon.variant;
    return `     <button type="button"${add_attribute("aria-label", item_label, 0)} class="btn btn-icon w-7 rounded bg-warning-400 p-0 text-surface-500 md:w-[1.875vw] md:rounded-[0.25vw]">${validate_component(component || missing_component, "svelte:component").$$render(
      $$result,
      {
        class: component_class,
        variant: component_variant
      },
      {},
      {}
    )} </button>`;
  })}</user-options></anime-details></anime-titles> <anime-synopsis class="col-span-12 mt-10 md:col-span-5 md:mt-0"><section-header class="flex gap-[0.75vw]"><header-title class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-7g8xhy">Synopsis</header-title> <button class="btn btn-icon hidden rounded-[0.1875vw] bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> ${validate_component(Scroll_area, "ScrollArea").$$render(
    $$result,
    {
      offsetScrollbar: true,
      gradientMask: true,
      parentClass: "max-h-40 mt-3 md:mt-[1.25vw] md:max-h-[10.25vw]",
      class: "text-justify text-xs md:text-[0.8vw] md:leading-[1vw] md:pb-[1.25vw]"
    },
    {},
    {
      default: () => {
        return `${escape(anime_synopsis)}`;
      }
    }
  )} <anime-genres class="hidden gap-[0.5vw] text-white md:mt-[1vw] md:flex md:text-[0.75vw] md:leading-[0.9vw]">${each(["Action", "Romance", "Horror"], (genre) => {
    return `<span class="bg-warning-400 text-black font-semibold md:px-[0.75vw] md:py-[0.4vw] rounded-[0.25vw]">${escape(genre)} </span>`;
  })}</anime-genres> <anime-scores class="hidden w-max gap-[0.75vw] rounded-[0.25vw] bg-surface-50/10 backdrop-blur-lg md:mt-[0.5vw] md:flex md:px-[0.75vw] md:py-[0.5vw] md:text-[0.75vw] md:leading-[0.75vw]"><score class="flex gap-[0.25vw]" data-svelte-h="svelte-1ujrkk"><span>Score:</span> <span class="font-semibold text-warning-400">79</span></score> <status class="flex gap-[0.25vw]"><span data-svelte-h="svelte-k2z92">Status:</span> <button class="btn p-0 leading-none md:text-[0.75vw]"><span class="font-semibold text-warning-400" data-svelte-h="svelte-1uekx12">Watching</span> ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[0.625vw] text-warning-400" }, {}, {})}</button></status> <episodes-count class="flex gap-[0.25vw]"><span data-svelte-h="svelte-74k8xv">Episode:</span> <span class="font-semibold text-warning-400">0/${escape(anime_episodes_count)}</span></episodes-count> <your-scrore class="flex gap-[0.25vw]"><span data-svelte-h="svelte-1j3pdr5">Your Score:</span> <button class="btn p-0 leading-none md:text-[0.75vw]"><span class="font-semibold text-warning-400" data-svelte-h="svelte-rfzzy2">Not Rated</span> ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[0.625vw] text-warning-400" }, {}, {})}</button></your-scrore></anime-scores></anime-synopsis></anime-main-infos> <anime-episodes-container class="my-7 block md:my-[6vw]"><section-header class="flex border-b-2 border-surface-50/10 pb-1 md:gap-x-[0.75vw] md:border-none md:pb-0"><header-title class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-11ldjpy">Episodes</header-title> <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <episodes-options class="mt-2 flex flex-col justify-between gap-y-5 md:mt-0 md:flex-row md:gap-y-0"><episodes-available-in class="hidden items-end gap-2 md:flex md:gap-[1.25vw]"><p class="flex items-center gap-1 md:gap-[0.75vw]"><span class="text-base font-bold leading-none md:text-[2vw] md:leading-[1.9vw]" data-svelte-h="svelte-lwtsmo">23</span> <span class="text-xs font-semibold md:text-[1vw]" data-svelte-h="svelte-r9gwh4">episodes</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.4vw] opacity-50" }, {}, {})}</p> <available-formats><div class="flex w-full items-center gap-2 leading-4 md:gap-[1vw] md:leading-[1.5vw]" data-svelte-h="svelte-13lvnsu"><span class="flex-shrink-0 text-[0.5rem] font-medium md:text-[0.75vw]">Available in</span> <div class="h-[0.1rem] w-full bg-surface-50/25 md:h-[0.08vw] md:bg-surface-300"></div></div> <formats class="flex h-5 gap-2 text-[0.5rem] font-bold md:h-[1.8vw] md:gap-[0.75vw] md:text-[0.75vw]">${each(["sub", "dub"], (item) => {
    return `<span class="flex h-full place-items-center rounded bg-surface-400 px-2 uppercase leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">${escape(item)} </span>`;
  })} ${validate_component(Circle, "Circle").$$render($$result, { class: "w-[0.4vw] opacity-50" }, {}, {})} ${each(["1080p", "720p", "480p"], (resolution) => {
    return `<span class="flex h-full place-items-center rounded bg-surface-400 px-2 leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">${escape(resolution)} </span>`;
  })}</formats></available-formats></episodes-available-in> <episodes-filtering class="flex items-center justify-between gap-2 md:items-end md:gap-[0.75vw]"><p class="flex items-center gap-1 md:hidden" data-svelte-h="svelte-hoi2bp"><span class="text-base font-bold leading-none">23</span> <span class="text-sm font-semibold text-surface-50">episodes</span></p> <by-formats class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]"><span class="text-[0.65rem] leading-[0.9vw] text-surface-50 transition-colors duration-300 group-hover:text-white md:text-[0.75vw]" data-svelte-h="svelte-4kg831">Type</span> <button class="btn h-7 rounded bg-surface-400 px-3 text-[0.65rem] font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw] md:leading-[0.9vw]"><span data-svelte-h="svelte-1sii61j">Subbed</span> ${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></by-formats> <by-modes class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]"><span class="text-[0.65rem] leading-[0.9vw] text-surface-50 transition-colors duration-300 group-hover:text-white md:text-[0.75vw]" data-svelte-h="svelte-16htgo0">Display Mode</span> <button class="btn h-7 rounded bg-surface-400 px-3 text-[0.65rem] font-semibold leading-[0.9vw] md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw]"><span data-svelte-h="svelte-1w3m1b">Thumbnails</span> ${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></by-modes> <button class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Search">${validate_component(Search, "Search").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></episodes-filtering></episodes-options> <anime-episodes-cards class="mt-4 grid grid-cols-12 gap-5 md:mt-[2.5vw] md:gap-[2.5vw]">${each(anime_episodes2, (episode) => {
    let thumbnail = episode.thumbnail, title = episode.title, episode_number = episode.number, japanese_name2 = episode.japanese_title, duration2 = episode.duration;
    return `     <a href="${"./" + escape(anime_id, true) + "/episode/" + escape(episode_number, true)}" class="relative col-span-12 grid grid-cols-12 gap-4 md:col-span-4"><card-banner-info class="relative col-span-5 h-full w-full md:col-span-12 md:h-[19vw]"><card-banner class="block h-24 md:h-[12vw] md:w-full">${validate_component(Image_loader, "ImageLoader").$$render(
      $$result,
      {
        src: thumbnail ?? "",
        class: "h-full w-full shrink-0 rounded-lg bg-cover bg-center md:rounded-t-[0.625vw]"
      },
      {},
      {}
    )}</card-banner> <overlay-effect class="absolute inset-0 hidden bg-gradient-to-t from-surface-900/75 to-transparent md:flex md:h-[12vw]"></overlay-effect> <card-info class="absolute bottom-0 flex h-max w-full justify-between p-1 md:top-0 md:p-[0.5vw]"><p class="rounded bg-surface-900/75 p-1 text-xs font-bold tracking-wider text-surface-50 md:h-max md:rounded-[0.4vw] md:bg-surface-900/75 md:px-[0.75vw] md:py-[0.75vw] md:text-[0.8vw] md:leading-none">EP ${escape(String(episode_number).padStart(2, "0"))}</p> <p class="rounded bg-surface-900/75 p-1 py-0 text-[0.7rem] font-semibold text-surface-50 md:h-max md:rounded-[0.4vw] md:bg-surface-900/75 md:px-[0.5vw] md:py-[0.55vw] md:text-[0.8vw] md:leading-none">${escape(new FormatTime(duration2).format_seconds_to_time_stamp_duration)}</p> </card-info></card-banner-info> <episode-info-card class="col-span-7 flex h-full w-full flex-col items-start justify-between md:absolute md:bottom-0 md:col-span-12 md:h-auto md:rounded-b-[0.625vw] md:bg-surface-900 md:p-[1vw]"><episode-titles class="relative flex w-full flex-col items-start gap-1 md:gap-[0.25vw]"><episode-name class="md:hover:overflow-scroll-y line-clamp-2 max-h-9 w-full overflow-hidden text-[0.8rem] font-light leading-snug text-white duration-500 ease-in-out scrollbar-none md:line-clamp-none md:max-h-[1.25vw] md:bg-surface-900 md:text-[0.9vw] md:leading-[1.25vw] md:text-surface-50/90 md:hover:max-h-[18vw] md:hover:text-surface-50 svelte-keg09q">${escape(title)}</episode-name> <episode-japanese-name class="md:hover:overflow-scroll-y line-clamp-2 max-h-4 w-full overflow-hidden text-[0.8rem] font-light leading-snug text-white duration-500 ease-in-out scrollbar-none md:line-clamp-none md:max-h-[1.3vw] md:bg-surface-900 md:text-[0.9vw] md:leading-[1.25vw] md:text-surface-50/90 md:hover:max-h-[18vw] md:hover:text-surface-50 svelte-keg09q">${escape(japanese_name2)} </episode-japanese-name></episode-titles> <episode-available-formats class="relative flex w-full items-center gap-2 bg-surface-900 md:gap-[0.65vw] md:pt-[0.75vw]"><formats class="flex gap-2 leading-none md:gap-[0.65vw]">${each(episode.formats, (format) => {
      return `<span class="rounded text-[0.6rem] font-semibold uppercase tracking-wider text-surface-50 md:bg-surface-400/50 md:p-[0.45vw] md:text-[0.8vw]">${escape(format)}</span>`;
    })}</formats> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-50 md:w-[0.25vw]" }, {}, {})} <resolutions class="flex gap-2 leading-none md:gap-[0.65vw]">${each(episode.resolutions, (episode_resolution) => {
      let resolution = (() => {
        switch (episode_resolution) {
          case "1080p":
            return "fhd";
          case "720p":
            return "hd";
          default:
            return "sd";
        }
      })();
      return ` <span class="text-[0.6rem] font-semibold uppercase tracking-wider text-surface-50 md:rounded md:bg-surface-400/25 md:p-[0.45vw] md:text-[0.8vw]">${escape(resolution)} </span>`;
    })}</resolutions> </episode-available-formats></episode-info-card> </a>`;
  })}</anime-episodes-cards> <anime-media-section class="mt-10 flex grid-cols-5 flex-col gap-10 md:mt-[3vw] md:grid md:gap-[4.375vw]"><comment-box class="md:col-span-3"><section-header class="flex gap-2 border-b-2 border-surface-50/10 pb-1 md:gap-[0.75vw] md:border-none md:pb-0"><header-title class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-v1dp1u">Comments</header-title> <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <comments-info class="mt-2 flex items-center justify-between md:hidden"><p class="flex items-center gap-1 md:hidden" data-svelte-h="svelte-kavhfj"><span class="text-base font-bold leading-none">69</span> <span class="text-sm font-semibold text-surface-50">comments</span></p> <button class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Filter">${validate_component(Filter, "Filter").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></comments-info> <form class="mt-3 md:mt-[1vw]">${validate_component(Text_editor, "TextEditor").$$render($$result, {}, {}, {})} <comment-submit class="mt-4 flex justify-between gap-5 md:mt-[0.75vw] md:gap-[1vw]"><comment-alert class="flex items-center gap-3 md:gap-[0.625vw]">${validate_component(Warning, "Warning").$$render($$result, { class: "w-10 md:w-[1.2vw]" }, {}, {})} <p class="text-[0.65rem] font-light leading-tight text-surface-300 md:text-[0.75vw] md:leading-[1.125vw]" data-svelte-h="svelte-19357bb">Please remember to follow our
                                        <a href="/" class="text-surface-200 underline">community guidelines</a>
                                        while commenting. Also please refrain from posting spoilers.</p></comment-alert> <button class="btn btn-sm h-9 w-40 rounded bg-primary-500 text-sm font-semibold md:h-[2.2vw] md:w-[7vw] md:rounded-[0.375vw] md:text-[0.85vw]" data-svelte-h="svelte-hpj9yr">Comment</button></comment-submit></form> <comments class="mt-10 flex flex-col gap-5 md:mt-[2vw] md:gap-[1.5vw]">${each(episode_comments, (comment, index) => {
    return `${validate_component(Comment, "Comment").$$render(
      $$result,
      {
        comment_user_profile_pic: comment.user.profile_pic,
        comment_username: comment.user.username,
        comment_date: comment.date,
        comment_content: comment.content,
        comment_likes: comment.likes,
        comment_replies: comment.replies,
        open: index === 0
      },
      {},
      {}
    )}`;
  })}</comments></comment-box> <forum-posts class="md:col-span-2"><section-header class="flex gap-2 border-b-2 border-surface-50/10 pb-1 md:gap-[0.75vw] md:border-none md:pb-0"><section-title class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-1c3584g">Forum Posts</section-title> <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <forum-details class="mt-2 flex items-center justify-between md:mt-[0.75vw]"><p class="flex items-center gap-1 md:hidden" data-svelte-h="svelte-relu4i"><span class="text-base font-bold leading-none">106</span> <span class="text-sm font-semibold text-surface-50">posts</span></p> <forum-options class="flex items-center gap-2 md:w-full md:justify-between"><button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">${validate_component(Cross, "Cross").$$render(
    $$result,
    {
      color: "surface-50",
      class: "w-4 rotate-45 md:w-[1vw]"
    },
    {},
    {}
  )}
                                    Create New</button> <button class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Filter">${validate_component(Filter, "Filter").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></forum-options></forum-details> <posts class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1.25vw] md:flex md:gap-[1vw]">${each(forum_posts, (post) => {
    return `${validate_component(Forum_posts, "ForumPosts").$$render(
      $$result,
      {
        link: "/",
        post_banner: post.banner,
        post_title: post.title,
        post_description: post.description,
        author: post.author,
        posted_on_date: post.posted_on,
        responses: post.responses
      },
      {},
      {}
    )}`;
  })}</posts></forum-posts></anime-media-section></anime-episodes-container></anime-info-episodes> <anime-more-details class="hidden flex-col md:col-span-2 md:flex"><section-header class="flex gap-[0.75vw]"><header-title class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-fcr951">Ratings</header-title> <button class="btn btn-icon rounded-[0.1875vw] bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <anime-ratings class="md:mt-[1.56vw]"><raing class="flex items-center gap-[0.5vw]" data-svelte-h="svelte-9h7f90"><span class="border-b-2 border-surface-50/50 pb-[0.5vw] font-bold md:text-[2vw] md:leading-[1.5vw]">92%</span> <span class="divider-vertical m-0 !border-surface-50/50 font-semibold text-surface-50 md:pl-1 md:text-[0.75vw] md:leading-[0.8vw]">2.8k ratings</span></raing> <raking class="block md:mt-[1vw]" data-svelte-h="svelte-b3rov8"><div class="flex items-center md:gap-[0.25vw]"><span class="font-semibold md:text-[1vw] md:leading-[1.5vw]">#80</span> <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Trending of all time</span></div> <div class="flex items-center md:gap-[0.25vw]"><span class="font-semibold md:text-[1vw] md:leading-[1.5vw]">#108</span> <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Most popular anime</span></div></raking> <button class="btn bg-secondary-100 text-surface-500 md:mt-[1.125vw] md:h-[1.5vw] md:w-[9vw] md:rounded-[0.18vw] md:text-[0.75vw] md:leading-[0.9vw]"><div class="flex place-items-center gap-[0.25vw]">${validate_component(Trending_up, "TrendingUp").$$render($$result, { class: "w-[1vw]" }, {}, {})}
                        Detailed Distribution</div></button> <star-rating class="md:mt-[0.4vw]"><span class="font-semibold md:text-[0.9vw] md:leading-[0.9vw]" data-svelte-h="svelte-jc620j">Your rating</span> <div class="flex items-center gap-[0.75vw] md:mt-[0.25vw]"><ratings>${validate_component(Ratings, "Ratings").$$render(
    $$result,
    {
      value: round_to_nearest_zero_point_five(4.5),
      max: 5
    },
    {},
    {
      full: () => {
        return `${validate_component(Star, "Star").$$render(
          $$result,
          {
            color: "white",
            variant: "full",
            fill_color: "white",
            class: "w-[1.25vw]"
          },
          {},
          {}
        )} `;
      },
      half: () => {
        return `${validate_component(Star, "Star").$$render(
          $$result,
          {
            color: "white",
            variant: "half",
            fill_color: "white",
            class: "w-[1.25vw]"
          },
          {},
          {}
        )} `;
      },
      empty: () => {
        return `${validate_component(Star, "Star").$$render(
          $$result,
          {
            color: "white",
            variant: "empty",
            fill_color: "white",
            class: "w-[1.25vw]"
          },
          {},
          {}
        )}`;
      }
    }
  )}</ratings> <span class="font-bold leading-none md:text-[0.95vw]" data-svelte-h="svelte-7rm839">92%</span> <button class="btn btn-icon bg-secondary-100 p-[0.3vw] text-surface-500 md:w-[1.375vw] md:rounded-[0.19vw]">${validate_component(Edit, "Edit").$$render(
    $$result,
    {
      variant: "without_underline_around_pencil",
      color: "bg-surface-500",
      style: "width: 0.75vw;"
    },
    {},
    {}
  )}</button></div></star-rating> <button class="btn btn-sm flex gap-[0.5vw] p-0 md:mt-[1vw] md:text-[0.8vw] md:leading-[0.9vw]">Add a review
                    ${validate_component(External_link, "ExternalLink").$$render($$result, { class: "w-[0.8vw]" }, {}, {})}</button></anime-ratings> <more-infos-header class="flex gap-[0.75vw] md:mt-[6vw]"><header-title class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-2w6ikd">Details</header-title> <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></more-infos-header> <more-infos class="md:mt-[1.25vw]"><anime-details class="flex flex-col gap-[1.125vw] capitalize">${each(Object.entries(anime_details), (details_item) => {
    let key = details_item[0], value = details_item[1];
    return `  ${Array.isArray(value) ? ` <div class="flex flex-col gap-[0.75vw] text-[0.9375vw] leading-none text-surface-50"><p class="font-semibold text-white">${escape(key)}</p> ${each(value.sort(), (item) => {
      return `<p>${escape(item)}</p>`;
    })} </div>` : ` <div class="flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none text-surface-50"><p class="font-semibold text-white">${escape(key)}</p> <p>${escape(value)}</p> </div>`}`;
  })}</anime-details> <voiceovercase class="mt-[2.5vw] block"><section-header class="flex gap-[0.75vw]"><header-title class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-15t97s4">Voiceover Cast</header-title> <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <div class="mt-[1vw] flex flex-col"><span class="text-[0.9375vw] text-surface-50" data-svelte-h="svelte-iybpe7">VAs</span> <button class="btn btn-sm mt-[0.3vw] h-[2.25vw] w-[6.625vw] gap-1 rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw]">Japanese
                            ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[0.9vw]" }, {}, {})}</button></div> <casts class="mt-[1vw] block"><casts-cards class="relative grid h-[9vw] w-full grid-cols-2 gap-[2px] overflow-hidden rounded-[0.75vw]"><cast-image class="relative col-span-1 w-full bg-cover">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "https://s4.anilist.co/file/anilistcdn/character/large/b55131-ypodHQCyHbzD.png",
      class: "absolute h-full w-full object-cover object-center"
    },
    {},
    {}
  )} <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1vw] md:px-[1vw]" data-svelte-h="svelte-1g23arn">Houtarou Oreki</span></cast-image> <cast-details class="relative col-span-1 w-full bg-cover">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "https://cdn.myanimelist.net/images/voiceactors/1/74056.jpg",
      class: "absolute h-full w-full object-cover object-center"
    },
    {},
    {}
  )} <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1vw] md:px-[1vw]" data-svelte-h="svelte-dz08k2">Yuuichi Nakamura</span></cast-details> <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25"></gradient-overlay></casts-cards> <casts-options class="mt-[1.5vw] flex flex-col"><pagination-buttons class="btn-group flex h-[2.25vw] w-1/2 rounded-[0.5vw] bg-surface-400"><button class="h-full w-full bg-surface-400 !p-0 font-semibold">${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw] rotate-180" }, {}, {})}</button> <button class="h-full w-full bg-surface-400 !p-0 !text-[0.9vw] font-bold" data-svelte-h="svelte-ay9v7f">01</button> <button class="h-full w-full bg-surface-400 !p-0 font-semibold">${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw]" }, {}, {})}</button></pagination-buttons> <span class="mt-[1vw] text-[0.75vw] leading-none text-surface-50" data-svelte-h="svelte-5r5l7u">Showing 1-5, out of 58 Voiceover Casts</span></casts-options></casts></voiceovercase> <recommendations class="mt-[2.5vw] block"><section-header class="flex gap-3"><header-title class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-dioo8v">Recommendations</header-title> <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw] opacity-75" }, {}, {})}</button></section-header> <recommendations-cards class="mt-[1vw] block"><cards-container class="grid grid-cols-2 gap-[1vw]"><a href="/myanimelist/1" class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover bg-center">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "https://wallup.net/wp-content/uploads/2017/10/27/112470-Yahari_Ore_no_Seishun_Love_Comedy_wa_Machigatteiru-Yuigahama_Yui-Hikigaya_Hachiman.jpg",
      class: "absolute h-full w-full object-cover object-center"
    },
    {},
    {}
  )} <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw]" data-svelte-h="svelte-88vwga">Yahari Ore no Seishun Love Come wa Machigatteiru.</span> <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25"></gradient-overlay></a> <a href="/myanimelist/1" class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyHBqVsDb9uqO0weu_Hi4DdFs-AywgumizkZnLQys-TJc19oks1tofYGDqijII7qDxzZEMqVdstNg&usqp=CAU&ec=48665698",
      class: "absolute h-full w-full object-cover object-center"
    },
    {},
    {}
  )} <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw]" data-svelte-h="svelte-w9tao2">Suzumiya Haruhi no Yuuutsu</span> <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25"></gradient-overlay></a></cards-container> <recommendations-options class="mt-[1.5vw] flex flex-col"><pagination-buttons class="btn-group flex h-[2.25vw] w-1/2 rounded-[0.5vw] bg-surface-400"><button class="h-full w-full bg-surface-400 !p-0 font-semibold">${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw] rotate-180" }, {}, {})}</button> <button class="h-full w-full bg-surface-400 !p-0 !text-[0.9vw] font-bold" data-svelte-h="svelte-ay9v7f">01</button> <button class="h-full w-full bg-surface-400 !p-0 font-semibold">${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw]" }, {}, {})}</button></pagination-buttons> <span class="mt-[1vw] text-[0.75vw] leading-none text-surface-50" data-svelte-h="svelte-138zbr">Showing 1-8, out of 47 Recommendations</span></recommendations-options></recommendations-cards></recommendations></more-infos></anime-more-details></anime-info-section> </anime-info-container>`;
});
const anime_episodes = [
  {
    id: 13,
    number: 1,
    title: "The Revival of the Long-established Classic Literature Club. The Descendants of the Classic Literature Club",
    japanese_title: "老舗古典部復活 カッコいいですよね 栄光の古典文学クラブの昔 古典文学部の活動",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-1.avif",
    duration: 1254,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 14,
    number: 2,
    title: "The Activities of the Esteemed Classic Literature Club",
    japanese_title: "古典文学部の活動",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-2.avif",
    duration: 1451,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 15,
    number: 3,
    title: "The Descendants of the Classic Literature Club",
    japanese_title: "古典文学部の末裔",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-3.avif",
    duration: 1257,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 16,
    number: 4,
    title: "The Old Days of the Glorious Classic Literature Club. The Truth of the Historic Classic Literature Club",
    japanese_title: "栄光の古典文学クラブの昔",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-4.avif",
    duration: 1405,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p"]
  },
  {
    id: 17,
    number: 5,
    title: "The Truth of the Historic Classic Literature Club",
    japanese_title: "歴史的古典文学部の真実",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-5.avif",
    duration: 1382,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 18,
    number: 6,
    title: "To Commit a Grave Sin",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-6.avif",
    japanese_title: "重大な罪を犯すには",
    duration: 1436,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 13,
    number: 7,
    title: "The Revival of the Long-established Classic Literature Club",
    japanese_title: "老舗古典部復活 カッコいいですよね",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-1.avif",
    duration: 1254,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 14,
    number: 8,
    title: "The Activities of the Esteemed Classic Literature Club",
    japanese_title: "古典文学部の活動",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-2.avif",
    duration: 1451,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 15,
    number: 9,
    title: "The Descendants of the Classic Literature Club",
    japanese_title: "古典文学部の末裔",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-3.avif",
    duration: 1257,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 16,
    number: 10,
    title: "The Old Days of the Glorious Classic Literature Club",
    japanese_title: "栄光の古典文学クラブの昔",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-4.avif",
    duration: 1405,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 17,
    number: 11,
    title: "The Truth of the Historic Classic Literature Club",
    japanese_title: "歴史的古典文学部の真実",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-5.avif",
    duration: 1382,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  },
  {
    id: 18,
    number: 12,
    title: "To Commit a Grave Sin",
    thumbnail: "/images/episodes/hyouka/Hyouka-ep-6.avif",
    japanese_title: "重大な罪を犯すには",
    duration: 1436,
    formats: ["sub", "dub"],
    resolutions: ["480p", "720p", "1080p"]
  }
];
const anime_list = [
  {
    id: 1,
    mal_id: 23273,
    anilist_id: null,
    kitsu_id: null,
    name: "Your Lie in April",
    japanese_name: "四月は君の嘘",
    source: null,
    aired_from: null,
    aired_to: null,
    banner: "/images/YourLieInApril-bg.avif",
    cover: "/images/Hyouka-bg.avif",
    banner_background_color: "#2A1710",
    cover_background_color: "#D8E4D8",
    synopsis: `Kousei Arima is a child prodigy known as the "Human Metronome" for playing the piano with precision and perfection. Guided by a strict mother and rigorous training, Kousei dominates every competition he enters, earning the admiration of his musical peers and praise from audiences. When his mother suddenly passes away, the subsequent trauma makes him unable to hear the sound of a piano, and he never takes the stage thereafter.\r
\r
Nowadays, Kousei lives a quiet and unassuming life as a junior high school student alongside his friends Tsubaki Sawabe and Ryouta Watari. While struggling to get over his mother's death, he continues to cling to music. His monochrome life turns upside down the day he encounters the eccentric violinist Kaori Miyazono, who thrusts him back into the spotlight as her accompanist. Through a little lie, these two young musicians grow closer together as Kaori tries to fill Kousei's world with color.`,
    background: "Winner in the anime division of the 2016 Sugoi Japan® Awards.",
    rating: "",
    updated: "2023-03-11T02:37:40.790Z",
    name_synonyms: [],
    genres: "/api/v1/anime/1/genres",
    themes: "/api/v1/anime/1/themes",
    characters: "/api/v1/anime/1/character",
    studios: "/api/v1/anime/1/studios",
    producers: "/api/v1/anime/1/producers",
    staffs: "/api/v1/anime/1/staffs",
    recommendations: [],
    episodes: "/api/v1/anime/1/episodes",
    openings: [],
    endings: [],
    episodes_count: 9,
    average_episode_length: 1611
  }
];
export {
  Anime_info as A,
  Error as E,
  anime_list as a,
  anime_episodes as b
};
