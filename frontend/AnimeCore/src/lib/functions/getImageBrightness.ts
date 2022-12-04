/**
 * Credit goes to = https://stackoverflow.com/questions/38211798/detect-if-image-is-dark-light-and-addclass-dark-light-to-parent
 *
 * @param image - The url of a image
 * @param callback - Callback function that will return a value
 */
export function getImageBrightness(imageSrc: string, callback: (brightness: number) => void): void {
    const img = document.createElement("img");
    img.src = imageSrc;
    img.crossOrigin = "anonymous";

    img.style.display = "none";
    document.body.appendChild(img);

    let colorSum = 0;

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
        callback(brightness);
    };
}
