import { url as url_store } from "$stores/url";

window.addEventListener("popstate", function () {
    url_store.set(this.location.pathname);
});
