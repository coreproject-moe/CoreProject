import { c as create_ssr_component, l as each, e as escape, j as subscribe, u as is_promise, n as noop, v as validate_component, m as missing_component } from "../../../../chunks/ssr.js";
import { p as page } from "../../../../chunks/stores.js";
import { O as OpengraphGenerator } from "../../../../chunks/opengraph.js";
const Register_page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<div class="h-max w-full bg-surface-900 md:h-full"><div class="flex h-full w-full animate-pulse flex-col justify-between p-10 pb-[10vw] pt-[7vw] md:rounded-none md:p-0"><form-fields><div class="placeholder mb-9 h-4 w-60 !bg-surface-400 md:mb-[2vw] md:h-[1vw] md:w-[19.47vw]"></div> <email-field data-svelte-h="svelte-ukycha"><div class="placeholder h-4 w-11 !bg-surface-400 md:h-[0.9vw] md:w-[2.4vw]"></div> <div class="placeholder mt-2 h-12 rounded-xl !bg-surface-400 md:mt-[0.75vw] md:h-[3.2vw] md:rounded-[0.75vw]"></div> <div class="mt-2 flex h-[0.5rem] gap-2 md:mt-[0.75vw] md:gap-[0.5vw]"><div class="placeholder-circle h-full w-2 !bg-surface-400 md:h-full md:w-[0.6vw]"></div> <div class="placeholder h-full w-[19.5rem] !bg-surface-400 md:h-full md:w-[21vw]"></div></div></email-field> <password-field><div class="placeholder mt-5 h-4 w-20 !bg-surface-400 md:mt-[1.5vw] md:h-[0.9vw] md:w-[4.5vw]"></div> <div class="placeholder mt-2 h-12 rounded-xl !bg-surface-400 md:mt-[0.75vw] md:h-[3.2vw] md:rounded-[0.75vw]"></div> <div class="grid grid-cols-4 gap-2 md:gap-[0.75vw]">${each(Array(4), (_) => {
    return `<div class="placeholder col-span-1 mt-2 h-2 rounded-[0.75vw] !bg-surface-400 md:mt-[1.1vw] md:h-[0.65vw]"></div>`;
  })}</div> <div class="mt-4 md:mt-[1.5vw]"><div class="placeholder h-3 w-[6.5rem] !bg-surface-400 md:h-[0.75vw] md:w-[7.2vw]"></div> <div class="ml-3 mt-3 md:ml-[0.75vw] md:mt-[1vw]"><div class="hidden flex-col gap-[0.5vw] md:flex">${each(Array("7.1vw", "9vw", "5vw", "13vw"), (width) => {
    return `<div class="flex w-full gap-[0.75vw]"><div class="placeholder-circle h-[0.6vw] !bg-surface-400"></div> <div class="placeholder h-[0.5vw] !bg-surface-400" style="${"width: " + escape(width, true) + ";"}"></div> </div>`;
  })}</div> <div class="flex flex-col gap-2 md:hidden">${each(Array("7rem", "9rem", "6rem", "14.5rem"), (width) => {
    return `<div class="flex w-full gap-2"><div class="placeholder-circle h-2 !bg-surface-400 md:h-[0.6vw]"></div> <div class="placeholder h-2 !bg-surface-400" style="${"width: " + escape(width, true) + ";"}"></div> </div>`;
  })}</div></div></div></password-field> <div class="placeholder mt-5 h-3 w-36 !bg-surface-400 md:mt-[2.3vw] md:h-[0.8vw] md:w-[8.75vw]"></div> <div class="placeholder mt-2 h-12 rounded-xl !bg-surface-400 md:mt-[0.75vw] md:h-[3.125vw] md:rounded-[0.75vw]"></div></form-fields> <div class="mt-10 flex items-center justify-between md:mt-0" data-svelte-h="svelte-xhvfbr"><div class="flex flex-col gap-2 md:gap-[0.8vw]"><div class="placeholder h-2 w-[8.5rem] !bg-surface-400 md:h-[0.55vw] md:w-[8.25vw]"></div> <div class="placeholder h-4 w-10 !bg-surface-400 md:h-[1vw] md:w-[3vw]"></div></div> <div class="placeholder h-12 w-32 !bg-surface-400 md:h-[2.75vw] md:w-[7.75vw]"></div></div></div></div>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $svelte_store_page, $$unsubscribe_svelte_store_page;
  $$unsubscribe_svelte_store_page = subscribe(page, (value) => $svelte_store_page = value);
  const opengraph_html = new OpengraphGenerator({
    title: "Register Page",
    site_name: "CoreProject",
    url: $svelte_store_page.url.href,
    image_url: "",
    // Use Opengraph later
    locale: "en_US",
    description: "A page where you can register your core account"
  }).generate_opengraph();
  let one = import("../../../../chunks/12.js");
  let two = import("../../../../chunks/22.js");
  let three = import("../../../../chunks/3.js");
  const pages = [one, two, three];
  let page$1 = 0;
  let pages_state = [];
  let current_page;
  current_page = pages[page$1];
  $$unsubscribe_svelte_store_page();
  return `${$$result.head += `<!-- HEAD_svelte-14lyi73_START -->${$$result.title = `<title>Register | CoreProject</title>`, ""}<!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-14lyi73_END -->`, ""}  ${function(__value) {
    if (is_promise(__value)) {
      __value.then(null, noop);
      return ` ${validate_component(Register_page, "RegisterFormSkeleton").$$render($$result, {}, {}, {})} `;
    }
    return function(Module) {
      return ` ${validate_component(Module.default || missing_component, "svelte:component").$$render($$result, { pages_state }, {}, {})} `;
    }(__value);
  }(current_page)}`;
});
export {
  Page as default
};
