<script lang="ts">
    import { cn } from '../../functions/classname';

    let klass = '';
    export { klass as class };

    export let parent_class = '';
    export let offset_scrollbar = false;
    export let gradient_mask = false;

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean;

    $: add_mask_bottom = scroll_area
        ? scroll_area.scrollHeight > scroll_area.clientHeight
        : false;

    function handle_scroll(event: Event) {
        const target = event.target as HTMLElement;
        const { scrollHeight, clientHeight, scrollTop } = target;
        add_mask_bottom =
            clientHeight + scrollTop === scrollHeight ? false : true;
    }
</script>

<div
    bind:this={scroll_area}
    on:scroll={handle_scroll}
    class={cn(
        parent_class,
        offset_scrollbar && 'pr-3 md:pr-[0.75vw]',
        'block h-full w-full overflow-y-scroll overscroll-y-contain scrollbar-thin [scrollbar-color:_rgba(255,255,255,0.12)_transparent]'
    )}
    class:[mask-image:linear-gradient(180deg,rgba(7,5,25,0.95)80%,rgba(0,0,0,0)100%)]={gradient_mask &&
        add_mask_bottom}
>
    <div>
        <div class={cn(klass)}>
            <slot />
        </div>
    </div>
</div>
