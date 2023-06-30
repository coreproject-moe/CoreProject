import fs from "fs";
import fetch from "node-fetch-retry";
import path from "path";
import sharp from "sharp";
import { fileURLToPath } from "url";

// Polyfill. Remove it later
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const emoji_data_path = path.join(__dirname, "..", "..", "src", "lib", "data", "emojis.json");
const emoji_input_path = path.join(__dirname, "data.json");
const download_path = path.join(__dirname, "..", "..", "static", "emojis");

// Check if folder exists
if (!fs.existsSync(download_path)) {
    fs.mkdirSync(download_path);
}

fs.readFile(emoji_input_path, "utf8", async (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }
    const emojis_data = JSON.parse(data);

    const emoji_map = {};

    for (const [emoji_name, emoji_link] of Object.entries(emojis_data)) {
        const image_filename = `${download_path}/${emoji_name}.avif`;

        try {
            const response = await fetch(emoji_link, { method: "GET", retry: 10, pause: 3000 });
            if (!response.ok) {
                throw new Error("Error while downloading image. HTTP status " + response.status);
            }
            // We get png files here
            const arrayBuffer = await response.arrayBuffer();
            const buffer = Buffer.from(arrayBuffer);

            const avif_image_buffer = await sharp(buffer).avif({ effort: 9 }).toBuffer();

            fs.writeFileSync(image_filename, avif_image_buffer);
            console.log(`Downloaded: ${emoji_name}`);
        } catch (error) {
            console.error("Error while downloading image:", error);
            return;
        } finally {
            // svelte specific code
            emoji_map[emoji_name] = `/emojis/${emoji_name}.avif`;
        }
    }

    fs.writeFile(emoji_data_path, JSON.stringify(emoji_map), function (err) {
        if (err) throw err;
        console.log("wrote data");
    });
});
