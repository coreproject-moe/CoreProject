const KOKORO_COLOR_WORD_MAP: {
    [key: string]: string | undefined;
} = {
    "-": "white",
    a: "white",
    c: "white",
    h: "white",
    k: "white",
    n: "white",
    o: "yellow",
    r: "white"
};

const TAILWIND_COLOR_MAP: {
    [key: string]: string | undefined;
} = {
    white: "text-white",
    yellow: "text-warning-400"
};

export function format_kokoro_color(input: string) {
    const kokoroRegex = new RegExp(/kokoro-chan/gm);

    // There is no kokoro-chan in the input ( which is odd )
    if (!kokoroRegex.exec(input)) {
        return input;
    }

    const coloredWrappedWords = "kokoro-chan".split("").map((word) => {
        return `<span class="inline-flex ${
            TAILWIND_COLOR_MAP[
                KOKORO_COLOR_WORD_MAP[word] ?? "white" // default to white
            ]
        }">${word}</span>`;
    });

    // Color the font.
    input = input.replaceAll(kokoroRegex, coloredWrappedWords.join("").toString());
    // Hyperlink the home
    return input;
}
