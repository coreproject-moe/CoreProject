import { writable } from "svelte/store";

import { browser } from "$app/env";

function handleWindowChange(e: MediaQueryList) {
    // Check if the media query is true
    return e.matches;
}

// Callback function to handle changes
const checkMode = () => {
    if (browser) {
        /*
            Mapped from here
            https://bulma.io/documentation/helpers/visibility-helpers/
        */

        const MOBILE = window.matchMedia("(max-width: 768px)");
        const TABLET = window.matchMedia("(min-width: 769px) and (max-width: 1023px)");
        const DESKTOP = window.matchMedia("(min-width: 1024px) and (max-width: 1215px)");
        const WIDESCREEN = window.matchMedia("(min-width: 1216px) and (max-width: 1407px)");
        const FULLHD = window.matchMedia("(min-width: 1408px )");

        if (handleWindowChange(MOBILE)) {
            return "mobile";
        } else if (handleWindowChange(TABLET)) {
            return "tablet";
        } else if (handleWindowChange(DESKTOP)) {
            return "desktop";
        } else if (handleWindowChange(WIDESCREEN)) {
            return "widescreen";
        } else if (handleWindowChange(FULLHD)) {
            return "fullhd";
        } else {
            return null;
        }
    } else {
        return null;
    }
};

export const responsiveMode = writable<
    "mobile" | "tablet" | "desktop" | "widescreen" | "fullhd" | null | undefined
>(checkMode());

// Final event listener to handle changes
browser &&
    window.addEventListener("resize", async () => {
        responsiveMode.set(checkMode());
    });
