import dayjs from "dayjs";
import duration from "dayjs/plugin/duration";
dayjs.extend(duration);

export function formatSecondsToMinutes(seconds: number) {
    const durationObject = dayjs.duration(seconds, "seconds");

    const timeString = dayjs(durationObject.asMilliseconds()).format("m");

    return timeString;
}
