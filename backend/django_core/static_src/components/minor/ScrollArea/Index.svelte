<script lang="ts">
    import IntersectionObserver from "$components/svelte/IntersectionOberser.svelte";
    import { cn } from "$functions/classname";

    let klass = "";
    export { klass as class };
    export let parent_class = "";
    export let offset_scrollbar = false;
    export let gradient_mask = false;

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean;

    let first_element_intersecting: boolean, end_element_intersecting: boolean, first_element: HTMLElement, end_element: HTMLElement;

    $: add_mask_bottom = scroll_area ? scroll_area.scrollHeight > scroll_area.clientHeight : false;

    const handle_scroll = async (event: Event) => {
            const target = event.target as HTMLElement;
            const { scrollHeight, clientHeight, scrollTop } = target;
            add_mask_bottom = clientHeight + scrollTop === scrollHeight ? false : true;
        },
        handle_mouseenter = () => {
            scroll_area.addEventListener("transitionend", () => {
                if (first_element_intersecting && end_element_intersecting) {
                    add_mask_bottom = false;
                }
            });
        },
        handle_mouseleave = () => {
            scroll_area.addEventListener("transitionend", () => {
                if (first_element_intersecting && end_element_intersecting) {
                    add_mask_bottom = true;
                }
            });
        };
    // TODO: Do AOT ( Ahead of Time ) calculations on `transitionrun` to  prevent flicker
</script>

<div
    role="contentinfo"
    bind:this={scroll_area}
    on:scroll|preventDefault={handle_scroll}
    on:mouseenter|preventDefault={handle_mouseenter}
    on:mouseleave|preventDefault={handle_mouseleave}
    class={cn(parent_class, offset_scrollbar && "pr-3 md:pr-[0.75vw]", "flex h-full w-full overflow-y-scroll overscroll-y-contain scrollbar-thin [scrollbar-color:rgba(255,255,255,0.12)transparent]")}
    class:[mask-image:linear-gradient(180deg,rgba(7,5,25,0.95)80%,rgba(0,0,0,0)100%)]={gradient_mask && add_mask_bottom}
>
    <div class={cn(klass)}>
        <IntersectionObserver
            root={scroll_area}
            element={first_element}
            bind:intersecting={first_element_intersecting}
            threshold={1}
        >
            <div
                bind:this={first_element}
                class="hidden h-0"
            />
        </IntersectionObserver>

        <slot />

        <IntersectionObserver
            root={scroll_area}
            element={end_element}
            bind:intersecting={end_element_intersecting}
            threshold={1}
        >
            <div
                bind:this={end_element}
                class="hidden h-0"
            />
        </IntersectionObserver>
    </div>
</div>
