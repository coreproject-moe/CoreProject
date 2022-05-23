import { get, writable } from "svelte/store";

export const fromYourListOption = writable({ state: "", opened: false }, function start(set) {
    const option = localStorage.getItem("fromYourListOption");
    if (option && option !== null) {
        set({ state: option, opened: get(fromYourListOption).opened });
    }
});

fromYourListOption.subscribe((change) => {
    localStorage.setItem("fromYourListOption", change.state);
});
