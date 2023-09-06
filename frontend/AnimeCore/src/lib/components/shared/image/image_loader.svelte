<script lang="ts">
    import { cn } from "$functions/classnames";
    import Image from "./image.svelte";
    import IntersectionObserver from "./intersection_observer.svelte";

    export let src: string,
        alt = "",
        style = "";
    let klass = "";
    export { klass as class };
</script>

<IntersectionObserver
    once={true}
    let:intersecting
    class={cn("h-full", klass)}
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
