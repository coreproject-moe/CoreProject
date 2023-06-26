import dayjs from "dayjs";
import type { Duration } from "dayjs/plugin/duration";
import duration from "dayjs/plugin/duration";
import utc from "dayjs/plugin/utc";

export class FormatTime {
    #duration: Duration;

    constructor(time: number) {
        dayjs.extend(utc);
        dayjs.extend(duration);
        this.#duration = dayjs.duration(time, "seconds");
    }

    public get format_seconds_to_time_stamp_duration() {
        const timeString = dayjs.utc(this.#duration.asMilliseconds()).format("mm:ss");
        return timeString;
    }

    public get format_seconds_to_minutes() {
        const timeString = dayjs.utc(this.#duration.asMilliseconds()).format("m");
        return timeString;
    }
}
