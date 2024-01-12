import { writable } from "svelte/store";
import htmx from "htmx.org";
export const url = writable(window.location.pathname);

// Hacky way

document.addEventListener("htmx:afterSwap", (event: any) => {
    const _url = new URL(event.detail.xhr.responseURL).pathname;
    // Ignore path if it has http in name
    if (!_url.startsWith("http")) {
        // Update store
        url.set(_url);
    }
});

window.addEventListener("popstate", function () {
    url.set(this.location.pathname);
});

// window.document.addEventListener("htmx:confirm", (event: any) => {
//     url.set(event.detail.path);
//     // https://htmx.org/events/#htmx:confirm
//     event.detail.issueRequest();
// });
