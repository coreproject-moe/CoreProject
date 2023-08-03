<script lang="ts">
    import { onMount } from "svelte";

    let klass = "";
    export { klass as class };

    export let parentClass = "";
    export let offsetScrollbar = false;
    export let gradientMask = false;

    let scroll_percent = 0;

    let element: HTMLDivElement;

    onMount(() => {
        if (gradientMask) {
            element?.addEventListener("scroll", (event) => {
                const el = event?.currentTarget as HTMLElement;
                scroll_percent = globalThis.Math.round((el.scrollTop / (el.scrollHeight - el.clientHeight)) * 100);
            });
        }
    });
</script>

<scroll-area
    bind:this={element}
    class:mask-top={gradientMask && scroll_percent <= 100 && scroll_percent >= 90}
    class:mask-middle={gradientMask && scroll_percent < 90 && scroll_percent >= 10}
    class:mask-bottom={gradientMask && scroll_percent < 10 && scroll_percent >= 0}
    class="{parentClass} {offsetScrollbar ? 'pr-3 md:pr-[0.75vw]' : 'pr-0'} block h-full w-full overflow-y-scroll overscroll-y-contain border-transparent scrollbar-thin"
>
    <div class="{klass} whitespace-pre-line">
        <slot />
    </div>
</scroll-area>

<style lang="scss">
    scroll-area {
        scrollbar-color: rgba(255, 255, 255, 0.12);
        /* here we make the color transition */
        transition: border-color 0.2s linear;
        &:hover {
            /* the color we want the scrollbar on hover */
            border-color: rgba(255, 255, 255, 0.15);
        }
        &::-webkit-scrollbar,
        &::-webkit-scrollbar-corner,
        &::-webkit-scrollbar-thumb {
            width: 5px;
            border-radius: 16px;
            /* add border to act as background-color */
            border-right-style: inset;
            /* sum viewport dimensions to guarantee border will fill scrollbar */
            border-right-width: calc(100vw + 100vh);
            /* inherit border-color to inherit transitions */
            border-color: inherit;
        }
        &::-webkit-scrollbar-track {
            background: transparent !important;
        }

        &.mask-top {
            mask-image: linear-gradient(0deg, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);
            mask-position: top;
        }
        &.mask-middle {
            mask-image: linear-gradient(0deg, rgba(0, 0, 0, 0.35) 10%, rgba(7, 5, 25, 0.95) 20%, rgba(7, 5, 25, 0.95) 80%, rgba(7, 5, 25, 0.35) 90%);
            mask-position: bottom;
        }
        &.mask-bottom {
            mask-image: linear-gradient(180deg, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);
            mask-position: bottom;
        }
    }
</style>
