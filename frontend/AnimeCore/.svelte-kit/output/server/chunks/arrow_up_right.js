import { c as create_ssr_component, b as spread, d as escape_object } from "./ssr.js";
const Info = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 30 30" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M15 27.5C21.9036 27.5 27.5 21.9036 27.5 15C27.5 8.09644 21.9036 2.5 15 2.5C8.09644 2.5 2.5 8.09644 2.5 15C2.5 21.9036 8.09644 27.5 15 27.5Z" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 20V15" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 10H15.0125" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Arrow_up_right = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 16 16" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M4.66699 11.3333L11.3337 4.66666" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4.66699 4.66666H11.3337V11.3333" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
export {
  Arrow_up_right as A,
  Info as I
};
