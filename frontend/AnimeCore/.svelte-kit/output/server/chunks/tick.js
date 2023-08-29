import { c as create_ssr_component, b as spread, d as escape_object } from "./ssr.js";
const Tick = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 16 16" },
      { baseProfile: "basic" }
    ],
    {}
  )}><polygon fill="currentColor" points="5.857,14.844 0.172,9.032 3.031,6.235 5.888,9.156 12.984,2.06 15.812,4.888"></polygon></svg>`;
});
export {
  Tick as T
};
