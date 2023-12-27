import { writable } from "svelte/store";

export const url = writable(window.location.pathname);
window.addEventListener("popstate", function () {
    url.set(this.location.pathname);
});
