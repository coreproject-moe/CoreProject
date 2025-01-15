import nProgress from "nprogress";

document.addEventListener("htmx:beforeRequest", () => {
    nProgress.done(true);
});
