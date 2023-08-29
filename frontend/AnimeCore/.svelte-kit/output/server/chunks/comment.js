import { c as create_ssr_component, j as subscribe, s as setContext, e as escape, k as createEventDispatcher, g as getContext, a as add_attribute, f as compute_slots, b as spread, d as escape_object, v as validate_component, u as is_promise, n as noop, l as each, m as missing_component } from "./ssr.js";
import { F as FormatDate } from "./play_circle.js";
import { I as Image_loader } from "./image_loader.js";
import xss from "xss";
import { Marked } from "marked";
import { markedEmoji } from "marked-emoji";
import { markedHighlight } from "marked-highlight";
import { mangle } from "marked-mangle";
import { markedXhtml } from "marked-xhtml";
import { markedSmartypants } from "marked-smartypants";
import "caret-pos";
import hljs from "highlight.js";
import { p as prefersReducedMotionStore } from "./ProgressBar.svelte_svelte_type_style_lang.js";
import { w as writable } from "./index.js";
import { s as slide } from "./index2.js";
const Accordion = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let classesBase;
  let $prefersReducedMotionStore, $$unsubscribe_prefersReducedMotionStore;
  $$unsubscribe_prefersReducedMotionStore = subscribe(prefersReducedMotionStore, (value) => $prefersReducedMotionStore = value);
  let { autocollapse = false } = $$props;
  let { width = "w-full" } = $$props;
  let { spacing = "space-y-1" } = $$props;
  let { disabled = false } = $$props;
  let { padding = "py-2 px-4" } = $$props;
  let { hover = "hover:bg-primary-hover-token" } = $$props;
  let { rounded = "rounded-container-token" } = $$props;
  let { caretOpen = "rotate-180" } = $$props;
  let { caretClosed = "" } = $$props;
  let { regionControl = "" } = $$props;
  let { regionPanel = "space-y-4" } = $$props;
  let { regionCaret = "" } = $$props;
  let { transitions = !$prefersReducedMotionStore } = $$props;
  let { transitionIn = slide } = $$props;
  let { transitionInParams = { duration: 200 } } = $$props;
  let { transitionOut = slide } = $$props;
  let { transitionOutParams = { duration: 200 } } = $$props;
  const active = writable(null);
  setContext("active", active);
  setContext("autocollapse", autocollapse);
  setContext("disabled", disabled);
  setContext("padding", padding);
  setContext("hover", hover);
  setContext("rounded", rounded);
  setContext("caretOpen", caretOpen);
  setContext("caretClosed", caretClosed);
  setContext("regionControl", regionControl);
  setContext("regionPanel", regionPanel);
  setContext("regionCaret", regionCaret);
  setContext("transitions", transitions);
  setContext("transitionIn", transitionIn);
  setContext("transitionInParams", transitionInParams);
  setContext("transitionOut", transitionOut);
  setContext("transitionOutParams", transitionOutParams);
  if ($$props.autocollapse === void 0 && $$bindings.autocollapse && autocollapse !== void 0)
    $$bindings.autocollapse(autocollapse);
  if ($$props.width === void 0 && $$bindings.width && width !== void 0)
    $$bindings.width(width);
  if ($$props.spacing === void 0 && $$bindings.spacing && spacing !== void 0)
    $$bindings.spacing(spacing);
  if ($$props.disabled === void 0 && $$bindings.disabled && disabled !== void 0)
    $$bindings.disabled(disabled);
  if ($$props.padding === void 0 && $$bindings.padding && padding !== void 0)
    $$bindings.padding(padding);
  if ($$props.hover === void 0 && $$bindings.hover && hover !== void 0)
    $$bindings.hover(hover);
  if ($$props.rounded === void 0 && $$bindings.rounded && rounded !== void 0)
    $$bindings.rounded(rounded);
  if ($$props.caretOpen === void 0 && $$bindings.caretOpen && caretOpen !== void 0)
    $$bindings.caretOpen(caretOpen);
  if ($$props.caretClosed === void 0 && $$bindings.caretClosed && caretClosed !== void 0)
    $$bindings.caretClosed(caretClosed);
  if ($$props.regionControl === void 0 && $$bindings.regionControl && regionControl !== void 0)
    $$bindings.regionControl(regionControl);
  if ($$props.regionPanel === void 0 && $$bindings.regionPanel && regionPanel !== void 0)
    $$bindings.regionPanel(regionPanel);
  if ($$props.regionCaret === void 0 && $$bindings.regionCaret && regionCaret !== void 0)
    $$bindings.regionCaret(regionCaret);
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
  classesBase = `${width} ${spacing} ${$$props.class ?? ""}`;
  $$unsubscribe_prefersReducedMotionStore();
  return ` <div class="${"accordion " + escape(classesBase, true)}" data-testid="accordion">${slots.default ? slots.default({}) : ``}</div>`;
});
const cBase = "";
const cControl = "text-left w-full flex items-center space-x-4";
const cControlCaret = "fill-current w-3 transition-transform duration-[200ms]";
const cPanel = "";
const AccordionItem = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let openState;
  let classesBase;
  let classesControl;
  let classesCaretState;
  let classesControlCaret;
  let classesPanel;
  let $$slots = compute_slots(slots);
  let $active, $$unsubscribe_active;
  const dispatch = createEventDispatcher();
  let { open = false } = $$props;
  let { id = String(Math.random()) } = $$props;
  let { autocollapse = getContext("autocollapse") } = $$props;
  let { active = getContext("active") } = $$props;
  $$unsubscribe_active = subscribe(active, (value) => $active = value);
  let { disabled = getContext("disabled") } = $$props;
  let { padding = getContext("padding") } = $$props;
  let { hover = getContext("hover") } = $$props;
  let { rounded = getContext("rounded") } = $$props;
  let { caretOpen = getContext("caretOpen") } = $$props;
  let { caretClosed = getContext("caretClosed") } = $$props;
  let { regionControl = getContext("regionControl") } = $$props;
  let { regionPanel = getContext("regionPanel") } = $$props;
  let { regionCaret = getContext("regionCaret") } = $$props;
  let { transitions = getContext("transitions") } = $$props;
  let { transitionIn = getContext("transitionIn") } = $$props;
  let { transitionInParams = getContext("transitionInParams") } = $$props;
  let { transitionOut = getContext("transitionOut") } = $$props;
  let { transitionOutParams = getContext("transitionOutParams") } = $$props;
  function setActive(event) {
    if (autocollapse === true) {
      active.set(id);
    } else {
      open = !open;
    }
    onToggle(event);
  }
  function onToggle(event) {
    const currentOpenState = autocollapse ? $active === id : open;
    dispatch("toggle", {
      event,
      id: `accordion-control-${id}`,
      open: currentOpenState,
      autocollapse
    });
  }
  if (autocollapse && open)
    setActive();
  if ($$props.open === void 0 && $$bindings.open && open !== void 0)
    $$bindings.open(open);
  if ($$props.id === void 0 && $$bindings.id && id !== void 0)
    $$bindings.id(id);
  if ($$props.autocollapse === void 0 && $$bindings.autocollapse && autocollapse !== void 0)
    $$bindings.autocollapse(autocollapse);
  if ($$props.active === void 0 && $$bindings.active && active !== void 0)
    $$bindings.active(active);
  if ($$props.disabled === void 0 && $$bindings.disabled && disabled !== void 0)
    $$bindings.disabled(disabled);
  if ($$props.padding === void 0 && $$bindings.padding && padding !== void 0)
    $$bindings.padding(padding);
  if ($$props.hover === void 0 && $$bindings.hover && hover !== void 0)
    $$bindings.hover(hover);
  if ($$props.rounded === void 0 && $$bindings.rounded && rounded !== void 0)
    $$bindings.rounded(rounded);
  if ($$props.caretOpen === void 0 && $$bindings.caretOpen && caretOpen !== void 0)
    $$bindings.caretOpen(caretOpen);
  if ($$props.caretClosed === void 0 && $$bindings.caretClosed && caretClosed !== void 0)
    $$bindings.caretClosed(caretClosed);
  if ($$props.regionControl === void 0 && $$bindings.regionControl && regionControl !== void 0)
    $$bindings.regionControl(regionControl);
  if ($$props.regionPanel === void 0 && $$bindings.regionPanel && regionPanel !== void 0)
    $$bindings.regionPanel(regionPanel);
  if ($$props.regionCaret === void 0 && $$bindings.regionCaret && regionCaret !== void 0)
    $$bindings.regionCaret(regionCaret);
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
  {
    if (open && autocollapse)
      setActive();
  }
  openState = autocollapse ? $active === id : open;
  classesBase = `${cBase} ${$$props.class ?? ""}`;
  classesControl = `${cControl} ${padding} ${hover} ${rounded} ${regionControl}`;
  classesCaretState = openState ? caretOpen : caretClosed;
  classesControlCaret = `${cControlCaret} ${regionCaret} ${classesCaretState}`;
  classesPanel = `${cPanel} ${padding} ${rounded} ${regionPanel}`;
  $$unsubscribe_active();
  return ` <div class="${"accordion-item " + escape(classesBase, true)}" data-testid="accordion-item"> <button type="button" class="${"accordion-control " + escape(classesControl, true)}" id="${"accordion-control-" + escape(id, true)}"${add_attribute("aria-expanded", openState, 0)} aria-controls="${"accordion-panel-" + escape(id, true)}" ${disabled ? "disabled" : ""}> ${$$slots.lead ? `<div class="accordion-lead">${slots.lead ? slots.lead({}) : ``}</div>` : ``}  <div class="accordion-summary flex-1">${slots.summary ? slots.summary({}) : `(summary)`}</div>  <div class="${"accordion-summary-caret " + escape(classesControlCaret, true)}"> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M201.4 374.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 306.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg></div></button>  ${openState ? `<div class="${"accordion-panel " + escape(classesPanel, true)}" id="${"accordion-panel-" + escape(id, true)}" role="region"${add_attribute("aria-hidden", !openState, 0)} aria-labelledby="${"accordion-control-" + escape(id, true)}">${slots.content ? slots.content({}) : `(content)`}</div>` : ``}</div>`;
});
const Message_circle = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 20" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M17.5 9.58336C17.5029 10.6832 17.2459 11.7683 16.75 12.75C16.162 13.9265 15.2581 14.916 14.1395 15.6078C13.021 16.2995 11.7319 16.6662 10.4167 16.6667C9.31678 16.6696 8.23176 16.4126 7.25 15.9167L2.5 17.5L4.08333 12.75C3.58744 11.7683 3.33047 10.6832 3.33333 9.58336C3.33384 8.26815 3.70051 6.97907 4.39227 5.86048C5.08402 4.7419 6.07355 3.838 7.25 3.25002C8.23176 2.75413 9.31678 2.49716 10.4167 2.50002H10.8333C12.5703 2.59585 14.2109 3.32899 15.441 4.55907C16.671 5.78915 17.4042 7.42973 17.5 9.16669V9.58336Z" stroke="#DCD9F7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Forum_posts = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { link } = $$props;
  let { post_banner } = $$props;
  let { post_title } = $$props;
  let { post_description } = $$props;
  let { author } = $$props;
  let { posted_on_date } = $$props;
  let { responses } = $$props;
  if ($$props.link === void 0 && $$bindings.link && link !== void 0)
    $$bindings.link(link);
  if ($$props.post_banner === void 0 && $$bindings.post_banner && post_banner !== void 0)
    $$bindings.post_banner(post_banner);
  if ($$props.post_title === void 0 && $$bindings.post_title && post_title !== void 0)
    $$bindings.post_title(post_title);
  if ($$props.post_description === void 0 && $$bindings.post_description && post_description !== void 0)
    $$bindings.post_description(post_description);
  if ($$props.author === void 0 && $$bindings.author && author !== void 0)
    $$bindings.author(author);
  if ($$props.posted_on_date === void 0 && $$bindings.posted_on_date && posted_on_date !== void 0)
    $$bindings.posted_on_date(posted_on_date);
  if ($$props.responses === void 0 && $$bindings.responses && responses !== void 0)
    $$bindings.responses(responses);
  return `<a${add_attribute("href", link, 0)} class="card w-full grid-cols-7 overflow-hidden rounded-lg !bg-surface-400 md:grid md:rounded-[0.625vw]"><post-banner class="col-span-2 block h-16 md:h-full md:w-full">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: post_banner,
      alt: post_title,
      class: "h-full w-full object-cover object-center"
    },
    {},
    {}
  )}</post-banner> <post-container class="flex h-36 flex-col justify-between p-3 md:col-span-5 md:h-full md:gap-[0.375vw] md:p-[1vw]"><post-head><post-title class="line-clamp-2 text-xs font-extrabold md:text-[0.875vw] md:leading-[1.25vw]">${escape(post_title)}</post-title> <post-description class="mt-2 line-clamp-3 text-[0.6rem] font-medium leading-snug text-surface-50 md:mt-[0.5vw] md:line-clamp-2 md:text-[0.75vw] md:leading-[1.125vw]">${escape(post_description)}</post-description></post-head> <post-infos class="flex items-end justify-between text-[0.6rem] leading-none md:mt-[0.75vw] md:items-center md:text-[0.75vw]"><post-user-infos class="flex flex-col gap-1 md:flex-row md:items-center md:gap-[0.25vw]"><post-author-name>Posted by <span class="text-[0.65rem] font-semibold md:text-[0.85vw]">${escape(author)}</span></post-author-name> <post-uploaded-date class="text-surface-50">${escape(new FormatDate(posted_on_date).format_to_time_from_now)}</post-uploaded-date></post-user-infos> <post-responses class="flex items-center gap-1 md:gap-[0.25vw]">${validate_component(Message_circle, "MessageCircle").$$render($$result, { class: "w-3 md:w-[1vw]" }, {}, {})} <responses-text>${escape(responses)}</responses-text></post-responses></post-infos></post-container></a>`;
});
const emojis = {
  "100": "/emojis/100.avif",
  "1234": "/emojis/1234.avif",
  "+1": "/emojis/+1.avif",
  "-1": "/emojis/-1.avif",
  "1st_place_medal": "/emojis/1st_place_medal.avif",
  "2nd_place_medal": "/emojis/2nd_place_medal.avif",
  "3rd_place_medal": "/emojis/3rd_place_medal.avif",
  "8ball": "/emojis/8ball.avif",
  a: "/emojis/a.avif",
  ab: "/emojis/ab.avif",
  abacus: "/emojis/abacus.avif",
  abc: "/emojis/abc.avif",
  abcd: "/emojis/abcd.avif",
  accept: "/emojis/accept.avif",
  accessibility: "/emojis/accessibility.avif",
  accordion: "/emojis/accordion.avif",
  adhesive_bandage: "/emojis/adhesive_bandage.avif",
  adult: "/emojis/adult.avif",
  aerial_tramway: "/emojis/aerial_tramway.avif",
  afghanistan: "/emojis/afghanistan.avif",
  airplane: "/emojis/airplane.avif",
  aland_islands: "/emojis/aland_islands.avif",
  alarm_clock: "/emojis/alarm_clock.avif",
  albania: "/emojis/albania.avif",
  alembic: "/emojis/alembic.avif",
  algeria: "/emojis/algeria.avif",
  alien: "/emojis/alien.avif",
  ambulance: "/emojis/ambulance.avif",
  american_samoa: "/emojis/american_samoa.avif",
  amphora: "/emojis/amphora.avif",
  anatomical_heart: "/emojis/anatomical_heart.avif",
  anchor: "/emojis/anchor.avif",
  andorra: "/emojis/andorra.avif",
  angel: "/emojis/angel.avif",
  anger: "/emojis/anger.avif",
  angola: "/emojis/angola.avif",
  angry: "/emojis/angry.avif",
  anguilla: "/emojis/anguilla.avif",
  anguished: "/emojis/anguished.avif",
  ant: "/emojis/ant.avif",
  antarctica: "/emojis/antarctica.avif",
  antigua_barbuda: "/emojis/antigua_barbuda.avif",
  apple: "/emojis/apple.avif",
  aquarius: "/emojis/aquarius.avif",
  argentina: "/emojis/argentina.avif",
  aries: "/emojis/aries.avif",
  armenia: "/emojis/armenia.avif",
  arrow_backward: "/emojis/arrow_backward.avif",
  arrow_double_down: "/emojis/arrow_double_down.avif",
  arrow_double_up: "/emojis/arrow_double_up.avif",
  arrow_down: "/emojis/arrow_down.avif",
  arrow_down_small: "/emojis/arrow_down_small.avif",
  arrow_forward: "/emojis/arrow_forward.avif",
  arrow_heading_down: "/emojis/arrow_heading_down.avif",
  arrow_heading_up: "/emojis/arrow_heading_up.avif",
  arrow_left: "/emojis/arrow_left.avif",
  arrow_lower_left: "/emojis/arrow_lower_left.avif",
  arrow_lower_right: "/emojis/arrow_lower_right.avif",
  arrow_right: "/emojis/arrow_right.avif",
  arrow_right_hook: "/emojis/arrow_right_hook.avif",
  arrow_up: "/emojis/arrow_up.avif",
  arrow_up_down: "/emojis/arrow_up_down.avif",
  arrow_up_small: "/emojis/arrow_up_small.avif",
  arrow_upper_left: "/emojis/arrow_upper_left.avif",
  arrow_upper_right: "/emojis/arrow_upper_right.avif",
  arrows_clockwise: "/emojis/arrows_clockwise.avif",
  arrows_counterclockwise: "/emojis/arrows_counterclockwise.avif",
  art: "/emojis/art.avif",
  articulated_lorry: "/emojis/articulated_lorry.avif",
  artificial_satellite: "/emojis/artificial_satellite.avif",
  artist: "/emojis/artist.avif",
  aruba: "/emojis/aruba.avif",
  ascension_island: "/emojis/ascension_island.avif",
  asterisk: "/emojis/asterisk.avif",
  astonished: "/emojis/astonished.avif",
  astronaut: "/emojis/astronaut.avif",
  athletic_shoe: "/emojis/athletic_shoe.avif",
  atm: "/emojis/atm.avif",
  atom: "/emojis/atom.avif",
  atom_symbol: "/emojis/atom_symbol.avif",
  australia: "/emojis/australia.avif",
  austria: "/emojis/austria.avif",
  auto_rickshaw: "/emojis/auto_rickshaw.avif",
  avocado: "/emojis/avocado.avif",
  axe: "/emojis/axe.avif",
  azerbaijan: "/emojis/azerbaijan.avif",
  b: "/emojis/b.avif",
  baby: "/emojis/baby.avif",
  baby_bottle: "/emojis/baby_bottle.avif",
  baby_chick: "/emojis/baby_chick.avif",
  baby_symbol: "/emojis/baby_symbol.avif",
  back: "/emojis/back.avif",
  bacon: "/emojis/bacon.avif",
  badger: "/emojis/badger.avif",
  badminton: "/emojis/badminton.avif",
  bagel: "/emojis/bagel.avif",
  baggage_claim: "/emojis/baggage_claim.avif",
  baguette_bread: "/emojis/baguette_bread.avif",
  bahamas: "/emojis/bahamas.avif",
  bahrain: "/emojis/bahrain.avif",
  balance_scale: "/emojis/balance_scale.avif",
  bald_man: "/emojis/bald_man.avif",
  bald_woman: "/emojis/bald_woman.avif",
  ballet_shoes: "/emojis/ballet_shoes.avif",
  balloon: "/emojis/balloon.avif",
  ballot_box: "/emojis/ballot_box.avif",
  ballot_box_with_check: "/emojis/ballot_box_with_check.avif",
  bamboo: "/emojis/bamboo.avif",
  banana: "/emojis/banana.avif",
  bangbang: "/emojis/bangbang.avif",
  bangladesh: "/emojis/bangladesh.avif",
  banjo: "/emojis/banjo.avif",
  bank: "/emojis/bank.avif",
  bar_chart: "/emojis/bar_chart.avif",
  barbados: "/emojis/barbados.avif",
  barber: "/emojis/barber.avif",
  baseball: "/emojis/baseball.avif",
  basecamp: "/emojis/basecamp.avif",
  basecampy: "/emojis/basecampy.avif",
  basket: "/emojis/basket.avif",
  basketball: "/emojis/basketball.avif",
  basketball_man: "/emojis/basketball_man.avif",
  basketball_woman: "/emojis/basketball_woman.avif",
  bat: "/emojis/bat.avif",
  bath: "/emojis/bath.avif",
  bathtub: "/emojis/bathtub.avif",
  battery: "/emojis/battery.avif",
  beach_umbrella: "/emojis/beach_umbrella.avif",
  bear: "/emojis/bear.avif",
  bearded_person: "/emojis/bearded_person.avif",
  beaver: "/emojis/beaver.avif",
  bed: "/emojis/bed.avif",
  bee: "/emojis/bee.avif",
  beer: "/emojis/beer.avif",
  beers: "/emojis/beers.avif",
  beetle: "/emojis/beetle.avif",
  beginner: "/emojis/beginner.avif",
  belarus: "/emojis/belarus.avif",
  belgium: "/emojis/belgium.avif",
  belize: "/emojis/belize.avif",
  bell: "/emojis/bell.avif",
  bell_pepper: "/emojis/bell_pepper.avif",
  bellhop_bell: "/emojis/bellhop_bell.avif",
  benin: "/emojis/benin.avif",
  bento: "/emojis/bento.avif",
  bermuda: "/emojis/bermuda.avif",
  beverage_box: "/emojis/beverage_box.avif",
  bhutan: "/emojis/bhutan.avif",
  bicyclist: "/emojis/bicyclist.avif",
  bike: "/emojis/bike.avif",
  biking_man: "/emojis/biking_man.avif",
  biking_woman: "/emojis/biking_woman.avif",
  bikini: "/emojis/bikini.avif",
  billed_cap: "/emojis/billed_cap.avif",
  biohazard: "/emojis/biohazard.avif",
  bird: "/emojis/bird.avif",
  birthday: "/emojis/birthday.avif",
  bison: "/emojis/bison.avif",
  black_cat: "/emojis/black_cat.avif",
  black_circle: "/emojis/black_circle.avif",
  black_flag: "/emojis/black_flag.avif",
  black_heart: "/emojis/black_heart.avif",
  black_joker: "/emojis/black_joker.avif",
  black_large_square: "/emojis/black_large_square.avif",
  black_medium_small_square: "/emojis/black_medium_small_square.avif",
  black_medium_square: "/emojis/black_medium_square.avif",
  black_nib: "/emojis/black_nib.avif",
  black_small_square: "/emojis/black_small_square.avif",
  black_square_button: "/emojis/black_square_button.avif",
  blond_haired_man: "/emojis/blond_haired_man.avif",
  blond_haired_person: "/emojis/blond_haired_person.avif",
  blond_haired_woman: "/emojis/blond_haired_woman.avif",
  blonde_woman: "/emojis/blonde_woman.avif",
  blossom: "/emojis/blossom.avif",
  blowfish: "/emojis/blowfish.avif",
  blue_book: "/emojis/blue_book.avif",
  blue_car: "/emojis/blue_car.avif",
  blue_heart: "/emojis/blue_heart.avif",
  blue_square: "/emojis/blue_square.avif",
  blueberries: "/emojis/blueberries.avif",
  blush: "/emojis/blush.avif",
  boar: "/emojis/boar.avif",
  boat: "/emojis/boat.avif",
  bolivia: "/emojis/bolivia.avif",
  bomb: "/emojis/bomb.avif",
  bone: "/emojis/bone.avif",
  book: "/emojis/book.avif",
  bookmark: "/emojis/bookmark.avif",
  bookmark_tabs: "/emojis/bookmark_tabs.avif",
  books: "/emojis/books.avif",
  boom: "/emojis/boom.avif",
  boomerang: "/emojis/boomerang.avif",
  boot: "/emojis/boot.avif",
  bosnia_herzegovina: "/emojis/bosnia_herzegovina.avif",
  botswana: "/emojis/botswana.avif",
  bouncing_ball_man: "/emojis/bouncing_ball_man.avif",
  bouncing_ball_person: "/emojis/bouncing_ball_person.avif",
  bouncing_ball_woman: "/emojis/bouncing_ball_woman.avif",
  bouquet: "/emojis/bouquet.avif",
  bouvet_island: "/emojis/bouvet_island.avif",
  bow: "/emojis/bow.avif",
  bow_and_arrow: "/emojis/bow_and_arrow.avif",
  bowing_man: "/emojis/bowing_man.avif",
  bowing_woman: "/emojis/bowing_woman.avif",
  bowl_with_spoon: "/emojis/bowl_with_spoon.avif",
  bowling: "/emojis/bowling.avif",
  bowtie: "/emojis/bowtie.avif",
  boxing_glove: "/emojis/boxing_glove.avif",
  boy: "/emojis/boy.avif",
  brain: "/emojis/brain.avif",
  brazil: "/emojis/brazil.avif",
  bread: "/emojis/bread.avif",
  breast_feeding: "/emojis/breast_feeding.avif",
  bricks: "/emojis/bricks.avif",
  bride_with_veil: "/emojis/bride_with_veil.avif",
  bridge_at_night: "/emojis/bridge_at_night.avif",
  briefcase: "/emojis/briefcase.avif",
  british_indian_ocean_territory: "/emojis/british_indian_ocean_territory.avif",
  british_virgin_islands: "/emojis/british_virgin_islands.avif",
  broccoli: "/emojis/broccoli.avif",
  broken_heart: "/emojis/broken_heart.avif",
  broom: "/emojis/broom.avif",
  brown_circle: "/emojis/brown_circle.avif",
  brown_heart: "/emojis/brown_heart.avif",
  brown_square: "/emojis/brown_square.avif",
  brunei: "/emojis/brunei.avif",
  bubble_tea: "/emojis/bubble_tea.avif",
  bucket: "/emojis/bucket.avif",
  bug: "/emojis/bug.avif",
  building_construction: "/emojis/building_construction.avif",
  bulb: "/emojis/bulb.avif",
  bulgaria: "/emojis/bulgaria.avif",
  bullettrain_front: "/emojis/bullettrain_front.avif",
  bullettrain_side: "/emojis/bullettrain_side.avif",
  burkina_faso: "/emojis/burkina_faso.avif",
  burrito: "/emojis/burrito.avif",
  burundi: "/emojis/burundi.avif",
  bus: "/emojis/bus.avif",
  business_suit_levitating: "/emojis/business_suit_levitating.avif",
  busstop: "/emojis/busstop.avif",
  bust_in_silhouette: "/emojis/bust_in_silhouette.avif",
  busts_in_silhouette: "/emojis/busts_in_silhouette.avif",
  butter: "/emojis/butter.avif",
  butterfly: "/emojis/butterfly.avif",
  cactus: "/emojis/cactus.avif",
  cake: "/emojis/cake.avif",
  calendar: "/emojis/calendar.avif",
  call_me_hand: "/emojis/call_me_hand.avif",
  calling: "/emojis/calling.avif",
  cambodia: "/emojis/cambodia.avif",
  camel: "/emojis/camel.avif",
  camera: "/emojis/camera.avif",
  camera_flash: "/emojis/camera_flash.avif",
  cameroon: "/emojis/cameroon.avif",
  camping: "/emojis/camping.avif",
  canada: "/emojis/canada.avif",
  canary_islands: "/emojis/canary_islands.avif",
  cancer: "/emojis/cancer.avif",
  candle: "/emojis/candle.avif",
  candy: "/emojis/candy.avif",
  canned_food: "/emojis/canned_food.avif",
  canoe: "/emojis/canoe.avif",
  cape_verde: "/emojis/cape_verde.avif",
  capital_abcd: "/emojis/capital_abcd.avif",
  capricorn: "/emojis/capricorn.avif",
  car: "/emojis/car.avif",
  card_file_box: "/emojis/card_file_box.avif",
  card_index: "/emojis/card_index.avif",
  card_index_dividers: "/emojis/card_index_dividers.avif",
  caribbean_netherlands: "/emojis/caribbean_netherlands.avif",
  carousel_horse: "/emojis/carousel_horse.avif",
  carpentry_saw: "/emojis/carpentry_saw.avif",
  carrot: "/emojis/carrot.avif",
  cartwheeling: "/emojis/cartwheeling.avif",
  cat: "/emojis/cat.avif",
  cat2: "/emojis/cat2.avif",
  cayman_islands: "/emojis/cayman_islands.avif",
  cd: "/emojis/cd.avif",
  central_african_republic: "/emojis/central_african_republic.avif",
  ceuta_melilla: "/emojis/ceuta_melilla.avif",
  chad: "/emojis/chad.avif",
  chains: "/emojis/chains.avif",
  chair: "/emojis/chair.avif",
  champagne: "/emojis/champagne.avif",
  chart: "/emojis/chart.avif",
  chart_with_downwards_trend: "/emojis/chart_with_downwards_trend.avif",
  chart_with_upwards_trend: "/emojis/chart_with_upwards_trend.avif",
  checkered_flag: "/emojis/checkered_flag.avif",
  cheese: "/emojis/cheese.avif",
  cherries: "/emojis/cherries.avif",
  cherry_blossom: "/emojis/cherry_blossom.avif",
  chess_pawn: "/emojis/chess_pawn.avif",
  chestnut: "/emojis/chestnut.avif",
  chicken: "/emojis/chicken.avif",
  child: "/emojis/child.avif",
  children_crossing: "/emojis/children_crossing.avif",
  chile: "/emojis/chile.avif",
  chipmunk: "/emojis/chipmunk.avif",
  chocolate_bar: "/emojis/chocolate_bar.avif",
  chopsticks: "/emojis/chopsticks.avif",
  christmas_island: "/emojis/christmas_island.avif",
  christmas_tree: "/emojis/christmas_tree.avif",
  church: "/emojis/church.avif",
  cinema: "/emojis/cinema.avif",
  circus_tent: "/emojis/circus_tent.avif",
  city_sunrise: "/emojis/city_sunrise.avif",
  city_sunset: "/emojis/city_sunset.avif",
  cityscape: "/emojis/cityscape.avif",
  cl: "/emojis/cl.avif",
  clamp: "/emojis/clamp.avif",
  clap: "/emojis/clap.avif",
  clapper: "/emojis/clapper.avif",
  classical_building: "/emojis/classical_building.avif",
  climbing: "/emojis/climbing.avif",
  climbing_man: "/emojis/climbing_man.avif",
  climbing_woman: "/emojis/climbing_woman.avif",
  clinking_glasses: "/emojis/clinking_glasses.avif",
  clipboard: "/emojis/clipboard.avif",
  clipperton_island: "/emojis/clipperton_island.avif",
  clock1: "/emojis/clock1.avif",
  clock10: "/emojis/clock10.avif",
  clock1030: "/emojis/clock1030.avif",
  clock11: "/emojis/clock11.avif",
  clock1130: "/emojis/clock1130.avif",
  clock12: "/emojis/clock12.avif",
  clock1230: "/emojis/clock1230.avif",
  clock130: "/emojis/clock130.avif",
  clock2: "/emojis/clock2.avif",
  clock230: "/emojis/clock230.avif",
  clock3: "/emojis/clock3.avif",
  clock330: "/emojis/clock330.avif",
  clock4: "/emojis/clock4.avif",
  clock430: "/emojis/clock430.avif",
  clock5: "/emojis/clock5.avif",
  clock530: "/emojis/clock530.avif",
  clock6: "/emojis/clock6.avif",
  clock630: "/emojis/clock630.avif",
  clock7: "/emojis/clock7.avif",
  clock730: "/emojis/clock730.avif",
  clock8: "/emojis/clock8.avif",
  clock830: "/emojis/clock830.avif",
  clock9: "/emojis/clock9.avif",
  clock930: "/emojis/clock930.avif",
  closed_book: "/emojis/closed_book.avif",
  closed_lock_with_key: "/emojis/closed_lock_with_key.avif",
  closed_umbrella: "/emojis/closed_umbrella.avif",
  cloud: "/emojis/cloud.avif",
  cloud_with_lightning: "/emojis/cloud_with_lightning.avif",
  cloud_with_lightning_and_rain: "/emojis/cloud_with_lightning_and_rain.avif",
  cloud_with_rain: "/emojis/cloud_with_rain.avif",
  cloud_with_snow: "/emojis/cloud_with_snow.avif",
  clown_face: "/emojis/clown_face.avif",
  clubs: "/emojis/clubs.avif",
  cn: "/emojis/cn.avif",
  coat: "/emojis/coat.avif",
  cockroach: "/emojis/cockroach.avif",
  cocktail: "/emojis/cocktail.avif",
  coconut: "/emojis/coconut.avif",
  cocos_islands: "/emojis/cocos_islands.avif",
  coffee: "/emojis/coffee.avif",
  coffin: "/emojis/coffin.avif",
  coin: "/emojis/coin.avif",
  cold_face: "/emojis/cold_face.avif",
  cold_sweat: "/emojis/cold_sweat.avif",
  collision: "/emojis/collision.avif",
  colombia: "/emojis/colombia.avif",
  comet: "/emojis/comet.avif",
  comoros: "/emojis/comoros.avif",
  compass: "/emojis/compass.avif",
  computer: "/emojis/computer.avif",
  computer_mouse: "/emojis/computer_mouse.avif",
  confetti_ball: "/emojis/confetti_ball.avif",
  confounded: "/emojis/confounded.avif",
  confused: "/emojis/confused.avif",
  congo_brazzaville: "/emojis/congo_brazzaville.avif",
  congo_kinshasa: "/emojis/congo_kinshasa.avif",
  congratulations: "/emojis/congratulations.avif",
  construction: "/emojis/construction.avif",
  construction_worker: "/emojis/construction_worker.avif",
  construction_worker_man: "/emojis/construction_worker_man.avif",
  construction_worker_woman: "/emojis/construction_worker_woman.avif",
  control_knobs: "/emojis/control_knobs.avif",
  convenience_store: "/emojis/convenience_store.avif",
  cook: "/emojis/cook.avif",
  cook_islands: "/emojis/cook_islands.avif",
  cookie: "/emojis/cookie.avif",
  cool: "/emojis/cool.avif",
  cop: "/emojis/cop.avif",
  copyright: "/emojis/copyright.avif",
  corn: "/emojis/corn.avif",
  costa_rica: "/emojis/costa_rica.avif",
  cote_divoire: "/emojis/cote_divoire.avif",
  couch_and_lamp: "/emojis/couch_and_lamp.avif",
  couple: "/emojis/couple.avif",
  couple_with_heart: "/emojis/couple_with_heart.avif",
  couple_with_heart_man_man: "/emojis/couple_with_heart_man_man.avif",
  couple_with_heart_woman_man: "/emojis/couple_with_heart_woman_man.avif",
  couple_with_heart_woman_woman: "/emojis/couple_with_heart_woman_woman.avif",
  couplekiss: "/emojis/couplekiss.avif",
  couplekiss_man_man: "/emojis/couplekiss_man_man.avif",
  couplekiss_man_woman: "/emojis/couplekiss_man_woman.avif",
  couplekiss_woman_woman: "/emojis/couplekiss_woman_woman.avif",
  cow: "/emojis/cow.avif",
  cow2: "/emojis/cow2.avif",
  cowboy_hat_face: "/emojis/cowboy_hat_face.avif",
  crab: "/emojis/crab.avif",
  crayon: "/emojis/crayon.avif",
  credit_card: "/emojis/credit_card.avif",
  crescent_moon: "/emojis/crescent_moon.avif",
  cricket: "/emojis/cricket.avif",
  cricket_game: "/emojis/cricket_game.avif",
  croatia: "/emojis/croatia.avif",
  crocodile: "/emojis/crocodile.avif",
  croissant: "/emojis/croissant.avif",
  crossed_fingers: "/emojis/crossed_fingers.avif",
  crossed_flags: "/emojis/crossed_flags.avif",
  crossed_swords: "/emojis/crossed_swords.avif",
  crown: "/emojis/crown.avif",
  cry: "/emojis/cry.avif",
  crying_cat_face: "/emojis/crying_cat_face.avif",
  crystal_ball: "/emojis/crystal_ball.avif",
  cuba: "/emojis/cuba.avif",
  cucumber: "/emojis/cucumber.avif",
  cup_with_straw: "/emojis/cup_with_straw.avif",
  cupcake: "/emojis/cupcake.avif",
  cupid: "/emojis/cupid.avif",
  curacao: "/emojis/curacao.avif",
  curling_stone: "/emojis/curling_stone.avif",
  curly_haired_man: "/emojis/curly_haired_man.avif",
  curly_haired_woman: "/emojis/curly_haired_woman.avif",
  curly_loop: "/emojis/curly_loop.avif",
  currency_exchange: "/emojis/currency_exchange.avif",
  curry: "/emojis/curry.avif",
  cursing_face: "/emojis/cursing_face.avif",
  custard: "/emojis/custard.avif",
  customs: "/emojis/customs.avif",
  cut_of_meat: "/emojis/cut_of_meat.avif",
  cyclone: "/emojis/cyclone.avif",
  cyprus: "/emojis/cyprus.avif",
  czech_republic: "/emojis/czech_republic.avif",
  dagger: "/emojis/dagger.avif",
  dancer: "/emojis/dancer.avif",
  dancers: "/emojis/dancers.avif",
  dancing_men: "/emojis/dancing_men.avif",
  dancing_women: "/emojis/dancing_women.avif",
  dango: "/emojis/dango.avif",
  dark_sunglasses: "/emojis/dark_sunglasses.avif",
  dart: "/emojis/dart.avif",
  dash: "/emojis/dash.avif",
  date: "/emojis/date.avif",
  de: "/emojis/de.avif",
  deaf_man: "/emojis/deaf_man.avif",
  deaf_person: "/emojis/deaf_person.avif",
  deaf_woman: "/emojis/deaf_woman.avif",
  deciduous_tree: "/emojis/deciduous_tree.avif",
  deer: "/emojis/deer.avif",
  denmark: "/emojis/denmark.avif",
  department_store: "/emojis/department_store.avif",
  dependabot: "/emojis/dependabot.avif",
  derelict_house: "/emojis/derelict_house.avif",
  desert: "/emojis/desert.avif",
  desert_island: "/emojis/desert_island.avif",
  desktop_computer: "/emojis/desktop_computer.avif",
  detective: "/emojis/detective.avif",
  diamond_shape_with_a_dot_inside: "/emojis/diamond_shape_with_a_dot_inside.avif",
  diamonds: "/emojis/diamonds.avif",
  diego_garcia: "/emojis/diego_garcia.avif",
  disappointed: "/emojis/disappointed.avif",
  disappointed_relieved: "/emojis/disappointed_relieved.avif",
  disguised_face: "/emojis/disguised_face.avif",
  diving_mask: "/emojis/diving_mask.avif",
  diya_lamp: "/emojis/diya_lamp.avif",
  dizzy: "/emojis/dizzy.avif",
  dizzy_face: "/emojis/dizzy_face.avif",
  djibouti: "/emojis/djibouti.avif",
  dna: "/emojis/dna.avif",
  do_not_litter: "/emojis/do_not_litter.avif",
  dodo: "/emojis/dodo.avif",
  dog: "/emojis/dog.avif",
  dog2: "/emojis/dog2.avif",
  dollar: "/emojis/dollar.avif",
  dolls: "/emojis/dolls.avif",
  dolphin: "/emojis/dolphin.avif",
  dominica: "/emojis/dominica.avif",
  dominican_republic: "/emojis/dominican_republic.avif",
  door: "/emojis/door.avif",
  doughnut: "/emojis/doughnut.avif",
  dove: "/emojis/dove.avif",
  dragon: "/emojis/dragon.avif",
  dragon_face: "/emojis/dragon_face.avif",
  dress: "/emojis/dress.avif",
  dromedary_camel: "/emojis/dromedary_camel.avif",
  drooling_face: "/emojis/drooling_face.avif",
  drop_of_blood: "/emojis/drop_of_blood.avif",
  droplet: "/emojis/droplet.avif",
  drum: "/emojis/drum.avif",
  duck: "/emojis/duck.avif",
  dumpling: "/emojis/dumpling.avif",
  dvd: "/emojis/dvd.avif",
  "e-mail": "/emojis/e-mail.avif",
  eagle: "/emojis/eagle.avif",
  ear: "/emojis/ear.avif",
  ear_of_rice: "/emojis/ear_of_rice.avif",
  ear_with_hearing_aid: "/emojis/ear_with_hearing_aid.avif",
  earth_africa: "/emojis/earth_africa.avif",
  earth_americas: "/emojis/earth_americas.avif",
  earth_asia: "/emojis/earth_asia.avif",
  ecuador: "/emojis/ecuador.avif",
  egg: "/emojis/egg.avif",
  eggplant: "/emojis/eggplant.avif",
  egypt: "/emojis/egypt.avif",
  eight: "/emojis/eight.avif",
  eight_pointed_black_star: "/emojis/eight_pointed_black_star.avif",
  eight_spoked_asterisk: "/emojis/eight_spoked_asterisk.avif",
  eject_button: "/emojis/eject_button.avif",
  el_salvador: "/emojis/el_salvador.avif",
  electric_plug: "/emojis/electric_plug.avif",
  electron: "/emojis/electron.avif",
  elephant: "/emojis/elephant.avif",
  elevator: "/emojis/elevator.avif",
  elf: "/emojis/elf.avif",
  elf_man: "/emojis/elf_man.avif",
  elf_woman: "/emojis/elf_woman.avif",
  email: "/emojis/email.avif",
  end: "/emojis/end.avif",
  england: "/emojis/england.avif",
  envelope: "/emojis/envelope.avif",
  envelope_with_arrow: "/emojis/envelope_with_arrow.avif",
  equatorial_guinea: "/emojis/equatorial_guinea.avif",
  eritrea: "/emojis/eritrea.avif",
  es: "/emojis/es.avif",
  estonia: "/emojis/estonia.avif",
  ethiopia: "/emojis/ethiopia.avif",
  eu: "/emojis/eu.avif",
  euro: "/emojis/euro.avif",
  european_castle: "/emojis/european_castle.avif",
  european_post_office: "/emojis/european_post_office.avif",
  european_union: "/emojis/european_union.avif",
  evergreen_tree: "/emojis/evergreen_tree.avif",
  exclamation: "/emojis/exclamation.avif",
  exploding_head: "/emojis/exploding_head.avif",
  expressionless: "/emojis/expressionless.avif",
  eye: "/emojis/eye.avif",
  eye_speech_bubble: "/emojis/eye_speech_bubble.avif",
  eyeglasses: "/emojis/eyeglasses.avif",
  eyes: "/emojis/eyes.avif",
  face_exhaling: "/emojis/face_exhaling.avif",
  face_in_clouds: "/emojis/face_in_clouds.avif",
  face_with_head_bandage: "/emojis/face_with_head_bandage.avif",
  face_with_spiral_eyes: "/emojis/face_with_spiral_eyes.avif",
  face_with_thermometer: "/emojis/face_with_thermometer.avif",
  facepalm: "/emojis/facepalm.avif",
  facepunch: "/emojis/facepunch.avif",
  factory: "/emojis/factory.avif",
  factory_worker: "/emojis/factory_worker.avif",
  fairy: "/emojis/fairy.avif",
  fairy_man: "/emojis/fairy_man.avif",
  fairy_woman: "/emojis/fairy_woman.avif",
  falafel: "/emojis/falafel.avif",
  falkland_islands: "/emojis/falkland_islands.avif",
  fallen_leaf: "/emojis/fallen_leaf.avif",
  family: "/emojis/family.avif",
  family_man_boy: "/emojis/family_man_boy.avif",
  family_man_boy_boy: "/emojis/family_man_boy_boy.avif",
  family_man_girl: "/emojis/family_man_girl.avif",
  family_man_girl_boy: "/emojis/family_man_girl_boy.avif",
  family_man_girl_girl: "/emojis/family_man_girl_girl.avif",
  family_man_man_boy: "/emojis/family_man_man_boy.avif",
  family_man_man_boy_boy: "/emojis/family_man_man_boy_boy.avif",
  family_man_man_girl: "/emojis/family_man_man_girl.avif",
  family_man_man_girl_boy: "/emojis/family_man_man_girl_boy.avif",
  family_man_man_girl_girl: "/emojis/family_man_man_girl_girl.avif",
  family_man_woman_boy: "/emojis/family_man_woman_boy.avif",
  family_man_woman_boy_boy: "/emojis/family_man_woman_boy_boy.avif",
  family_man_woman_girl: "/emojis/family_man_woman_girl.avif",
  family_man_woman_girl_boy: "/emojis/family_man_woman_girl_boy.avif",
  family_man_woman_girl_girl: "/emojis/family_man_woman_girl_girl.avif",
  family_woman_boy: "/emojis/family_woman_boy.avif",
  family_woman_boy_boy: "/emojis/family_woman_boy_boy.avif",
  family_woman_girl: "/emojis/family_woman_girl.avif",
  family_woman_girl_boy: "/emojis/family_woman_girl_boy.avif",
  family_woman_girl_girl: "/emojis/family_woman_girl_girl.avif",
  family_woman_woman_boy: "/emojis/family_woman_woman_boy.avif",
  family_woman_woman_boy_boy: "/emojis/family_woman_woman_boy_boy.avif",
  family_woman_woman_girl: "/emojis/family_woman_woman_girl.avif",
  family_woman_woman_girl_boy: "/emojis/family_woman_woman_girl_boy.avif",
  family_woman_woman_girl_girl: "/emojis/family_woman_woman_girl_girl.avif",
  farmer: "/emojis/farmer.avif",
  faroe_islands: "/emojis/faroe_islands.avif",
  fast_forward: "/emojis/fast_forward.avif",
  fax: "/emojis/fax.avif",
  fearful: "/emojis/fearful.avif",
  feather: "/emojis/feather.avif",
  feelsgood: "/emojis/feelsgood.avif",
  feet: "/emojis/feet.avif",
  female_detective: "/emojis/female_detective.avif",
  female_sign: "/emojis/female_sign.avif",
  ferris_wheel: "/emojis/ferris_wheel.avif",
  ferry: "/emojis/ferry.avif",
  field_hockey: "/emojis/field_hockey.avif",
  fiji: "/emojis/fiji.avif",
  file_cabinet: "/emojis/file_cabinet.avif",
  file_folder: "/emojis/file_folder.avif",
  film_projector: "/emojis/film_projector.avif",
  film_strip: "/emojis/film_strip.avif",
  finland: "/emojis/finland.avif",
  finnadie: "/emojis/finnadie.avif",
  fire: "/emojis/fire.avif",
  fire_engine: "/emojis/fire_engine.avif",
  fire_extinguisher: "/emojis/fire_extinguisher.avif",
  firecracker: "/emojis/firecracker.avif",
  firefighter: "/emojis/firefighter.avif",
  fireworks: "/emojis/fireworks.avif",
  first_quarter_moon: "/emojis/first_quarter_moon.avif",
  first_quarter_moon_with_face: "/emojis/first_quarter_moon_with_face.avif",
  fish: "/emojis/fish.avif",
  fish_cake: "/emojis/fish_cake.avif",
  fishing_pole_and_fish: "/emojis/fishing_pole_and_fish.avif",
  fishsticks: "/emojis/fishsticks.avif",
  fist: "/emojis/fist.avif",
  fist_left: "/emojis/fist_left.avif",
  fist_oncoming: "/emojis/fist_oncoming.avif",
  fist_raised: "/emojis/fist_raised.avif",
  fist_right: "/emojis/fist_right.avif",
  five: "/emojis/five.avif",
  flags: "/emojis/flags.avif",
  flamingo: "/emojis/flamingo.avif",
  flashlight: "/emojis/flashlight.avif",
  flat_shoe: "/emojis/flat_shoe.avif",
  flatbread: "/emojis/flatbread.avif",
  fleur_de_lis: "/emojis/fleur_de_lis.avif",
  flight_arrival: "/emojis/flight_arrival.avif",
  flight_departure: "/emojis/flight_departure.avif",
  flipper: "/emojis/flipper.avif",
  floppy_disk: "/emojis/floppy_disk.avif",
  flower_playing_cards: "/emojis/flower_playing_cards.avif",
  flushed: "/emojis/flushed.avif",
  fly: "/emojis/fly.avif",
  flying_disc: "/emojis/flying_disc.avif",
  flying_saucer: "/emojis/flying_saucer.avif",
  fog: "/emojis/fog.avif",
  foggy: "/emojis/foggy.avif",
  fondue: "/emojis/fondue.avif",
  foot: "/emojis/foot.avif",
  football: "/emojis/football.avif",
  footprints: "/emojis/footprints.avif",
  fork_and_knife: "/emojis/fork_and_knife.avif",
  fortune_cookie: "/emojis/fortune_cookie.avif",
  fountain: "/emojis/fountain.avif",
  fountain_pen: "/emojis/fountain_pen.avif",
  four: "/emojis/four.avif",
  four_leaf_clover: "/emojis/four_leaf_clover.avif",
  fox_face: "/emojis/fox_face.avif",
  fr: "/emojis/fr.avif",
  framed_picture: "/emojis/framed_picture.avif",
  free: "/emojis/free.avif",
  french_guiana: "/emojis/french_guiana.avif",
  french_polynesia: "/emojis/french_polynesia.avif",
  french_southern_territories: "/emojis/french_southern_territories.avif",
  fried_egg: "/emojis/fried_egg.avif",
  fried_shrimp: "/emojis/fried_shrimp.avif",
  fries: "/emojis/fries.avif",
  frog: "/emojis/frog.avif",
  frowning: "/emojis/frowning.avif",
  frowning_face: "/emojis/frowning_face.avif",
  frowning_man: "/emojis/frowning_man.avif",
  frowning_person: "/emojis/frowning_person.avif",
  frowning_woman: "/emojis/frowning_woman.avif",
  fu: "/emojis/fu.avif",
  fuelpump: "/emojis/fuelpump.avif",
  full_moon: "/emojis/full_moon.avif",
  full_moon_with_face: "/emojis/full_moon_with_face.avif",
  funeral_urn: "/emojis/funeral_urn.avif",
  gabon: "/emojis/gabon.avif",
  gambia: "/emojis/gambia.avif",
  game_die: "/emojis/game_die.avif",
  garlic: "/emojis/garlic.avif",
  gb: "/emojis/gb.avif",
  gear: "/emojis/gear.avif",
  gem: "/emojis/gem.avif",
  gemini: "/emojis/gemini.avif",
  genie: "/emojis/genie.avif",
  genie_man: "/emojis/genie_man.avif",
  genie_woman: "/emojis/genie_woman.avif",
  georgia: "/emojis/georgia.avif",
  ghana: "/emojis/ghana.avif",
  ghost: "/emojis/ghost.avif",
  gibraltar: "/emojis/gibraltar.avif",
  gift: "/emojis/gift.avif",
  gift_heart: "/emojis/gift_heart.avif",
  giraffe: "/emojis/giraffe.avif",
  girl: "/emojis/girl.avif",
  globe_with_meridians: "/emojis/globe_with_meridians.avif",
  gloves: "/emojis/gloves.avif",
  goal_net: "/emojis/goal_net.avif",
  goat: "/emojis/goat.avif",
  goberserk: "/emojis/goberserk.avif",
  godmode: "/emojis/godmode.avif",
  goggles: "/emojis/goggles.avif",
  golf: "/emojis/golf.avif",
  golfing: "/emojis/golfing.avif",
  golfing_man: "/emojis/golfing_man.avif",
  golfing_woman: "/emojis/golfing_woman.avif",
  gorilla: "/emojis/gorilla.avif",
  grapes: "/emojis/grapes.avif",
  greece: "/emojis/greece.avif",
  green_apple: "/emojis/green_apple.avif",
  green_book: "/emojis/green_book.avif",
  green_circle: "/emojis/green_circle.avif",
  green_heart: "/emojis/green_heart.avif",
  green_salad: "/emojis/green_salad.avif",
  green_square: "/emojis/green_square.avif",
  greenland: "/emojis/greenland.avif",
  grenada: "/emojis/grenada.avif",
  grey_exclamation: "/emojis/grey_exclamation.avif",
  grey_question: "/emojis/grey_question.avif",
  grimacing: "/emojis/grimacing.avif",
  grin: "/emojis/grin.avif",
  grinning: "/emojis/grinning.avif",
  guadeloupe: "/emojis/guadeloupe.avif",
  guam: "/emojis/guam.avif",
  guard: "/emojis/guard.avif",
  guardsman: "/emojis/guardsman.avif",
  guardswoman: "/emojis/guardswoman.avif",
  guatemala: "/emojis/guatemala.avif",
  guernsey: "/emojis/guernsey.avif",
  guide_dog: "/emojis/guide_dog.avif",
  guinea: "/emojis/guinea.avif",
  guinea_bissau: "/emojis/guinea_bissau.avif",
  guitar: "/emojis/guitar.avif",
  gun: "/emojis/gun.avif",
  guyana: "/emojis/guyana.avif",
  haircut: "/emojis/haircut.avif",
  haircut_man: "/emojis/haircut_man.avif",
  haircut_woman: "/emojis/haircut_woman.avif",
  haiti: "/emojis/haiti.avif",
  hamburger: "/emojis/hamburger.avif",
  hammer: "/emojis/hammer.avif",
  hammer_and_pick: "/emojis/hammer_and_pick.avif",
  hammer_and_wrench: "/emojis/hammer_and_wrench.avif",
  hamster: "/emojis/hamster.avif",
  hand: "/emojis/hand.avif",
  hand_over_mouth: "/emojis/hand_over_mouth.avif",
  handbag: "/emojis/handbag.avif",
  handball_person: "/emojis/handball_person.avif",
  handshake: "/emojis/handshake.avif",
  hankey: "/emojis/hankey.avif",
  hash: "/emojis/hash.avif",
  hatched_chick: "/emojis/hatched_chick.avif",
  hatching_chick: "/emojis/hatching_chick.avif",
  headphones: "/emojis/headphones.avif",
  headstone: "/emojis/headstone.avif",
  health_worker: "/emojis/health_worker.avif",
  hear_no_evil: "/emojis/hear_no_evil.avif",
  heard_mcdonald_islands: "/emojis/heard_mcdonald_islands.avif",
  heart: "/emojis/heart.avif",
  heart_decoration: "/emojis/heart_decoration.avif",
  heart_eyes: "/emojis/heart_eyes.avif",
  heart_eyes_cat: "/emojis/heart_eyes_cat.avif",
  heart_on_fire: "/emojis/heart_on_fire.avif",
  heartbeat: "/emojis/heartbeat.avif",
  heartpulse: "/emojis/heartpulse.avif",
  hearts: "/emojis/hearts.avif",
  heavy_check_mark: "/emojis/heavy_check_mark.avif",
  heavy_division_sign: "/emojis/heavy_division_sign.avif",
  heavy_dollar_sign: "/emojis/heavy_dollar_sign.avif",
  heavy_exclamation_mark: "/emojis/heavy_exclamation_mark.avif",
  heavy_heart_exclamation: "/emojis/heavy_heart_exclamation.avif",
  heavy_minus_sign: "/emojis/heavy_minus_sign.avif",
  heavy_multiplication_x: "/emojis/heavy_multiplication_x.avif",
  heavy_plus_sign: "/emojis/heavy_plus_sign.avif",
  hedgehog: "/emojis/hedgehog.avif",
  helicopter: "/emojis/helicopter.avif",
  herb: "/emojis/herb.avif",
  hibiscus: "/emojis/hibiscus.avif",
  high_brightness: "/emojis/high_brightness.avif",
  high_heel: "/emojis/high_heel.avif",
  hiking_boot: "/emojis/hiking_boot.avif",
  hindu_temple: "/emojis/hindu_temple.avif",
  hippopotamus: "/emojis/hippopotamus.avif",
  hocho: "/emojis/hocho.avif",
  hole: "/emojis/hole.avif",
  honduras: "/emojis/honduras.avif",
  honey_pot: "/emojis/honey_pot.avif",
  honeybee: "/emojis/honeybee.avif",
  hong_kong: "/emojis/hong_kong.avif",
  hook: "/emojis/hook.avif",
  horse: "/emojis/horse.avif",
  horse_racing: "/emojis/horse_racing.avif",
  hospital: "/emojis/hospital.avif",
  hot_face: "/emojis/hot_face.avif",
  hot_pepper: "/emojis/hot_pepper.avif",
  hotdog: "/emojis/hotdog.avif",
  hotel: "/emojis/hotel.avif",
  hotsprings: "/emojis/hotsprings.avif",
  hourglass: "/emojis/hourglass.avif",
  hourglass_flowing_sand: "/emojis/hourglass_flowing_sand.avif",
  house: "/emojis/house.avif",
  house_with_garden: "/emojis/house_with_garden.avif",
  houses: "/emojis/houses.avif",
  hugs: "/emojis/hugs.avif",
  hungary: "/emojis/hungary.avif",
  hurtrealbad: "/emojis/hurtrealbad.avif",
  hushed: "/emojis/hushed.avif",
  hut: "/emojis/hut.avif",
  ice_cream: "/emojis/ice_cream.avif",
  ice_cube: "/emojis/ice_cube.avif",
  ice_hockey: "/emojis/ice_hockey.avif",
  ice_skate: "/emojis/ice_skate.avif",
  icecream: "/emojis/icecream.avif",
  iceland: "/emojis/iceland.avif",
  id: "/emojis/id.avif",
  ideograph_advantage: "/emojis/ideograph_advantage.avif",
  imp: "/emojis/imp.avif",
  inbox_tray: "/emojis/inbox_tray.avif",
  incoming_envelope: "/emojis/incoming_envelope.avif",
  india: "/emojis/india.avif",
  indonesia: "/emojis/indonesia.avif",
  infinity: "/emojis/infinity.avif",
  information_desk_person: "/emojis/information_desk_person.avif",
  information_source: "/emojis/information_source.avif",
  innocent: "/emojis/innocent.avif",
  interrobang: "/emojis/interrobang.avif",
  iphone: "/emojis/iphone.avif",
  iran: "/emojis/iran.avif",
  iraq: "/emojis/iraq.avif",
  ireland: "/emojis/ireland.avif",
  isle_of_man: "/emojis/isle_of_man.avif",
  israel: "/emojis/israel.avif",
  it: "/emojis/it.avif",
  izakaya_lantern: "/emojis/izakaya_lantern.avif",
  jack_o_lantern: "/emojis/jack_o_lantern.avif",
  jamaica: "/emojis/jamaica.avif",
  japan: "/emojis/japan.avif",
  japanese_castle: "/emojis/japanese_castle.avif",
  japanese_goblin: "/emojis/japanese_goblin.avif",
  japanese_ogre: "/emojis/japanese_ogre.avif",
  jeans: "/emojis/jeans.avif",
  jersey: "/emojis/jersey.avif",
  jigsaw: "/emojis/jigsaw.avif",
  jordan: "/emojis/jordan.avif",
  joy: "/emojis/joy.avif",
  joy_cat: "/emojis/joy_cat.avif",
  joystick: "/emojis/joystick.avif",
  jp: "/emojis/jp.avif",
  judge: "/emojis/judge.avif",
  juggling_person: "/emojis/juggling_person.avif",
  kaaba: "/emojis/kaaba.avif",
  kangaroo: "/emojis/kangaroo.avif",
  kazakhstan: "/emojis/kazakhstan.avif",
  kenya: "/emojis/kenya.avif",
  key: "/emojis/key.avif",
  keyboard: "/emojis/keyboard.avif",
  keycap_ten: "/emojis/keycap_ten.avif",
  kick_scooter: "/emojis/kick_scooter.avif",
  kimono: "/emojis/kimono.avif",
  kiribati: "/emojis/kiribati.avif",
  kiss: "/emojis/kiss.avif",
  kissing: "/emojis/kissing.avif",
  kissing_cat: "/emojis/kissing_cat.avif",
  kissing_closed_eyes: "/emojis/kissing_closed_eyes.avif",
  kissing_heart: "/emojis/kissing_heart.avif",
  kissing_smiling_eyes: "/emojis/kissing_smiling_eyes.avif",
  kite: "/emojis/kite.avif",
  kiwi_fruit: "/emojis/kiwi_fruit.avif",
  kneeling_man: "/emojis/kneeling_man.avif",
  kneeling_person: "/emojis/kneeling_person.avif",
  kneeling_woman: "/emojis/kneeling_woman.avif",
  knife: "/emojis/knife.avif",
  knot: "/emojis/knot.avif",
  koala: "/emojis/koala.avif",
  koko: "/emojis/koko.avif",
  kosovo: "/emojis/kosovo.avif",
  kr: "/emojis/kr.avif",
  kuwait: "/emojis/kuwait.avif",
  kyrgyzstan: "/emojis/kyrgyzstan.avif",
  lab_coat: "/emojis/lab_coat.avif",
  label: "/emojis/label.avif",
  lacrosse: "/emojis/lacrosse.avif",
  ladder: "/emojis/ladder.avif",
  lady_beetle: "/emojis/lady_beetle.avif",
  lantern: "/emojis/lantern.avif",
  laos: "/emojis/laos.avif",
  large_blue_circle: "/emojis/large_blue_circle.avif",
  large_blue_diamond: "/emojis/large_blue_diamond.avif",
  large_orange_diamond: "/emojis/large_orange_diamond.avif",
  last_quarter_moon: "/emojis/last_quarter_moon.avif",
  last_quarter_moon_with_face: "/emojis/last_quarter_moon_with_face.avif",
  latin_cross: "/emojis/latin_cross.avif",
  latvia: "/emojis/latvia.avif",
  laughing: "/emojis/laughing.avif",
  leafy_green: "/emojis/leafy_green.avif",
  leaves: "/emojis/leaves.avif",
  lebanon: "/emojis/lebanon.avif",
  ledger: "/emojis/ledger.avif",
  left_luggage: "/emojis/left_luggage.avif",
  left_right_arrow: "/emojis/left_right_arrow.avif",
  left_speech_bubble: "/emojis/left_speech_bubble.avif",
  leftwards_arrow_with_hook: "/emojis/leftwards_arrow_with_hook.avif",
  leg: "/emojis/leg.avif",
  lemon: "/emojis/lemon.avif",
  leo: "/emojis/leo.avif",
  leopard: "/emojis/leopard.avif",
  lesotho: "/emojis/lesotho.avif",
  level_slider: "/emojis/level_slider.avif",
  liberia: "/emojis/liberia.avif",
  libra: "/emojis/libra.avif",
  libya: "/emojis/libya.avif",
  liechtenstein: "/emojis/liechtenstein.avif",
  light_rail: "/emojis/light_rail.avif",
  link: "/emojis/link.avif",
  lion: "/emojis/lion.avif",
  lips: "/emojis/lips.avif",
  lipstick: "/emojis/lipstick.avif",
  lithuania: "/emojis/lithuania.avif",
  lizard: "/emojis/lizard.avif",
  llama: "/emojis/llama.avif",
  lobster: "/emojis/lobster.avif",
  lock: "/emojis/lock.avif",
  lock_with_ink_pen: "/emojis/lock_with_ink_pen.avif",
  lollipop: "/emojis/lollipop.avif",
  long_drum: "/emojis/long_drum.avif",
  loop: "/emojis/loop.avif",
  lotion_bottle: "/emojis/lotion_bottle.avif",
  lotus_position: "/emojis/lotus_position.avif",
  lotus_position_man: "/emojis/lotus_position_man.avif",
  lotus_position_woman: "/emojis/lotus_position_woman.avif",
  loud_sound: "/emojis/loud_sound.avif",
  loudspeaker: "/emojis/loudspeaker.avif",
  love_hotel: "/emojis/love_hotel.avif",
  love_letter: "/emojis/love_letter.avif",
  love_you_gesture: "/emojis/love_you_gesture.avif",
  low_brightness: "/emojis/low_brightness.avif",
  luggage: "/emojis/luggage.avif",
  lungs: "/emojis/lungs.avif",
  luxembourg: "/emojis/luxembourg.avif",
  lying_face: "/emojis/lying_face.avif",
  m: "/emojis/m.avif",
  macau: "/emojis/macau.avif",
  macedonia: "/emojis/macedonia.avif",
  madagascar: "/emojis/madagascar.avif",
  mag: "/emojis/mag.avif",
  mag_right: "/emojis/mag_right.avif",
  mage: "/emojis/mage.avif",
  mage_man: "/emojis/mage_man.avif",
  mage_woman: "/emojis/mage_woman.avif",
  magic_wand: "/emojis/magic_wand.avif",
  magnet: "/emojis/magnet.avif",
  mahjong: "/emojis/mahjong.avif",
  mailbox: "/emojis/mailbox.avif",
  mailbox_closed: "/emojis/mailbox_closed.avif",
  mailbox_with_mail: "/emojis/mailbox_with_mail.avif",
  mailbox_with_no_mail: "/emojis/mailbox_with_no_mail.avif",
  malawi: "/emojis/malawi.avif",
  malaysia: "/emojis/malaysia.avif",
  maldives: "/emojis/maldives.avif",
  male_detective: "/emojis/male_detective.avif",
  male_sign: "/emojis/male_sign.avif",
  mali: "/emojis/mali.avif",
  malta: "/emojis/malta.avif",
  mammoth: "/emojis/mammoth.avif",
  man: "/emojis/man.avif",
  man_artist: "/emojis/man_artist.avif",
  man_astronaut: "/emojis/man_astronaut.avif",
  man_beard: "/emojis/man_beard.avif",
  man_cartwheeling: "/emojis/man_cartwheeling.avif",
  man_cook: "/emojis/man_cook.avif",
  man_dancing: "/emojis/man_dancing.avif",
  man_facepalming: "/emojis/man_facepalming.avif",
  man_factory_worker: "/emojis/man_factory_worker.avif",
  man_farmer: "/emojis/man_farmer.avif",
  man_feeding_baby: "/emojis/man_feeding_baby.avif",
  man_firefighter: "/emojis/man_firefighter.avif",
  man_health_worker: "/emojis/man_health_worker.avif",
  man_in_manual_wheelchair: "/emojis/man_in_manual_wheelchair.avif",
  man_in_motorized_wheelchair: "/emojis/man_in_motorized_wheelchair.avif",
  man_in_tuxedo: "/emojis/man_in_tuxedo.avif",
  man_judge: "/emojis/man_judge.avif",
  man_juggling: "/emojis/man_juggling.avif",
  man_mechanic: "/emojis/man_mechanic.avif",
  man_office_worker: "/emojis/man_office_worker.avif",
  man_pilot: "/emojis/man_pilot.avif",
  man_playing_handball: "/emojis/man_playing_handball.avif",
  man_playing_water_polo: "/emojis/man_playing_water_polo.avif",
  man_scientist: "/emojis/man_scientist.avif",
  man_shrugging: "/emojis/man_shrugging.avif",
  man_singer: "/emojis/man_singer.avif",
  man_student: "/emojis/man_student.avif",
  man_teacher: "/emojis/man_teacher.avif",
  man_technologist: "/emojis/man_technologist.avif",
  man_with_gua_pi_mao: "/emojis/man_with_gua_pi_mao.avif",
  man_with_probing_cane: "/emojis/man_with_probing_cane.avif",
  man_with_turban: "/emojis/man_with_turban.avif",
  man_with_veil: "/emojis/man_with_veil.avif",
  mandarin: "/emojis/mandarin.avif",
  mango: "/emojis/mango.avif",
  mans_shoe: "/emojis/mans_shoe.avif",
  mantelpiece_clock: "/emojis/mantelpiece_clock.avif",
  manual_wheelchair: "/emojis/manual_wheelchair.avif",
  maple_leaf: "/emojis/maple_leaf.avif",
  marshall_islands: "/emojis/marshall_islands.avif",
  martial_arts_uniform: "/emojis/martial_arts_uniform.avif",
  martinique: "/emojis/martinique.avif",
  mask: "/emojis/mask.avif",
  massage: "/emojis/massage.avif",
  massage_man: "/emojis/massage_man.avif",
  massage_woman: "/emojis/massage_woman.avif",
  mate: "/emojis/mate.avif",
  mauritania: "/emojis/mauritania.avif",
  mauritius: "/emojis/mauritius.avif",
  mayotte: "/emojis/mayotte.avif",
  meat_on_bone: "/emojis/meat_on_bone.avif",
  mechanic: "/emojis/mechanic.avif",
  mechanical_arm: "/emojis/mechanical_arm.avif",
  mechanical_leg: "/emojis/mechanical_leg.avif",
  medal_military: "/emojis/medal_military.avif",
  medal_sports: "/emojis/medal_sports.avif",
  medical_symbol: "/emojis/medical_symbol.avif",
  mega: "/emojis/mega.avif",
  melon: "/emojis/melon.avif",
  memo: "/emojis/memo.avif",
  men_wrestling: "/emojis/men_wrestling.avif",
  mending_heart: "/emojis/mending_heart.avif",
  menorah: "/emojis/menorah.avif",
  mens: "/emojis/mens.avif",
  mermaid: "/emojis/mermaid.avif",
  merman: "/emojis/merman.avif",
  merperson: "/emojis/merperson.avif",
  metal: "/emojis/metal.avif",
  metro: "/emojis/metro.avif",
  mexico: "/emojis/mexico.avif",
  microbe: "/emojis/microbe.avif",
  micronesia: "/emojis/micronesia.avif",
  microphone: "/emojis/microphone.avif",
  microscope: "/emojis/microscope.avif",
  middle_finger: "/emojis/middle_finger.avif",
  military_helmet: "/emojis/military_helmet.avif",
  milk_glass: "/emojis/milk_glass.avif",
  milky_way: "/emojis/milky_way.avif",
  minibus: "/emojis/minibus.avif",
  minidisc: "/emojis/minidisc.avif",
  mirror: "/emojis/mirror.avif",
  mobile_phone_off: "/emojis/mobile_phone_off.avif",
  moldova: "/emojis/moldova.avif",
  monaco: "/emojis/monaco.avif",
  money_mouth_face: "/emojis/money_mouth_face.avif",
  money_with_wings: "/emojis/money_with_wings.avif",
  moneybag: "/emojis/moneybag.avif",
  mongolia: "/emojis/mongolia.avif",
  monkey: "/emojis/monkey.avif",
  monkey_face: "/emojis/monkey_face.avif",
  monocle_face: "/emojis/monocle_face.avif",
  monorail: "/emojis/monorail.avif",
  montenegro: "/emojis/montenegro.avif",
  montserrat: "/emojis/montserrat.avif",
  moon: "/emojis/moon.avif",
  moon_cake: "/emojis/moon_cake.avif",
  morocco: "/emojis/morocco.avif",
  mortar_board: "/emojis/mortar_board.avif",
  mosque: "/emojis/mosque.avif",
  mosquito: "/emojis/mosquito.avif",
  motor_boat: "/emojis/motor_boat.avif",
  motor_scooter: "/emojis/motor_scooter.avif",
  motorcycle: "/emojis/motorcycle.avif",
  motorized_wheelchair: "/emojis/motorized_wheelchair.avif",
  motorway: "/emojis/motorway.avif",
  mount_fuji: "/emojis/mount_fuji.avif",
  mountain: "/emojis/mountain.avif",
  mountain_bicyclist: "/emojis/mountain_bicyclist.avif",
  mountain_biking_man: "/emojis/mountain_biking_man.avif",
  mountain_biking_woman: "/emojis/mountain_biking_woman.avif",
  mountain_cableway: "/emojis/mountain_cableway.avif",
  mountain_railway: "/emojis/mountain_railway.avif",
  mountain_snow: "/emojis/mountain_snow.avif",
  mouse: "/emojis/mouse.avif",
  mouse2: "/emojis/mouse2.avif",
  mouse_trap: "/emojis/mouse_trap.avif",
  movie_camera: "/emojis/movie_camera.avif",
  moyai: "/emojis/moyai.avif",
  mozambique: "/emojis/mozambique.avif",
  mrs_claus: "/emojis/mrs_claus.avif",
  muscle: "/emojis/muscle.avif",
  mushroom: "/emojis/mushroom.avif",
  musical_keyboard: "/emojis/musical_keyboard.avif",
  musical_note: "/emojis/musical_note.avif",
  musical_score: "/emojis/musical_score.avif",
  mute: "/emojis/mute.avif",
  mx_claus: "/emojis/mx_claus.avif",
  myanmar: "/emojis/myanmar.avif",
  nail_care: "/emojis/nail_care.avif",
  name_badge: "/emojis/name_badge.avif",
  namibia: "/emojis/namibia.avif",
  national_park: "/emojis/national_park.avif",
  nauru: "/emojis/nauru.avif",
  nauseated_face: "/emojis/nauseated_face.avif",
  nazar_amulet: "/emojis/nazar_amulet.avif",
  neckbeard: "/emojis/neckbeard.avif",
  necktie: "/emojis/necktie.avif",
  negative_squared_cross_mark: "/emojis/negative_squared_cross_mark.avif",
  nepal: "/emojis/nepal.avif",
  nerd_face: "/emojis/nerd_face.avif",
  nesting_dolls: "/emojis/nesting_dolls.avif",
  netherlands: "/emojis/netherlands.avif",
  neutral_face: "/emojis/neutral_face.avif",
  new: "/emojis/new.avif",
  new_caledonia: "/emojis/new_caledonia.avif",
  new_moon: "/emojis/new_moon.avif",
  new_moon_with_face: "/emojis/new_moon_with_face.avif",
  new_zealand: "/emojis/new_zealand.avif",
  newspaper: "/emojis/newspaper.avif",
  newspaper_roll: "/emojis/newspaper_roll.avif",
  next_track_button: "/emojis/next_track_button.avif",
  ng: "/emojis/ng.avif",
  ng_man: "/emojis/ng_man.avif",
  ng_woman: "/emojis/ng_woman.avif",
  nicaragua: "/emojis/nicaragua.avif",
  niger: "/emojis/niger.avif",
  nigeria: "/emojis/nigeria.avif",
  night_with_stars: "/emojis/night_with_stars.avif",
  nine: "/emojis/nine.avif",
  ninja: "/emojis/ninja.avif",
  niue: "/emojis/niue.avif",
  no_bell: "/emojis/no_bell.avif",
  no_bicycles: "/emojis/no_bicycles.avif",
  no_entry: "/emojis/no_entry.avif",
  no_entry_sign: "/emojis/no_entry_sign.avif",
  no_good: "/emojis/no_good.avif",
  no_good_man: "/emojis/no_good_man.avif",
  no_good_woman: "/emojis/no_good_woman.avif",
  no_mobile_phones: "/emojis/no_mobile_phones.avif",
  no_mouth: "/emojis/no_mouth.avif",
  no_pedestrians: "/emojis/no_pedestrians.avif",
  no_smoking: "/emojis/no_smoking.avif",
  "non-potable_water": "/emojis/non-potable_water.avif",
  norfolk_island: "/emojis/norfolk_island.avif",
  north_korea: "/emojis/north_korea.avif",
  northern_mariana_islands: "/emojis/northern_mariana_islands.avif",
  norway: "/emojis/norway.avif",
  nose: "/emojis/nose.avif",
  notebook: "/emojis/notebook.avif",
  notebook_with_decorative_cover: "/emojis/notebook_with_decorative_cover.avif",
  notes: "/emojis/notes.avif",
  nut_and_bolt: "/emojis/nut_and_bolt.avif",
  o: "/emojis/o.avif",
  o2: "/emojis/o2.avif",
  ocean: "/emojis/ocean.avif",
  octocat: "/emojis/octocat.avif",
  octopus: "/emojis/octopus.avif",
  oden: "/emojis/oden.avif",
  office: "/emojis/office.avif",
  office_worker: "/emojis/office_worker.avif",
  oil_drum: "/emojis/oil_drum.avif",
  ok: "/emojis/ok.avif",
  ok_hand: "/emojis/ok_hand.avif",
  ok_man: "/emojis/ok_man.avif",
  ok_person: "/emojis/ok_person.avif",
  ok_woman: "/emojis/ok_woman.avif",
  old_key: "/emojis/old_key.avif",
  older_adult: "/emojis/older_adult.avif",
  older_man: "/emojis/older_man.avif",
  older_woman: "/emojis/older_woman.avif",
  olive: "/emojis/olive.avif",
  om: "/emojis/om.avif",
  oman: "/emojis/oman.avif",
  on: "/emojis/on.avif",
  oncoming_automobile: "/emojis/oncoming_automobile.avif",
  oncoming_bus: "/emojis/oncoming_bus.avif",
  oncoming_police_car: "/emojis/oncoming_police_car.avif",
  oncoming_taxi: "/emojis/oncoming_taxi.avif",
  one: "/emojis/one.avif",
  one_piece_swimsuit: "/emojis/one_piece_swimsuit.avif",
  onion: "/emojis/onion.avif",
  open_book: "/emojis/open_book.avif",
  open_file_folder: "/emojis/open_file_folder.avif",
  open_hands: "/emojis/open_hands.avif",
  open_mouth: "/emojis/open_mouth.avif",
  open_umbrella: "/emojis/open_umbrella.avif",
  ophiuchus: "/emojis/ophiuchus.avif",
  orange: "/emojis/orange.avif",
  orange_book: "/emojis/orange_book.avif",
  orange_circle: "/emojis/orange_circle.avif",
  orange_heart: "/emojis/orange_heart.avif",
  orange_square: "/emojis/orange_square.avif",
  orangutan: "/emojis/orangutan.avif",
  orthodox_cross: "/emojis/orthodox_cross.avif",
  otter: "/emojis/otter.avif",
  outbox_tray: "/emojis/outbox_tray.avif",
  owl: "/emojis/owl.avif",
  ox: "/emojis/ox.avif",
  oyster: "/emojis/oyster.avif",
  package: "/emojis/package.avif",
  page_facing_up: "/emojis/page_facing_up.avif",
  page_with_curl: "/emojis/page_with_curl.avif",
  pager: "/emojis/pager.avif",
  paintbrush: "/emojis/paintbrush.avif",
  pakistan: "/emojis/pakistan.avif",
  palau: "/emojis/palau.avif",
  palestinian_territories: "/emojis/palestinian_territories.avif",
  palm_tree: "/emojis/palm_tree.avif",
  palms_up_together: "/emojis/palms_up_together.avif",
  panama: "/emojis/panama.avif",
  pancakes: "/emojis/pancakes.avif",
  panda_face: "/emojis/panda_face.avif",
  paperclip: "/emojis/paperclip.avif",
  paperclips: "/emojis/paperclips.avif",
  papua_new_guinea: "/emojis/papua_new_guinea.avif",
  parachute: "/emojis/parachute.avif",
  paraguay: "/emojis/paraguay.avif",
  parasol_on_ground: "/emojis/parasol_on_ground.avif",
  parking: "/emojis/parking.avif",
  parrot: "/emojis/parrot.avif",
  part_alternation_mark: "/emojis/part_alternation_mark.avif",
  partly_sunny: "/emojis/partly_sunny.avif",
  partying_face: "/emojis/partying_face.avif",
  passenger_ship: "/emojis/passenger_ship.avif",
  passport_control: "/emojis/passport_control.avif",
  pause_button: "/emojis/pause_button.avif",
  paw_prints: "/emojis/paw_prints.avif",
  peace_symbol: "/emojis/peace_symbol.avif",
  peach: "/emojis/peach.avif",
  peacock: "/emojis/peacock.avif",
  peanuts: "/emojis/peanuts.avif",
  pear: "/emojis/pear.avif",
  pen: "/emojis/pen.avif",
  pencil: "/emojis/pencil.avif",
  pencil2: "/emojis/pencil2.avif",
  penguin: "/emojis/penguin.avif",
  pensive: "/emojis/pensive.avif",
  people_holding_hands: "/emojis/people_holding_hands.avif",
  people_hugging: "/emojis/people_hugging.avif",
  performing_arts: "/emojis/performing_arts.avif",
  persevere: "/emojis/persevere.avif",
  person_bald: "/emojis/person_bald.avif",
  person_curly_hair: "/emojis/person_curly_hair.avif",
  person_feeding_baby: "/emojis/person_feeding_baby.avif",
  person_fencing: "/emojis/person_fencing.avif",
  person_in_manual_wheelchair: "/emojis/person_in_manual_wheelchair.avif",
  person_in_motorized_wheelchair: "/emojis/person_in_motorized_wheelchair.avif",
  person_in_tuxedo: "/emojis/person_in_tuxedo.avif",
  person_red_hair: "/emojis/person_red_hair.avif",
  person_white_hair: "/emojis/person_white_hair.avif",
  person_with_probing_cane: "/emojis/person_with_probing_cane.avif",
  person_with_turban: "/emojis/person_with_turban.avif",
  person_with_veil: "/emojis/person_with_veil.avif",
  peru: "/emojis/peru.avif",
  petri_dish: "/emojis/petri_dish.avif",
  philippines: "/emojis/philippines.avif",
  phone: "/emojis/phone.avif",
  pick: "/emojis/pick.avif",
  pickup_truck: "/emojis/pickup_truck.avif",
  pie: "/emojis/pie.avif",
  pig: "/emojis/pig.avif",
  pig2: "/emojis/pig2.avif",
  pig_nose: "/emojis/pig_nose.avif",
  pill: "/emojis/pill.avif",
  pilot: "/emojis/pilot.avif",
  pinata: "/emojis/pinata.avif",
  pinched_fingers: "/emojis/pinched_fingers.avif",
  pinching_hand: "/emojis/pinching_hand.avif",
  pineapple: "/emojis/pineapple.avif",
  ping_pong: "/emojis/ping_pong.avif",
  pirate_flag: "/emojis/pirate_flag.avif",
  pisces: "/emojis/pisces.avif",
  pitcairn_islands: "/emojis/pitcairn_islands.avif",
  pizza: "/emojis/pizza.avif",
  placard: "/emojis/placard.avif",
  place_of_worship: "/emojis/place_of_worship.avif",
  plate_with_cutlery: "/emojis/plate_with_cutlery.avif",
  play_or_pause_button: "/emojis/play_or_pause_button.avif",
  pleading_face: "/emojis/pleading_face.avif",
  plunger: "/emojis/plunger.avif",
  point_down: "/emojis/point_down.avif",
  point_left: "/emojis/point_left.avif",
  point_right: "/emojis/point_right.avif",
  point_up: "/emojis/point_up.avif",
  point_up_2: "/emojis/point_up_2.avif",
  poland: "/emojis/poland.avif",
  polar_bear: "/emojis/polar_bear.avif",
  police_car: "/emojis/police_car.avif",
  police_officer: "/emojis/police_officer.avif",
  policeman: "/emojis/policeman.avif",
  policewoman: "/emojis/policewoman.avif",
  poodle: "/emojis/poodle.avif",
  poop: "/emojis/poop.avif",
  popcorn: "/emojis/popcorn.avif",
  portugal: "/emojis/portugal.avif",
  post_office: "/emojis/post_office.avif",
  postal_horn: "/emojis/postal_horn.avif",
  postbox: "/emojis/postbox.avif",
  potable_water: "/emojis/potable_water.avif",
  potato: "/emojis/potato.avif",
  potted_plant: "/emojis/potted_plant.avif",
  pouch: "/emojis/pouch.avif",
  poultry_leg: "/emojis/poultry_leg.avif",
  pound: "/emojis/pound.avif",
  pout: "/emojis/pout.avif",
  pouting_cat: "/emojis/pouting_cat.avif",
  pouting_face: "/emojis/pouting_face.avif",
  pouting_man: "/emojis/pouting_man.avif",
  pouting_woman: "/emojis/pouting_woman.avif",
  pray: "/emojis/pray.avif",
  prayer_beads: "/emojis/prayer_beads.avif",
  pregnant_woman: "/emojis/pregnant_woman.avif",
  pretzel: "/emojis/pretzel.avif",
  previous_track_button: "/emojis/previous_track_button.avif",
  prince: "/emojis/prince.avif",
  princess: "/emojis/princess.avif",
  printer: "/emojis/printer.avif",
  probing_cane: "/emojis/probing_cane.avif",
  puerto_rico: "/emojis/puerto_rico.avif",
  punch: "/emojis/punch.avif",
  purple_circle: "/emojis/purple_circle.avif",
  purple_heart: "/emojis/purple_heart.avif",
  purple_square: "/emojis/purple_square.avif",
  purse: "/emojis/purse.avif",
  pushpin: "/emojis/pushpin.avif",
  put_litter_in_its_place: "/emojis/put_litter_in_its_place.avif",
  qatar: "/emojis/qatar.avif",
  question: "/emojis/question.avif",
  rabbit: "/emojis/rabbit.avif",
  rabbit2: "/emojis/rabbit2.avif",
  raccoon: "/emojis/raccoon.avif",
  racehorse: "/emojis/racehorse.avif",
  racing_car: "/emojis/racing_car.avif",
  radio: "/emojis/radio.avif",
  radio_button: "/emojis/radio_button.avif",
  radioactive: "/emojis/radioactive.avif",
  rage: "/emojis/rage.avif",
  rage1: "/emojis/rage1.avif",
  rage2: "/emojis/rage2.avif",
  rage3: "/emojis/rage3.avif",
  rage4: "/emojis/rage4.avif",
  railway_car: "/emojis/railway_car.avif",
  railway_track: "/emojis/railway_track.avif",
  rainbow: "/emojis/rainbow.avif",
  rainbow_flag: "/emojis/rainbow_flag.avif",
  raised_back_of_hand: "/emojis/raised_back_of_hand.avif",
  raised_eyebrow: "/emojis/raised_eyebrow.avif",
  raised_hand: "/emojis/raised_hand.avif",
  raised_hand_with_fingers_splayed: "/emojis/raised_hand_with_fingers_splayed.avif",
  raised_hands: "/emojis/raised_hands.avif",
  raising_hand: "/emojis/raising_hand.avif",
  raising_hand_man: "/emojis/raising_hand_man.avif",
  raising_hand_woman: "/emojis/raising_hand_woman.avif",
  ram: "/emojis/ram.avif",
  ramen: "/emojis/ramen.avif",
  rat: "/emojis/rat.avif",
  razor: "/emojis/razor.avif",
  receipt: "/emojis/receipt.avif",
  record_button: "/emojis/record_button.avif",
  recycle: "/emojis/recycle.avif",
  red_car: "/emojis/red_car.avif",
  red_circle: "/emojis/red_circle.avif",
  red_envelope: "/emojis/red_envelope.avif",
  red_haired_man: "/emojis/red_haired_man.avif",
  red_haired_woman: "/emojis/red_haired_woman.avif",
  red_square: "/emojis/red_square.avif",
  registered: "/emojis/registered.avif",
  relaxed: "/emojis/relaxed.avif",
  relieved: "/emojis/relieved.avif",
  reminder_ribbon: "/emojis/reminder_ribbon.avif",
  repeat: "/emojis/repeat.avif",
  repeat_one: "/emojis/repeat_one.avif",
  rescue_worker_helmet: "/emojis/rescue_worker_helmet.avif",
  restroom: "/emojis/restroom.avif",
  reunion: "/emojis/reunion.avif",
  revolving_hearts: "/emojis/revolving_hearts.avif",
  rewind: "/emojis/rewind.avif",
  rhinoceros: "/emojis/rhinoceros.avif",
  ribbon: "/emojis/ribbon.avif",
  rice: "/emojis/rice.avif",
  rice_ball: "/emojis/rice_ball.avif",
  rice_cracker: "/emojis/rice_cracker.avif",
  rice_scene: "/emojis/rice_scene.avif",
  right_anger_bubble: "/emojis/right_anger_bubble.avif",
  ring: "/emojis/ring.avif",
  ringed_planet: "/emojis/ringed_planet.avif",
  robot: "/emojis/robot.avif",
  rock: "/emojis/rock.avif",
  rocket: "/emojis/rocket.avif",
  rofl: "/emojis/rofl.avif",
  roll_eyes: "/emojis/roll_eyes.avif",
  roll_of_paper: "/emojis/roll_of_paper.avif",
  roller_coaster: "/emojis/roller_coaster.avif",
  roller_skate: "/emojis/roller_skate.avif",
  romania: "/emojis/romania.avif",
  rooster: "/emojis/rooster.avif",
  rose: "/emojis/rose.avif",
  rosette: "/emojis/rosette.avif",
  rotating_light: "/emojis/rotating_light.avif",
  round_pushpin: "/emojis/round_pushpin.avif",
  rowboat: "/emojis/rowboat.avif",
  rowing_man: "/emojis/rowing_man.avif",
  rowing_woman: "/emojis/rowing_woman.avif",
  ru: "/emojis/ru.avif",
  rugby_football: "/emojis/rugby_football.avif",
  runner: "/emojis/runner.avif",
  running: "/emojis/running.avif",
  running_man: "/emojis/running_man.avif",
  running_shirt_with_sash: "/emojis/running_shirt_with_sash.avif",
  running_woman: "/emojis/running_woman.avif",
  rwanda: "/emojis/rwanda.avif",
  sa: "/emojis/sa.avif",
  safety_pin: "/emojis/safety_pin.avif",
  safety_vest: "/emojis/safety_vest.avif",
  sagittarius: "/emojis/sagittarius.avif",
  sailboat: "/emojis/sailboat.avif",
  sake: "/emojis/sake.avif",
  salt: "/emojis/salt.avif",
  samoa: "/emojis/samoa.avif",
  san_marino: "/emojis/san_marino.avif",
  sandal: "/emojis/sandal.avif",
  sandwich: "/emojis/sandwich.avif",
  santa: "/emojis/santa.avif",
  sao_tome_principe: "/emojis/sao_tome_principe.avif",
  sari: "/emojis/sari.avif",
  sassy_man: "/emojis/sassy_man.avif",
  sassy_woman: "/emojis/sassy_woman.avif",
  satellite: "/emojis/satellite.avif",
  satisfied: "/emojis/satisfied.avif",
  saudi_arabia: "/emojis/saudi_arabia.avif",
  sauna_man: "/emojis/sauna_man.avif",
  sauna_person: "/emojis/sauna_person.avif",
  sauna_woman: "/emojis/sauna_woman.avif",
  sauropod: "/emojis/sauropod.avif",
  saxophone: "/emojis/saxophone.avif",
  scarf: "/emojis/scarf.avif",
  school: "/emojis/school.avif",
  school_satchel: "/emojis/school_satchel.avif",
  scientist: "/emojis/scientist.avif",
  scissors: "/emojis/scissors.avif",
  scorpion: "/emojis/scorpion.avif",
  scorpius: "/emojis/scorpius.avif",
  scotland: "/emojis/scotland.avif",
  scream: "/emojis/scream.avif",
  scream_cat: "/emojis/scream_cat.avif",
  screwdriver: "/emojis/screwdriver.avif",
  scroll: "/emojis/scroll.avif",
  seal: "/emojis/seal.avif",
  seat: "/emojis/seat.avif",
  secret: "/emojis/secret.avif",
  see_no_evil: "/emojis/see_no_evil.avif",
  seedling: "/emojis/seedling.avif",
  selfie: "/emojis/selfie.avif",
  senegal: "/emojis/senegal.avif",
  serbia: "/emojis/serbia.avif",
  service_dog: "/emojis/service_dog.avif",
  seven: "/emojis/seven.avif",
  sewing_needle: "/emojis/sewing_needle.avif",
  seychelles: "/emojis/seychelles.avif",
  shallow_pan_of_food: "/emojis/shallow_pan_of_food.avif",
  shamrock: "/emojis/shamrock.avif",
  shark: "/emojis/shark.avif",
  shaved_ice: "/emojis/shaved_ice.avif",
  sheep: "/emojis/sheep.avif",
  shell: "/emojis/shell.avif",
  shield: "/emojis/shield.avif",
  shinto_shrine: "/emojis/shinto_shrine.avif",
  ship: "/emojis/ship.avif",
  shipit: "/emojis/shipit.avif",
  shirt: "/emojis/shirt.avif",
  shit: "/emojis/shit.avif",
  shoe: "/emojis/shoe.avif",
  shopping: "/emojis/shopping.avif",
  shopping_cart: "/emojis/shopping_cart.avif",
  shorts: "/emojis/shorts.avif",
  shower: "/emojis/shower.avif",
  shrimp: "/emojis/shrimp.avif",
  shrug: "/emojis/shrug.avif",
  shushing_face: "/emojis/shushing_face.avif",
  sierra_leone: "/emojis/sierra_leone.avif",
  signal_strength: "/emojis/signal_strength.avif",
  singapore: "/emojis/singapore.avif",
  singer: "/emojis/singer.avif",
  sint_maarten: "/emojis/sint_maarten.avif",
  six: "/emojis/six.avif",
  six_pointed_star: "/emojis/six_pointed_star.avif",
  skateboard: "/emojis/skateboard.avif",
  ski: "/emojis/ski.avif",
  skier: "/emojis/skier.avif",
  skull: "/emojis/skull.avif",
  skull_and_crossbones: "/emojis/skull_and_crossbones.avif",
  skunk: "/emojis/skunk.avif",
  sled: "/emojis/sled.avif",
  sleeping: "/emojis/sleeping.avif",
  sleeping_bed: "/emojis/sleeping_bed.avif",
  sleepy: "/emojis/sleepy.avif",
  slightly_frowning_face: "/emojis/slightly_frowning_face.avif",
  slightly_smiling_face: "/emojis/slightly_smiling_face.avif",
  slot_machine: "/emojis/slot_machine.avif",
  sloth: "/emojis/sloth.avif",
  slovakia: "/emojis/slovakia.avif",
  slovenia: "/emojis/slovenia.avif",
  small_airplane: "/emojis/small_airplane.avif",
  small_blue_diamond: "/emojis/small_blue_diamond.avif",
  small_orange_diamond: "/emojis/small_orange_diamond.avif",
  small_red_triangle: "/emojis/small_red_triangle.avif",
  small_red_triangle_down: "/emojis/small_red_triangle_down.avif",
  smile: "/emojis/smile.avif",
  smile_cat: "/emojis/smile_cat.avif",
  smiley: "/emojis/smiley.avif",
  smiley_cat: "/emojis/smiley_cat.avif",
  smiling_face_with_tear: "/emojis/smiling_face_with_tear.avif",
  smiling_face_with_three_hearts: "/emojis/smiling_face_with_three_hearts.avif",
  smiling_imp: "/emojis/smiling_imp.avif",
  smirk: "/emojis/smirk.avif",
  smirk_cat: "/emojis/smirk_cat.avif",
  smoking: "/emojis/smoking.avif",
  snail: "/emojis/snail.avif",
  snake: "/emojis/snake.avif",
  sneezing_face: "/emojis/sneezing_face.avif",
  snowboarder: "/emojis/snowboarder.avif",
  snowflake: "/emojis/snowflake.avif",
  snowman: "/emojis/snowman.avif",
  snowman_with_snow: "/emojis/snowman_with_snow.avif",
  soap: "/emojis/soap.avif",
  sob: "/emojis/sob.avif",
  soccer: "/emojis/soccer.avif",
  socks: "/emojis/socks.avif",
  softball: "/emojis/softball.avif",
  solomon_islands: "/emojis/solomon_islands.avif",
  somalia: "/emojis/somalia.avif",
  soon: "/emojis/soon.avif",
  sos: "/emojis/sos.avif",
  sound: "/emojis/sound.avif",
  south_africa: "/emojis/south_africa.avif",
  south_georgia_south_sandwich_islands: "/emojis/south_georgia_south_sandwich_islands.avif",
  south_sudan: "/emojis/south_sudan.avif",
  space_invader: "/emojis/space_invader.avif",
  spades: "/emojis/spades.avif",
  spaghetti: "/emojis/spaghetti.avif",
  sparkle: "/emojis/sparkle.avif",
  sparkler: "/emojis/sparkler.avif",
  sparkles: "/emojis/sparkles.avif",
  sparkling_heart: "/emojis/sparkling_heart.avif",
  speak_no_evil: "/emojis/speak_no_evil.avif",
  speaker: "/emojis/speaker.avif",
  speaking_head: "/emojis/speaking_head.avif",
  speech_balloon: "/emojis/speech_balloon.avif",
  speedboat: "/emojis/speedboat.avif",
  spider: "/emojis/spider.avif",
  spider_web: "/emojis/spider_web.avif",
  spiral_calendar: "/emojis/spiral_calendar.avif",
  spiral_notepad: "/emojis/spiral_notepad.avif",
  sponge: "/emojis/sponge.avif",
  spoon: "/emojis/spoon.avif",
  squid: "/emojis/squid.avif",
  sri_lanka: "/emojis/sri_lanka.avif",
  st_barthelemy: "/emojis/st_barthelemy.avif",
  st_helena: "/emojis/st_helena.avif",
  st_kitts_nevis: "/emojis/st_kitts_nevis.avif",
  st_lucia: "/emojis/st_lucia.avif",
  st_martin: "/emojis/st_martin.avif",
  st_pierre_miquelon: "/emojis/st_pierre_miquelon.avif",
  st_vincent_grenadines: "/emojis/st_vincent_grenadines.avif",
  stadium: "/emojis/stadium.avif",
  standing_man: "/emojis/standing_man.avif",
  standing_person: "/emojis/standing_person.avif",
  standing_woman: "/emojis/standing_woman.avif",
  star: "/emojis/star.avif",
  star2: "/emojis/star2.avif",
  star_and_crescent: "/emojis/star_and_crescent.avif",
  star_of_david: "/emojis/star_of_david.avif",
  star_struck: "/emojis/star_struck.avif",
  stars: "/emojis/stars.avif",
  station: "/emojis/station.avif",
  statue_of_liberty: "/emojis/statue_of_liberty.avif",
  steam_locomotive: "/emojis/steam_locomotive.avif",
  stethoscope: "/emojis/stethoscope.avif",
  stew: "/emojis/stew.avif",
  stop_button: "/emojis/stop_button.avif",
  stop_sign: "/emojis/stop_sign.avif",
  stopwatch: "/emojis/stopwatch.avif",
  straight_ruler: "/emojis/straight_ruler.avif",
  strawberry: "/emojis/strawberry.avif",
  stuck_out_tongue: "/emojis/stuck_out_tongue.avif",
  stuck_out_tongue_closed_eyes: "/emojis/stuck_out_tongue_closed_eyes.avif",
  stuck_out_tongue_winking_eye: "/emojis/stuck_out_tongue_winking_eye.avif",
  student: "/emojis/student.avif",
  studio_microphone: "/emojis/studio_microphone.avif",
  stuffed_flatbread: "/emojis/stuffed_flatbread.avif",
  sudan: "/emojis/sudan.avif",
  sun_behind_large_cloud: "/emojis/sun_behind_large_cloud.avif",
  sun_behind_rain_cloud: "/emojis/sun_behind_rain_cloud.avif",
  sun_behind_small_cloud: "/emojis/sun_behind_small_cloud.avif",
  sun_with_face: "/emojis/sun_with_face.avif",
  sunflower: "/emojis/sunflower.avif",
  sunglasses: "/emojis/sunglasses.avif",
  sunny: "/emojis/sunny.avif",
  sunrise: "/emojis/sunrise.avif",
  sunrise_over_mountains: "/emojis/sunrise_over_mountains.avif",
  superhero: "/emojis/superhero.avif",
  superhero_man: "/emojis/superhero_man.avif",
  superhero_woman: "/emojis/superhero_woman.avif",
  supervillain: "/emojis/supervillain.avif",
  supervillain_man: "/emojis/supervillain_man.avif",
  supervillain_woman: "/emojis/supervillain_woman.avif",
  surfer: "/emojis/surfer.avif",
  surfing_man: "/emojis/surfing_man.avif",
  surfing_woman: "/emojis/surfing_woman.avif",
  suriname: "/emojis/suriname.avif",
  sushi: "/emojis/sushi.avif",
  suspect: "/emojis/suspect.avif",
  suspension_railway: "/emojis/suspension_railway.avif",
  svalbard_jan_mayen: "/emojis/svalbard_jan_mayen.avif",
  swan: "/emojis/swan.avif",
  swaziland: "/emojis/swaziland.avif",
  sweat: "/emojis/sweat.avif",
  sweat_drops: "/emojis/sweat_drops.avif",
  sweat_smile: "/emojis/sweat_smile.avif",
  sweden: "/emojis/sweden.avif",
  sweet_potato: "/emojis/sweet_potato.avif",
  swim_brief: "/emojis/swim_brief.avif",
  swimmer: "/emojis/swimmer.avif",
  swimming_man: "/emojis/swimming_man.avif",
  swimming_woman: "/emojis/swimming_woman.avif",
  switzerland: "/emojis/switzerland.avif",
  symbols: "/emojis/symbols.avif",
  synagogue: "/emojis/synagogue.avif",
  syria: "/emojis/syria.avif",
  syringe: "/emojis/syringe.avif",
  "t-rex": "/emojis/t-rex.avif",
  taco: "/emojis/taco.avif",
  tada: "/emojis/tada.avif",
  taiwan: "/emojis/taiwan.avif",
  tajikistan: "/emojis/tajikistan.avif",
  takeout_box: "/emojis/takeout_box.avif",
  tamale: "/emojis/tamale.avif",
  tanabata_tree: "/emojis/tanabata_tree.avif",
  tangerine: "/emojis/tangerine.avif",
  tanzania: "/emojis/tanzania.avif",
  taurus: "/emojis/taurus.avif",
  taxi: "/emojis/taxi.avif",
  tea: "/emojis/tea.avif",
  teacher: "/emojis/teacher.avif",
  teapot: "/emojis/teapot.avif",
  technologist: "/emojis/technologist.avif",
  teddy_bear: "/emojis/teddy_bear.avif",
  telephone: "/emojis/telephone.avif",
  telephone_receiver: "/emojis/telephone_receiver.avif",
  telescope: "/emojis/telescope.avif",
  tennis: "/emojis/tennis.avif",
  tent: "/emojis/tent.avif",
  test_tube: "/emojis/test_tube.avif",
  thailand: "/emojis/thailand.avif",
  thermometer: "/emojis/thermometer.avif",
  thinking: "/emojis/thinking.avif",
  thong_sandal: "/emojis/thong_sandal.avif",
  thought_balloon: "/emojis/thought_balloon.avif",
  thread: "/emojis/thread.avif",
  three: "/emojis/three.avif",
  thumbsdown: "/emojis/thumbsdown.avif",
  thumbsup: "/emojis/thumbsup.avif",
  ticket: "/emojis/ticket.avif",
  tickets: "/emojis/tickets.avif",
  tiger: "/emojis/tiger.avif",
  tiger2: "/emojis/tiger2.avif",
  timer_clock: "/emojis/timer_clock.avif",
  timor_leste: "/emojis/timor_leste.avif",
  tipping_hand_man: "/emojis/tipping_hand_man.avif",
  tipping_hand_person: "/emojis/tipping_hand_person.avif",
  tipping_hand_woman: "/emojis/tipping_hand_woman.avif",
  tired_face: "/emojis/tired_face.avif",
  tm: "/emojis/tm.avif",
  togo: "/emojis/togo.avif",
  toilet: "/emojis/toilet.avif",
  tokelau: "/emojis/tokelau.avif",
  tokyo_tower: "/emojis/tokyo_tower.avif",
  tomato: "/emojis/tomato.avif",
  tonga: "/emojis/tonga.avif",
  tongue: "/emojis/tongue.avif",
  toolbox: "/emojis/toolbox.avif",
  tooth: "/emojis/tooth.avif",
  toothbrush: "/emojis/toothbrush.avif",
  top: "/emojis/top.avif",
  tophat: "/emojis/tophat.avif",
  tornado: "/emojis/tornado.avif",
  tr: "/emojis/tr.avif",
  trackball: "/emojis/trackball.avif",
  tractor: "/emojis/tractor.avif",
  traffic_light: "/emojis/traffic_light.avif",
  train: "/emojis/train.avif",
  train2: "/emojis/train2.avif",
  tram: "/emojis/tram.avif",
  transgender_flag: "/emojis/transgender_flag.avif",
  transgender_symbol: "/emojis/transgender_symbol.avif",
  triangular_flag_on_post: "/emojis/triangular_flag_on_post.avif",
  triangular_ruler: "/emojis/triangular_ruler.avif",
  trident: "/emojis/trident.avif",
  trinidad_tobago: "/emojis/trinidad_tobago.avif",
  tristan_da_cunha: "/emojis/tristan_da_cunha.avif",
  triumph: "/emojis/triumph.avif",
  trolleybus: "/emojis/trolleybus.avif",
  trollface: "/emojis/trollface.avif",
  trophy: "/emojis/trophy.avif",
  tropical_drink: "/emojis/tropical_drink.avif",
  tropical_fish: "/emojis/tropical_fish.avif",
  truck: "/emojis/truck.avif",
  trumpet: "/emojis/trumpet.avif",
  tshirt: "/emojis/tshirt.avif",
  tulip: "/emojis/tulip.avif",
  tumbler_glass: "/emojis/tumbler_glass.avif",
  tunisia: "/emojis/tunisia.avif",
  turkey: "/emojis/turkey.avif",
  turkmenistan: "/emojis/turkmenistan.avif",
  turks_caicos_islands: "/emojis/turks_caicos_islands.avif",
  turtle: "/emojis/turtle.avif",
  tuvalu: "/emojis/tuvalu.avif",
  tv: "/emojis/tv.avif",
  twisted_rightwards_arrows: "/emojis/twisted_rightwards_arrows.avif",
  two: "/emojis/two.avif",
  two_hearts: "/emojis/two_hearts.avif",
  two_men_holding_hands: "/emojis/two_men_holding_hands.avif",
  two_women_holding_hands: "/emojis/two_women_holding_hands.avif",
  u5272: "/emojis/u5272.avif",
  u5408: "/emojis/u5408.avif",
  u55b6: "/emojis/u55b6.avif",
  u6307: "/emojis/u6307.avif",
  u6708: "/emojis/u6708.avif",
  u6709: "/emojis/u6709.avif",
  u6e80: "/emojis/u6e80.avif",
  u7121: "/emojis/u7121.avif",
  u7533: "/emojis/u7533.avif",
  u7981: "/emojis/u7981.avif",
  u7a7a: "/emojis/u7a7a.avif",
  uganda: "/emojis/uganda.avif",
  uk: "/emojis/uk.avif",
  ukraine: "/emojis/ukraine.avif",
  umbrella: "/emojis/umbrella.avif",
  unamused: "/emojis/unamused.avif",
  underage: "/emojis/underage.avif",
  unicorn: "/emojis/unicorn.avif",
  united_arab_emirates: "/emojis/united_arab_emirates.avif",
  united_nations: "/emojis/united_nations.avif",
  unlock: "/emojis/unlock.avif",
  up: "/emojis/up.avif",
  upside_down_face: "/emojis/upside_down_face.avif",
  uruguay: "/emojis/uruguay.avif",
  us: "/emojis/us.avif",
  us_outlying_islands: "/emojis/us_outlying_islands.avif",
  us_virgin_islands: "/emojis/us_virgin_islands.avif",
  uzbekistan: "/emojis/uzbekistan.avif",
  v: "/emojis/v.avif",
  vampire: "/emojis/vampire.avif",
  vampire_man: "/emojis/vampire_man.avif",
  vampire_woman: "/emojis/vampire_woman.avif",
  vanuatu: "/emojis/vanuatu.avif",
  vatican_city: "/emojis/vatican_city.avif",
  venezuela: "/emojis/venezuela.avif",
  vertical_traffic_light: "/emojis/vertical_traffic_light.avif",
  vhs: "/emojis/vhs.avif",
  vibration_mode: "/emojis/vibration_mode.avif",
  video_camera: "/emojis/video_camera.avif",
  video_game: "/emojis/video_game.avif",
  vietnam: "/emojis/vietnam.avif",
  violin: "/emojis/violin.avif",
  virgo: "/emojis/virgo.avif",
  volcano: "/emojis/volcano.avif",
  volleyball: "/emojis/volleyball.avif",
  vomiting_face: "/emojis/vomiting_face.avif",
  vs: "/emojis/vs.avif",
  vulcan_salute: "/emojis/vulcan_salute.avif",
  waffle: "/emojis/waffle.avif",
  wales: "/emojis/wales.avif",
  walking: "/emojis/walking.avif",
  walking_man: "/emojis/walking_man.avif",
  walking_woman: "/emojis/walking_woman.avif",
  wallis_futuna: "/emojis/wallis_futuna.avif",
  waning_crescent_moon: "/emojis/waning_crescent_moon.avif",
  waning_gibbous_moon: "/emojis/waning_gibbous_moon.avif",
  warning: "/emojis/warning.avif",
  wastebasket: "/emojis/wastebasket.avif",
  watch: "/emojis/watch.avif",
  water_buffalo: "/emojis/water_buffalo.avif",
  water_polo: "/emojis/water_polo.avif",
  watermelon: "/emojis/watermelon.avif",
  wave: "/emojis/wave.avif",
  wavy_dash: "/emojis/wavy_dash.avif",
  waxing_crescent_moon: "/emojis/waxing_crescent_moon.avif",
  waxing_gibbous_moon: "/emojis/waxing_gibbous_moon.avif",
  wc: "/emojis/wc.avif",
  weary: "/emojis/weary.avif",
  wedding: "/emojis/wedding.avif",
  weight_lifting: "/emojis/weight_lifting.avif",
  weight_lifting_man: "/emojis/weight_lifting_man.avif",
  weight_lifting_woman: "/emojis/weight_lifting_woman.avif",
  western_sahara: "/emojis/western_sahara.avif",
  whale: "/emojis/whale.avif",
  whale2: "/emojis/whale2.avif",
  wheel_of_dharma: "/emojis/wheel_of_dharma.avif",
  wheelchair: "/emojis/wheelchair.avif",
  white_check_mark: "/emojis/white_check_mark.avif",
  white_circle: "/emojis/white_circle.avif",
  white_flag: "/emojis/white_flag.avif",
  white_flower: "/emojis/white_flower.avif",
  white_haired_man: "/emojis/white_haired_man.avif",
  white_haired_woman: "/emojis/white_haired_woman.avif",
  white_heart: "/emojis/white_heart.avif",
  white_large_square: "/emojis/white_large_square.avif",
  white_medium_small_square: "/emojis/white_medium_small_square.avif",
  white_medium_square: "/emojis/white_medium_square.avif",
  white_small_square: "/emojis/white_small_square.avif",
  white_square_button: "/emojis/white_square_button.avif",
  wilted_flower: "/emojis/wilted_flower.avif",
  wind_chime: "/emojis/wind_chime.avif",
  wind_face: "/emojis/wind_face.avif",
  window: "/emojis/window.avif",
  wine_glass: "/emojis/wine_glass.avif",
  wink: "/emojis/wink.avif",
  wolf: "/emojis/wolf.avif",
  woman: "/emojis/woman.avif",
  woman_artist: "/emojis/woman_artist.avif",
  woman_astronaut: "/emojis/woman_astronaut.avif",
  woman_beard: "/emojis/woman_beard.avif",
  woman_cartwheeling: "/emojis/woman_cartwheeling.avif",
  woman_cook: "/emojis/woman_cook.avif",
  woman_dancing: "/emojis/woman_dancing.avif",
  woman_facepalming: "/emojis/woman_facepalming.avif",
  woman_factory_worker: "/emojis/woman_factory_worker.avif",
  woman_farmer: "/emojis/woman_farmer.avif",
  woman_feeding_baby: "/emojis/woman_feeding_baby.avif",
  woman_firefighter: "/emojis/woman_firefighter.avif",
  woman_health_worker: "/emojis/woman_health_worker.avif",
  woman_in_manual_wheelchair: "/emojis/woman_in_manual_wheelchair.avif",
  woman_in_motorized_wheelchair: "/emojis/woman_in_motorized_wheelchair.avif",
  woman_in_tuxedo: "/emojis/woman_in_tuxedo.avif",
  woman_judge: "/emojis/woman_judge.avif",
  woman_juggling: "/emojis/woman_juggling.avif",
  woman_mechanic: "/emojis/woman_mechanic.avif",
  woman_office_worker: "/emojis/woman_office_worker.avif",
  woman_pilot: "/emojis/woman_pilot.avif",
  woman_playing_handball: "/emojis/woman_playing_handball.avif",
  woman_playing_water_polo: "/emojis/woman_playing_water_polo.avif",
  woman_scientist: "/emojis/woman_scientist.avif",
  woman_shrugging: "/emojis/woman_shrugging.avif",
  woman_singer: "/emojis/woman_singer.avif",
  woman_student: "/emojis/woman_student.avif",
  woman_teacher: "/emojis/woman_teacher.avif",
  woman_technologist: "/emojis/woman_technologist.avif",
  woman_with_headscarf: "/emojis/woman_with_headscarf.avif",
  woman_with_probing_cane: "/emojis/woman_with_probing_cane.avif",
  woman_with_turban: "/emojis/woman_with_turban.avif",
  woman_with_veil: "/emojis/woman_with_veil.avif",
  womans_clothes: "/emojis/womans_clothes.avif",
  womans_hat: "/emojis/womans_hat.avif",
  women_wrestling: "/emojis/women_wrestling.avif",
  womens: "/emojis/womens.avif",
  wood: "/emojis/wood.avif",
  woozy_face: "/emojis/woozy_face.avif",
  world_map: "/emojis/world_map.avif",
  worm: "/emojis/worm.avif",
  worried: "/emojis/worried.avif",
  wrench: "/emojis/wrench.avif",
  wrestling: "/emojis/wrestling.avif",
  writing_hand: "/emojis/writing_hand.avif",
  x: "/emojis/x.avif",
  yarn: "/emojis/yarn.avif",
  yawning_face: "/emojis/yawning_face.avif",
  yellow_circle: "/emojis/yellow_circle.avif",
  yellow_heart: "/emojis/yellow_heart.avif",
  yellow_square: "/emojis/yellow_square.avif",
  yemen: "/emojis/yemen.avif",
  yen: "/emojis/yen.avif",
  yin_yang: "/emojis/yin_yang.avif",
  yo_yo: "/emojis/yo_yo.avif",
  yum: "/emojis/yum.avif",
  zambia: "/emojis/zambia.avif",
  zany_face: "/emojis/zany_face.avif",
  zap: "/emojis/zap.avif",
  zebra: "/emojis/zebra.avif",
  zero: "/emojis/zero.avif",
  zimbabwe: "/emojis/zimbabwe.avif",
  zipper_mouth_face: "/emojis/zipper_mouth_face.avif",
  zombie: "/emojis/zombie.avif",
  zombie_man: "/emojis/zombie_man.avif",
  zombie_woman: "/emojis/zombie_woman.avif",
  zzz: "/emojis/zzz.avif"
};
const Bold = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 24 24" },
      { id: "bold-text" }
    ],
    {}
  )}><path fill="none" d="M0 0h24v24H0V0z"></path><path fill="currentColor" d="M15.6 10.79c.97-.67 1.65-1.77 1.65-2.79 0-2.26-1.75-4-4-4H8c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h5.78c2.07 0 3.96-1.69 3.97-3.77.01-1.53-.85-2.84-2.15-3.44zM10 6.5h3c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5h-3v-3zm3.5 9H10v-3h3.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5z"></path></svg>`;
});
const Code = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 24 24" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M8 8L3 12L8 16M16 16L21 12L16 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Hyperlink = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 24 24" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path fill-rule="evenodd" clip-rule="evenodd" d="M10.975 14.51a1.05 1.05 0 0 0 0-1.485 2.95 2.95 0 0 1 0-4.172l3.536-3.535a2.95 2.95 0 1 1 4.172 4.172l-1.093 1.092a1.05 1.05 0 0 0 1.485 1.485l1.093-1.092a5.05 5.05 0 0 0-7.142-7.142L9.49 7.368a5.05 5.05 0 0 0 0 7.142c.41.41 1.075.41 1.485 0zm2.05-5.02a1.05 1.05 0 0 0 0 1.485 2.95 2.95 0 0 1 0 4.172l-3.5 3.5a2.95 2.95 0 1 1-4.171-4.172l1.025-1.025a1.05 1.05 0 0 0-1.485-1.485L3.87 12.99a5.05 5.05 0 0 0 7.142 7.142l3.5-3.5a5.05 5.05 0 0 0 0-7.142 1.05 1.05 0 0 0-1.485 0z" fill="currentColor"></path></svg>`;
});
const Italic = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 24 24" },
      { xmlns: "http://www.w3.org/2000/svg" },
      { fill: "currentColor" }
    ],
    {}
  )}><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6h4m4 0h-4m0 0-4 12m0 0h4m-4 0H6"></path></svg>`;
});
const Strike = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 24 24" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path fill-rule="evenodd" clip-rule="evenodd" d="M12.1818 4.5H12.2572C14.6518 4.49998 16.06 5.70029 16.6667 6.27002C17.0694 6.64806 17.0893 7.28091 16.7112 7.68353C16.3332 8.08615 15.7003 8.10606 15.2977 7.72803C14.8402 7.2984 13.9043 6.5 12.2572 6.5H12.1818C11.3372 6.5 10.5747 7.0042 10.2433 7.78217C9.76004 8.91658 10.3492 10.2218 11.5197 10.6097L12.6975 11H19C19.5523 11 20 11.4477 20 12C20 12.5523 19.5523 13 19 13H5C4.44772 13 4 12.5523 4 12C4 11.4477 4.44772 11 5 11H8.84183C8.04044 9.87767 7.81744 8.37359 8.40331 6.99832C9.04851 5.48375 10.5346 4.5 12.1818 4.5ZM14.3007 14H16.6374C17.0712 15.0358 17.1365 16.2306 16.7304 17.3744C16.0672 19.2426 14.2995 20.4908 12.317 20.4908H11.725C9.84848 20.4908 8.54549 19.8758 7.31543 18.7208C6.91281 18.3428 6.8929 17.7099 7.27094 17.3073C7.64899 16.9047 8.28183 16.8848 8.68445 17.2628C9.58301 18.1065 10.4086 18.4908 11.725 18.4908H12.317C13.4529 18.4908 14.4657 17.7757 14.8456 16.7053C15.1889 15.7383 14.9443 14.7076 14.3007 14Z" fill="currentColor"></path></svg>`;
});
const Underline = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { fill: "currentColor" },
      { xmlns: "http://www.w3.org/2000/svg" },
      { viewBox: "0 0 52 52" },
      { "enable-background": "new 0 0 52 52" },
      { "xml:space": "preserve" }
    ],
    {}
  )}><path d="M44.5,42h-37C6.7,42,6,42.7,6,43.5v3C6,47.3,6.7,48,7.5,48h37c0.8,0,1.5-0.7,1.5-1.5v-3
	C46,42.7,45.3,42,44.5,42z"></path><g><path d="M25.3,38C17.8,37.6,12,31.1,12,23.6L12,10c0-1.1,0.9-2,2-2h2c1.1,0,2,0.9,2,2l0,13.7c0,4.3,3.2,8,7.5,8.3
		c4.7,0.3,8.5-3.4,8.5-8V10c0-1.1,0.9-2,2-2h2c1.1,0,2,0.9,2,2v14C40,32,33.3,38.4,25.3,38z"></path></g></svg>`;
});
async function sanitize(_text) {
  const text = await _text;
  return xss(text ?? "", {
    whiteList: {
      blockquote: ["class"],
      del: ["class"],
      p: ["class"],
      strong: ["class"],
      em: ["class"],
      b: ["class"],
      a: ["href", "class"],
      u: ["class"],
      i: ["class"],
      img: ["src", "alt", "class"],
      code: ["class"],
      pre: ["class"],
      span: ["class"],
      h1: ["class"],
      h2: ["class"],
      h3: ["class"],
      h4: ["class"],
      h5: ["class"]
    }
  });
}
const markdown_svelte_svelte_type_style_lang = "";
const css = {
  code: "markdown pre{border-radius:0.375rem !important;background-color:transparent !important;padding:0px !important\n}markdown code{background-color:rgb(var(--color-surface-400) / 0.5) !important;font-size:0.75rem;line-height:1rem;line-height:1.375\n}@media(min-width: 768px){markdown code{border-radius:0.5vw;padding:0.75rem;font-size:0.9vw;line-height:1.25vw\n    }}",
  map: null
};
const Markdown = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { markdown = "" } = $$props;
  let { class: klass = "" } = $$props;
  const emoji_options = { emojis, unicode: false };
  const marked = new Marked(
    // Highlight.js
    markedHighlight({
      langPrefix: "hljs language-",
      highlight: (code, lang) => {
        const language = hljs.getLanguage(lang) ? lang : "plaintext";
        return hljs.highlight(code, { language }).value;
      }
    }),
    // Emoji plugin
    markedEmoji(emoji_options),
    {
      extensions: [
        {
          name: "emoji",
          renderer: (token) => {
            return `<img class="inline-flex w-4 justify-center align-center -translate-y-0.5 md:w-[1vw]" alt="${token.name}" src="${token.emoji}">`;
          }
        }
      ]
    },
    // Smartypants plugin
    markedSmartypants(),
    // XHTML plugin
    markedXhtml(),
    // Mangle plugin
    mangle(),
    // Marked defaults
    {
      // We dont need github like header prefix
      headerIds: false
    }
  );
  let html;
  if ($$props.markdown === void 0 && $$bindings.markdown && markdown !== void 0)
    $$bindings.markdown(markdown);
  if ($$props.class === void 0 && $$bindings.class && klass !== void 0)
    $$bindings.class(klass);
  $$result.css.add(css);
  html = sanitize(marked.parse(markdown));
  return `<markdown${add_attribute("class", klass, 0)}>${function(__value) {
    if (is_promise(__value)) {
      __value.then(null, noop);
      return ``;
    }
    return function(html2) {
      return ` <!-- HTML_TAG_START -->${html2}<!-- HTML_TAG_END --> `;
    }(__value);
  }(html)} </markdown>`;
});
async function bold_text(element) {
  await operate_on_selected_text({
    element,
    starting_operator: "**",
    ending_operator: "**"
  });
}
async function italic_text(element) {
  await operate_on_selected_text({
    element,
    starting_operator: "_",
    ending_operator: "_"
  });
}
async function code_text(element) {
  await operate_on_selected_text({
    element,
    starting_operator: "`",
    ending_operator: "`"
  });
}
async function underline_text(element) {
  await operate_on_selected_text({
    element,
    starting_operator: "<u>",
    ending_operator: "</u>"
  });
}
async function strike_text(element) {
  await operate_on_selected_text({
    element,
    starting_operator: "~~",
    ending_operator: "~~"
  });
}
async function hyperlink_text(element) {
  const selection_start = element.selectionStart, selection_end = element.selectionEnd, selection_text = element.value.substring(selection_start, selection_end);
  if (element.value.substring(selection_start - 3, selection_start) == "[](" && element.value.substring(selection_end, selection_end + 1) == ")") {
    element.focus();
    element.setSelectionRange(selection_start - 3, selection_end + 1);
    document.execCommand("delete");
  } else {
    const replacement_text = `[${selection_text}]()`;
    await insert_text({
      target: element,
      text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
    });
    element.setSelectionRange(selection_start + selection_text.length + 3, selection_start + selection_text.length + 3);
  }
}
async function insert_text({ target, text }) {
  target.select();
  document.execCommand("insertText", false, text);
}
async function operate_on_selected_text({ element, starting_operator, ending_operator }) {
  element.focus();
  const selection_start = element.selectionStart, selection_end = element.selectionEnd, selection_text = element.value.substring(selection_start, selection_end);
  const regex_pattern_for_operator = new RegExp("^" + starting_operator.replace(/[|\\{}()[\]^$+*?.]/g, "\\$&") + "|" + ending_operator.replace(/[|\\{}()[\]^$+*?.]/g, "\\$&") + "$", "g");
  if (element.value.substring(selection_start - starting_operator.length, selection_start) == starting_operator && element.value.substring(selection_end, selection_end + ending_operator.length) == ending_operator) {
    if (selection_text) {
      const replacement_text = element.value.substring(selection_start - starting_operator.length, selection_end + ending_operator.length).replace(regex_pattern_for_operator, "");
      await insert_text({
        target: element,
        text: element.value.substring(0, selection_start - starting_operator.length) + replacement_text + element.value.substring(selection_end + ending_operator.length)
      });
      element.setSelectionRange(selection_start - starting_operator.length, selection_end - starting_operator.length);
    } else {
      element.focus();
      element.setSelectionRange(selection_start - starting_operator.length, selection_end + ending_operator.length);
      document.execCommand("delete", false);
    }
  } else if (element.value.substring(selection_start, selection_start + starting_operator.length) == starting_operator && element.value.substring(selection_end - ending_operator.length, selection_end) == ending_operator) {
    const replacement_text = element.value.substring(selection_start - starting_operator.length, selection_end + ending_operator.length).replace(regex_pattern_for_operator, "");
    await insert_text({
      target: element,
      text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
    });
    element.setSelectionRange(selection_start, selection_end - (starting_operator.length + ending_operator.length));
  } else {
    const replacement_text = starting_operator + selection_text + ending_operator;
    await insert_text({
      target: element,
      text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
    });
    element.setSelectionRange(selection_start + starting_operator.length, selection_end + starting_operator.length);
  }
}
const Text_editor = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { textarea_value = "" } = $$props;
  let textarea_element;
  const icon_and_function_mapping = {
    bold: {
      function: (element) => bold_text(element),
      icon: {
        component: Bold,
        class: "w-5 md:w-[1.4vw]  text-surface-200"
      },
      description: "Add bold text, <Ctrl + b>"
    },
    italic: {
      function: (element) => italic_text(element),
      icon: {
        component: Italic,
        class: "w-5 md:w-[1.5vw] text-surface-200"
      },
      description: "Add italic text, <Ctrl + i>"
    },
    underline: {
      function: (element) => underline_text(element),
      icon: {
        component: Underline,
        class: "w-5 md:w-[1.35vw] text-surface-200"
      },
      description: "Add underline text, <Ctrl + u>"
    },
    strike: {
      function: (element) => strike_text(element),
      icon: {
        component: Strike,
        class: "w-5 md:w-[1.5vw] text-surface-200"
      },
      description: "Add strikethrough text, <Ctrl + Shift + x>"
    },
    code: {
      function: (element) => code_text(element),
      icon: {
        component: Code,
        class: "w-5 md:w-[1.5vw] text-surface-200"
      },
      description: "Add code text, <Ctrl + e>"
    },
    hyperlink: {
      function: (element) => hyperlink_text(element),
      icon: {
        component: Hyperlink,
        class: "w-4 md:w-[1.25vw] text-surface-200 ml-3 md:ml-[1vw]"
      },
      description: "Add hyperlinked text, <Ctrl + k>"
    }
  };
  let tab_type = "edit";
  if ($$props.textarea_value === void 0 && $$bindings.textarea_value && textarea_value !== void 0)
    $$bindings.textarea_value(textarea_value);
  return `<div class="relative rounded-lg ring-2 ring-surface-300/25 transition duration-300 focus-within:ring-primary-500 md:rounded-[0.75vw] md:ring-[0.15vw]"><textarea-navbar class="flex h-8 items-center justify-between overflow-hidden rounded-t-lg bg-surface-400/50 md:h-[2.5vw] md:rounded-t-[0.75vw]"><div>${each(["edit", "preview"], (item) => {
    let active = tab_type.toLowerCase() == item;
    return ` <button type="button" class="${escape(
      active ? "bg-surface-900 text-surface-50" : "text-surface-300",
      true
    ) + " h-8 px-5 text-xs capitalize leading-[1.5vw] transition-colors duration-100 md:h-[2.5vw] md:px-[1.5vw] md:text-[1vw]"}">${escape(item)} </button>`;
  })}</div> <div class="flex place-items-center gap-2 pr-4 md:gap-[0.75vw] md:pr-[1vw]">${each(Object.entries(icon_and_function_mapping), (item) => {
    let item_label = item[0], icon = item[1].icon.component, icon_class = item[1].icon.class;
    item[1].function;
    item[1].description;
    return `     <button class="${"btn p-0 " + escape(icon_class, true)}" type="button"${add_attribute("aria-label", item_label, 0)}>${validate_component(icon || missing_component, "svelte:component").$$render($$result, {}, {}, {})} </button>`;
  })}</div></textarea-navbar> <textarea-body class="block h-28 overflow-y-scroll md:h-[8vw]">${`<textarea spellcheck="true" class="h-full w-full resize-none border-none bg-surface-900 p-3 text-sm leading-tight text-surface-50 outline-none duration-300 ease-in-out placeholder:text-surface-200 focus:ring-0 md:p-[1vw] md:text-[1vw] md:leading-[1.5vw]" placeholder="Leave a comment"${add_attribute("this", textarea_element, 0)}>${escape(textarea_value || "")}</textarea>`}</textarea-body> <textarea-footer class="flex justify-between bg-surface-400/50 px-4 py-2 text-[0.65rem] font-thin leading-[1.5vw] text-surface-200 md:px-[1vw] md:py-[0.1vw] md:text-[0.75vw]" data-svelte-h="svelte-4ipsmt"><div></div> <div>Learn more about
            <a class="underline" href="/">core editor</a></div></textarea-footer> ${``}</div>`;
});
const episode_comments = [
  {
    user: {
      username: "Tokito",
      profile_pic: "/images/DemonSlayer-bg.avif"
    },
    date: "2023-03-11T02:37:40.790Z",
    content: `Hi **Tokito** here! `,
    likes: 1204,
    replies: [
      {
        user: {
          username: "Sora amamiya",
          profile_pic: "/images/Avatar.avif"
        },
        date: "2023-03-11T02:37:40.790Z",
        content: `Hi **Tokito-san**, long time no see`,
        likes: 699
      }
    ]
  },
  {
    user: {
      username: "Sora amamiya",
      profile_pic: "/images/Avatar.avif"
    },
    date: "2023-01-11T02:37:40.790Z",
    content: `**_Tokito_** Love you :P`,
    likes: 106,
    replies: []
  },
  {
    user: {
      username: "Sora amamiya",
      profile_pic: "/images/Avatar.avif"
    },
    date: "2023-01-11T02:37:40.790Z",
    content: `This episode is damn good. **Tokito** is the best :P`,
    likes: 69,
    replies: []
  }
];
const forum_posts = [
  {
    link: "/forum/",
    title: "Celebrating 10 years of Hyouka!",
    description: `Ousei Arima is a child prodigy known as the "Human Metronome" for playing the piano with precision and perfection. Guided by a strict mother and rigorous training, Kousei dominates every competition he enters`,
    banner: "https://blog.sakugabooru.com/wp-content/uploads/2017/11/hk22-1038x576.jpg",
    author: "Eiennlaio",
    posted_on: "2023-04-20T15:38:51.162Z",
    responses: 69
  },
  {
    link: "/forum/",
    title: "Can You See Hyouka as a Point-n-Click Adventure Game?",
    description: `So, while watching the series, I can see it being adapted as a point-n-click game in which you ask people around, looking for clues and solve mysteries on the top given to you.
					Player would be controlling Oreki in a 3D-esque environment and go around interrogate people around. You have choice of responses and see where that gets you.
					Would you play a game like that based on Hyouka? `,
    banner: "https://99px.ru/sstorage/53/2019/04/tmb_257550_218851.jpg",
    author: "simonitro",
    posted_on: "2022-11-20T15:38:51.162Z",
    responses: 55
  }
];
const Download = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { viewBox: "0 0 18 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props)
    ],
    {}
  )}><path d="M15.75 11.25V14.25C15.75 14.6478 15.592 15.0294 15.3107 15.3107C15.0294 15.592 14.6478 15.75 14.25 15.75H3.75C3.35218 15.75 2.97064 15.592 2.68934 15.3107C2.40804 15.0294 2.25 14.6478 2.25 14.25V11.25" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.25 7.5L9 11.25L12.75 7.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 11.25V2.25" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Filter = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 20 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M18.3332 1.5H1.6665L8.33317 9.38333V14.8333L11.6665 16.5V9.38333L18.3332 1.5Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Share = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      { viewBox: "0 0 18 18" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" },
      escape_object($$props)
    ],
    {}
  )}><path d="M13.5 6C14.7426 6 15.75 4.99264 15.75 3.75C15.75 2.50736 14.7426 1.5 13.5 1.5C12.2574 1.5 11.25 2.50736 11.25 3.75C11.25 4.99264 12.2574 6 13.5 6Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4.5 11.25C5.74264 11.25 6.75 10.2426 6.75 9C6.75 7.75736 5.74264 6.75 4.5 6.75C3.25736 6.75 2.25 7.75736 2.25 9C2.25 10.2426 3.25736 11.25 4.5 11.25Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M13.5 16.5C14.7426 16.5 15.75 15.4926 15.75 14.25C15.75 13.0074 14.7426 12 13.5 12C12.2574 12 11.25 13.0074 11.25 14.25C11.25 15.4926 12.2574 16.5 13.5 16.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6.44238 10.1328L11.5649 13.1178" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M11.5574 4.88281L6.44238 7.86781" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Warning = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 16 12" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M6.86001 1.92961L1.21335 8.99961C1.09693 9.15083 1.03533 9.32226 1.03467 9.49687C1.03402 9.67148 1.09434 9.84318 1.20963 9.99488C1.32492 10.1466 1.49116 10.273 1.69182 10.3615C1.89247 10.4501 2.12055 10.4977 2.35335 10.4996H13.6467C13.8795 10.4977 14.1076 10.4501 14.3082 10.3615C14.5089 10.273 14.6751 10.1466 14.7904 9.99488C14.9057 9.84318 14.966 9.67148 14.9654 9.49687C14.9647 9.32226 14.9031 9.15083 14.7867 8.99961L9.14001 1.92961C9.02117 1.78267 8.85383 1.66117 8.65414 1.57686C8.45446 1.49254 8.22917 1.44824 8.00001 1.44824C7.77086 1.44824 7.54557 1.49254 7.34588 1.57686C7.1462 1.66117 6.97886 1.78267 6.86001 1.92961V1.92961Z" stroke="currentColor" stroke-opacity="0.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 4.5V6.5" stroke="currentColor" stroke-opacity="0.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 8.5H8.00667" stroke="currentColor" stroke-opacity="0.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>`;
});
const Heart = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 12 12" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M10.4201 2.30506C10.1647 2.04956 9.86147 1.84688 9.52774 1.7086C9.19401 1.57032 8.8363 1.49915 8.47506 1.49915C8.11382 1.49915 7.75611 1.57032 7.42238 1.7086C7.08865 1.84688 6.78544 2.04956 6.53006 2.30506L6.00006 2.83506L5.47006 2.30506C4.95421 1.78921 4.25458 1.49941 3.52506 1.49941C2.79554 1.49941 2.09591 1.78921 1.58006 2.30506C1.06421 2.8209 0.774414 3.52054 0.774414 4.25006C0.774414 4.97957 1.06421 5.67921 1.58006 6.19506L2.11006 6.72506L6.00006 10.6151L9.89006 6.72506L10.4201 6.19506C10.6756 5.93968 10.8782 5.63647 11.0165 5.30274C11.1548 4.96901 11.226 4.6113 11.226 4.25006C11.226 3.88881 11.1548 3.53111 11.0165 3.19738C10.8782 2.86365 10.6756 2.56044 10.4201 2.30506Z" fill="currentColor"></path></svg>`;
});
const Comment = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { comment_user_profile_pic } = $$props;
  let { comment_username } = $$props;
  let { comment_date } = $$props;
  let { comment_content } = $$props;
  let { comment_likes } = $$props;
  let { comment_replies } = $$props;
  let { open } = $$props;
  if ($$props.comment_user_profile_pic === void 0 && $$bindings.comment_user_profile_pic && comment_user_profile_pic !== void 0)
    $$bindings.comment_user_profile_pic(comment_user_profile_pic);
  if ($$props.comment_username === void 0 && $$bindings.comment_username && comment_username !== void 0)
    $$bindings.comment_username(comment_username);
  if ($$props.comment_date === void 0 && $$bindings.comment_date && comment_date !== void 0)
    $$bindings.comment_date(comment_date);
  if ($$props.comment_content === void 0 && $$bindings.comment_content && comment_content !== void 0)
    $$bindings.comment_content(comment_content);
  if ($$props.comment_likes === void 0 && $$bindings.comment_likes && comment_likes !== void 0)
    $$bindings.comment_likes(comment_likes);
  if ($$props.comment_replies === void 0 && $$bindings.comment_replies && comment_replies !== void 0)
    $$bindings.comment_replies(comment_replies);
  if ($$props.open === void 0 && $$bindings.open && open !== void 0)
    $$bindings.open(open);
  return `<comment class="flex gap-3 md:gap-[1vw]"><a href="/user/" class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]">${validate_component(Image_loader, "ImageLoader").$$render(
    $$result,
    {
      src: comment_user_profile_pic,
      alt: "Avatar",
      class: "h-full w-full shrink-0 rounded-full object-cover"
    },
    {},
    {}
  )}</a> <comment-details class="flex flex-col items-start gap-1 md:gap-0"><a href="/user/" class="text-xs leading-none md:text-[1vw]"><username>${escape(comment_username)}</username> <comment-time class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">${escape(new FormatDate(comment_date).format_to_time_from_now)}</comment-time></a> ${validate_component(Markdown, "Markdown").$$render(
    $$result,
    {
      class: "text-sm leading-snug text-surface-50 md:text-[1vw] md:leading-[1.5vw]",
      markdown: comment_content
    },
    {},
    {}
  )} <options class="mt-2 flex items-center gap-3 md:mt-[0.75vw] md:gap-[0.75vw]"><button class="btn p-0">${validate_component(Heart, "Heart").$$render($$result, { class: "w-3 text-surface-300 md:w-[1vw]" }, {}, {})} <likes class="text-xs md:text-[0.75vw]">${escape(comment_likes)}</likes></button> <button class="btn p-0 text-xs uppercase text-surface-50 md:text-[0.8vw]" data-svelte-h="svelte-y2kxur">Replay</button></options> ${Array.isArray(comment_replies) && comment_replies.length ? `<replies-section class="md:mt-[0.35vw]">${validate_component(Accordion, "Accordion").$$render($$result, { padding: "p-0", hover: "bg-transparent" }, {}, {
    default: () => {
      return `${validate_component(AccordionItem, "AccordionItem").$$render(
        $$result,
        {
          open,
          regionPanel: "text-surface md:text-[1vw] md:leading-[1.35vw] items-start justify-start",
          regionControl: "text-sm text-warning-400 font-semibold md:text-[0.9vw] md:leading-[1vw] pb-2 md:pb-[0.75vw] w-max",
          regionCaret: "md:w-[0.75vw] items-start justify-start"
        },
        {},
        {
          content: () => {
            return `${each(comment_replies, (reply) => {
              return `<reply class="flex gap-3 md:gap-[1vw]"><a href="/user/" class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]">${validate_component(Image_loader, "ImageLoader").$$render(
                $$result,
                {
                  src: reply.user.profile_pic,
                  alt: "Avatar",
                  class: "h-full w-full shrink-0 rounded-full object-cover"
                },
                {},
                {}
              )}</a> <reply-details class="flex flex-col items-start gap-1 md:gap-0"><a href="/user/" class="text-xs leading-none md:text-[1vw]"><username>${escape(reply.user.username)}</username> <reply-time class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">${escape(new FormatDate(reply.date).format_to_time_from_now)}</reply-time></a> ${validate_component(Markdown, "Markdown").$$render(
                $$result,
                {
                  class: "text-sm leading-snug text-surface-50 md:text-[1vw] md:leading-[1.5vw]",
                  markdown: reply.content
                },
                {},
                {}
              )} <options class="mt-2 flex items-center md:mt-[0.75vw] md:gap-[0.75vw]"><button class="btn p-0">${validate_component(Heart, "Heart").$$render($$result, { class: "w-3 text-surface-300 md:w-[1vw]" }, {}, {})} <likes class="text-xs md:text-[0.75vw]">${escape(reply.likes)}</likes></button> </options></reply-details> </reply>`;
            })} `;
          },
          summary: () => {
            return `Replies`;
          }
        }
      )}`;
    }
  })}</replies-section>` : ``}</comment-details></comment>`;
});
export {
  Accordion as A,
  Comment as C,
  Download as D,
  Filter as F,
  Share as S,
  Text_editor as T,
  Warning as W,
  AccordionItem as a,
  Forum_posts as b,
  episode_comments as e,
  forum_posts as f
};
