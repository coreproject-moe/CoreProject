import { detect } from "detect-browser";
import * as _ from "lodash-es";

const browser = detect();

const IS_CHROME: boolean = _.includes(["chrome", "chromium-webview", "android", "yandexbrowser"], browser?.name.toLowerCase());
const IS_SAFARI: boolean = _.includes(["safari"], browser?.name.toLowerCase());
const IS_EDGE: boolean = _.includes(["edge-chromium"], browser?.name.toLowerCase());
const IS_OPERA: boolean = _.includes(["opera"], browser?.name.toLowerCase());

const IS_INTERNET_EXPLORER: boolean = _.includes(["ie", "edge"], browser?.name.toLowerCase());

export const IS_FIREFOX = _.includes(['"firefox"'], browser?.name.toLowerCase());

export const IS_CHROMIUM = (IS_CHROME || IS_EDGE || IS_OPERA) && !(IS_FIREFOX && IS_INTERNET_EXPLORER && IS_SAFARI);
