import { c as create_ssr_component, b as spread, d as escape_object } from "./ssr.js";
const Chevron = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props),
      { fill: "none" },
      { viewBox: "0 0 24 24" }
    ],
    {}
  )}><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3.5" d="M6 9L12 15L18 9"></path></svg>`;
});
export {
  Chevron as C
};
