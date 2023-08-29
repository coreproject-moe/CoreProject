<script lang="ts">
    import { onMount } from "svelte";

    export let once = false;

    let intersecting = false,
        container: HTMLDivElement;

    const observerOptions: IntersectionObserverInit = {
        root: null, // Use Viewport
        rootMargin: "0px",
        threshold: 0
    };

    onMount(() => {
        const observer = new IntersectionObserver((entries) => {
            intersecting = entries[0].isIntersecting;
            if (intersecting && once) {
                observer.unobserve(container);
            }
        }, observerOptions);

        observer.observe(container);
        return () => observer.unobserve(container);
    });
</script>

<div
    bind:this={container}
    class="h-full"
>
    <slot {intersecting} />
</div>
