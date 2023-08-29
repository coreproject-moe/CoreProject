import { c as create_ssr_component, a as add_attribute, e as escape, b as spread, d as escape_object, s as setContext, g as getContext, f as compute_slots, h as compute_rest_props, i as escape_attribute_value, j as subscribe, k as createEventDispatcher, v as validate_component, m as missing_component, l as each } from "../../chunks/ssr.js";
import { p as page } from "../../chunks/stores.js";
/* empty css                                                      */import { S as Search } from "../../chunks/search.js";
import { w as writable, d as derived } from "../../chunks/index.js";
import { p as prefersReducedMotionStore, l as localStorageStore } from "../../chunks/ProgressBar.svelte_svelte_type_style_lang.js";
import { f as fly } from "../../chunks/index2.js";
import { F as Forum } from "../../chunks/forum.js";
import NProgress from "nprogress";
function client_method(key) {
  {
    if (key === "before_navigate" || key === "after_navigate") {
      return () => {
      };
    } else {
      const name_lookup = {
        disable_scroll_handling: "disableScrollHandling",
        preload_data: "preloadData",
        preload_code: "preloadCode",
        invalidate_all: "invalidateAll"
      };
      return () => {
        throw new Error(`Cannot call ${name_lookup[key] ?? key}(...) on the server`);
      };
    }
  }
}
const beforeNavigate = /* @__PURE__ */ client_method("before_navigate");
const afterNavigate = /* @__PURE__ */ client_method("after_navigate");
const Vercel_hover = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { glider_container_class = "" } = $$props;
  let { active_element_class = "" } = $$props;
  let { direction } = $$props;
  let hover_glider_element, glider_container_element, GLIDER_TRANSITION_DURATION = 200, is_hovered = false, mouse_leave_timeout = null;
  const handle_mouseenter = (event) => {
    const target = event.target;
    const target_computed_style = getComputedStyle(target);
    glider_container_element.style.position = "relative";
    hover_glider_element.style.height = target_computed_style.height;
    hover_glider_element.style.width = target_computed_style.width;
    const target_zindex = parseInt(target_computed_style.zIndex);
    hover_glider_element.style.zIndex = String(target_zindex ? target_zindex - 1 : -1);
    switch (direction) {
      case "vertical":
        hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;
        break;
      case "horizontal":
        hover_glider_element.style.transform = `translateX(${target.offsetLeft}px)`;
        break;
    }
    if (!is_hovered) {
      GLIDER_TRANSITION_DURATION = 50;
      hover_glider_element.style.opacity = "100";
      is_hovered = true;
    } else {
      GLIDER_TRANSITION_DURATION = 200;
    }
    clearTimeout(mouse_leave_timeout);
  };
  const handle_mouseleave = () => {
    mouse_leave_timeout = setTimeout(
      () => {
        hover_glider_element.style.opacity = "0";
        is_hovered = false;
      },
      GLIDER_TRANSITION_DURATION
    );
  };
  if ($$props.glider_container_class === void 0 && $$bindings.glider_container_class && glider_container_class !== void 0)
    $$bindings.glider_container_class(glider_container_class);
  if ($$props.active_element_class === void 0 && $$bindings.active_element_class && active_element_class !== void 0)
    $$bindings.active_element_class(active_element_class);
  if ($$props.direction === void 0 && $$bindings.direction && direction !== void 0)
    $$bindings.direction(direction);
  return `<glider-container${add_attribute("class", glider_container_class, 0)}${add_attribute("this", glider_container_element, 0)}><active_glider class="${escape(active_element_class, true) + " absolute opacity-0 ease-in-out duration-" + escape(GLIDER_TRANSITION_DURATION, true)}"${add_attribute("this", hover_glider_element, 0)}></active_glider> ${slots.default ? slots.default({ handle_mouseleave, handle_mouseenter }) : ``}</glider-container>`;
});
const List = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 26 24" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><g filter="url(#filter0_d_1011_784)"><path d="M9.6665 5H20.4998" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.6665 10H20.4998" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.6665 15H20.4998" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.5 5H5.50833" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.5 10H5.50833" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.5 15H5.50833" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><filter id="filter0_d_1011_784" x="-1" y="0" width="28" height="28" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></feColorMatrix><feOffset dy="4"></feOffset><feGaussianBlur stdDeviation="2"></feGaussianBlur><feComposite in2="hardAlpha" operator="out"></feComposite><feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"></feColorMatrix><feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_1011_784"></feBlend><feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_1011_784" result="shape"></feBlend></filter></defs></svg>`;
});
const DRAWER_STORE_KEY = "drawerStore";
function initializeDrawerStore() {
  const drawerStore = drawerService();
  return setContext(DRAWER_STORE_KEY, drawerStore);
}
function drawerService() {
  const { subscribe: subscribe2, set, update } = writable({});
  return {
    subscribe: subscribe2,
    set,
    update,
    /** Open the drawer. */
    open: (newSettings) => update(() => {
      return { open: true, ...newSettings };
    }),
    /** Close the drawer. */
    close: () => update((d) => {
      d.open = false;
      return d;
    })
  };
}
const MODAL_STORE_KEY = "modalStore";
function getModalStore() {
  const modalStore = getContext(MODAL_STORE_KEY);
  if (!modalStore)
    throw new Error("modalStore is not initialized. Please ensure that `initializeStores()` is invoked in the root layout file of this app!");
  return modalStore;
}
function initializeModalStore() {
  const modalStore = modalService();
  return setContext(MODAL_STORE_KEY, modalStore);
}
function modalService() {
  const { subscribe: subscribe2, set, update } = writable([]);
  return {
    subscribe: subscribe2,
    set,
    update,
    /** Append to end of queue. */
    trigger: (modal) => update((mStore) => {
      mStore.push(modal);
      return mStore;
    }),
    /**  Remove first item in queue. */
    close: () => update((mStore) => {
      if (mStore.length > 0)
        mStore.shift();
      return mStore;
    }),
    /** Remove all items from queue. */
    clear: () => set([])
  };
}
const toastDefaults = { message: "Missing Toast Message", autohide: true, timeout: 5e3 };
const TOAST_STORE_KEY = "toastStore";
function initializeToastStore() {
  const toastStore = toastService();
  return setContext(TOAST_STORE_KEY, toastStore);
}
function randomUUID() {
  const random = Math.random();
  return Number(random).toString(32);
}
function toastService() {
  const { subscribe: subscribe2, set, update } = writable([]);
  const close = (id) => update((tStore) => {
    if (tStore.length > 0) {
      const index = tStore.findIndex((t) => t.id === id);
      const selectedToast = tStore[index];
      if (selectedToast) {
        if (selectedToast.callback)
          selectedToast.callback({ id, status: "closed" });
        if (selectedToast.timeoutId)
          clearTimeout(selectedToast.timeoutId);
        tStore.splice(index, 1);
      }
    }
    return tStore;
  });
  function handleAutoHide(toast) {
    if (toast.autohide === true) {
      return setTimeout(() => {
        close(toast.id);
      }, toast.timeout);
    }
  }
  return {
    subscribe: subscribe2,
    close,
    /** Add a new toast to the queue. */
    trigger: (toast) => {
      const id = randomUUID();
      update((tStore) => {
        if (toast && toast.callback)
          toast.callback({ id, status: "queued" });
        if (toast.hideDismiss)
          toast.autohide = true;
        const tMerged = { ...toastDefaults, ...toast, id };
        tMerged.timeoutId = handleAutoHide(tMerged);
        tStore.push(tMerged);
        return tStore;
      });
      return id;
    },
    /** Remain visible on hover */
    freeze: (index) => update((tStore) => {
      if (tStore.length > 0)
        clearTimeout(tStore[index].timeoutId);
      return tStore;
    }),
    /** Cancel remain visible on leave */
    unfreeze: (index) => update((tStore) => {
      if (tStore.length > 0)
        tStore[index].timeoutId = handleAutoHide(tStore[index]);
      return tStore;
    }),
    /** Remove all toasts from queue */
    clear: () => set([])
  };
}
function initializeStores() {
  initializeModalStore();
  initializeToastStore();
  initializeDrawerStore();
}
const cBaseAppShell = "w-full h-full flex flex-col overflow-hidden";
const cContentArea = "w-full h-full flex overflow-hidden";
const cPage = "flex-1 overflow-x-hidden flex flex-col";
const cSidebarLeft = "flex-none overflow-x-hidden overflow-y-auto";
const cSidebarRight = "flex-none overflow-x-hidden overflow-y-auto";
const AppShell = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let classesBase;
  let classesHeader;
  let classesSidebarLeft;
  let classesSidebarRight;
  let classesPageHeader;
  let classesPageContent;
  let classesPageFooter;
  let classesFooter;
  let $$slots = compute_slots(slots);
  let { regionPage = "" } = $$props;
  let { slotHeader = "z-10" } = $$props;
  let { slotSidebarLeft = "w-auto" } = $$props;
  let { slotSidebarRight = "w-auto" } = $$props;
  let { slotPageHeader = "" } = $$props;
  let { slotPageContent = "" } = $$props;
  let { slotPageFooter = "" } = $$props;
  let { slotFooter = "" } = $$props;
  if ($$props.regionPage === void 0 && $$bindings.regionPage && regionPage !== void 0)
    $$bindings.regionPage(regionPage);
  if ($$props.slotHeader === void 0 && $$bindings.slotHeader && slotHeader !== void 0)
    $$bindings.slotHeader(slotHeader);
  if ($$props.slotSidebarLeft === void 0 && $$bindings.slotSidebarLeft && slotSidebarLeft !== void 0)
    $$bindings.slotSidebarLeft(slotSidebarLeft);
  if ($$props.slotSidebarRight === void 0 && $$bindings.slotSidebarRight && slotSidebarRight !== void 0)
    $$bindings.slotSidebarRight(slotSidebarRight);
  if ($$props.slotPageHeader === void 0 && $$bindings.slotPageHeader && slotPageHeader !== void 0)
    $$bindings.slotPageHeader(slotPageHeader);
  if ($$props.slotPageContent === void 0 && $$bindings.slotPageContent && slotPageContent !== void 0)
    $$bindings.slotPageContent(slotPageContent);
  if ($$props.slotPageFooter === void 0 && $$bindings.slotPageFooter && slotPageFooter !== void 0)
    $$bindings.slotPageFooter(slotPageFooter);
  if ($$props.slotFooter === void 0 && $$bindings.slotFooter && slotFooter !== void 0)
    $$bindings.slotFooter(slotFooter);
  classesBase = `${cBaseAppShell} ${$$props.class ?? ""}`;
  classesHeader = `${slotHeader}`;
  classesSidebarLeft = `${cSidebarLeft} ${slotSidebarLeft}`;
  classesSidebarRight = `${cSidebarRight} ${slotSidebarRight}`;
  classesPageHeader = `${slotPageHeader}`;
  classesPageContent = `${slotPageContent}`;
  classesPageFooter = `${slotPageFooter}`;
  classesFooter = `${slotFooter}`;
  return `<div id="appShell"${add_attribute("class", classesBase, 0)} data-testid="app-shell"> ${$$slots.header ? `<header id="shell-header" class="${"flex-none " + escape(classesHeader, true)}">${slots.header ? slots.header({}) : ``}</header>` : ``}  <div class="${"flex-auto " + escape(cContentArea, true)}"> ${$$slots.sidebarLeft ? `<aside id="sidebar-left"${add_attribute("class", classesSidebarLeft, 0)}>${slots.sidebarLeft ? slots.sidebarLeft({}) : ``}</aside>` : ``}  <div id="page" class="${escape(regionPage, true) + " " + escape(cPage, true)}"> ${$$slots.pageHeader ? `<header id="page-header" class="${"flex-none " + escape(classesPageHeader, true)}">${slots.pageHeader ? slots.pageHeader({}) : `(slot:header)`}</header>` : ``}  <main id="page-content" class="${"flex-auto " + escape(classesPageContent, true)}">${slots.default ? slots.default({}) : ``}</main>  ${$$slots.pageFooter ? `<footer id="page-footer" class="${"flex-none " + escape(classesPageFooter, true)}">${slots.pageFooter ? slots.pageFooter({}) : `(slot:footer)`}</footer>` : ``}</div>  ${$$slots.sidebarRight ? `<aside id="sidebar-right"${add_attribute("class", classesSidebarRight, 0)}>${slots.sidebarRight ? slots.sidebarRight({}) : ``}</aside>` : ``}</div>  ${$$slots.footer ? `<footer id="shell-footer" class="${"flex-none " + escape(classesFooter, true)}">${slots.footer ? slots.footer({}) : ``}</footer>` : ``}</div>`;
});
let cBase = "flex aspect-square text-surface-50 font-semibold justify-center items-center overflow-hidden isolate";
let cImage = "w-full h-full object-cover";
const Avatar = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let classesBase;
  let $$restProps = compute_rest_props($$props, [
    "initials",
    "fill",
    "src",
    "fallback",
    "action",
    "actionParams",
    "background",
    "width",
    "border",
    "rounded",
    "shadow",
    "cursor"
  ]);
  let { initials = "AB" } = $$props;
  let { fill = "fill-token" } = $$props;
  let { src = "" } = $$props;
  let { fallback = "" } = $$props;
  let { action = () => {
  } } = $$props;
  let { actionParams = "" } = $$props;
  let { background = "bg-surface-400-500-token" } = $$props;
  let { width = "w-16" } = $$props;
  let { border = "" } = $$props;
  let { rounded = "rounded-full" } = $$props;
  let { shadow = "" } = $$props;
  let { cursor = "" } = $$props;
  function prunedRestProps() {
    delete $$restProps.class;
    return $$restProps;
  }
  if ($$props.initials === void 0 && $$bindings.initials && initials !== void 0)
    $$bindings.initials(initials);
  if ($$props.fill === void 0 && $$bindings.fill && fill !== void 0)
    $$bindings.fill(fill);
  if ($$props.src === void 0 && $$bindings.src && src !== void 0)
    $$bindings.src(src);
  if ($$props.fallback === void 0 && $$bindings.fallback && fallback !== void 0)
    $$bindings.fallback(fallback);
  if ($$props.action === void 0 && $$bindings.action && action !== void 0)
    $$bindings.action(action);
  if ($$props.actionParams === void 0 && $$bindings.actionParams && actionParams !== void 0)
    $$bindings.actionParams(actionParams);
  if ($$props.background === void 0 && $$bindings.background && background !== void 0)
    $$bindings.background(background);
  if ($$props.width === void 0 && $$bindings.width && width !== void 0)
    $$bindings.width(width);
  if ($$props.border === void 0 && $$bindings.border && border !== void 0)
    $$bindings.border(border);
  if ($$props.rounded === void 0 && $$bindings.rounded && rounded !== void 0)
    $$bindings.rounded(rounded);
  if ($$props.shadow === void 0 && $$bindings.shadow && shadow !== void 0)
    $$bindings.shadow(shadow);
  if ($$props.cursor === void 0 && $$bindings.cursor && cursor !== void 0)
    $$bindings.cursor(cursor);
  classesBase = `${cBase} ${background} ${width} ${border} ${rounded} ${shadow} ${cursor} ${$$props.class ?? ""}`;
  return `  <figure class="${"avatar " + escape(classesBase, true)}" data-testid="avatar">${src ? `<img${spread(
    [
      {
        class: "avatar-image " + escape(cImage, true)
      },
      {
        style: escape_attribute_value($$props.style ?? "")
      },
      { src: escape_attribute_value(src) },
      {
        alt: escape_attribute_value($$props.alt || "")
      },
      escape_object(prunedRestProps())
    ],
    {}
  )}>` : `<svg class="avatar-initials w-full h-full" viewBox="0 0 512 512"><text x="50%" y="50%" dominant-baseline="central" text-anchor="middle" font-weight="bold"${add_attribute("font-size", 150, 0)} class="${"avatar-text " + escape(fill, true)}">${escape(String(initials).substring(0, 2).toUpperCase())}</text></svg>`}</figure>`;
});
const cBackdrop = "fixed top-0 left-0 right-0 bottom-0 overflow-y-auto";
const cTransitionLayer = "w-full h-fit min-h-full p-4 overflow-y-auto flex justify-center";
const cModal = "block overflow-y-auto";
const cModalImage = "w-full h-auto";
const Modal = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let cPosition;
  let classesBackdrop;
  let classesTransitionLayer;
  let classesModal;
  let parent;
  let $modalStore, $$unsubscribe_modalStore;
  let $prefersReducedMotionStore, $$unsubscribe_prefersReducedMotionStore;
  $$unsubscribe_prefersReducedMotionStore = subscribe(prefersReducedMotionStore, (value) => $prefersReducedMotionStore = value);
  createEventDispatcher();
  let { position = "items-center" } = $$props;
  let { components = {} } = $$props;
  let { background = "bg-surface-100-800-token" } = $$props;
  let { width = "w-modal" } = $$props;
  let { height = "h-auto" } = $$props;
  let { padding = "p-4" } = $$props;
  let { spacing = "space-y-4" } = $$props;
  let { rounded = "rounded-container-token" } = $$props;
  let { shadow = "shadow-xl" } = $$props;
  let { zIndex = "z-[999]" } = $$props;
  let { buttonNeutral = "variant-ghost-surface" } = $$props;
  let { buttonPositive = "variant-filled" } = $$props;
  let { buttonTextCancel = "Cancel" } = $$props;
  let { buttonTextConfirm = "Confirm" } = $$props;
  let { buttonTextSubmit = "Submit" } = $$props;
  let { regionBackdrop = "bg-surface-backdrop-token" } = $$props;
  let { regionHeader = "text-2xl font-bold" } = $$props;
  let { regionBody = "max-h-[200px] overflow-hidden" } = $$props;
  let { regionFooter = "flex justify-end space-x-2" } = $$props;
  let { transitions = !$prefersReducedMotionStore } = $$props;
  let { transitionIn = fly } = $$props;
  let { transitionInParams = { duration: 150, opacity: 0, x: 0, y: 100 } } = $$props;
  let { transitionOut = fly } = $$props;
  let { transitionOutParams = { duration: 150, opacity: 0, x: 0, y: 100 } } = $$props;
  let promptValue;
  const buttonTextDefaults = {
    buttonTextCancel,
    buttonTextConfirm,
    buttonTextSubmit
  };
  let currentComponent;
  const modalStore = getModalStore();
  $$unsubscribe_modalStore = subscribe(modalStore, (value) => $modalStore = value);
  modalStore.subscribe((modals) => {
    if (!modals.length)
      return;
    if (modals[0].type === "prompt")
      promptValue = modals[0].value;
    buttonTextCancel = modals[0].buttonTextCancel || buttonTextDefaults.buttonTextCancel;
    buttonTextConfirm = modals[0].buttonTextConfirm || buttonTextDefaults.buttonTextConfirm;
    buttonTextSubmit = modals[0].buttonTextSubmit || buttonTextDefaults.buttonTextSubmit;
    currentComponent = typeof modals[0].component === "string" ? components[modals[0].component] : modals[0].component;
  });
  function onClose() {
    if ($modalStore[0].response)
      $modalStore[0].response(false);
    modalStore.close();
  }
  if ($$props.position === void 0 && $$bindings.position && position !== void 0)
    $$bindings.position(position);
  if ($$props.components === void 0 && $$bindings.components && components !== void 0)
    $$bindings.components(components);
  if ($$props.background === void 0 && $$bindings.background && background !== void 0)
    $$bindings.background(background);
  if ($$props.width === void 0 && $$bindings.width && width !== void 0)
    $$bindings.width(width);
  if ($$props.height === void 0 && $$bindings.height && height !== void 0)
    $$bindings.height(height);
  if ($$props.padding === void 0 && $$bindings.padding && padding !== void 0)
    $$bindings.padding(padding);
  if ($$props.spacing === void 0 && $$bindings.spacing && spacing !== void 0)
    $$bindings.spacing(spacing);
  if ($$props.rounded === void 0 && $$bindings.rounded && rounded !== void 0)
    $$bindings.rounded(rounded);
  if ($$props.shadow === void 0 && $$bindings.shadow && shadow !== void 0)
    $$bindings.shadow(shadow);
  if ($$props.zIndex === void 0 && $$bindings.zIndex && zIndex !== void 0)
    $$bindings.zIndex(zIndex);
  if ($$props.buttonNeutral === void 0 && $$bindings.buttonNeutral && buttonNeutral !== void 0)
    $$bindings.buttonNeutral(buttonNeutral);
  if ($$props.buttonPositive === void 0 && $$bindings.buttonPositive && buttonPositive !== void 0)
    $$bindings.buttonPositive(buttonPositive);
  if ($$props.buttonTextCancel === void 0 && $$bindings.buttonTextCancel && buttonTextCancel !== void 0)
    $$bindings.buttonTextCancel(buttonTextCancel);
  if ($$props.buttonTextConfirm === void 0 && $$bindings.buttonTextConfirm && buttonTextConfirm !== void 0)
    $$bindings.buttonTextConfirm(buttonTextConfirm);
  if ($$props.buttonTextSubmit === void 0 && $$bindings.buttonTextSubmit && buttonTextSubmit !== void 0)
    $$bindings.buttonTextSubmit(buttonTextSubmit);
  if ($$props.regionBackdrop === void 0 && $$bindings.regionBackdrop && regionBackdrop !== void 0)
    $$bindings.regionBackdrop(regionBackdrop);
  if ($$props.regionHeader === void 0 && $$bindings.regionHeader && regionHeader !== void 0)
    $$bindings.regionHeader(regionHeader);
  if ($$props.regionBody === void 0 && $$bindings.regionBody && regionBody !== void 0)
    $$bindings.regionBody(regionBody);
  if ($$props.regionFooter === void 0 && $$bindings.regionFooter && regionFooter !== void 0)
    $$bindings.regionFooter(regionFooter);
  if ($$props.transitions === void 0 && $$bindings.transitions && transitions !== void 0)
    $$bindings.transitions(transitions);
  if ($$props.transitionIn === void 0 && $$bindings.transitionIn && transitionIn !== void 0)
    $$bindings.transitionIn(transitionIn);
  if ($$props.transitionInParams === void 0 && $$bindings.transitionInParams && transitionInParams !== void 0)
    $$bindings.transitionInParams(transitionInParams);
  if ($$props.transitionOut === void 0 && $$bindings.transitionOut && transitionOut !== void 0)
    $$bindings.transitionOut(transitionOut);
  if ($$props.transitionOutParams === void 0 && $$bindings.transitionOutParams && transitionOutParams !== void 0)
    $$bindings.transitionOutParams(transitionOutParams);
  cPosition = $modalStore[0]?.position ?? position;
  classesBackdrop = `${cBackdrop} ${regionBackdrop} ${zIndex} ${$$props.class ?? ""} ${$modalStore[0]?.backdropClasses ?? ""}`;
  classesTransitionLayer = `${cTransitionLayer} ${cPosition ?? ""}`;
  classesModal = `${cModal} ${background} ${width} ${height} ${padding} ${spacing} ${rounded} ${shadow} ${$modalStore[0]?.modalClasses ?? ""}`;
  parent = {
    position,
    // ---
    background,
    width,
    height,
    padding,
    spacing,
    rounded,
    shadow,
    // ---
    buttonNeutral,
    buttonPositive,
    buttonTextCancel,
    buttonTextConfirm,
    buttonTextSubmit,
    // ---
    regionBackdrop,
    regionHeader,
    regionBody,
    regionFooter,
    // ---
    onClose
  };
  $$unsubscribe_modalStore();
  $$unsubscribe_prefersReducedMotionStore();
  return ` ${$modalStore.length > 0 ? `   <div class="${"modal-backdrop " + escape(classesBackdrop, true)}" data-testid="modal-backdrop"> <div class="${"modal-transition " + escape(classesTransitionLayer, true)}">${$modalStore[0].type !== "component" ? ` <div class="${"modal " + escape(classesModal, true)}" data-testid="modal" role="dialog" aria-modal="true"${add_attribute("aria-label", $modalStore[0].title ?? "", 0)}> ${$modalStore[0]?.title ? `<header class="${"modal-header " + escape(regionHeader, true)}"><!-- HTML_TAG_START -->${$modalStore[0].title}<!-- HTML_TAG_END --></header>` : ``}  ${$modalStore[0]?.body ? `<article class="${"modal-body " + escape(regionBody, true)}"><!-- HTML_TAG_START -->${$modalStore[0].body}<!-- HTML_TAG_END --></article>` : ``}  ${$modalStore[0]?.image && typeof $modalStore[0]?.image === "string" ? `<img class="${"modal-image " + escape(cModalImage, true)}"${add_attribute("src", $modalStore[0]?.image, 0)} alt="Modal">` : ``}  ${$modalStore[0].type === "alert" ? ` <footer class="${"modal-footer " + escape(regionFooter, true)}"><button type="button" class="${"btn " + escape(buttonNeutral, true)}">${escape(buttonTextCancel)}</button></footer>` : `${$modalStore[0].type === "confirm" ? ` <footer class="${"modal-footer " + escape(regionFooter, true)}"><button type="button" class="${"btn " + escape(buttonNeutral, true)}">${escape(buttonTextCancel)}</button> <button type="button" class="${"btn " + escape(buttonPositive, true)}">${escape(buttonTextConfirm)}</button></footer>` : `${$modalStore[0].type === "prompt" ? ` <form class="space-y-4"><input${spread(
    [
      { class: "modal-prompt-input input" },
      { name: "prompt" },
      { type: "text" },
      escape_object($modalStore[0].valueAttr)
    ],
    {}
  )}${add_attribute("value", promptValue, 0)}> <footer class="${"modal-footer " + escape(regionFooter, true)}"><button type="button" class="${"btn " + escape(buttonNeutral, true)}">${escape(buttonTextCancel)}</button> <button type="submit" class="${"btn " + escape(buttonPositive, true)}">${escape(buttonTextSubmit)}</button></footer></form>` : ``}`}`}</div>` : `  <div class="${"modal contents " + escape($modalStore[0]?.modalClasses ?? "", true)}" data-testid="modal-component" role="dialog" aria-modal="true"${add_attribute("aria-label", $modalStore[0].title ?? "", 0)}>${validate_component(currentComponent?.ref || missing_component, "svelte:component").$$render($$result, Object.assign({}, currentComponent?.props, { parent }), {}, {
    default: () => {
      return `${currentComponent?.slot ? `<!-- HTML_TAG_START -->${currentComponent?.slot}<!-- HTML_TAG_END -->` : ``}`;
    }
  })}</div>`}</div></div>` : ``}`;
});
const profile_dropdown_svelte_svelte_type_style_lang = "";
const Anime_core = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 140 28" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><g filter="url(#filter0_d_3571_5637)"><path d="M14.912 19.7753C15.4643 19.7753 15.912 19.3276 15.912 18.7753V13.427C15.912 8.37079 13.2925 6.51685 10.1766 6.51685C8.54377 6.51685 7.26248 6.92613 6.29359 7.42579C5.85055 7.65427 5.70348 8.19993 5.91771 8.65003L6.40075 9.66494C6.65214 10.1931 7.29841 10.3837 7.84132 10.1659C8.41308 9.93651 9.05315 9.77528 9.73542 9.77528C10.733 9.77528 11.4202 10.0223 11.8373 10.5105C12.2928 11.0436 11.6016 11.6438 10.9076 11.5435C7.3015 11.0223 4 12.5648 4 15.6461C4 18.0056 5.7096 20 8.7979 20C9.95425 20 10.8941 19.6377 11.6638 19.0664C11.943 18.8592 12.3825 19.0424 12.3825 19.3902C12.3825 19.6029 12.555 19.7753 12.7677 19.7753H14.912ZM11.5398 14.2884C12.0279 14.3998 12.3302 14.8999 12.1186 15.3535C11.5785 16.5115 10.4543 17.191 9.45968 17.191C8.38429 17.191 7.52949 16.6292 7.52949 15.6461C7.52949 14.3635 9.20927 13.7564 11.5398 14.2884Z" fill="white"></path><path d="M25.6155 6.51685C24.4216 6.51685 23.5936 6.88973 23.0037 7.36581C22.75 7.57049 22.3066 7.40819 22.3066 7.08226C22.3066 6.8941 22.1541 6.74157 21.966 6.74157H19.7772C19.2249 6.74157 18.7772 7.18929 18.7772 7.74157V18.7753C18.7772 19.3276 19.2249 19.7753 19.7772 19.7753H21.3066C21.8589 19.7753 22.3066 19.3276 22.3066 18.7753V13.0337C22.3066 10.7303 23.7129 9.88764 24.7332 9.88764C25.8086 9.88764 27.1597 10.3652 27.1597 12.5843V18.7753C27.1597 19.3276 27.6074 19.7753 28.1597 19.7753H29.6892C30.2415 19.7753 30.6892 19.3276 30.6892 18.7753V12.5843C30.6892 8.37079 28.4005 6.51685 25.6155 6.51685Z" fill="white"></path><path d="M35.3253 4.49438C36.5386 4.49438 37.5312 3.48315 37.5312 2.24719C37.5312 1.01124 36.5386 0 35.3253 0C34.112 0 33.1194 1.01124 33.1194 2.24719C33.1194 3.48315 34.112 4.49438 35.3253 4.49438ZM33.5606 18.7753C33.5606 19.3276 34.0083 19.7753 34.5606 19.7753H36.09C36.6423 19.7753 37.09 19.3276 37.09 18.7753V7.74157C37.09 7.18929 36.6423 6.74157 36.09 6.74157H34.5606C34.0083 6.74157 33.5606 7.18929 33.5606 7.74157V18.7753Z" fill="white"></path><path d="M54.6285 6.51685C53.5715 6.51685 52.6695 6.78012 51.896 7.3517C51.3429 7.7604 50.5058 7.73059 49.9607 7.31138C49.2753 6.78436 48.4389 6.51685 47.4592 6.51685C46.3412 6.51685 45.4329 6.77991 44.6357 7.40664C44.3698 7.61568 43.9297 7.44431 43.9297 7.10608C43.9297 6.90477 43.7665 6.74157 43.5652 6.74157H41.4002C40.848 6.74157 40.4002 7.18929 40.4002 7.74157V18.7753C40.4002 19.3276 40.848 19.7753 41.4002 19.7753H42.9297C43.482 19.7753 43.9297 19.3276 43.9297 18.7753V13.0337C43.9297 10.5056 45.336 9.88764 46.246 9.88764C47.2111 9.88764 48.3416 10.3652 48.3416 12.5843V18.7753C48.3416 19.3276 48.7893 19.7753 49.3416 19.7753H50.8711C51.4234 19.7753 51.8711 19.3276 51.8711 18.7753V13.0337C51.8711 10.5056 53.1946 9.88764 54.077 9.88764C55.0421 9.88764 56.283 10.3652 56.283 12.5843V18.7753C56.283 19.3276 56.7307 19.7753 57.283 19.7753H58.8124C59.3647 19.7753 59.8124 19.3276 59.8124 18.7753V12.5843C59.8124 8.37079 57.6341 6.51685 54.6285 6.51685Z" fill="white"></path><path d="M68.9507 16.6292C68.8747 16.6292 68.8005 16.6278 68.7279 16.6248C67.9796 16.5947 67.9171 15.738 68.5539 15.3436L74.1963 11.8494C74.5694 11.6183 74.7547 11.1683 74.6061 10.7554C73.4093 7.42917 70.5231 6.51685 68.8955 6.51685C64.6215 6.51685 62.0296 9.55056 62.0296 13.2584C62.0296 16.9382 64.6767 20 68.8955 20C70.5646 20 72.0332 19.4896 73.3015 18.4862C73.6872 18.181 73.7319 17.6261 73.4472 17.2251L72.7952 16.307C72.4226 15.7823 71.6482 15.7465 71.088 16.0632C70.4335 16.4331 69.6751 16.6292 68.9507 16.6292ZM68.9507 9.88764C69.2575 9.88764 69.5318 9.93725 69.7767 10.0254C70.3622 10.236 70.2528 10.9949 69.7186 11.3138L66.0515 13.503C65.8439 13.6269 65.5591 13.5002 65.5591 13.2584C65.5591 11.4045 66.9653 9.88764 68.9507 9.88764Z" fill="white"></path><path d="M86.5607 15.7303C84.7408 15.7303 83.3621 14.2978 83.3621 12.5843C83.3621 10.8708 84.7408 9.4382 86.5607 9.4382C87.1144 9.4382 87.6253 9.56931 88.0788 9.8169C88.6442 10.1255 89.4129 10.1255 89.8001 9.61075L90.8071 8.27213C91.0953 7.88912 91.0761 7.34898 90.715 7.03375C89.496 5.96944 87.9686 5.39326 86.3401 5.39326C81.7352 5.39326 78.9502 8.59551 78.9502 12.5843C78.9502 16.573 81.7352 19.7753 86.3401 19.7753C87.9686 19.7753 89.496 19.1991 90.715 18.1348C91.0761 17.8196 91.0953 17.2794 90.8071 16.8964L89.8001 15.5578C89.4129 15.043 88.6442 15.043 88.0788 15.3516C87.6253 15.5992 87.1144 15.7303 86.5607 15.7303Z" fill="#DCD9F7"></path><path d="M100.561 5.39326C96.066 5.39326 93.0604 8.59551 93.0604 12.5843C93.0604 16.573 96.1488 19.7753 100.561 19.7753C104.807 19.7753 108.061 16.573 108.061 12.5843C108.061 8.59551 104.752 5.39326 100.561 5.39326ZM100.561 15.7303C98.8786 15.7303 97.4723 14.2978 97.4723 12.5843C97.4723 10.8708 98.8786 9.4382 100.561 9.4382C102.243 9.4382 103.649 10.8708 103.649 12.5843C103.649 14.2978 102.243 15.7303 100.561 15.7303Z" fill="#F2C94C"></path><path d="M115.131 6.8427C115.131 6.29041 114.683 5.8427 114.131 5.8427H111.719C111.167 5.8427 110.719 6.29041 110.719 6.8427V18.3258C110.719 18.8781 111.167 19.3258 111.719 19.3258H114.131C114.683 19.3258 115.131 18.8781 115.131 18.3258V14.3539C115.131 12.1348 116.261 10.7022 117.557 10.3371C117.928 10.2329 118.293 10.171 118.663 10.1597C119.331 10.1394 119.984 9.66674 119.984 8.99851V6.47469C119.984 5.89161 119.485 5.42411 118.911 5.52776C117.05 5.86387 115.902 6.69947 115.131 8.3427V6.8427Z" fill="#DCD9F7"></path><path d="M128.748 15.8427C128.103 15.8427 128.032 15.1573 128.583 14.8215L134.586 11.1607C134.953 10.9371 135.141 10.501 135.015 10.0904C133.821 6.19781 130.713 5.39326 128.913 5.39326C124.308 5.39326 121.523 8.59551 121.523 12.5843C121.523 16.573 124.308 19.7753 128.913 19.7753C130.729 19.7753 132.323 19.2 133.661 18.1372C134.054 17.825 134.092 17.2562 133.79 16.8551L132.73 15.4464C132.371 14.969 131.676 14.9193 131.155 15.2125C130.465 15.6013 129.638 15.8427 128.748 15.8427ZM128.913 9.32584C129.17 9.32584 129.393 9.36917 129.585 9.44089C130.102 9.63369 129.966 10.2878 129.494 10.5741L127.063 12.0513C126.45 12.4236 125.66 12.021 125.892 11.3424C126.319 10.0924 127.548 9.32584 128.913 9.32584Z" fill="#DCD9F7"></path><circle cx="35.1998" cy="2.4" r="2.4" fill="#EDD68D"></circle></g><defs><filter id="filter0_d_3571_5637" x="0" y="0" width="139.054" height="28" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></feColorMatrix><feOffset dy="4"></feOffset><feGaussianBlur stdDeviation="2"></feGaussianBlur><feComposite in2="hardAlpha" operator="out"></feComposite><feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"></feColorMatrix><feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_3571_5637"></feBlend><feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_3571_5637" result="shape"></feBlend></filter></defs></svg>`;
});
const Explore = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 4.48 20 10 20C15.52 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM10 18C5.59 18 2 14.41 2 10C2 5.59 5.59 2 10 2C14.41 2 18 5.59 18 10C18 14.41 14.41 18 10 18ZM5.65317 13.0185C5.26027 13.864 6.13598 14.7397 6.98146 14.3468L11.3472 12.318C11.7752 12.1191 12.1191 11.7752 12.318 11.3472L14.3468 6.98146C14.7397 6.13599 13.864 5.26026 13.0185 5.65317L8.65283 7.68197C8.22479 7.88089 7.88089 8.22479 7.68197 8.65283L5.65317 13.0185ZM10 8.9C10.61 8.9 11.1 9.39 11.1 10C11.1 10.61 10.61 11.1 10 11.1C9.39 11.1 8.9 10.61 8.9 10C8.9 9.39 9.39 8.9 10 8.9Z" fill="currentColor"></path></svg>`;
});
const Home = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 17" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M7.99961 16V12C7.99961 11.4477 8.44733 11 8.99961 11H10.9996C11.5519 11 11.9996 11.4477 11.9996 12V16C11.9996 16.55 12.4496 17 12.9996 17H15.9996C16.5496 17 16.9996 16.55 16.9996 16V9.99997C16.9996 9.44769 17.4473 8.99997 17.9996 8.99997H18.6996C19.1596 8.99997 19.3796 8.42997 19.0296 8.12997L10.6696 0.599971C10.2896 0.259971 9.70961 0.259971 9.32961 0.599971L0.96961 8.12997C0.62961 8.42997 0.83961 8.99997 1.29961 8.99997H1.99961C2.55189 8.99997 2.99961 9.44769 2.99961 9.99997V16C2.99961 16.55 3.44961 17 3.99961 17H6.99961C7.54961 17 7.99961 16.55 7.99961 16Z" fill="currentColor"></path></svg>`;
});
const Logo = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 28 40" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><g filter="url(#filter0_d_3565_5702)"><path fill-rule="evenodd" clip-rule="evenodd" d="M14 31.9999C19.5228 31.9999 24 27.5536 24 22.0689C24 16.5841 19.5228 12.1378 14 12.1378C8.47715 12.1378 4 16.5841 4 22.0689C4 27.5536 8.47715 31.9999 14 31.9999ZM13.9991 26.4828C16.4537 26.4828 18.4436 24.5067 18.4436 22.069C18.4436 19.6313 16.4537 17.6552 13.9991 17.6552C11.5445 17.6552 9.55469 19.6313 9.55469 22.069C9.55469 24.5067 11.5445 26.4828 13.9991 26.4828Z" fill="#7569E1"></path><ellipse cx="13.9993" cy="3.31035" rx="3.33333" ry="3.31035" fill="#DCD9F7"></ellipse></g><defs><filter id="filter0_d_3565_5702" x="0" y="0" width="28" height="39.9999" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></feColorMatrix><feOffset dy="4"></feOffset><feGaussianBlur stdDeviation="2"></feGaussianBlur><feComposite in2="hardAlpha" operator="out"></feComposite><feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"></feColorMatrix><feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_3565_5702"></feBlend><feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_3565_5702" result="shape"></feBlend></filter></defs></svg>`;
});
const Misc = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 18 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M9.00033 0.666656C4.40033 0.666656 0.666992 4.39999 0.666992 8.99999C0.666992 13.6 4.40033 17.3333 9.00033 17.3333C13.6003 17.3333 17.3337 13.6 17.3337 8.99999C17.3337 4.39999 13.6003 0.666656 9.00033 0.666656ZM9.00033 15.6667C5.32533 15.6667 2.33366 12.675 2.33366 8.99999C2.33366 5.32499 5.32533 2.33332 9.00033 2.33332C12.6753 2.33332 15.667 5.32499 15.667 8.99999C15.667 12.675 12.6753 15.6667 9.00033 15.6667ZM8.16699 12.3333H9.83366V14H8.16699V12.3333ZM9.50866 4.03332C7.79199 3.78332 6.27533 4.84166 5.81699 6.35832C5.66699 6.84166 6.03366 7.33332 6.54199 7.33332H6.70866C7.05033 7.33332 7.32533 7.09166 7.44199 6.77499C7.70866 6.03332 8.50033 5.52499 9.35866 5.70832C10.1503 5.87499 10.7337 6.64999 10.667 7.45832C10.5837 8.57499 9.31699 8.81666 8.62533 9.85832C8.62533 9.86666 8.61699 9.86666 8.61699 9.87499C8.60866 9.89166 8.60033 9.89999 8.59199 9.91666C8.51699 10.0417 8.44199 10.1833 8.38366 10.3333C8.37533 10.3583 8.35866 10.375 8.35033 10.4C8.34199 10.4167 8.34199 10.4333 8.33366 10.4583C8.23366 10.7417 8.16699 11.0833 8.16699 11.5H9.83366C9.83366 11.15 9.92533 10.8583 10.067 10.6083C10.0837 10.5833 10.092 10.5583 10.1087 10.5333C10.1753 10.4167 10.2587 10.3083 10.342 10.2083C10.3503 10.2 10.3587 10.1833 10.367 10.175C10.4503 10.075 10.542 9.98332 10.642 9.89166C11.442 9.13332 12.5253 8.51666 12.3003 6.92499C12.1003 5.47499 10.9587 4.24999 9.50866 4.03332Z" fill="white"></path></svg>`;
});
const Schedule = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 18 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M15.667 2.49998H15.3337C15.0575 2.49998 14.8337 2.27612 14.8337 1.99998V1.66665C14.8337 1.20831 14.4587 0.833313 14.0003 0.833313C13.542 0.833313 13.167 1.20831 13.167 1.66665V1.99998C13.167 2.27612 12.9431 2.49998 12.667 2.49998H5.33366C5.05752 2.49998 4.83366 2.27612 4.83366 1.99998V1.66665C4.83366 1.20831 4.45866 0.833313 4.00033 0.833313C3.54199 0.833313 3.16699 1.20831 3.16699 1.66665V1.99998C3.16699 2.27612 2.94313 2.49998 2.66699 2.49998H2.33366C1.41699 2.49998 0.666992 3.24998 0.666992 4.16665V17.5C0.666992 18.4166 1.41699 19.1666 2.33366 19.1666H15.667C16.5837 19.1666 17.3337 18.4166 17.3337 17.5V4.16665C17.3337 3.24998 16.5837 2.49998 15.667 2.49998ZM14.8337 17.5H3.16699C2.70866 17.5 2.33366 17.125 2.33366 16.6666V6.66665H15.667V16.6666C15.667 17.125 15.292 17.5 14.8337 17.5Z" fill="currentColor"></path></svg>`;
});
const Settings = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><g clip-path="url(#clip0_3607_1064)"><path d="M16.4153 10.9913C16.2768 10.883 16.2068 10.71 16.2233 10.5349C16.2398 10.3606 16.2504 10.1838 16.2504 9.99999C16.2504 9.81617 16.2398 9.63937 16.2233 9.46504C16.2068 9.28999 16.2768 9.11702 16.4153 9.00871L17.9504 7.80832C18.1087 7.68332 18.1504 7.45832 18.0504 7.27499L16.3837 4.39166C16.2837 4.20832 16.0587 4.14166 15.8754 4.20832L14.0653 4.93527C13.9011 5.0012 13.7152 4.9742 13.5704 4.87252C13.2804 4.66886 12.9757 4.49056 12.654 4.33992C12.4935 4.26476 12.3766 4.11725 12.3514 3.9418L12.0754 2.01666C12.0504 1.81666 11.8754 1.66666 11.667 1.66666H8.33369C8.12535 1.66666 7.95035 1.81666 7.92535 2.01666L7.6493 3.9418C7.62414 4.11725 7.50721 4.26472 7.34696 4.34043C7.02442 4.49282 6.71902 4.6747 6.42844 4.87679C6.28498 4.97656 6.10133 5.00189 5.93918 4.93677L4.12535 4.20832C3.93369 4.13332 3.71702 4.20832 3.61702 4.39166L1.95035 7.27499C1.84202 7.45832 1.89202 7.68332 2.05035 7.80832L3.58539 9.00871C3.7239 9.11702 3.794 9.29 3.77756 9.46506C3.76096 9.64183 3.75035 9.82091 3.75035 9.99999C3.75035 10.1791 3.76096 10.3581 3.77756 10.5349C3.794 10.71 3.7239 10.883 3.58539 10.9913L2.05035 12.1917C1.89202 12.3167 1.85035 12.5417 1.95035 12.725L3.61702 15.6083C3.71702 15.7917 3.94202 15.8583 4.12535 15.7917L5.93544 15.0647C6.09961 14.9988 6.28554 15.0258 6.43031 15.1275C6.72026 15.3311 7.02496 15.5094 7.34672 15.6601C7.50725 15.7352 7.62414 15.8827 7.6493 16.0582L7.92535 17.9833C7.95035 18.1833 8.12535 18.3333 8.33369 18.3333H11.667C11.8754 18.3333 12.0504 18.1833 12.0754 17.9833L12.3514 16.0582C12.3766 15.8827 12.4935 15.7353 12.6538 15.6595C12.9763 15.5072 13.2817 15.3253 13.5723 15.1232C13.7157 15.0234 13.8994 14.9981 14.0615 15.0632L15.8754 15.7917C16.067 15.8667 16.2837 15.7917 16.3837 15.6083L18.0504 12.725C18.1504 12.5417 18.1087 12.3167 17.9504 12.1917L16.4153 10.9913ZM10.0004 12.9167C8.39202 12.9167 7.08369 11.6083 7.08369 9.99999C7.08369 8.39166 8.39202 7.08332 10.0004 7.08332C11.6087 7.08332 12.917 8.39166 12.917 9.99999C12.917 11.6083 11.6087 12.9167 10.0004 12.9167Z" fill="currentColor"></path></g><defs><clipPath id="clip0_3607_1064"><rect width="20" height="20" fill="currentColor"></rect></clipPath></defs></svg>`;
});
function get_logo_variant(pathname) {
  let logo_type;
  if (pathname.match(/user/gm)) {
    logo_type = "logo";
  } else {
    logo_type = "form";
  }
  return logo_type;
}
const navbar_middle_section_variant = derived(page, ($page) => get_logo_variant($page.url.pathname));
localStorageStore("theme", "kokoro");
const app = "";
const nprogress = "";
const tippy = "";
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  let $navbar_middle_section_variant, $$unsubscribe_navbar_middle_section_variant;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  $$unsubscribe_navbar_middle_section_variant = subscribe(navbar_middle_section_variant, (value) => $navbar_middle_section_variant = value);
  initializeStores();
  const icon_mapping = {
    top: {
      search: {
        icon: {
          component: Search,
          class: "w-[1.25vw] text-black"
        }
      }
    },
    middle: {
      home: {
        icon: {
          component: Home,
          class: "w-[1.25vw] text-white"
        },
        url: "/",
        show_on_mobile: true
      },
      explore: {
        icon: {
          component: Explore,
          class: "w-[1.25vw] text-white"
        },
        url: "/explore",
        show_on_mobile: true
      },
      list: {
        icon: {
          component: List,
          class: "w-[1.7vw] text-white"
        },
        url: "/list",
        show_on_mobile: false
      },
      schedule: {
        icon: {
          component: Schedule,
          class: "w-[1.25vw] text-white"
        },
        url: "/shedule",
        show_on_mobile: false
      },
      forum: {
        icon: {
          component: Forum,
          class: "w-[1.25vw] text-white"
        },
        url: "/forum",
        show_on_mobile: true
      }
    },
    bottom: {
      settings: {
        icon: {
          component: Settings,
          class: "w-[1.25vw] text-white"
        },
        url: void 0
      },
      "misc.": {
        icon: {
          component: Misc,
          class: "w-[1.25vw] text-white"
        },
        url: void 0
      }
    }
  };
  beforeNavigate(async function() {
    NProgress.start();
  });
  afterNavigate(async function() {
    NProgress.done();
  });
  getModalStore();
  $$unsubscribe_page();
  $$unsubscribe_navbar_middle_section_variant();
  return `<div class="relative h-[100dvh]">${validate_component(Modal, "Modal").$$render($$result, {}, {}, {})} ${validate_component(AppShell, "AppShell").$$render($$result, {}, {}, {
    footer: () => {
      return `<div class="flex h-24 items-center justify-center md:hidden"><div class="flex items-start justify-center gap-5">${each(Object.entries(icon_mapping.middle).filter(([_, value]) => value.show_on_mobile), (item) => {
        let item_name = item[0], item_icon = item[1].icon, item_href = item[1].url, component = item_icon.component, klass = "w-5", is_active = $page.url.pathname === item_href;
        return `      <a${add_attribute("href", item_href ?? "javascript:void(0)", 0)} type="button" class="flex flex-col items-center gap-[0.5vh]"><div class="${escape(is_active ? "bg-primary-500" : "bg-initial", true) + " btn btn-icon h-12 w-20 rounded-xl p-0"}"><div>${is_active ? `${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: klass }, {}, {})}` : `${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: klass }, {}, {})}`} </div></div> <span class="text-xs font-bold capitalize text-surface-50">${escape(item_name)}</span> </a>`;
      })}</div></div> `;
    },
    sidebarLeft: () => {
      return `<div class="hidden h-full w-[6.25vw] flex-col justify-between py-[2vw] md:flex"><div><div class="flex flex-col items-center gap-5">${each(Object.entries(icon_mapping.top), (item) => {
        let item_icon = item[1].icon;
        return ` <button type="button" class="btn btn-icon w-[2.5vw] rounded-[0.375vw] bg-warning-400 p-0">${validate_component(item_icon.component || missing_component, "svelte:component").$$render($$result, { class: item_icon.class }, {}, {})} </button>`;
      })}</div> ${validate_component(Vercel_hover, "VercelHover").$$render(
        $$result,
        {
          direction: "vertical",
          glider_container_class: "mt-[2.8125vw] flex flex-col items-center gap-[0.75vw]",
          active_element_class: "rounded-[0.75vw] bg-white/10"
        },
        {},
        {
          default: ({ handle_mouseenter, handle_mouseleave }) => {
            return `${each(Object.entries(icon_mapping.middle), (item) => {
              let item_name = item[0], item_icon = item[1].icon, item_href = item[1].url, component = item_icon.component, is_active = $page.url.pathname === item_href;
              return `     <a${add_attribute("href", item_href, 0)} type="button" class="${[
                escape(
                  is_active ? "relative bg-secondary-100 before:absolute before:-left-[0.15vw] before:z-10 before:h-[1.25vw] before:w-[0.25vw] before:rounded-full before:bg-primary-500" : "bg-initial",
                  true
                ) + " btn btn-icon relative w-[4vw] rounded-[0.75vw] p-0",
                !item_href ? "pointer-events-none" : ""
              ].join(" ").trim()}"><div class="inline-grid">${is_active ? `<div class="absolute inset-0 flex items-center justify-center">${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: "!text-black " + item_icon.class }, {}, {})} </div>` : `<div class="absolute inset-0 flex flex-col items-center justify-center gap-[0.35vw]">${validate_component(component || missing_component, "svelte:component").$$render($$result, { class: item_icon.class }, {}, {})} <span class="text-[0.75vw] font-semibold capitalize leading-[1.05vw]">${escape(item_name)}</span> </div>`}</div> </a>`;
            })}`;
          }
        }
      )}</div> <div class="flex flex-col-reverse items-center gap-[1vw]">${each(Object.entries(icon_mapping.bottom), (item) => {
        let item_name = item[0], item_icon = item[1].icon;
        return `  <button type="button" class="bg-initial btn btn-icon w-[3.375vw] flex-col justify-center gap-[0.45vw] p-0 text-sm">${validate_component(item_icon.component || missing_component, "svelte:component").$$render($$result, { class: item_icon.class }, {}, {})} <span class="!m-0 text-[0.75vw] font-semibold capitalize leading-[1.05vw]">${escape(item_name)}</span> </button>`;
      })}</div></div> `;
    },
    header: () => {
      return `<navbar class="absolute top-0 flex h-[4.5rem] w-full items-center justify-between bg-surface-900/95 px-4 backdrop-blur-3xl md:static md:h-[10vh] md:bg-surface-900 md:py-[0.9375vw] md:pl-[2.1vw] md:pr-[3.75vw]">${["form", "logo"].includes($navbar_middle_section_variant) ? `<a href="/">${validate_component(Logo, "Logo").$$render(
        $$result,
        {
          class: "w-9 md:w-[2.25vw] md:pt-[0.75vw]"
        },
        {},
        {}
      )}</a> <div class="relative flex items-center">${$navbar_middle_section_variant === "logo" ? `<a href="/" class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform">${validate_component(Anime_core, "AnimeCore").$$render($$result, { class: "w-36 md:w-[10vw]" }, {}, {})}</a>` : `${$navbar_middle_section_variant === "form" ? `<div class="absolute left-1/2 -translate-x-1/2"><a href="/" class="hidden md:flex">${validate_component(Anime_core, "AnimeCore").$$render($$result, { class: "w-[10vw]" }, {}, {})}</a> <search-form><form class="relative flex h-12 w-[65vw] items-center md:hidden"><button class="btn absolute left-4 p-0" aria-label="Search">${validate_component(Search, "Search").$$render($$result, { class: "w-5 opacity-75" }, {}, {})}</button> <input type="text" placeholder="Search for animes, mangas..." class="h-full w-full rounded-[0.4rem] border-none bg-surface-400 pl-12 text-sm font-semibold text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-200"></form></search-form></div>` : ``}`}</div> <button class="avatar" aria-label="Avatar">${validate_component(Avatar, "Avatar").$$render(
        $$result,
        {
          rounded: "rounded-[0.4rem] md:rounded-[0.375vw]",
          width: "w-12 md:w-[3.125vw]",
          src: "/images/Avatar.avif",
          initials: "JD"
        },
        {},
        {}
      )}</button>` : ``}</navbar> `;
    },
    default: () => {
      return `<div class="h-full">${slots.default ? slots.default({}) : ``}</div>`;
    }
  })}</div>`;
});
export {
  Layout as default
};
