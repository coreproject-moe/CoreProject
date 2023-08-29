import { c as create_ssr_component, e as escape, a as add_attribute, b as spread, d as escape_object } from "./ssr.js";
/* empty css                                           */const css = {
  code: "scroll-area.svelte-1paasz3{scrollbar-color:rgba(255, 255, 255, 0.12) transparent;transition:border-color 0.2s linear}scroll-area.svelte-1paasz3:hover{border-color:rgba(255, 255, 255, 0.15)}scroll-area.svelte-1paasz3::-webkit-scrollbar,scroll-area.svelte-1paasz3::-webkit-scrollbar-corner,scroll-area.svelte-1paasz3::-webkit-scrollbar-thumb{width:5px;border-radius:16px;border-right-style:inset;border-right-width:calc(100vw + 100vh);border-color:inherit}scroll-area.svelte-1paasz3::-webkit-scrollbar-track{background:transparent !important}scroll-area.mask-bottom.svelte-1paasz3{-webkit-mask-image:linear-gradient(180deg, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);mask-image:linear-gradient(180deg, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);-webkit-mask-position:bottom;mask-position:bottom}",
  map: null
};
const Scroll_area = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { class: klass = "" } = $$props;
  let { parentClass = "" } = $$props;
  let { offsetScrollbar = false } = $$props;
  let { gradientMask = false } = $$props;
  let scroll_area;
  let add_mask_bottom;
  if ($$props.class === void 0 && $$bindings.class && klass !== void 0)
    $$bindings.class(klass);
  if ($$props.parentClass === void 0 && $$bindings.parentClass && parentClass !== void 0)
    $$bindings.parentClass(parentClass);
  if ($$props.offsetScrollbar === void 0 && $$bindings.offsetScrollbar && offsetScrollbar !== void 0)
    $$bindings.offsetScrollbar(offsetScrollbar);
  if ($$props.gradientMask === void 0 && $$bindings.gradientMask && gradientMask !== void 0)
    $$bindings.gradientMask(gradientMask);
  $$result.css.add(css);
  add_mask_bottom = false;
  return `<scroll-area class="${[
    escape(parentClass, true) + " " + escape(offsetScrollbar && "pr-3 md:pr-[0.75vw]", true) + " block h-full w-full overflow-y-scroll overscroll-y-contain border-transparent scrollbar-thin svelte-1paasz3",
    gradientMask && add_mask_bottom ? "mask-bottom" : ""
  ].join(" ").trim()}"${add_attribute("this", scroll_area, 0)}><div><div class="${escape(klass, true) + " whitespace-pre-line"}">${slots.default ? slots.default({}) : ``}</div></div> </scroll-area>`;
});
const Circle = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 10 10" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><circle cx="5" cy="5" r="5" fill="currentColor"></circle></svg>`;
});
export {
  Circle as C,
  Scroll_area as S
};
