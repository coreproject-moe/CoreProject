import { detect } from "detect-browser";

const browser = detect();

const IS_CHROME: boolean = ["chrome", "chromium-webview", "android", "yandexbrowser"].includes(browser?.name!);
const IS_SAFARI: boolean = browser?.name === "safari";
const IS_EDGE: boolean = browser?.name === "edge-chromium";
const IS_OPERA: boolean = browser?.name === "opera";
const IS_INTERNET_EXPLORER: boolean = browser?.name === "ie" || browser?.name === "edge";

export const IS_FIREFOX = browser?.name === "firefox";

export const IS_CHROMIUM = (IS_CHROME || IS_EDGE || IS_OPERA) && !(IS_FIREFOX && IS_INTERNET_EXPLORER && IS_SAFARI);
