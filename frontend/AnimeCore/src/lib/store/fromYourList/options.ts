import { get, writable } from "svelte/store";

import { browser } from "$app/env";

export const fromYourListOption = writable({ state: "", opened: false }, function start(set) {
    if (browser) {
        const option = localStorage.getItem("fromYourListOption");
        if (option && option !== null) {
            set({ state: option, opened: get(fromYourListOption).opened });
        } else {
            set({ state: "watching", opened: get(fromYourListOption).opened });
        }
    }
});

fromYourListOption.subscribe((change) => {
    browser && localStorage.setItem("fromYourListOption", change.state);
});
