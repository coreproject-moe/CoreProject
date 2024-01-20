import { url as url_store } from "$stores/url";

import { clear_commentbox_if_needed } from "$stores/comment";
document.addEventListener("htmx:afterSwap", (event: any) => {
    clear_commentbox_if_needed();

    const _url = new URL(event.detail.xhr.responseURL as string);
    // Ignore path if it has http in name
    if (_url.origin == window.location.origin) {
        // Update store
        url_store.set(_url.pathname);
    }
});
