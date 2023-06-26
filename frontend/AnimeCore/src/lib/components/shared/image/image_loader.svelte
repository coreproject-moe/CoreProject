<script lang="ts">
    import Image from "./image.svelte";
    import IntersectionObserver from "./intersection_observer.svelte";

    export let src: string;
    export let alt = "";
    export let style = "";
    let klass = "";
    export { klass as class };
</script>

<IntersectionObserver
    once={true}
    let:intersecting
>
    {#if intersecting}
        <Image
            class={klass}
            {src}
            {alt}
            {style}
        />
    {:else}
        <div class="placeholder animate-pulse !bg-surface-400 {klass}" />
    {/if}
</IntersectionObserver>
