import { c as create_ssr_component, a as add_attribute, v as validate_component, e as escape } from "./ssr.js";
const Image = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { src } = $$props;
  let { alt } = $$props;
  let { style } = $$props;
  let { class: klass } = $$props;
  if ($$props.src === void 0 && $$bindings.src && src !== void 0)
    $$bindings.src(src);
  if ($$props.alt === void 0 && $$bindings.alt && alt !== void 0)
    $$bindings.alt(alt);
  if ($$props.style === void 0 && $$bindings.style && style !== void 0)
    $$bindings.style(style);
  if ($$props.class === void 0 && $$bindings.class && klass !== void 0)
    $$bindings.class(klass);
  return `<img${add_attribute("class", klass, 0)}${add_attribute("src", src, 0)}${add_attribute("alt", alt, 0)}${add_attribute("style", style, 0)} loading="lazy">`;
});
const Intersection_observer = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { once = false } = $$props;
  let intersecting = false;
  let container;
  if ($$props.once === void 0 && $$bindings.once && once !== void 0)
    $$bindings.once(once);
  return `<div class="h-full"${add_attribute("this", container, 0)}>${slots.default ? slots.default({ intersecting }) : ``}</div>`;
});
const Image_loader = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { src } = $$props;
  let { alt = "" } = $$props;
  let { style = "" } = $$props;
  let { class: klass = "" } = $$props;
  if ($$props.src === void 0 && $$bindings.src && src !== void 0)
    $$bindings.src(src);
  if ($$props.alt === void 0 && $$bindings.alt && alt !== void 0)
    $$bindings.alt(alt);
  if ($$props.style === void 0 && $$bindings.style && style !== void 0)
    $$bindings.style(style);
  if ($$props.class === void 0 && $$bindings.class && klass !== void 0)
    $$bindings.class(klass);
  return `${validate_component(Intersection_observer, "IntersectionObserver").$$render($$result, { once: true }, {}, {
    default: ({ intersecting }) => {
      return `${intersecting ? `${validate_component(Image, "Image").$$render($$result, { class: klass, src, alt, style }, {}, {})}` : `<div class="${"placeholder animate-pulse !bg-surface-400 " + escape(klass, true)}"></div>`}`;
    }
  })}`;
});
export {
  Image_loader as I
};
