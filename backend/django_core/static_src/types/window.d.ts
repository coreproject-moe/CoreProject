import _hyperscript from "hyperscript.org";

declare global {
    interface Window {
        _hyperscript: typeof _hyperscript;
        csrfmiddlewaretoken: string;
        urls: Map<string, string>;
        request: {
            user: {
                is_authenticated: string;
                is_superuser: string;
                is_staff: string;
            };
        };
    }
}
