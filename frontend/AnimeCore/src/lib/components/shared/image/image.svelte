<script lang="ts">
    import { fade } from "svelte/transition";

    export let src: string,
        alt = "",
        style = "";
    let klass: string;
    export { klass as class };
</script>

<img
    class={klass}
    {src}
    {alt}
    {style}
    loading="lazy"
    transition:fade
/>
