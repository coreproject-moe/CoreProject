import nProgress from "nprogress";

document.addEventListener("htmx:beforeRequest", () => {
    nProgress.start();
});
