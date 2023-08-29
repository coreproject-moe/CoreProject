<script lang="ts">
    let klass = "";
    export { klass as class };

    export let parentClass = "";
    export let offsetScrollbar = false;
    export let gradientMask = false;

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean;

    $: add_mask_bottom = scroll_area ? scroll_area.scrollHeight > scroll_area.clientHeight : false;

    function handle_scroll(event: Event) {
        const target = event.target as HTMLElement;
        const { scrollHeight, clientHeight, scrollTop } = target;

        if (clientHeight + scrollTop === scrollHeight) add_mask_bottom = false;
        else add_mask_bottom = true;
    }
</script>

<scroll-area
    bind:this={scroll_area}
    on:scroll={handle_scroll}
    class="{parentClass} {offsetScrollbar && "pr-3 md:pr-[0.75vw]"} block h-full w-full overflow-y-scroll overscroll-y-contain border-transparent scrollbar-thin"
    class:mask-bottom={gradientMask && add_mask_bottom}
>
    <div>
        <div class="{klass} whitespace-pre-line">
            <slot />
        </div>
    </div>
</scroll-area>

<style lang="scss">
    scroll-area {
        scrollbar-color: rgba(255, 255, 255, 0.12) transparent;
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
        &.mask-bottom {
            mask-image: linear-gradient(180deg, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);
            mask-position: bottom;
        }
    }
</style>
