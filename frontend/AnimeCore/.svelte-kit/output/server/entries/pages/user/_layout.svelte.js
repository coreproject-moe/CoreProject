import { c as create_ssr_component, b as spread, d as escape_object, o as onDestroy, v as validate_component, l as each, e as escape } from "../../../chunks/ssr.js";
import { I as Image_loader } from "../../../chunks/image_loader.js";
import { l as latest_animes, C as Core_project } from "../../../chunks/core_project.js";
import { Timer } from "easytimer.js";
import sample from "lodash/sample.js";
const Refresh = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 12 12" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M11.5 2V5H8.5" stroke="white" stroke-linecap="round" stroke-linejoin="round"></path><path d="M0.5 10V7H3.5" stroke="white" stroke-linecap="round" stroke-linejoin="round"></path><path d="M1.755 4.50001C2.00858 3.7834 2.43957 3.14271 3.00773 2.63772C3.5759 2.13272 4.26273 1.77989 5.00414 1.61214C5.74555 1.44438 6.51738 1.46718 7.2476 1.67839C7.97781 1.88961 8.64263 2.28236 9.18 2.82001L11.5 5.00001M0.5 7.00001L2.82 9.18001C3.35737 9.71765 4.02219 10.1104 4.7524 10.3216C5.48262 10.5328 6.25445 10.5556 6.99586 10.3879C7.73727 10.2201 8.4241 9.86729 8.99227 9.3623C9.56043 8.85731 9.99142 8.21662 10.245 7.50001" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let image;
  let name;
  let timer = new Timer({
    target: { seconds: 20 },
    precision: "secondTenths"
  });
  timer.on("targetAchieved", () => {
    change_index();
  });
  const change_index = () => {
    const item = sample(latest_animes);
    image = item?.cover;
    name = item?.name;
    timer.isRunning() ? timer.reset() : timer.start();
  };
  onDestroy(() => {
    timer.stop();
  });
  return `${$$result.head += `<!-- HEAD_svelte-1gd190a_START --><style data-svelte-h="svelte-1exy7pr">#page {
            overflow-y: hidden;
        }</style><!-- HEAD_svelte-1gd190a_END -->`, ""} <root class="relative inline-grid h-full w-full md:grid-cols-2">${image && name ? `<div class="relative col-start-1 col-end-2 row-start-1 row-end-2">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: image,
      class: "absolute h-full w-full object-cover"
    },
    {},
    {}
  )} <div class="absolute inset-0 bg-gradient-to-r from-surface-900 to-surface-900/60"></div> <div class="absolute inset-0 bg-gradient-to-t from-surface-900/50 to-surface-900/0"></div> <div class="absolute inset-0 bottom-[6vw] hidden flex-col items-center justify-center text-center md:flex"><span class="text-[0.75vw] font-semibold uppercase leading-none text-surface-50" data-svelte-h="svelte-t3ibms">welcome to</span> <div class="mt-[0.75vw] flex items-center leading-none">${validate_component(Core_project, "CoreProject").$$render($$result, {}, {}, {})} ${each(".moe".split(""), (letter) => {
    return `<span class="inline-flex text-[1.5vw] font-bold text-surface-300">${escape(letter)}</span>`;
  })}</div> <span class="mt-[2.875vw] max-w-[22vw] text-[1.25vw] font-semibold leading-[1.75vw]" data-svelte-h="svelte-m6v3be">Bridging the gap between streaming and torrenting sites with a modern and clean interface.</span> <span class="mt-[4vw] text-[0.9vw] font-semibold leading-none" data-svelte-h="svelte-8s6wgf">With a coreproject account, you can</span> <span class="mt-[1vw] max-w-[20.375vw] text-[0.9vw] font-medium leading-[1vw] text-surface-200" data-svelte-h="svelte-1mktp3c">continue on animecore, mangacore and soundcore with same account.</span></div> <div class="absolute bottom-[1.85vw] left-10 md:left-[2vw] md:flex"><div class="flex flex-col gap-2 md:gap-[0.75vw]"><span class="text-[2.25vw] font-semibold uppercase leading-none tracking-widest text-surface-300/75 md:text-[0.75vw]" data-svelte-h="svelte-1bjrkqd">Background from anime</span> <div class="flex items-center gap-[2vw] md:gap-[0.5vw]"><span class="text-[3vw] font-bold uppercase leading-none tracking-widest text-warning-400 md:text-[1vw]">${escape(name)}</span> <button class="btn p-0">${validate_component(Refresh, "Refresh").$$render(
    $$result,
    {
      class: "hidden w-[2vw] md:flex md:w-[0.8vw]"
    },
    {},
    {}
  )}</button></div></div></div></div>` : ``} <div class="z-0 col-start-1 col-end-1 row-start-1 row-end-1 flex items-center justify-center md:col-start-2 md:col-end-2 md:block md:items-end md:px-[8vw] md:py-[2.2vw]">${slots.default ? slots.default({}) : ``}</div></root>`;
});
export {
  Layout as default
};
