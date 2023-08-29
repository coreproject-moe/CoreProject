import { c as create_ssr_component, b as spread, d as escape_object, v as validate_component, l as each, e as escape, a as add_attribute, w as add_classes, m as missing_component, j as subscribe } from "../../../../../chunks/ssr.js";
import { p as page } from "../../../../../chunks/stores.js";
import { S as Share, A as Accordion, a as AccordionItem, F as Filter, T as Text_editor, W as Warning, C as Comment, e as episode_comments, b as Forum_posts, f as forum_posts, D as Download } from "../../../../../chunks/comment.js";
import { I as Image_loader } from "../../../../../chunks/image_loader.js";
import { C as Chevron } from "../../../../../chunks/chevron.js";
import { C as Cross } from "../../../../../chunks/cross.js";
import { P as Play_circle } from "../../../../../chunks/play_circle.js";
import "../../../../../chunks/ProgressBar.svelte_svelte_type_style_lang.js";
import { O as OpengraphGenerator } from "../../../../../chunks/opengraph.js";
import { d as derived } from "../../../../../chunks/index.js";
const recommendations = [
  {
    id: 1,
    mal_id: 38e3,
    name: "Demon Slayer: Kimetsu no Yaiba",
    japanese_name: "鬼滅の刃",
    cover: "/images/DemonSlayer-bg.avif",
    episodes_count: 12
  },
  {
    id: 2,
    mal_id: 12189,
    name: "Hyouka",
    japanese_name: "氷菓",
    cover: "/images/Hyouka-bg.avif",
    episodes_count: 41
  },
  {
    id: 3,
    mal_id: 23273,
    name: "You Lie in April",
    japanese_name: "四月は君の嘘",
    cover: "/images/YourLieInApril-bg.avif",
    episodes_count: 88
  },
  {
    id: 4,
    mal_id: 16498,
    name: "Attack on Titan",
    japanese_name: "進撃の巨人",
    cover: "/images/AttackOnTitan-bg.avif",
    episodes_count: 53
  },
  {
    id: 5,
    mal_id: 40748,
    name: "Jujutsu Kaisen",
    japanese_name: "呪術廻戦",
    cover: "/images/JujutsuKaisen.avif",
    episodes_count: 23
  },
  {
    id: 6,
    mal_id: 1535,
    name: "Death Note",
    japanese_name: "デスノート",
    cover: "/images/DeathNote-bg.avif",
    episodes_count: 38
  }
];
const Next = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 24 24" }
    ],
    {}
  )}><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M0 0h24v24H0z"></path><path fill="currentColor" d="M2 5v14c0 .86 1.012 1.318 1.659.753l8-7a1 1 0 0 0 0-1.506l-8-7C3.012 3.682 2 4.141 2 5zm11 0v14c0 .86 1.012 1.318 1.659.753l8-7a1 1 0 0 0 0-1.506l-8-7C14.012 3.682 13 4.141 13 5z"></path></g></svg>`;
});
const Episode = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let comment_body;
  const button_state_mapping = { lights: false };
  const video_player_mapping = {
    preferences: { lights: { text: "Lights" } },
    options: {
      download: {
        component: Download,
        link: "./",
        class: "w-4 md:w-[1.4vw]",
        text: "Download"
      },
      prev: {
        component: Next,
        link: "./",
        class: "w-4 md:w-[1.4vw] rotate-180",
        text: "Previous Episode"
      },
      next: {
        component: Next,
        link: "./",
        class: "w-4 md:w-[1.4vw]",
        text: "Next Episode"
      }
    }
  };
  let { episode_number } = $$props;
  let { episode_details = `The autumn he was twelve, piano prodigy Kousei Arima suddenly found himself unable to play the piano after his mother's death. Ever since then, it's like he's been frozen in time. His childhood friend, Tsubaki Sawabe, watches over him with concern; one day, she invites him on a double date. Kousei's other childhood friend, Ryouta Watari, is being introduced to a certain girl. Kousei reluctantly heads over to the rendezvous spot. There, he sees a girl playing a melodica. This girl, who allegedly has a crush on Watari, is Kaori Miyazono. And she turns out to be a violinist!` } = $$props;
  let { episode_name = `Monotone/Colorful` } = $$props;
  if ($$props.episode_number === void 0 && $$bindings.episode_number && episode_number !== void 0)
    $$bindings.episode_number(episode_number);
  if ($$props.episode_details === void 0 && $$bindings.episode_details && episode_details !== void 0)
    $$bindings.episode_details(episode_details);
  if ($$props.episode_name === void 0 && $$bindings.episode_name && episode_name !== void 0)
    $$bindings.episode_name(episode_name);
  return `${``} <episode-container class="mt-16 flex flex-col md:mt-0 md:gap-[3.5vw] md:py-[2vw] md:pl-[1vw] md:pr-[3.75vw]"><episode-content class="grid grid-cols-12 md:gap-[5vw]"><video-player class="col-span-12 flex flex-col md:col-span-8 md:gap-[0.75vw]"><player class="relative h-64 w-full md:z-30 md:h-[35vw]"> ${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "/images/DemonSlayer-episode.webp",
      alt: "Episode image",
      class: "h-full w-full rounded-none object-cover md:rounded-[0.5vw] "
    },
    {},
    {}
  )}</player> <video-player-options class="flex flex-col gap-2 px-5 md:flex-row md:items-center md:justify-between md:gap-0 md:p-0"><preferences class="flex gap-2 md:items-center md:gap-[1vw]"><sub-dub class="hidden items-center gap-[0.75vw] md:flex"><span class="text-[1vw] font-semibold uppercase" data-svelte-h="svelte-dszpe2">sub/dub:</span> <button class="btn flex items-center gap-[0.5vw] rounded-[0.35vw] bg-surface-400 px-[0.75vw] py-[0.5vw] text-[1vw] leading-none">Vidstreaming (sub)
                            ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-[1vw]" }, {}, {})}</button></sub-dub> ${each(Object.entries(video_player_mapping.preferences), (item) => {
    let text = item[1].text, enabled = button_state_mapping[item[0]];
    return `  <button class="btn hidden items-center p-0 text-xs leading-none md:flex md:text-[0.9vw]"><span>${escape(text)}:</span> ${enabled ? `<status class="font-semibold text-warning-500" data-svelte-h="svelte-r09gz">On</status>` : `<status class="font-semibold text-primary-300" data-svelte-h="svelte-ajl8jh">Off</status>`} </button>`;
  })}</preferences> <div class="flex w-full items-center justify-between md:w-auto"><sub-dub class="flex items-center gap-2 md:hidden"><span class="text-xs font-semibold uppercase" data-svelte-h="svelte-65wj7">sub/dub:</span> <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs leading-none">Vidstreaming (sub)
                            ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-3" }, {}, {})}</button></sub-dub> <video-options class="flex items-center gap-3 md:gap-[0.75vw]">${each(Object.entries(video_player_mapping.options), (item) => {
    let component = item[1].component, link = item[1].link, klass = item[1].class;
    item[1].text;
    return `    <a${add_attribute("href", link, 0)}${add_classes((!link ? "pointer-events-none" : "").trim())}>${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: klass }, {}, {})} </a>`;
  })}</video-options></div></video-player-options></video-player> <episode-info class="col-span-12 flex flex-col gap-3 p-5 md:col-span-4 md:gap-[1.5vw] md:p-0"><header class="flex items-center justify-between"><span class="text-lg font-semibold md:text-[1.35vw]" data-svelte-h="svelte-1ox2gge">Episodes</span> <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs font-semibold leading-none md:gap-[0.5vw] md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.5vw] md:text-[1vw]">EPS: 1 - 60
                    ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-3 md:w-[1vw]" }, {}, {})}</button></header> <episodes class="grid grid-cols-7 gap-2 md:grid-cols-6 md:gap-[0.75vw]">${each(Array(60), (item, index) => {
    let actual_index = index + 1, button_active = actual_index === episode_number;
    return `  <a href="${"./" + escape(actual_index, true)}" class="${escape(button_active ? "bg-primary-500" : "bg-surface-400", true) + " btn rounded py-3 text-sm font-semibold leading-none md:rounded-[0.35vw] md:py-[0.75vw] md:text-[1.2vw]"}">${escape(actual_index)} </a>`;
  })}</episodes></episode-info></episode-content> <episode-details class="grid grid-cols-12 gap-5 p-5 md:gap-[5vw] md:p-0"><episode-info class="col-span-12 flex flex-col gap-2 md:col-span-8 md:gap-[1vw]"><anime-name-options class="flex items-center justify-between"><div data-svelte-h="svelte-8kw9d2"><a href="/mal/1" class="flex flex-col gap-1 text-lg leading-none md:gap-[0.25vw] md:text-[1.1vw]"><span class="font-semibold uppercase">Demon Slayer S1</span> <span class="text-base text-surface-50 md:text-[1vw]">Kimetsu no yaiba</span></a></div> <options><button class="btn bg-transparent p-0">${validate_component(Share, "Share").$$render($$result, { class: "md:w-[1.25vw]" }, {}, {})}</button></options></anime-name-options> ${validate_component(Accordion, "Accordion").$$render(
    $$result,
    {
      padding: "p-0",
      hover: "bg-transparent",
      duration: 300
    },
    {},
    {
      default: () => {
        return `${validate_component(AccordionItem, "AccordionItem").$$render(
          $$result,
          {
            open: true,
            regionPanel: "text-surface-50 text-sm leading-snug md:text-[1vw] md:leading-[1.35vw]",
            regionControl: "text-base text-warning-400 font-semibold md:text-[1.25vw] md:leading-[1vw] md:pb-[1vw]",
            regionCaret: "md:w-[1vw]"
          },
          {},
          {
            content: () => {
              return `${escape(episode_details)} `;
            },
            summary: () => {
              return `${escape(episode_name)}`;
            },
            lead: () => {
              return `EP${escape(episode_number)}`;
            }
          }
        )}`;
      }
    }
  )} <a href="/mal/1" class="btn w-max rounded-md bg-primary-500 py-3 text-sm font-semibold leading-none md:rounded-[0.5vw] md:py-[0.9vw] md:text-[1vw]"><span data-svelte-h="svelte-tpj0x0">View detail</span> ${validate_component(Chevron, "Chevron").$$render($$result, { class: "w-3 -rotate-90 md:w-[1vw]" }, {}, {})}</a></episode-info> <next-episode class="col-span-4 hidden flex-col md:flex"><span class="font-semibold uppercase md:text-[1.1vw]" data-svelte-h="svelte-1pwgppm">next episode</span> <a href="${"./" + escape(episode_number + 1, true)}" class="flex md:mt-[0.75vw] md:gap-[1vw]"><episode-cover class="relative">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "/images/episodes/hyouka/Hyouka-ep-6.avif",
      class: "md:w-[12vw] md:rounded-[0.25vw]"
    },
    {},
    {}
  )} <overlay class="absolute inset-0 flex items-center justify-center bg-surface-900/40"><play class="rounded-full bg-surface-900/50 md:p-[1vw]">${validate_component(Play_circle, "PlayCircle").$$render($$result, { class: "md:w-[1.25vw]" }, {}, {})}</play></overlay></episode-cover> <episode-info class="flex flex-col justify-between leading-none md:py-[1vw]"><div class="flex flex-col md:gap-[0.5vw]"><span class="text-warning-200 md:text-[1.1vw]" data-svelte-h="svelte-urba2z">Finally they met</span> <span class="md:text-[1vw]">Episode - ${escape(episode_number + 1)}</span></div> <span class="text-surface-50 md:text-[1vw]" data-svelte-h="svelte-zt83tm">23 min</span></episode-info></a></next-episode></episode-details> <episode-media class="grid grid-cols-12 p-5 md:gap-[5vw] md:p-0"><comments-section class="col-span-12 flex flex-col md:col-span-7 md:gap-[0.75vw]"><span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-lg font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-fcwu4f">Comments</span> <comments-info class="mt-2 flex items-center justify-between md:hidden"><p class="flex items-center gap-1" data-svelte-h="svelte-1mufn9w"><span class="text-base font-bold leading-none">69</span> <span class="text-sm font-semibold text-surface-50">comments</span></p> <button class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Filter">${validate_component(Filter, "Filter").$$render(
    $$result,
    {
      class: "w-3 md:w-[1vw]",
      color: "lightgray"
    },
    {},
    {}
  )}</button></comments-info> <comment-form class="flex flex-col md:flex-row md:gap-[1vw]"><a href="/user/" class="hidden h-7 w-7 flex-shrink-0 md:mt-[0.5vw] md:flex md:h-[2vw] md:w-[2vw]">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: "/images/DemonSlayer-bg.avif",
      alt: "Avatar",
      class: "h-full w-full shrink-0 rounded-full object-cover"
    },
    {},
    {}
  )}</a> <form class="mt-3 flex flex-col gap-3 md:mt-[1vw] md:gap-[0.75vw]"><span class="leading-none text-surface-50 md:text-[1vw]" data-svelte-h="svelte-1hojf2e">Comment as <strong>Tokito</strong></span> ${validate_component(Text_editor, "TextEditor").$$render($$result, { textarea_value: comment_body }, {}, {})} <warning-submit class="flex justify-between gap-5 md:gap-[1vw]"><warning class="flex items-center gap-3 md:gap-[0.625vw]">${validate_component(Warning, "Warning").$$render($$result, { class: "w-10 md:w-[1.2vw]" }, {}, {})} <p class="text-[0.65rem] font-light leading-tight text-surface-300 md:text-[0.75vw] md:leading-[1.125vw]" data-svelte-h="svelte-1cqjq6f">Please remember to follow our
                                <a href="/" class="text-surface-200 underline">community guidelines</a>
                                while commenting. Also please refrain from posting spoilers.</p></warning> <button class="btn btn-sm h-9 w-40 rounded bg-primary-500 text-sm font-semibold md:h-[2.2vw] md:w-[6vw] md:rounded-[0.375vw] md:text-[0.85vw]" data-svelte-h="svelte-x7w50w">Comment</button></warning-submit></form></comment-form> <comments class="mt-10 flex flex-col gap-5 md:mt-[2vw] md:gap-[1.5vw]">${each(episode_comments, (comment, index) => {
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
  })}</comments></comments-section> <forum-recommendations class="col-span-12 mt-10 flex flex-col gap-5 md:col-span-5 md:mt-0 md:gap-[2vw]"><forum-posts><span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-lg font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]" data-svelte-h="svelte-1fshqmj">Forum posts</span> <forum-options class="mt-3 flex items-center justify-between md:mt-[1.25vw]"><posts-count class="flex items-center gap-1 md:hidden" data-svelte-h="svelte-120qm6q"><span class="text-base font-bold leading-none">106</span> <span class="text-sm font-semibold text-surface-50">posts</span></posts-count> <forum-buttons class="flex items-center gap-2 md:w-full md:justify-between"><button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">${validate_component(Cross, "Cross").$$render(
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
  )}</button></forum-buttons></forum-options> <posts class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1vw] md:flex md:gap-[1vw]">${each(forum_posts, (post) => {
    return `${validate_component(Forum_posts, "ForumPosts").$$render(
      $$result,
      {
        post_title: post.title,
        post_banner: post.banner,
        post_description: post.description,
        author: post.author,
        posted_on_date: post.posted_on,
        link: post.link,
        responses: Number(post.responses)
      },
      {},
      {}
    )}`;
  })}</posts> <load-more class="mt-3 flex w-full justify-center md:mt-[1vw]"><button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-3 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">Load more
                        ${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      color: "surface-50",
      class: "w-4 md:w-[1vw]"
    },
    {},
    {}
  )}</button></load-more></forum-posts> <recommendations-container><span class="text-lg font-semibold md:text-[1.35vw]" data-svelte-h="svelte-1brbazo">Recommendations</span> <container class="mt-3 grid grid-cols-3 gap-4 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1vw]">${each(recommendations, (anime) => {
    return `<a href="${"/myanimelist/" + escape(anime.mal_id, true)}" class="card relative col-span-1 h-44 w-full overflow-hidden md:h-[15vw] md:rounded-[0.75vw]">${validate_component(Image_loader, "ImageLoader").$$render(
      $$result,
      {
        src: anime.cover,
        class: "h-full w-full object-cover object-center"
      },
      {},
      {}
    )} <anime-details class="absolute bottom-3 z-10 flex w-full flex-col items-center gap-1 px-[0.5vw] text-center md:bottom-[1vw] md:gap-[0.25vw]"><anime-title class="text-sm font-semibold leading-snug duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[1vw] md:leading-[1.25vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">${escape(anime.name)}</anime-title> <anime-japanese-name class="text-xs leading-none md:text-[0.9vw]">${escape(anime.japanese_name)}</anime-japanese-name> <anime-episodes-count class="text-xs leading-none text-surface-50 duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[0.9vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">Episodes: <b>${escape(anime.episodes_count)}</b> </anime-episodes-count></anime-details> <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/80 to-surface-900/25"></gradient-overlay> </a>`;
  })}</container> <load-more class="mt-3 flex w-full justify-center md:mt-[1vw]"><button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-3 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">Load more
                        ${validate_component(Chevron, "Chevron").$$render(
    $$result,
    {
      color: "surface-50",
      class: "w-4 md:w-[1vw]"
    },
    {},
    {}
  )}</button></load-more></recommendations-container></forum-recommendations></episode-media></episode-container>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  let $episode_number, $$unsubscribe_episode_number;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  let episode_number = derived(page, (page2) => page2.params.id);
  $$unsubscribe_episode_number = subscribe(episode_number, (value) => $episode_number = value);
  const opengraph_html = new OpengraphGenerator({
    title: `Watch  on AnimeCore | Episode ${episode_number}`,
    url: $page.url.href,
    description: "",
    site_name: "CoreProject",
    locale: "en_US",
    image_url: ""
  }).generate_opengraph();
  $$unsubscribe_page();
  $$unsubscribe_episode_number();
  return `${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} ${validate_component(Episode, "EpisodePage").$$render($$result, { episode_number: Number($episode_number) }, {}, {})}`;
});
export {
  Page as default
};
