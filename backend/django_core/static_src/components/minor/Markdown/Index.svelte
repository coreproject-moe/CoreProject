<script lang="ts">
    // Import scss
    import "highlight.js/scss/github-dark.scss";

    // Import js codes
    import emojis from "../../../data/emoji.json";

    import { sanitize } from "$functions/sanitize";
    import { Marked } from "marked";
    import { markedEmoji } from "marked-emoji";
    import { markedHighlight } from "marked-highlight";
    import { mangle } from "marked-mangle";
    import { markedXhtml } from "marked-xhtml";
    import { markedSmartypants } from "marked-smartypants";
    import { cn } from "$functions/classname";
    import hljs from "highlight.js";

    export let markdown = "";
    let klass = "";
    export { klass as class };

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
        markedEmoji({
            emojis,
            unicode: false
        }),
        {
            extensions: [
                {
                    name: "emoji",
                    renderer: (token) => {
                        return `<img class="inline-flex w-4 justify-center align-center -translate-y-0.5 md:w-[1vw]" alt="${token.name}" src="${token.emoji}">`;
                    }
                }
            ]
        },
        // Smartypants plugin
        markedSmartypants(),
        // XHTML plugin
        markedXhtml(),
        // Mangle plugin
        mangle(),
        // Marked defaults
        {
            gfm: true
        }
    );

    let html: string | Promise<string>;
    $: html = sanitize(marked.parse(markdown));
</script>

<div class={cn(klass)}>
    {#await html then html}
        {@html html}
    {/await}
</div>
