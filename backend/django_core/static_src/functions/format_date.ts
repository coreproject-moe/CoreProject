import dayjs from "dayjs";
import { parseIso } from "date-fns";
// Define modules
[
    (await import("dayjs/plugin/localeData")).default,
    (await import("dayjs/plugin/relativeTime")).default,
    (await import("dayjs/plugin/utc")).default
].forEach((item) => {
    dayjs.extend(item);
});

export class FormatDate {
    #date: dayjs.Dayjs;
    #date_fns: any;

    constructor(date: string) {
        this.#date = dayjs(date);
        this.#date_fns = parseIso(date);
    }

    public get format_to_human_readable_form() {
        return `${dayjs().localeData().monthsShort(this.#date)} ${this.#date.format(
            "D"
        )}, ${this.#date.format("YYYY")}`;
    }

    public get format_to_time_from_now() {
        return dayjs.utc(this.#date).fromNow();
    }

    public get format_to_season() {
        let season: string;

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
