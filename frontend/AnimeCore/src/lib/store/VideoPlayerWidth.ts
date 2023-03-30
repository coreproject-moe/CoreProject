import { get, writable } from "svelte/store";

import { browser } from "$app/environment";

import { responsiveMode } from "./Responsive";

export const video_player_width = writable<"normal" | "wide" | "mobile" | undefined>(
    "normal",
    function start(set) {
        if (!browser) {
            return;
        }
        if (get(responsiveMode) === "mobile") {
            set("mobile");
            return;
        }

        const videoPlayerWidthValueFromLocalStorage = localStorage.getItem("video_player_width");
        if (videoPlayerWidthValueFromLocalStorage) {
            set(videoPlayerWidthValueFromLocalStorage as "normal" | "wide" | "mobile");
        } else {
            set("normal");
        }
    }
);

video_player_width.subscribe((value) => {
    if (browser) {
        localStorage.setItem("video_player_width", String(value));
    }
});
