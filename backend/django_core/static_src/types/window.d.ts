export {};

declare global {
    interface Window {
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
