import { url as url_store } from "$stores/url";

window.addEventListener("htmx:historyRestore", function (event: any) {
    url_store.set(event.detail.path);
});
