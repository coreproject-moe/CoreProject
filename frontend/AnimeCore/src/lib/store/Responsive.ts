import { writable } from "svelte/store";

import { browser } from "$app/environment";

// Callback function to handle changes
const checkMode = () => {
    /*
        Mapped from here
        https://bulma.io/documentation/helpers/visibility-helpers/
    */

    const MOBILE = window.matchMedia("(max-width: 768px)");
    const TABLET = window.matchMedia("(min-width: 769px) and (max-width: 1023px)");
    const DESKTOP = window.matchMedia("(min-width: 1024px) and (max-width: 1215px)");
    const WIDESCREEN = window.matchMedia("(min-width: 1216px) and (max-width: 1407px)");
    const FULLHD = window.matchMedia("(min-width: 1408px)");

    switch (true) {
        case MOBILE.matches:
            return "mobile";
        case TABLET.matches:
            return "tablet";
        case DESKTOP.matches:
            return "desktop";
        case WIDESCREEN.matches:
            return "widescreen";
        case FULLHD.matches:
            return "fullhd";
        default:
            return null;
    }
};

export const responsiveMode = writable<
    "mobile" | "tablet" | "desktop" | "widescreen" | "fullhd" | null | undefined
>(browser ? checkMode() : undefined);

// Final event listener to handle changes
browser &&
    window.addEventListener("resize", async () => {
        responsiveMode.set(checkMode());
    });
