<script lang="ts">
    import { emojis } from "$data/emojis";
    import { sanitize } from "$functions/sanitize";
    import hljs from "highlight.js";
    import { Marked } from "marked";
    import { markedEmoji } from "marked-emoji";
    import { markedHighlight } from "marked-highlight";
    import { mangle } from "marked-mangle";
    import { markedXhtml } from "marked-xhtml";
    import { markedSmartypants } from "marked-smartypants";

    export let markdown = "";
    export { klass as class };

    let klass = "";

    const emoji_options = {
        emojis,
        unicode: false
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
            // We dont need github like header prefix
            headerIds: false
        }
    );

    let html: string | Promise<string>;
    $: html = sanitize(marked.parse(markdown));
</script>

<markdown class={klass}>
    {#await html then html}
        {@html html}
    {/await}
</markdown>

<style lang="postcss">
    :global(markdown pre) {
        @apply !rounded-md !bg-transparent !p-0;
    }
    :global(markdown code) {
        @apply !bg-surface-400/50 text-xs leading-snug md:rounded-[0.5vw] md:p-3 md:text-[0.9vw] md:leading-[1.25vw];
    }
</style>
