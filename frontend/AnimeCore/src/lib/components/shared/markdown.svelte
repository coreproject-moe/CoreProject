<script lang="ts">
    import { emojis } from "$data/emojis";
    import { sanitize } from "$functions/sanitize";
    import hljs from "highlight.js";
    import "highlight.js/scss/github-dark.scss";
    import type { marked as markedType } from "marked";
    import { Marked } from "marked";
    import type { MarkedEmojiOptions } from "marked-emoji";
    import { markedEmoji } from "marked-emoji";
    import { markedHighlight } from "marked-highlight";
    import { mangle } from "marked-mangle";

    export let markdown = "";
    export { klass as class };

    let klass = "";

    const emoji_options: MarkedEmojiOptions = {
        emojis,
        unicode: false
    };

    // Override function
    const renderer: markedType.RendererObject = {
        del(text: string) {
            return `<del class='unstyled'>${text}</del>`;
        }
    };

    const marked = new Marked(
        // Highlight.js
        markedHighlight({
            langPrefix: "hljs language-",
            highlight: (code, lang) => {
                const language = hljs.getLanguage(lang) ? lang : "plaintext";
                return hljs.highlight(code, { language }).value;
            }
        }),
        // Emoji plugin
        markedEmoji(emoji_options),
        // Mangle plugin
        mangle(),
        // Marked defaults
        {
            renderer,
            // Disable it as marked-mangle doesn't support typescript
            mangle: false,
            // We dont need github like header prefix
            headerIds: false
        }
    );

    let html: string;
    $: html = sanitize(marked.parse(markdown));
</script>

<markdown class={klass}>
    {@html html}
</markdown>
