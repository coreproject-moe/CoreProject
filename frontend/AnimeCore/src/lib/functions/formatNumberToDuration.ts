import dayjs from "dayjs";
import duration from "dayjs/plugin/duration";
dayjs.extend(duration);

export function formatNumberToDuration(seconds: number) {
    const durationObject = dayjs.duration(seconds, "seconds");

    const timeString = dayjs(durationObject.asMilliseconds()).format("mm:ss");

    return timeString;
}
