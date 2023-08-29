import { c as create_ssr_component, k as createEventDispatcher, j as subscribe, v as validate_component } from "../../../chunks/ssr.js";
import { p as page } from "../../../chunks/stores.js";
import { O as OpengraphGenerator } from "../../../chunks/opengraph.js";
import { r as reporter } from "../../../chunks/reporter.js";
import { validator } from "@felte/validator-zod";
import "../../../chunks/ProgressBar.svelte_svelte_type_style_lang.js";
import "lodash";
import { z } from "zod";
import { c as createForm } from "../../../chunks/create-form.js";
import "dayjs";
import "dayjs/plugin/localeData.js";
import "dayjs/plugin/relativeTime.js";
import "dayjs/plugin/utc.js";
import "pretty-bytes";
const Login = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const dispatch = createEventDispatcher();
  const schema = z.object({
    streamsb: z.string().min(20, "Please provide a valid API token")
  });
  createForm({
    initialValues: { streamsb: "" },
    onSubmit: async (values) => {
      dispatch("submit", values);
    },
    extend: [reporter, validator({ schema })]
  });
  return `${``}`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  const opengraph_html = new OpengraphGenerator({
    title: `Upload on AnimeCore`,
    url: $page.url.href,
    description: "Upload on animecore",
    site_name: "CoreProject",
    locale: "en_US",
    image_url: ""
  }).generate_opengraph();
  $$unsubscribe_page();
  return `${$$result.head += `<!-- HEAD_svelte-a9xomp_START --><!-- HTML_TAG_START -->${opengraph_html}<!-- HTML_TAG_END --><!-- HEAD_svelte-a9xomp_END -->`, ""} ${` ${validate_component(Login, "Login").$$render($$result, {}, {}, {})}`}`;
});
export {
  Page as default
};
