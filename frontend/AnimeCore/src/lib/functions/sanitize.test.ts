import { sanitize } from "$functions/sanitize";
import { expect, test } from "vitest";

test("sanitize function", () => {
    const html = `<h1>hello world <script>console.log('sora amamiya is the best')</script></h1>`;
    expect(sanitize(html)).toBe(`<h1>hello world &lt;script&gt;console.log('sora amamiya is the best')&lt;/script&gt;</h1>`);

    const image_src = `<img src='#' alt='sora_amamiya' onerror=alert(1) />`;
    expect(sanitize(image_src)).toBe(`<img src="#" alt="sora_amamiya" />`);
});
