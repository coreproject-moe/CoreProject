import dayjs from "dayjs";

function getSeason(date: dayjs.Dayjs): string {
    const month = date.month();

    if (month >= 2 && month <= 4) {
        return "spring";
    } else if (month >= 5 && month <= 7) {
        return "summer";
    } else if (month >= 8 && month <= 10) {
        return "autumn";
    } else {
        return "winter";
    }
}

export function formatDateString(dateString: string): string {
    const date = dayjs(dateString);
    const season = getSeason(date);
    const formattedDate = `${season} ${date.format("YYYY")}`;
    return formattedDate;
}
