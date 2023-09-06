import { format_kokoro_color } from "$functions/format_kokoro";
import { expect, test } from "vitest";

test("format kokoro color", () => {
    const text = "Hello world, kokoro-chan is ready for duty";
    const formated_html = format_kokoro_color(text);
    expect(formated_html).toBe(
        `Hello world, <span class="inline-flex text-white">k</span><span class="inline-flex text-warning-400">o</span><span class="inline-flex text-white">k</span><span class="inline-flex text-warning-400">o</span><span class="inline-flex text-white">r</span><span class="inline-flex text-warning-400">o</span><span class="inline-flex text-white">-</span><span class="inline-flex text-white">c</span><span class="inline-flex text-white">h</span><span class="inline-flex text-white">a</span><span class="inline-flex text-white">n</span> is ready for duty`
    );
});
