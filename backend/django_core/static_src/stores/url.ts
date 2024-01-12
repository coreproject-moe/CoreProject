import { writable } from "svelte/store";
export const url = writable(window.location.pathname);

// Hacky way

// window.addEventListener("popstate", function () {
//     url.set(this.location.pathname);
// });

// window.document.addEventListener("htmx:confirm", (event: any) => {
//     url.set(event.detail.path);
//     // https://htmx.org/events/#htmx:confirm
//     event.detail.issueRequest();
// });
