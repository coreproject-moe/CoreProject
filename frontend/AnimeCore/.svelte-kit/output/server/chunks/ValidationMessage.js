import { c as create_ssr_component, a as add_attribute, f as compute_slots } from "./ssr.js";
const ValidationMessage = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let messages;
  let $$slots = compute_slots(slots);
  let { level = "error" } = $$props;
  let { for: errorFor } = $$props;
  let errorPath;
  let element;
  if ($$props.level === void 0 && $$bindings.level && level !== void 0)
    $$bindings.level(level);
  if ($$props.for === void 0 && $$bindings.for && errorFor !== void 0)
    $$bindings.for(errorFor);
  messages = errorPath;
  return `<div style="display: none;"${add_attribute("this", element, 0)}></div> ${!$$slots.placeholder || messages ? `${slots.default ? slots.default({ messages }) : ``}` : `${slots.placeholder ? slots.placeholder({}) : ``}`}`;
});
const ValidationMessage$1 = ValidationMessage;
export {
  ValidationMessage$1 as V
};
