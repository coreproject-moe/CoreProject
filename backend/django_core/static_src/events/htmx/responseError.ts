import nProgress from "nprogress";

document.addEventListener("htmx:responseError", (event) => {
    console.log(event);
});
