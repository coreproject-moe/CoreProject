// https://htmx.org/events/#htmx:configRequest

document.body.addEventListener("htmx:configRequest", (evt: any) => {
    evt.detail.parameters["auth_token"] = window.csrfmiddlewaretoken; // add a new parameter into the mix
});
