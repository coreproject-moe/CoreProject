const IS_CHROME = navigator.userAgent.includes("Chrome");
const IS_SAFARI = navigator.userAgent.includes("Safari");
const IS_EDGE = navigator.userAgent.includes("Edge");
const IS_OPERA = navigator.userAgent.includes("Opera") || navigator.userAgent.includes("OPR");
const IS_INTERNET_EXPLORER = navigator.userAgent.includes("Trident") || navigator.userAgent.includes("MSIE");
export const IS_FIREFOX = navigator.userAgent.includes("Firefox");

export const IS_CHROMIUM = (IS_CHROME || IS_EDGE || IS_OPERA) && !(IS_FIREFOX && IS_INTERNET_EXPLORER && IS_SAFARI);
