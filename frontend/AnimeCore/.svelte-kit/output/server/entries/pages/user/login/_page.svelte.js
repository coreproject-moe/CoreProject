import { c as create_ssr_component, j as subscribe, u as is_promise, n as noop, v as validate_component, m as missing_component } from "../../../../chunks/ssr.js";
import { p as page } from "../../../../chunks/stores.js";
import { O as OpengraphGenerator } from "../../../../chunks/opengraph.js";
const Login_page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<form class="flex h-max w-full animate-pulse flex-col gap-[15vw] bg-surface-900 p-10 md:h-full md:justify-between md:gap-0 md:rounded-none md:p-0" data-svelte-h="svelte-stbc39"><div class="placeholder h-4 w-60 !bg-surface-400 md:h-[1vw] md:w-[18vw]"></div> <div class="flex flex-col gap-7 md:block"><email-username-field><div class="placeholder h-4 w-32 !bg-surface-400 md:h-[0.9vw] md:w-[8.5vw]"></div> <div class="placeholder mt-2 h-12 rounded-xl !bg-surface-400 md:mt-[0.75vw] md:h-[3.2vw] md:rounded-[0.75vw]"></div> <div class="mt-2 flex h-[0.5rem] gap-2 md:mt-[0.75vw] md:h-[0.6vw] md:gap-[0.5vw]"><div class="placeholder-circle h-full w-2 !bg-surface-400 md:w-[0.6vw]"></div> <div class="placeholder h-full w-[19.5rem] !bg-surface-400 md:w-[21vw]"></div></div></email-username-field> <password-field class="flex flex-col gap-2 md:mt-[1.75vw] md:gap-[0.5vw]"><div class="placeholder h-4 w-16 !bg-surface-400 md:h-[0.9vw] md:w-[4.5vw]"></div> <div class="placeholder h-12 rounded-xl !bg-surface-400 md:h-[3.2vw] md:rounded-[0.75vw]"></div></password-field> <div class="placeholder h-3 w-36 !bg-surface-400 md:mt-[3vw] md:h-[0.9vw] md:w-[9.5vw]"></div></div> <div class="flex items-center justify-between"><div class="flex flex-col gap-2 md:gap-[0.8vw]"><div class="placeholder h-2 w-[8.5rem] !bg-surface-400 md:h-[0.55vw] md:w-[8.75vw]"></div> <div class="placeholder h-4 w-16 !bg-surface-400 md:h-[1vw] md:w-[4vw]"></div></div> <div class="placeholder h-12 w-32 !bg-surface-400 md:h-[2.75vw] md:w-[7.75vw]"></div></div></form>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $svelte_store_page, $$unsubscribe_svelte_store_page;
  $$unsubscribe_svelte_store_page = subscribe(page, (value) => $svelte_store_page = value);
  const opengraph_html = new OpengraphGenerator({
    title: "Register Page",
    site_name: "CoreProject",
    image_url: "",
    // Use Opengraph later
    url: $svelte_store_page.url.href,
    locale: "en_US",
    description: "A page where you can register your core account"
  }).generate_opengraph();
  let one = import("../../../../chunks/1.js");
  let two = import("../../../../chunks/2.js");
  const pages = [one, two];
  let page$1 = 0;
  let current_page;
  current_page = pages[page$1];
  $$unsubscribe_svelte_store_page();
  return `${$$result.head += `<!-- HEAD_svelte-5boj73_START -->${$$result.title = `<title>Login | CoreProject</title>`, ""}<!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-5boj73_END -->`, ""}  ${function(__value) {
    if (is_promise(__value)) {
      __value.then(null, noop);
      return ` ${validate_component(Login_page, "LoginFormSkeleton").$$render($$result, {}, {}, {})} `;
    }
    return function(Module) {
      return ` ${validate_component(Module.default || missing_component, "svelte:component").$$render($$result, {}, {}, {})} `;
    }(__value);
  }(current_page)}`;
});
export {
  Page as default
};
