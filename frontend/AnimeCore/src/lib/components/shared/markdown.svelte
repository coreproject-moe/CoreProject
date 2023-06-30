<script lang="ts">
    import { emojis } from "$data/emojis";
    import { marked } from "marked";
    import { markedEmoji } from "marked-emoji";
    import xss from "xss";

    export let markdown = "";
    export { klass as class };

    let klass = "";

    const emoji_options = {
        emojis,
        unicode: false
    };

    // Override function
    const renderer: marked.RendererObject = {
        del(text: string) {
            /** Dont convert s (tag) -> del (tag)
             * Reason 1: Skeleton.dev is formatting `del` tag | Source : https://www.skeleton.dev/elements/typography
             * Reason 2: Marked.js is not allowing us to add unstyled class to rendered text.
             */

            return `<s>${text}</s>`;
        }
    };

    marked.use(
        // Emoji plugin
        markedEmoji(emoji_options),
        {
            renderer,
            // Disable it as marked-mangle doesn't support typescript
            mangle: false,
            // We dont need github like header prefix
            headerIds: false
        }
    );

    let html: string;
    $: html = xss(marked.parse(markdown));
</script>

<markdown class={klass}>
    {@html html}
</markdown>
