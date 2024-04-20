import nProgress from "nprogress";

window.addEventListener("popstate", () => {
    nProgress.done();
});
