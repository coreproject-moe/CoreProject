import nProgress from "nprogress";

document.addEventListener("htmx:afterOnLoad", () => {
    nProgress.done();
});
