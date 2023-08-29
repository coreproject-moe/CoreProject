import dayjs from "dayjs";
import localeData from "dayjs/plugin/localeData.js";
import relativeTime from "dayjs/plugin/relativeTime.js";
import utc from "dayjs/plugin/utc.js";
import { c as create_ssr_component, b as spread, d as escape_object } from "./ssr.js";
class FormatDate {
  #date;
  constructor(date) {
    dayjs.extend(localeData);
    dayjs.extend(relativeTime);
    dayjs.extend(utc);
    this.#date = dayjs(date);
  }
  get format_to_human_readable_form() {
    return `${dayjs().localeData().monthsShort(this.#date)} ${this.#date.format("D")}, ${this.#date.format("YYYY")}`;
  }
  get format_to_time_from_now() {
    return dayjs.utc(this.#date).fromNow();
  }
  get format_to_season() {
    let season;
    const month = this.#date.month();
    if (month >= 2 && month <= 4) {
      season = "spring";
    } else if (month >= 5 && month <= 7) {
      season = "summer";
    } else if (month >= 8 && month <= 10) {
      season = "autumn";
    } else {
      season = "winter";
    }
    return `${season} ${this.#date.format("YYYY")}`;
  }
}
const Play_circle = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<svg${spread(
    [
      escape_object($$props),
      { viewBox: "0 0 14 14" },
      { fill: "none" },
      { xmlns: "http://www.w3.org/2000/svg" }
    ],
    {}
  )}><path d="M12.9615 7.89235C13.1685 7.73214 13.3361 7.52665 13.4513 7.29164C13.5666 7.05663 13.6266 6.79834 13.6266 6.53658C13.6266 6.27482 13.5666 6.01653 13.4513 5.78152C13.3361 5.54651 13.1685 5.34102 12.9615 5.18081C10.2808 3.10657 7.28748 1.47165 4.09351 0.337231L3.50952 0.129752C2.39342 -0.266427 1.21383 0.488369 1.06269 1.64113C0.640479 4.89111 0.640479 8.18205 1.06269 11.432C1.21473 12.5848 2.39342 13.3396 3.50952 12.9434L4.09351 12.7359C7.28748 11.6015 10.2808 9.96659 12.9615 7.89235Z" fill="currentColor"></path></svg>`;
});
export {
  FormatDate as F,
  Play_circle as P
};
