import { r as get_store_value, c as create_ssr_component, j as subscribe, g as getContext, t as getAllContexts, s as setContext, o as onDestroy, a as add_attribute, f as compute_slots, v as validate_component } from "../../../../chunks/ssr.js";
import * as React from "react";
import { w as writable } from "../../../../chunks/index.js";
import React$$ReactDOM from "react-dom/client";
import { createPortal } from "react-dom";
import { renderToString } from "react-dom/server";
import { API } from "@stoplight/elements";
function useStore(store) {
  const [value, setValue] = React.useState(() => get_store_value(store));
  React.useEffect(() => {
    let first = true;
    const cancel = store.subscribe((next) => {
      if (first) {
        first = false;
        if (next === value) {
          return;
        }
      }
      setValue(next);
    });
    return cancel;
  }, [store]);
  return value;
}
const SvelteWrapper_svelte_svelte_type_style_lang = "";
const SvelteToReactContext = React.createContext(void 0);
SvelteToReactContext.displayName = "SvelteToReactContext";
const ReactWrapper_svelte_svelte_type_style_lang = "";
const css = {
  code: "react-portal-target.svelte-1rt0kpf{display:contents}svelte-slot.svelte-1rt0kpf{display:none}",
  map: null
};
function extractProps(values) {
  const { svelteInit: excluded, ...rest } = values;
  return rest;
}
const ReactWrapper = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $$slots = compute_slots(slots);
  let $target, $$unsubscribe_target;
  let $slot, $$unsubscribe_slot;
  let { svelteInit } = $$props;
  const props = writable(extractProps($$props));
  const target2 = writable();
  $$unsubscribe_target = subscribe(target2, (value) => $target = value);
  const slot = writable();
  $$unsubscribe_slot = subscribe(slot, (value) => $slot = value);
  const hooks = writable([]);
  const listeners = [];
  const parent = getContext("ReactWrapper");
  const node = svelteInit({
    parent,
    props,
    target: target2,
    slot,
    hooks,
    contexts: getAllContexts(),
    onDestroy(callback) {
      listeners.push(callback);
    }
  });
  setContext("ReactWrapper", node);
  onDestroy(() => {
    listeners.forEach((callback) => callback());
  });
  if ($$props.svelteInit === void 0 && $$bindings.svelteInit && svelteInit !== void 0)
    $$bindings.svelteInit(svelteInit);
  $$result.css.add(css);
  $$unsubscribe_target();
  $$unsubscribe_slot();
  return `<react-portal-target class="svelte-1rt0kpf"${add_attribute("this", $target, 0)}></react-portal-target> ${$$slots.default ? `<svelte-slot class="svelte-1rt0kpf"${add_attribute("this", $slot, 0)}>${slots.default ? slots.default({}) : ``}</svelte-slot>` : ``}`;
});
const Slot = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `${slots.default ? slots.default({}) : ``}`;
});
const Child = ({ el }) => {
  const ref = React.useRef();
  React.useEffect(() => {
    if (!ref.current) {
      return;
    }
    if (el) {
      el.style.display = "contents";
      ref.current.appendChild(el);
    }
  }, [ref, el]);
  return React.createElement("react-child", {
    ref,
    style: { display: "contents" }
  });
};
const Bridge = ({ createPortal: createPortal2, node }) => {
  const target2 = useStore(node.target);
  let props = useStore(node.props);
  const slot = useStore(node.slot);
  const hooks = useStore(node.hooks);
  if (!target2) {
    return null;
  }
  let children;
  if (node.nodes.length === 0 && slot === void 0 && hooks.length === 0) {
    if (props.children) {
      children = props.children;
      props = { ...props };
      delete props.children;
    }
  } else {
    children = node.nodes.map((subnode) => React.createElement(Bridge, {
      key: `bridge${subnode.key}`,
      createPortal: createPortal2,
      node: subnode
    }));
    if (props.children) {
      children.push(props.children);
      props = { ...props };
      delete props.children;
    }
    if (slot) {
      children.push(React.createElement(Child, { key: "svelte-slot", el: slot }));
    }
    if (hooks.length >= 0) {
      children.push(...hooks.map(({ Hook, key }) => React.createElement(Hook, { key: `hook${key}` })));
    }
  }
  return createPortal2(React.createElement(SvelteToReactContext.Provider, { value: node.contexts }, children === void 0 ? React.createElement(node.reactComponent, props) : React.createElement(node.reactComponent, props, children)), target2);
};
let rerender;
let autokey = 0;
const never = writable();
const target = writable();
const tree = {
  key: autokey,
  svelteInstance: never,
  reactComponent: ({ children }) => children,
  target,
  props: writable({}),
  slot: never,
  nodes: [],
  contexts: /* @__PURE__ */ new Map(),
  hooks: writable([])
};
let current;
function sveltify(reactComponent, createPortal2, ReactDOMClient, renderToString2) {
  const Wrapper = ReactWrapper;
  const ssr = typeof Wrapper.$$render === "function";
  if (ssr) {
    const { $$render } = Slot;
    return {
      ...Slot,
      $$render(result, props, bindings, slots, context) {
        if (!renderToString2) {
          return "";
        }
        if (current !== void 0) {
          current.push({ reactComponent, props });
          return `<ssr-portal${current.length - 1}/>`;
        }
        current = [];
        try {
          const contexts = getAllContexts();
          const html = $$render.call(Slot, result, {}, bindings, slots, context);
          const leaf = !slots.default && current.length === 0;
          const vdom = leaf ? React.createElement(reactComponent, props) : React.createElement(reactComponent, props, [
            React.createElement("svelte-slot", {
              key: "svelte-slot",
              style: { display: "contents" },
              dangerouslySetInnerHTML: { __html: html }
            }),
            ...current.map((child, i) => React.createElement(`ssr-portal${i}`, { key: `ssr-portal${i}` }, React.createElement(child.reactComponent, child.props)))
          ]);
          let rendered = renderToString2(React.createElement(SvelteToReactContext.Provider, {
            value: context || contexts
          }, vdom));
          current.forEach((_, i) => {
            const start = `<ssr-portal${i}>`;
            const end = `</ssr-portal${i}>`;
            const startPosition = rendered.indexOf(start);
            const endPosition = rendered.indexOf(end);
            let content = "";
            if (startPosition !== -1) {
              content = rendered.substring(startPosition + start.length, endPosition);
              rendered = rendered.substring(0, startPosition) + rendered.substring(endPosition + end.length);
            }
            rendered = rendered.replace(`<ssr-portal${i}/>`, content);
          });
          return rendered;
        } finally {
          current = void 0;
        }
      }
    };
  }
  if (!rerender) {
    const rootEl = document.createElement("react-root");
    const root = ReactDOMClient.createRoot?.(rootEl);
    const targetEl = document.createElement("bridge-root");
    target.set(targetEl);
    document.head.appendChild(rootEl);
    document.head.appendChild(targetEl);
    if (root) {
      rerender = (props) => {
        root.render(React.createElement(Bridge, props));
      };
    } else {
      rerender = (props) => {
        ReactDOMClient.render(React.createElement(Bridge, props), rootEl);
      };
    }
  }
  function Sveltified(options) {
    const svelteInstance = writable();
    const instance = new ReactWrapper({
      ...options,
      props: {
        svelteInit(init) {
          autokey += 1;
          const node = {
            key: autokey,
            svelteInstance,
            reactComponent,
            props: init.props,
            slot: init.slot,
            target: init.target,
            hooks: init.hooks,
            contexts: init.contexts,
            nodes: []
          };
          const parent = init.parent ?? tree;
          parent.nodes.push(node);
          rerender({ createPortal: createPortal2, node: tree });
          init.onDestroy(() => {
            parent.nodes = parent.nodes.filter((n) => n.svelteInstance !== svelteInstance);
            rerender({ createPortal: createPortal2, node: tree });
          });
          return node;
        },
        ...options.props
      }
    });
    svelteInstance.set(instance);
    return instance;
  }
  return Sveltified;
}
const styles_min = "";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const React$API = sveltify(API, createPortal, React$$ReactDOM, renderToString);
  return `${validate_component(React$API, "React$API").$$render($$result, { apiDescriptionUrl: "/openapi/schema.yml" }, {}, {})}`;
});
export {
  Page as default
};
