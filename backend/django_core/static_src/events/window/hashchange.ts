import nProgress from "nprogress";

window.addEventListener("hashchange", () => {
    nProgress.done();
});
