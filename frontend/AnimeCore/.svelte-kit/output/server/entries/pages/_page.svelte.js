import { n as noop, c as create_ssr_component, b as spread, d as escape_object, p as assign, q as identity, j as subscribe, o as onDestroy, a as add_attribute, l as each, e as escape, v as validate_component, m as missing_component } from "../../chunks/ssr.js";
import { p as page } from "../../chunks/stores.js";
import { I as Image_loader } from "../../chunks/image_loader.js";
import { C as Circle, S as Scroll_area } from "../../chunks/circle.js";
import { F as FormatDate, P as Play_circle } from "../../chunks/play_circle.js";
import { I as Info, A as Arrow_up_right } from "../../chunks/arrow_up_right.js";
import "../../chunks/ProgressBar.svelte_svelte_type_style_lang.js";
import { l as latest_animes, C as Core_project } from "../../chunks/core_project.js";
import { O as OpengraphGenerator } from "../../chunks/opengraph.js";
import { C as Chevron } from "../../chunks/chevron.js";
import { E as Edit, S as Settings_outline } from "../../chunks/edit.js";
import { F as Forum } from "../../chunks/forum.js";
import { w as writable } from "../../chunks/index.js";
import { Timer } from "easytimer.js";
import "svelte-gestures";
const is_client = typeof window !== "undefined";
let now = is_client ? () => window.performance.now() : () => Date.now();
let raf = is_client ? (cb) => requestAnimationFrame(cb) : noop;
const tasks = /* @__PURE__ */ new Set();
function run_tasks(now2) {
  tasks.forEach((task) => {
    if (!task.c(now2)) {
      tasks.delete(task);
      task.f();
    }
  });
  if (tasks.size !== 0)
    raf(run_tasks);
}
function loop(callback) {
  let task;
  if (tasks.size === 0)
    raf(run_tasks);
  return {
    promise: new Promise((fulfill) => {
      tasks.add(task = { c: callback, f: fulfill });
    }),
    abort() {
      tasks.delete(task);
    }
  };
}
const Moon = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 18 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M16.5004 9.65833C16.3693 11.0768 15.837 12.4287 14.9656 13.5557C14.0943 14.6826 12.92 15.5382 11.5802 16.0221C10.2403 16.5061 8.79039 16.5984 7.39999 16.2884C6.00959 15.9784 4.73623 15.2788 3.72893 14.2715C2.72162 13.2642 2.02202 11.9908 1.712 10.6004C1.40197 9.21001 1.49434 7.76007 1.97829 6.42025C2.46224 5.08042 3.31776 3.90614 4.44475 3.03479C5.57174 2.16345 6.92357 1.63109 8.34207 1.5C7.51158 2.62356 7.11195 4.00787 7.21585 5.40118C7.31975 6.79448 7.92029 8.10422 8.90824 9.09217C9.89619 10.0801 11.2059 10.6807 12.5992 10.7846C13.9925 10.8885 15.3768 10.4888 16.5004 9.65833Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const latest_episodes = [
  {
    id: 1,
    name: "SpyxFamily",
    cover: "/images/SpyxFamily.avif",
    episode_number: 6,
    release_date: "2023-06-28T10:30:00.000Z"
  },
  {
    id: 2,
    name: "Kaguya-sama: Love Is War",
    cover: "/images/KaguyaSama.avif",
    episode_number: 5,
    release_date: "2023-06-22T10:30:00.000Z"
  },
  {
    id: 3,
    name: "Aharen-san wa Hakaraenai",
    cover: "/images/AharenSan.avif",
    episode_number: 9,
    release_date: "2023-06-18T11:30:00.000Z"
  },
  {
    id: 4,
    name: "Summer time Rendering",
    cover: "/images/SummerTimeRendering.avif",
    episode_number: 12,
    release_date: "2023-06-10T12:30:00.000Z"
  },
  {
    id: 5,
    name: "Jujutsu Kaisen",
    cover: "/images/JujutsuKaisen.avif",
    episode_number: 27,
    release_date: "2023-06-03T12:30:00.000Z"
  }
];
const my_list = [
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
    id: 6,
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
    id: 7,
    name: "To LOVE-Ru",
    cover: "/images/ToLOVERu.avif",
    synopsis: `Rito Yuuki never gets a break—he's always finding himself in lewd accidents with girls around him. Although his heart still yearns for Haruna, his childhood love, Rito can't help but question his feelings for Lala, the alien princess who appeared in front of him and declared she would marry him. But now, it's not just Lala he has to deal with: her younger twin sisters, Momo and Nana, have also traveled to Earth, wanting to meet their older sister's fiancé, and just as luck would have it, they end up staying at Rito's home.`,
    current_episode: 9,
    episodes_count: 26,
    genres: ["Romantic", "Ecchi", "School"],
    type: "TV",
    release_date: "2021-7-22T10:30:00.000Z",
    studios: ["Bibury Animation Studios"]
  }
];
const Language = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 19 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M10.5388 12.0572C10.6519 11.7536 10.5765 11.4119 10.346 11.1841L8.74376 9.60081C8.66778 9.52573 8.66433 9.40428 8.73474 9.32395C10.0521 7.821 11.0686 6.04288 11.6803 4.14053C11.7071 4.05709 11.7844 3.99999 11.8721 3.99999H13.333C13.7932 3.99999 14.1663 3.62689 14.1663 3.16666C14.1663 2.70642 13.7932 2.33332 13.333 2.33332H8.33301V1.49999C8.33301 1.03975 7.95991 0.666656 7.49967 0.666656C7.03944 0.666656 6.66634 1.03975 6.66634 1.49999V2.33332H1.66634C1.2061 2.33332 0.833008 2.70642 0.833008 3.16666C0.833008 3.62689 1.2061 3.99999 1.66634 3.99999H9.85972C9.99741 3.99999 10.0939 4.13585 10.0457 4.26484C9.50884 5.70242 8.70714 7.07353 7.64674 8.29215C7.56886 8.38164 7.43039 8.38179 7.35241 8.29238C6.74997 7.60176 6.23177 6.85983 5.79781 6.08334C5.65624 5.83003 5.39216 5.66666 5.10197 5.66666C4.54126 5.66666 4.17002 6.24377 4.44131 6.73448C4.945 7.64553 5.55458 8.51419 6.2645 9.32382C6.33497 9.40418 6.33145 9.52572 6.25536 9.60077L2.74749 13.0604C2.418 13.3854 2.41616 13.9165 2.74339 14.2437C3.06903 14.5693 3.59699 14.5693 3.92263 14.2437L7.35825 10.8081C7.43636 10.73 7.56299 10.73 7.6411 10.8081L9.18501 12.352C9.60899 12.776 10.3295 12.6191 10.5388 12.0572ZM15.6597 7.9822C15.5133 7.5919 15.1402 7.33332 14.7233 7.33332H14.4427C14.0258 7.33332 13.6527 7.5919 13.5063 7.9822L10.3948 16.2796C10.2036 16.7895 10.5805 17.3333 11.125 17.3333C11.4505 17.3333 11.7418 17.1312 11.8557 16.8262L12.5511 14.9634C12.5803 14.8852 12.655 14.8333 12.7385 14.8333H16.4196C16.5029 14.8333 16.5774 14.8849 16.6068 14.9628L17.3093 16.8278C17.4238 17.132 17.7148 17.3333 18.0398 17.3333C18.5849 17.3333 18.9622 16.7889 18.7708 16.2785L15.6597 7.9822ZM13.5214 13.1667C13.3818 13.1667 13.2851 13.0273 13.3341 12.8966L14.3957 10.059C14.4605 9.88577 14.7055 9.88577 14.7703 10.059L15.832 12.8966C15.8809 13.0273 15.7842 13.1667 15.6446 13.1667H13.5214Z" fill="currentColor"></path></svg>`;
});
const Notifications = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 14 17" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M6.99967 16.3333C7.74508 16.3333 8.38028 15.8374 8.59161 15.1592C8.67376 14.8955 8.44248 14.6667 8.16634 14.6667H5.83301C5.55686 14.6667 5.32559 14.8955 5.40774 15.1592C5.61907 15.8374 6.25427 16.3333 6.99967 16.3333ZM12.1461 11.4798C12.0524 11.386 11.9997 11.2588 11.9997 11.1262V7.16666C11.9997 4.74749 10.7851 2.7009 8.63075 2.00626C8.41019 1.93515 8.24967 1.73635 8.24967 1.50462V1.33333C8.24967 0.641662 7.69134 0.0833282 6.99967 0.0833282C6.30801 0.0833282 5.74967 0.641662 5.74967 1.33333V1.50494C5.74967 1.73653 5.58936 1.93524 5.369 2.00646C3.22139 2.70056 1.99967 4.73992 1.99967 7.16666V11.1262C1.99967 11.2588 1.947 11.386 1.85323 11.4798L0.479454 12.8535C0.385686 12.9473 0.333008 13.0745 0.333008 13.2071V13.3333C0.333008 13.6095 0.556865 13.8333 0.833008 13.8333H13.1663C13.4425 13.8333 13.6663 13.6095 13.6663 13.3333V13.2071C13.6663 13.0745 13.6137 12.9473 13.5199 12.8535L12.1461 11.4798ZM10.333 11.6667C10.333 11.9428 10.1091 12.1667 9.83301 12.1667H4.16634C3.8902 12.1667 3.66634 11.9428 3.66634 11.6667V7.16666C3.66634 5.09999 4.92467 3.41666 6.99967 3.41666C9.07467 3.41666 10.333 5.09999 10.333 7.16666V11.6667Z" fill="currentColor"></path></svg>`;
});
const Play = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { viewBox: "0 0 20 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props)
    ],
    {}
  )}><path d="M4.16675 2.5L15.8334 10L4.16675 17.5V2.5Z" stroke="#070519" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Preference = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 18 16" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path fill-rule="evenodd" clip-rule="evenodd" d="M14 6.125C14.4973 6.125 14.9742 5.92746 15.3258 5.57583C15.6775 5.2242 15.875 4.74728 15.875 4.25C15.875 3.75272 15.6775 3.27581 15.3258 2.92418C14.9742 2.57255 14.4973 2.375 14 2.375C13.5027 2.375 13.0258 2.57255 12.6742 2.92418C12.3225 3.27581 12.125 3.75272 12.125 4.25C12.125 4.74728 12.3225 5.2242 12.6742 5.57583C13.0258 5.92746 13.5027 6.125 14 6.125ZM14 8C14.7014 7.99994 15.3887 7.80319 15.9838 7.4321C16.5789 7.06101 17.0581 6.53045 17.3668 5.90069C17.6756 5.27093 17.8015 4.56721 17.7303 3.86947C17.6591 3.17173 17.3937 2.50793 16.9642 1.95347C16.5347 1.39902 15.9583 0.976128 15.3005 0.732839C14.6427 0.489551 13.9298 0.435617 13.2429 0.577162C12.5559 0.718708 11.9225 1.05006 11.4144 1.53358C10.9438 1.98145 10.5983 2.54324 10.4106 3.16333C10.3841 3.25062 10.305 3.3125 10.2138 3.3125H1.1875C0.93886 3.3125 0.700403 3.41127 0.524588 3.58709C0.348772 3.7629 0.25 4.00136 0.25 4.25C0.25 4.49864 0.348772 4.7371 0.524588 4.91291C0.700403 5.08873 0.93886 5.1875 1.1875 5.1875H10.2139C10.3051 5.1875 10.3842 5.24935 10.4106 5.33661C10.6359 6.08032 11.0872 6.73707 11.7036 7.21448C12.3609 7.72355 13.1686 7.99986 14 8ZM5.875 11.75C5.875 12.2473 5.67746 12.7242 5.32583 13.0758C4.9742 13.4275 4.49728 13.625 4 13.625C3.50272 13.625 3.02581 13.4275 2.67418 13.0758C2.32254 12.7242 2.125 12.2473 2.125 11.75C2.125 11.2527 2.32254 10.7758 2.67418 10.4242C3.02581 10.0725 3.50272 9.875 4 9.875C4.49728 9.875 4.9742 10.0725 5.32583 10.4242C5.67746 10.7758 5.875 11.2527 5.875 11.75ZM7.78581 12.6875C7.69478 12.6875 7.61577 12.7492 7.5892 12.8362C7.33917 13.6558 6.8154 14.3668 6.10312 14.8486C5.34808 15.3594 4.43289 15.5777 3.52859 15.4629C2.62428 15.348 1.79274 14.9078 1.18936 14.2245C0.585987 13.5412 0.252065 12.6616 0.25 11.75C0.24969 10.8371 0.582434 9.95535 1.18583 9.27023C1.78923 8.58511 2.62183 8.14365 3.5275 8.02861C4.43318 7.91358 5.34971 8.13289 6.10522 8.64541C6.81789 9.12888 7.34111 9.84192 7.58947 10.6633C7.61587 10.7506 7.695 10.8125 7.78623 10.8125H16.8125C17.0611 10.8125 17.2996 10.9113 17.4754 11.0871C17.6512 11.2629 17.75 11.5014 17.75 11.75C17.75 11.9986 17.6512 12.2371 17.4754 12.4129C17.2996 12.5887 17.0611 12.6875 16.8125 12.6875H7.78581Z" fill="currentColor"></path></svg>`;
});
const Recent = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 18 16" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M9.83301 0.5C5.85939 0.5 2.60682 3.59134 2.34942 7.4999C2.33128 7.77545 2.10915 8 1.83301 8H1.04225C0.5965 8 0.373554 8.5392 0.689144 8.854L2.81323 10.9728C3.00839 11.1674 3.32429 11.1674 3.51945 10.9728L5.64354 8.854C5.95913 8.53919 5.73618 8 5.29043 8H4.49967C4.22353 8 3.99744 7.77536 4.02072 7.50021C4.27371 4.50975 6.77638 2.16667 9.83301 2.16667C13.058 2.16667 15.6663 4.775 15.6663 8C15.6663 11.225 13.058 13.8333 9.83301 13.8333C8.4051 13.8333 7.09543 13.3144 6.08478 12.4574C5.87357 12.2783 5.5572 12.2758 5.36139 12.4716L4.88656 12.9464C4.6913 13.1417 4.69026 13.4597 4.8979 13.6417C6.21687 14.7981 7.93806 15.5 9.83301 15.5C13.9747 15.5 17.333 12.1417 17.333 8C17.333 3.85833 13.9747 0.5 9.83301 0.5ZM9.49967 4.66667C9.22353 4.66667 8.99967 4.89052 8.99967 5.16667V8.54852C8.99967 8.72508 9.09279 8.88855 9.24466 8.9786L12.114 10.6799C12.3504 10.8201 12.6557 10.7432 12.7974 10.5076L12.9238 10.2976C13.0667 10.06 12.989 9.75148 12.7506 9.60992L10.4944 8.27031C10.3427 8.18022 10.2497 8.01683 10.2497 7.84038V5.16667C10.2497 4.89052 10.0258 4.66667 9.74967 4.66667H9.49967Z" fill="currentColor"></path></svg>`;
});
const timer = writable("start");
function is_date(obj) {
  return Object.prototype.toString.call(obj) === "[object Date]";
}
function get_interpolator(a, b) {
  if (a === b || a !== a)
    return () => a;
  const type = typeof a;
  if (type !== typeof b || Array.isArray(a) !== Array.isArray(b)) {
    throw new Error("Cannot interpolate values of different type");
  }
  if (Array.isArray(a)) {
    const arr = b.map((bi, i) => {
      return get_interpolator(a[i], bi);
    });
    return (t) => arr.map((fn) => fn(t));
  }
  if (type === "object") {
    if (!a || !b)
      throw new Error("Object cannot be null");
    if (is_date(a) && is_date(b)) {
      a = a.getTime();
      b = b.getTime();
      const delta = b - a;
      return (t) => new Date(a + t * delta);
    }
    const keys = Object.keys(b);
    const interpolators = {};
    keys.forEach((key) => {
      interpolators[key] = get_interpolator(a[key], b[key]);
    });
    return (t) => {
      const result = {};
      keys.forEach((key) => {
        result[key] = interpolators[key](t);
      });
      return result;
    };
  }
  if (type === "number") {
    const delta = b - a;
    return (t) => a + t * delta;
  }
  throw new Error(`Cannot interpolate ${type} values`);
}
function tweened(value, defaults = {}) {
  const store = writable(value);
  let task;
  let target_value = value;
  function set(new_value, opts) {
    if (value == null) {
      store.set(value = new_value);
      return Promise.resolve();
    }
    target_value = new_value;
    let previous_task = task;
    let started = false;
    let {
      delay = 0,
      duration = 400,
      easing = identity,
      interpolate = get_interpolator
    } = assign(assign({}, defaults), opts);
    if (duration === 0) {
      if (previous_task) {
        previous_task.abort();
        previous_task = null;
      }
      store.set(value = target_value);
      return Promise.resolve();
    }
    const start = now() + delay;
    let fn;
    task = loop((now2) => {
      if (now2 < start)
        return true;
      if (!started) {
        fn = interpolate(value, new_value);
        if (typeof duration === "function")
          duration = duration(value, new_value);
        started = true;
      }
      if (previous_task) {
        previous_task.abort();
        previous_task = null;
      }
      const elapsed = now2 - start;
      if (elapsed > /** @type {number} */
      duration) {
        store.set(value = new_value);
        return false;
      }
      store.set(value = fn(easing(elapsed / duration)));
      return true;
    });
    return task.promise;
  }
  return {
    set,
    update: (fn, opts) => set(fn(target_value, value), opts),
    subscribe: store.subscribe
  };
}
const slider_delay = 10;
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  let $timerStore, $$unsubscribe_timerStore;
  let $tweened_progress_value, $$unsubscribe_tweened_progress_value;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  $$unsubscribe_timerStore = subscribe(timer, (value) => $timerStore = value);
  let my_list_grid;
  let main_hero_slider_element;
  let main_hero_slide_active_index = 0;
  const add_one_to_main_hero_slide_active_index = () => {
    if (main_hero_slide_active_index + 1 === latest_animes.length) {
      main_hero_slide_active_index = 0;
      return;
    }
    main_hero_slide_active_index += 1;
  };
  let progress_value = 0;
  let tweened_progress_value = tweened(progress_value);
  $$unsubscribe_tweened_progress_value = subscribe(tweened_progress_value, (value) => $tweened_progress_value = value);
  let timer$1 = new Timer({
    target: { seconds: slider_delay },
    precision: "secondTenths"
  });
  timer$1.on("targetAchieved", () => {
    add_one_to_main_hero_slide_active_index();
    timer$1.reset();
  });
  timer$1.on("secondTenthsUpdated", () => {
    const time = timer$1.getTotalTimeValues().secondTenths;
    const value = 100 / slider_delay * (time / 10);
    progress_value = value;
  });
  onDestroy(() => {
    timer$1.reset();
    timer$1.stop();
  });
  let slide_buttons = [
    {
      background: "bg-surface-50",
      border: "border-surface-50"
    },
    {
      background: "bg-secondary-300",
      border: "border-secondary-300"
    },
    {
      background: "bg-warning-400",
      border: "border-warning-400"
    },
    {
      background: "bg-white",
      border: "border-white"
    },
    {
      background: "bg-primary-300",
      border: "border-primary-300"
    },
    {
      background: "bg-error-200",
      border: "border-error-200"
    }
  ];
  const icon_mapping = {
    left: {
      forums: {
        title: "Forums",
        icon: {
          component: Forum,
          class: "text-surface-900 w-[1.25vw]"
        }
      },
      last_watched: {
        title: "Last watched anime",
        icon: {
          component: Recent,
          class: "text-surface-900 w-[1.25vw]"
        }
      },
      notifications: {
        title: "Notifications",
        icon: {
          component: Notifications,
          class: "text-surface-900 w-[1.25vw]"
        }
      }
    },
    bottom: {
      language: {
        icon: {
          component: Language,
          class: "text-surface-900 w-[1.25vw]"
        }
      },
      preferences: {
        icon: {
          component: Preference,
          class: "text-surface-900 w-[1.25vw]"
        }
      },
      theme: {
        icon: {
          component: Moon,
          class: "text-surface-900 w-[1.25vw]"
        }
      },
      settings: {
        icon: {
          component: Settings_outline,
          class: "text-surface-900 w-[1.25vw]"
        }
      }
    }
  };
  const opengraph_html = new OpengraphGenerator({
    title: "AnimeCore - A modern anime streaming site",
    site_name: "CoreProject",
    image_url: "",
    // Use Opengraph later
    url: $page.url.href,
    locale: "en_US",
    description: "The most modern anime streaming site"
  }).generate_opengraph();
  {
    tweened_progress_value.set(progress_value);
  }
  {
    {
      switch ($timerStore) {
        case "start":
          timer$1?.start();
          break;
        case "pause":
          timer$1?.pause();
          break;
        case "reset":
          timer$1?.reset();
          timer$1?.start();
          break;
      }
    }
  }
  $$unsubscribe_page();
  $$unsubscribe_timerStore();
  $$unsubscribe_tweened_progress_value();
  return ` ${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} <home-container class="mt-16 block md:mt-0 md:p-[1.25vw] md:pr-[3.75vw]"><hero-section class="flex flex-col justify-between md:flex-row"><latest-animes-slider class="relative h-96 w-full md:h-[27.875vw] md:w-[42.1875vw]"${add_attribute("this", main_hero_slider_element, 0)}>${each(latest_animes, (anime, index) => {
    let active = index === main_hero_slide_active_index, slide_button_background = slide_buttons[main_hero_slide_active_index].background;
    return `  ${active ? `<anime-slide role="presentation" class="absolute inset-0 md:bottom-[2vw]">${validate_component(Image_loader, "ImageLoader").$$render(
      $$result,
      {
        src: anime.cover,
        class: "absolute h-full w-full object-cover object-center md:rounded-t-[0.875vw]"
      },
      {},
      {}
    )} <gradient-overlay class="absolute inset-0 bg-gradient-to-t from-surface-900/90 to-surface-900/50 md:to-surface-900/25"></gradient-overlay> <gradient-overlay class="absolute inset-0 hidden bg-gradient-to-r from-surface-900 to-surface-900/25 md:flex md:from-surface-900/50"></gradient-overlay> <anime-details class="absolute bottom-7 left-7 flex flex-col md:bottom-0 md:left-0 md:px-[3.75vw] md:py-[2.625vw]"><anime-name class="text-3xl font-bold md:text-[2vw] md:leading-[2.375vw]">${escape(anime.name)}</anime-name> <japanese-name class="text-base font-semibold text-white/90 md:hidden md:text-[2vw] md:leading-[2.375vw]">${escape(anime.japanese_name)}</japanese-name> <anime-infos class="flex flex-wrap items-center gap-2 pt-4 text-xs font-semibold text-white/90 md:gap-[0.65vw] md:pt-[0.5vw] md:text-[0.9375vw]"><span class="leading-[1.125vw]">${escape(anime.type)}</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-75 md:w-[0.25vw]" }, {}, {})} <span class="leading-[1.125vw]">${escape(anime.episodes_count)} eps</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-75 md:w-[0.25vw]" }, {}, {})} <span class="leading-[1.125vw]" data-svelte-h="svelte-3tnepj">Completed</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-75 md:w-[0.25vw]" }, {}, {})} <span class="capitalize leading-[1.125vw]">${escape(new FormatDate(anime.aired_from).format_to_season)}</span> ${validate_component(Circle, "Circle").$$render($$result, { class: "w-1 opacity-75 md:w-[0.25vw]" }, {}, {})} <span class="leading-[1.125vw]">${escape(anime.studios[0])} </span></anime-infos> <anime-genres class="flex gap-2 pb-2 pt-3 md:gap-[0.5vw] md:pt-[0.5vw]">${each(anime.genres, (item) => {
      return `<span class="rounded-lg bg-surface-900 p-2 px-3 text-xs md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.4vw] md:text-[0.75vw] md:font-semibold">${escape(item)}</span>`;
    })}</anime-genres> ${validate_component(Scroll_area, "ScrollArea").$$render(
      $$result,
      {
        gradientMask: true,
        offsetScrollbar: true,
        parentClass: "max-h-16 md:max-h-[6vw] hidden md:flex",
        class: "text-xs font-medium leading-4 text-surface-200 md:pt-[0.75vw] md:text-[0.85vw] md:leading-[1.1vw]"
      },
      {},
      {
        default: () => {
          return `${escape(anime.synopsis)} `;
        }
      }
    )} <options class="mb-2 mt-5 flex gap-3 md:mb-0 md:mt-[1.5vw] md:gap-[1vw]"><button class="${escape(slide_button_background, true) + " btn btn-icon flex h-14 w-24 justify-center gap-1 rounded-xl text-base font-bold text-surface-900 md:h-[3.125vw] md:w-[5.4375vw] md:rounded-[0.625vw] md:text-[0.875vw]"}">${validate_component(Play_circle, "PlayCircle").$$render($$result, { class: "w-4 text-surface-900 md:w-[1vw]" }, {}, {})} <span data-svelte-h="svelte-3vgftk">Ep 1</span></button> <a href="${"./mal/" + escape(anime.mal_id, true)}"><button class="btn btn-icon flex h-14 w-28 items-center justify-center rounded-xl bg-surface-900 text-base font-semibold text-surface-50 md:h-[3.125vw] md:w-[6.5vw] md:rounded-[0.5vw] md:text-[0.875vw] md:font-bold">${validate_component(Info, "Info").$$render(
      $$result,
      {
        class: "w-5 text-surface-50 md:w-[1.25vw]"
      },
      {},
      {}
    )} <span data-svelte-h="svelte-17ve4f4">Details</span> </button></a> <button class="btn btn-icon h-14 w-14 rounded-xl bg-surface-900 text-[3vw] font-bold text-surface-50 md:h-[3.125vw] md:w-[3.125vw] md:rounded-[0.5vw] md:text-[0.875vw]">${validate_component(Edit, "Edit").$$render(
      $$result,
      {
        variant: "with_underline_around_pencil",
        class: "w-4 text-surface-50 md:w-[1.25vw]"
      },
      {},
      {}
    )}</button> </options></anime-details> </anime-slide>` : ``}`;
  })} <slide-progress class="absolute bottom-0 flex w-full flex-col"><progress-bar class="${"h-[0.2rem] md:h-[0.145vw] " + escape(slide_buttons[main_hero_slide_active_index].background, true)}" style="${"width: " + escape($tweened_progress_value, true) + "%;"}"></progress-bar> <animes-boxes class="hidden w-full grid-cols-6 gap-[0.9375vw] md:mt-[1.25vw] md:grid">${each(latest_animes, (_, index) => {
    return `<button class="${"col-span-1 h-[0.625vw] w-full rounded-[0.1875vw] border-[0.15vw] " + escape(slide_buttons[index].border, true) + " transition duration-300 hover:border-surface-50/50 " + escape(
      index === main_hero_slide_active_index ? slide_buttons[index].background : "",
      true
    )}"></button>`;
  })}</animes-boxes></slide-progress> <button class="btn btn-icon absolute -left-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] bg-secondary-800 md:flex">${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      color: "text-white",
      class: "w-[1.25vw] rotate-90"
    },
    {},
    {}
  )}</button> <button class="btn btn-icon absolute -right-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] bg-secondary-800 md:flex">${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      color: "text-white",
      class: "w-[1.25vw] -rotate-90"
    },
    {},
    {}
  )}</button></latest-animes-slider> <latest-episodes class="hidden w-[21.5625vw] md:block"><section-header class="flex items-center justify-between pr-[0.75vw]"><header-title class="flex items-center gap-[0.625vw]"><span class="text-[1.25vw] font-bold" data-svelte-h="svelte-1yxzzdm">Latest Episodes</span> <button class="btn btn-icon h-[1.7vw] w-[1.7vw] rounded-[0.3vw] bg-surface-400">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.8vw]" }, {}, {})}</button></header-title> <button class="btn btn-icon h-[1.75vw] w-[6vw] rounded-[0.3vw] bg-surface-400 text-[0.9vw] font-semibold"><span data-svelte-h="svelte-bmzaoz">Full List</span> ${validate_component(Arrow_up_right, "ArrowUpRight").$$render($$result, { class: "w-[0.9vw]" }, {}, {})}</button></section-header> ${validate_component(Scroll_area, "ScrollArea").$$render(
    $$result,
    {
      offsetScrollbar: true,
      parentClass: "mt-[1vw] max-h-[22.25vw]",
      class: "flex flex-col gap-[1vw]"
    },
    {},
    {
      default: () => {
        return `${each(latest_episodes, (anime) => {
          return `<anime-episode class="relative h-[5vw]">${validate_component(Image_loader, "ImageLoader").$$render(
            $$result,
            {
              src: anime.cover,
              class: "absolute h-full w-full rounded-[0.75vw] object-cover object-center"
            },
            {},
            {}
          )} <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-t from-surface-900/75 to-surface-900/0"></gradient-overlay> <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-r from-surface-900/50 to-surface-900/0"></gradient-overlay> <episode-info class="absolute inset-0 flex items-start justify-between p-[1.3125vw]"><div class="flex flex-col gap-[0.25vw]"><episode-name class="text-[1vw] font-semibold leading-[1.1875vw] text-white">${escape(anime.name)}</episode-name> <episode-dates class="flex items-center gap-[0.35vw] text-[0.8vw] text-surface-50"><span class="font-semibold">Ep ${escape(String(anime.episode_number).padStart(2, "0"))}</span> <span>aired ${escape(new FormatDate(anime.release_date).format_to_time_from_now)}</span> </episode-dates></div> <button class="btn btn-icon h-[2.5vw] w-[2.5vw] rounded-full bg-warning-400 text-surface-900">${validate_component(Play, "Play").$$render($$result, { class: "w-[1.25vw]" }, {}, {})} </button></episode-info> </anime-episode>`;
        })}`;
      }
    }
  )} <section-bottom class="mt-[0.75vw] flex items-start justify-between gap-[2vw] pr-[0.75vw]" data-svelte-h="svelte-1wmumhz"><span class="text-[0.75vw] font-semibold md:leading-[1.25vw]">showing recently aired episodes from your Anime List</span> <button class="btn p-0 text-[0.75vw] font-semibold text-warning-400">Change to All</button></section-bottom></latest-episodes> <navigation-card class="relative mt-[2.75vw] hidden h-[24.5vw] w-[16.625vw] md:block">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "/images/NavigationBox-bg.avif",
      class: "absolute h-full w-full rounded-[0.875vw] object-cover object-center"
    },
    {},
    {}
  )} <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-t from-surface-900 from-[1%] to-surface-900/25"></gradient-overlay> <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-r from-surface-900/50 to-surface-900/25"></gradient-overlay> <navigation-content class="absolute inset-0 flex flex-col justify-between px-[1.875vw] pt-[2vw]"><section-header class="flex flex-col gap-[0.2w]" data-svelte-h="svelte-1rpglw4"><span class="text-[1.5vw] font-bold leading-[1vw]">Welcome</span> <span class="text-[0.875vw] font-semibold leading-[2.5vw]">Jump quickly into</span></section-header> <navigation-left-buttons class="mt-[1vw] flex flex-col gap-[0.75vw]">${each(Object.entries(icon_mapping.left), (item) => {
    let item_title = item[1].title, item_icon = item[1].icon;
    return `  <div class="flex items-center gap-[1vw]"><button class="btn h-[2.5vw] w-[2.5vw] rounded-[0.375vw] bg-surface-50 p-0">${validate_component(item_icon.component || missing_component, "svelte:component").$$render($$result, { class: item_icon.class }, {}, {})}</button> <span class="text-[1vw] font-bold">${escape(item_title)}</span> </div>`;
  })}</navigation-left-buttons> <navigation-right-buttons class="mt-[0.4vw]"><span class="text-[0.9vw] font-semibold leading-none" data-svelte-h="svelte-1evfjai">More</span> <div class="mt-[0.75vw] flex gap-[0.9375vw]">${each(Object.entries(icon_mapping.bottom), (item) => {
    let item_icon = item[1].icon;
    return ` <button class="btn h-[2.5vw] w-[2.5vw] rounded-[0.375vw] bg-surface-50 p-0">${validate_component(item_icon.component || missing_component, "svelte:component").$$render($$result, { class: item_icon.class }, {}, {})} </button>`;
  })}</div></navigation-right-buttons> <coreproject-logo class="mt-[1vw] flex items-center justify-center">${validate_component(Core_project, "CoreProject").$$render($$result, {}, {}, {})}</coreproject-logo></navigation-content></navigation-card></hero-section> <my-list class="flex flex-col p-4 pt-7 md:mb-[1vw] md:mt-[2.1875vw] md:flex md:w-[68vw] md:p-0"><section-header class="flex items-center gap-[0.625vw]"><header-title class="text-lg font-bold md:text-[1.25vw]" data-svelte-h="svelte-1ng29d9">My List</header-title> <button class="btn btn-icon hidden h-[1.7vw] w-[1.7vw] rounded-[0.3vw] bg-surface-400 md:flex">${validate_component(Settings_outline, "SettingsOutline").$$render($$result, { class: "w-[0.9vw]" }, {}, {})}</button></section-header> <my-list-info class="flex items-center justify-between"><span class="text-sm text-surface-50 md:text-[1vw] md:font-semibold">${escape(my_list.length)} anime in Watching</span> <my-list-options class="hidden items-center gap-[1vw] md:flex"><button class="btn btn-icon h-[2.25vw] w-[6.625vw] gap-[0.625vw] rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw] font-semibold">Watching
                    ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw]" }, {}, {})}</button> <button class="btn btn-icon h-[2.25vw] w-[5.625vw] gap-[0.625vw] rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw] font-semibold">Full List
                    ${validate_component(Arrow_up_right, "ArrowUpRight").$$render($$result, { class: "w-[1vw]" }, {}, {})}</button></my-list-options> <see-all class="md:hidden"><button class="btn gap-2 p-0 text-sm">See all
                    ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-4 -rotate-90 text-primary-400" }, {}, {})}</button></see-all></my-list-info> <my-list-animes class="relative mt-4 grid grid-cols-3 gap-3 md:mt-[1vw] md:grid-cols-5 md:gap-[1.25vw]"${add_attribute("this", my_list_grid, 0)}>${each(my_list, (anime) => {
    return `<a href="${"/mal/" + escape(anime.id, true) + "/episode/" + escape(anime.current_episode, true)}" class="relative">${validate_component(Image_loader, "ImageLoader").$$render(
      $$result,
      {
        src: anime.cover,
        alt: anime.name,
        class: "h-60 w-full rounded-lg object-cover object-center md:h-[20vw] md:rounded-[0.5vw]"
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
    )} <anime_info class="flex items-center gap-2 text-xs leading-none text-surface-50 md:gap-[0.5vw] md:text-[0.8vw]"><span class="hidden md:flex" data-svelte-h="svelte-1opiboo">Watching</span> ${validate_component(Circle, "Circle").$$render(
      $$result,
      {
        class: "hidden opacity-75 md:flex md:w-[0.25vw]"
      },
      {},
      {}
    )} <span>${escape(anime.current_episode)}/${escape(anime.episodes_count)} eps</span></anime_info> </div></anime-info> </a>`;
  })}</my-list-animes></my-list></home-container>`;
});
export {
  Page as default
};
