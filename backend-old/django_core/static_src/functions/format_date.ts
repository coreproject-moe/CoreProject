import { parseISO, formatDistance, format } from "date-fns";

export class FormatDate {
    #date_fns: Date;

    constructor(date: string) {
        this.#date_fns = parseISO(date);
    }

    public get format_to_human_readable_form() {
        return format(this.#date_fns, `MMM dd, yyyy`);
    }

    public get format_to_time_from_now() {
        return formatDistance(this.#date_fns, new Date(), { addSuffix: true });
    }

    public get format_to_season() {
        // https://chat.openai.com/share/52a90543-2a22-43b9-bbd9-4833bb778363
        let season: string | null = null;

        const month = this.#date_fns.getMonth() + 1; // Month is zero-based

        if (month >= 3 && month <= 5) {
            season = "spring";
        } else if (month >= 6 && month <= 8) {
            season = "summer";
        } else if (month >= 9 && month <= 11) {
            season = "autumn";
        } else {
            season = "winter";
        }

        return `${season} ${this.#date_fns.getFullYear()}`;
    }
}
