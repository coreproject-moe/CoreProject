import { get } from "svelte/store";

import { page } from "$app/stores";
import { UrlMaps } from "$data/urls";
import { navbar_variant } from "$store/Navbar_Variant";
/**
 * Credit goes to = https://stackoverflow.com/questions/38211798/detect-if-image-is-dark-light-and-addclass-dark-light-to-parent
 *
 * @param image - The url of a image
 * @param callback - Callback function that will return a value
 */
export function getImageBrightness(imageSrc: string): void {
    const urlMap = new UrlMaps();

    // If Url is
    // "/sora_amamiya"
    // Convert it to https://localhost:5173/sora_amamiya
    let url;
    if (imageSrc.startsWith("/")) {
        url = urlMap.media_url + imageSrc;
    }

    // If url's domain is not controlled by us return an 'undefined' state
    if (!url?.startsWith(get(page).url.origin)) {
        navbar_variant.set("black");
    }

    const img = new Image();
    let colorSum = 0;

    img.crossOrigin = "anonymous";
    img.src = String(url);

    img.onload = () => {
        // create canvas
        const canvas = document.createElement("canvas");
        canvas.width = img.width;
        canvas.height = img.height;

        const ctx = canvas.getContext("2d");
        ctx?.drawImage(img, 0, 0);

        const imageData = ctx?.getImageData(0, 0, canvas.width, canvas.height);
        const data = imageData?.data;
        let r, g, b, avg;

        for (let x = 0, len = data?.length; x < Number(len); x += 4) {
            r = data?.[x];
            g = data?.[x + 1];
            b = data?.[x + 2];

            avg = Math.floor((Number(r) + Number(g) + Number(b)) / 3);
            colorSum += avg;
        }

        const brightness = Math.floor(colorSum / (img.width * img.height));
        if (brightness > 120) {
            navbar_variant.set("black");
        } else {
            navbar_variant.set("white");
        }
    };
}
