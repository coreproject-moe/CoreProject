import nProgress from "nprogress";

document.addEventListener("htmx:afterSettle", () => {
    nProgress.done();
});
