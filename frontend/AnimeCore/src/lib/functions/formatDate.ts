import dayjs from "dayjs";

export class formatDate {
    #date: dayjs.Dayjs;

    constructor(date: string) {
        this.#date = dayjs(date);
    }

    public get formatToSeason() {
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

        const formattedDate = `${season} ${this.#date.format("YYYY")}`;
        return formattedDate;
    }
}
