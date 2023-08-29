import { c as create_ssr_component, k as createEventDispatcher, v as validate_component } from "./ssr.js";
import { I as Info, A as Arrow_up_right } from "./arrow_up_right.js";
import { r as reporter } from "./reporter.js";
import { V as ValidationMessage } from "./ValidationMessage.js";
import { validator } from "@felte/validator-zod";
import "./ProgressBar.svelte_svelte_type_style_lang.js";
import { z } from "zod";
import { c as createForm } from "./create-form.js";
const _2 = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const dispatch = createEventDispatcher();
  const schema = z.object({ username: z.string(), otp: z.string() });
  createForm({
    initialValues: { username: "", otp: "" },
    onSubmit: async (values) => {
      dispatch("submit", values);
    },
    extend: [reporter, validator({ schema })]
  });
  return `<form class="flex h-max w-full flex-col bg-surface-900 p-10 pb-[10vw] pt-[7vw] md:h-full md:justify-between md:rounded-none md:p-0"><div class="flex flex-col items-start gap-[1.5vw]"><form-title data-svelte-h="svelte-do5bw9"><span class="text-base font-bold uppercase tracking-widest md:text-[1.2vw]">choose your username and verify</span></form-title> <username-field class="mt-[4vw] w-full"><label for="username" class="text-lg font-semibold md:text-[1.1vw]" data-svelte-h="svelte-1ow9yif">Username</label> <input name="username" placeholder="choose any username" class="mt-[0.25vw] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"> ${validate_component(ValidationMessage, "ValidationMessage").$$render($$result, { for: "username" }, {}, {
    placeholder: () => {
      return `<div slot="placeholder"><info class="mt-[0.75vw] flex items-start gap-2 md:mt-[0.5vw]">${validate_component(Info, "Info").$$render($$result, { class: "w-3 opacity-70 md:w-[0.9vw]" }, {}, {})} <span class="text-xs text-surface-300 md:text-[0.75vw]" data-svelte-h="svelte-59kgxl">you can change username in your user settings later, so go bonkers!</span></info></div>`;
    },
    default: ({ messages: message }) => {
      return `<span class="mt-[0.75vw] text-xs text-surface-300 md:mt-[0.5vw] md:text-[0.75vw]"><!-- HTML_TAG_START -->${message}<!-- HTML_TAG_END --></span>`;
    }
  })}</username-field> <otp-field class="mt-2 w-full md:mt-0"><label for="otp" class="text-lg font-semibold md:text-[1.1vw]" data-svelte-h="svelte-4z4k3h">One Time Verification Code</label> <input name="otp" placeholder="enter the code" class="mt-[0.25vw] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"> ${validate_component(ValidationMessage, "ValidationMessage").$$render($$result, { for: "otp" }, {}, {
    placeholder: () => {
      return `<div slot="placeholder"><info class="mt-[0.75vw] flex items-start gap-2 md:mt-[0.5vw]">${validate_component(Info, "Info").$$render($$result, { class: "w-3 opacity-70 md:w-[0.9vw]" }, {}, {})} <span class="text-xs text-surface-300 md:text-[0.75vw]" data-svelte-h="svelte-1m99buu">if you didn’t receive the code, check your spam folder. Or use the resend button</span></info></div>`;
    },
    default: ({ messages: message }) => {
      return `<span class="mt-[0.75vw] text-xs text-surface-300 md:mt-[0.5vw] md:text-[0.75vw]"><!-- HTML_TAG_START -->${message}<!-- HTML_TAG_END --></span>`;
    }
  })}</otp-field> <div class="mt-3 flex flex-col items-start md:mt-0"><button type="button" class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"><!-- HTML_TAG_START -->${`< resend code >`}<!-- HTML_TAG_END --></button> <button type="button" class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"><!-- HTML_TAG_START -->${`< change email >`}<!-- HTML_TAG_END --></button></div></div> <div class="mt-10 flex items-center justify-between md:mt-0"><div class="flex flex-col gap-1 md:gap-0" data-svelte-h="svelte-mswqy1"><span class="text-xs text-surface-100 md:text-[0.75vw]">Already have an account?</span> <a href="./login" class="text-base md:text-[1.1vw]">Login</a></div> <button type="submit" class="btn h-12 rounded-lg bg-secondary-800 p-0 px-5 text-base font-semibold md:h-[2.75vw] md:rounded-[0.5vw] md:px-[1.25vw] md:text-[0.95vw]"><span data-svelte-h="svelte-1fjw2ub">Continue</span> ${validate_component(Arrow_up_right, "ArrowUpRight").$$render($$result, { class: "w-4 rotate-45 md:w-[1vw]" }, {}, {})}</button></div></form>`;
});
export {
  _2 as default
};
