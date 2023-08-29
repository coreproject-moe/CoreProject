import { c as create_ssr_component, b as spread, d as escape_object } from "./ssr.js";
const Search = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props),
      { fill: "none" },
      { viewBox: "0 0 36 36" }
    ],
    {}
  )}><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="6" d="M16.5 28.5C23.1274 28.5 28.5 23.1274 28.5 16.5C28.5 9.87258 23.1274 4.5 16.5 4.5C9.87258 4.5 4.5 9.87258 4.5 16.5C4.5 23.1274 9.87258 28.5 16.5 28.5Z"></path><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="6" d="M31.5001 31.5001L24.9751 24.9751"></path></svg>`;
});
export {
  Search as S
};
