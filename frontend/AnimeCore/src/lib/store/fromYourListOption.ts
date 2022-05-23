import { writable } from "svelte/store";

let states: "watching" | "planning" | "completed" | "rewatching" | "pause" | "dropped";

export const fromYourListOption = writable({ state: states, opened: false });

fromYourListOption.subscribe((change) => {
    localStorage.setItem("fromYourListOption", "");
});
