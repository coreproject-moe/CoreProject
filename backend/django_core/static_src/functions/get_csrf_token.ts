export function get_csrf_token() {
    // Set by django
    let token: string | null = null;
    token = window.csrfmiddlewaretoken;

    if (token === null) {
        throw new Error("There is no CSRF Token set by `django`");
    }

    return token;
}
