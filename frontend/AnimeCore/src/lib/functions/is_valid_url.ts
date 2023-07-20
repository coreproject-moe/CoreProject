// Functions
export function is_valid_url(url_string: string) {
    /**
     * Credit : https://stackoverflow.com/a/43467144
     */
    let url: URL;

    try {
        url = new URL(url_string);
    } catch (_) {
        return false;
    }

    return url.protocol === "http:" || url.protocol === "https:";
}
