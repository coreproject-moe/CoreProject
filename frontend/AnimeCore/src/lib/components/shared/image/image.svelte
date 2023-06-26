<script lang="ts">
    import { fade } from "svelte/transition";

    export let src: string;
    export let alt: string;
    export let style: string;
    let klass: string;
    export { klass as class };

    let image: HTMLImageElement;
</script>

<img
    class={klass}
    {src}
    {alt}
    {style}
    bind:this={image}
    transition:fade|local
/>
