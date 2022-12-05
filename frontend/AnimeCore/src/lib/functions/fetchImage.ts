import { page } from "$app/stores";
import { get } from "svelte/store";

export const fetchImageAndConvertToBlob = async (url: string) => {
    // If the domain is not controlled by us we cant have control over cors
    if (!url.startsWith(get(page).url.origin)) {
        return url;
    }

    const response = await fetch(url, {
        method: "GET",
        // https://stackoverflow.com/questions/41030425/disabling-cors-using-js-fetch
        mode: "no-cors"
    });
    const blob = await response.blob();

    return URL.createObjectURL(blob);
};
