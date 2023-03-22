import dayjs from "dayjs";
import type { Duration } from "dayjs/plugin/duration";
import duration from "dayjs/plugin/duration";

export class formatTime {
    #duration: Duration;

    constructor(time: number) {
        dayjs.extend(duration);
        this.#duration = dayjs.duration(time, "seconds");
    }

    public get formatSecondsToTimeStampDuration() {
        const timeString = dayjs(this.#duration.asMilliseconds()).format("mm:ss");
        return timeString;
    }

    public get formatSecondsToMinutes() {
        const timeString = dayjs(this.#duration.asMilliseconds()).format("m");
        return timeString;
    }
}
