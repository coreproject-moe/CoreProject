import { sanitize } from "$functions/sanitize";
import { expect, test } from "vitest";

test("sanitize function", async () => {
    const html = `<h1>hello world <script>console.log('sora amamiya is the best')</script></h1>`;
    expect(await sanitize(html)).toBe(`<h1>hello world &lt;script&gt;console.log('sora amamiya is the best')&lt;/script&gt;</h1>`);

    const image_src = `<img src='#' alt='sora_amamiya' onerror=alert(1) />`;
    expect(await sanitize(image_src)).toBe(`<img src="#" alt="sora_amamiya" />`);

    const blockquote_src = `<blockquote class='hello'>hello</blockquote>`;
    expect(await sanitize(blockquote_src)).toBe(`<blockquote class="hello">hello</blockquote>`);

    const marked_src = `<p><a href="mailto:&#101;&#109;&#97;&#x69;&#x6c;&#x40;&#101;&#120;&#x61;&#x6d;&#x70;&#x6c;&#x65;&#46;&#x63;&#x6f;&#109;">&#101;&#109;&#97;&#x69;&#x6c;&#x40;&#101;&#120;&#x61;&#x6d;&#x70;&#x6c;&#x65;&#46;&#x63;&#x6f;&#109;</a></p>`;
    expect(await sanitize(marked_src)).toBe(`<p><a href="mailto:email@example.com">&#101;&#109;&#97;&#x69;&#x6c;&#x40;&#101;&#120;&#x61;&#x6d;&#x70;&#x6c;&#x65;&#46;&#x63;&#x6f;&#109;</a></p>`);
});
