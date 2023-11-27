<svelte:options
    customElement={{
        tag: 'scroll-area',
        shadow: 'none',
    }}
/>

<script lang="ts">
    import { cn } from '../functions/classname.js';

    let klass = '';
    export { klass as class };

    export let parentClass = '';
    export let offsetScrollbar = false;
    export let gradientMask = false;

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean;

    $: add_mask_bottom = scroll_area
        ? scroll_area.scrollHeight > scroll_area.clientHeight
        : false;

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
    class={cn(
        parentClass,
        offsetScrollbar && 'pr-3 md:pr-[0.75vw]',
        'block h-full w-full overflow-y-scroll overscroll-y-contain scrollbar-thin [scrollbar-color:_rgba(255,255,255,0.12)_transparent]'
    )}
    class:[mask-image:_linear-gradient(180deg,_rgba(7,5,25,0.95)_80%,_rgba(0,0,0,0)_100%)]={gradientMask &&
        add_mask_bottom}
>
    <div>
        <div class={cn(klass)}>
            <slot />
        </div>
    </div>
</scroll-area>
