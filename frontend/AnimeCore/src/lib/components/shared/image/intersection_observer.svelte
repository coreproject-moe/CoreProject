<script lang="ts">
    import { onMount } from "svelte";

    export let top = 0;
    export let bottom = 0;
    export let left = 0;
    export let right = 0;
    export let once = false;

    let intersecting = false;
    let container: HTMLDivElement;

    onMount(() => {
        const rootMargin = `${bottom}px ${left}px ${top}px ${right}px`;

        const observer = new IntersectionObserver(
            (entries) => {
                intersecting = entries[0].isIntersecting;
                if (intersecting && once) {
                    observer.unobserve(container);
                }
            },
            {
                rootMargin
            }
        );

        observer.observe(container);
        return () => observer.unobserve(container);
    });
</script>

<div
    class="h-full"
    bind:this={container}
>
    <slot {intersecting} />
</div>
