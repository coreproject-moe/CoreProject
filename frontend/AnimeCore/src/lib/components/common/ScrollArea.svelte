<script lang="ts">
    let klass = "";
    export { klass as class };
</script>

<div on:mouseenter on:mouseleave class="{klass} scrollbar overflow-y-scroll">
    <slot />
</div>

<style lang="scss">
    .scrollbar {
        scrollbar-width: thin;
        scrollbar-color: rgba(255, 255, 255, 0.12);

        /* fill parent */
        display: block;
        width: 100%;
        height: 100%;

        /* set to some transparent color */
        border-color: rgba(255, 255, 255, 0);
        /* here we make the color transition */
        transition: border-color 0.2s linear;

        &:hover {
            /* the color we want the scrollbar on hover */
            border-color: rgba(255, 255, 255, 0.12);
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
    }
</style>
