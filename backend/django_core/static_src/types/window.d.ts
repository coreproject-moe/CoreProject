import _hyperscript from "hyperscript.org";

declare global {
    interface Window {
        _hyperscript: typeof _hyperscript;
        csrfmiddlewaretoken: string;
        urls: Map<string, string>;
        user_authenticated: string; // is Boolean
    }
}
