import { c as create_ssr_component, k as createEventDispatcher, l as each, e as escape, v as validate_component, a as add_attribute } from "./ssr.js";
import { T as Tick } from "./tick.js";
import "./ProgressBar.svelte_svelte_type_style_lang.js";
import { c as createForm } from "./create-form.js";
const _3 = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { pages_state } = $$props;
  const core_color_mapping = {
    c: "text-surface-50",
    e: "text-surface-50",
    o: "text-warning-400",
    r: "text-surface-50"
  };
  const dispatch = createEventDispatcher();
  createForm({
    onSubmit: (values) => {
      dispatch("submit", values);
    }
  });
  const combined_object = Object.assign({}, ...pages_state);
  if ($$props.pages_state === void 0 && $$bindings.pages_state && pages_state !== void 0)
    $$bindings.pages_state(pages_state);
  return `<form class="flex h-max w-full flex-col bg-surface-900 px-10 py-14 md:h-full md:justify-between md:rounded-none md:p-0"><div class="flex flex-col items-start gap-[3vw]"><span class="flex items-center pb-3 text-base font-bold uppercase tracking-widest text-white md:text-[1.2vw]">welcome to 
            <p class="inline-flex items-center text-surface-50">${each("core".split(""), (item) => {
    return `<span${add_attribute("class", core_color_mapping[item], 0)}>${escape(item)}</span>`;
  })}</p>
            project</span> <user-info class="flex flex-col"><span class="text-lg font-semibold text-primary-500 md:text-[1.5vw]" data-svelte-h="svelte-4li0if">Summary</span> <username class="flex flex-col pt-5"><span class="text-lg font-medium md:text-[1.1vw]" data-svelte-h="svelte-1wi1uev">Username</span> <span class="text-base font-medium text-surface-300 md:text-[1.1vw]">${escape(combined_object.username)}</span></username> <email class="flex flex-col pt-3"><span class="text-lg font-medium md:text-[1.1vw]" data-svelte-h="svelte-1dy9i0j">Email</span> <span class="text-base font-medium text-surface-300 md:text-[1.1vw]">${escape(combined_object.email)}</span></email></user-info> <div class="flex flex-col items-start"><button type="button" class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"><!-- HTML_TAG_START -->${`< resend code >`}<!-- HTML_TAG_END --></button> <button type="button" class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"><!-- HTML_TAG_START -->${`< change email >`}<!-- HTML_TAG_END --></button></div></div> <div class="mt-10 flex items-center justify-between md:mt-0"><div class="flex flex-col gap-1 md:gap-0" data-svelte-h="svelte-mswqy1"><span class="text-xs text-surface-100 md:text-[0.75vw]">Already have an account?</span> <a href="./login" class="text-base md:text-[1.1vw]">Login</a></div> <button type="submit" class="btn h-12 rounded-lg bg-secondary-800 p-0 px-5 text-base font-semibold md:h-[2.75vw] md:rounded-[0.5vw] md:px-[1.25vw] md:text-[0.95vw]"><span data-svelte-h="svelte-8wouzp">Finish</span> ${validate_component(Tick, "Tick").$$render($$result, { class: "w-3 md:w-[0.75vw]" }, {}, {})}</button></div></form>`;
});
export {
  _3 as default
};
