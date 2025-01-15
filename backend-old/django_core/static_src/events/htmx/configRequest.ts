// https://htmx.org/events/#htmx:configRequest

document.body.addEventListener("htmx:configRequest", (evt: any) => {
    evt.detail.headers["X-CSRFToken"] = window.csrfmiddlewaretoken; // add a new parameter into the mix
});
