// @ts-ignore
import ColorThief from "colorthief/dist/color-thief.umd.js";

export function get_dominant_color(img: HTMLImageElement) {
    const colorthief = new ColorThief();
    let color: any | null = null;
    if (img.complete) {
        color = colorthief.getColor(img);
    } else {
        img.addEventListener("load", function () {
            color = colorthief.getColor(img);
        });
    }
    return color;
}
