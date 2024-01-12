import { url as url_store } from "$stores/url";

document.addEventListener("htmx:afterSwap", (event: any) => {
    const _url = new URL(event.detail.xhr.responseURL as string);
    // Ignore path if it has http in name
    if (_url.origin == window.location.origin) {
        // Update store
        url_store.set(_url.pathname);
    }
});
