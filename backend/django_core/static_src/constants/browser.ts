import { type Browser } from "detect-browser";
import { detect } from "detect-browser";
import * as _ from "lodash-es";

const browser = detect();

const MAPPING: { [key: string]: Browser[] } = {
    chromium: [
        "chrome",
        "chromium-webview",
        "android",
        // Yandex browser is chromium
        "yandexbrowser",
        // Edge is chrome too
        "edge-chromium",
        // Opera is chromium
        "opera"
    ],
    firefox: ["firefox"]
};

// const IS_INTERNET_EXPLORER: boolean = _.includes([`ie`, `edge`], browser?.name.toLowerCase());

export const IS_FIREFOX = _.includes(MAPPING["firefox"], browser?.name.toLowerCase());
export const IS_CHROMIUM = _.includes(MAPPING["chromium"], browser?.name.toLowerCase());
