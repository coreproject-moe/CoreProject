<script lang="ts">
    import IntersectionObserver from "svelte-intersection-observer";
    import { cn } from "$functions/classname";
    import { get_transition_duration_as_ms } from "$functions/get_transition_durtion_as_ms";

    let klass = "";
    export { klass as class };
    export let parent_class = "";
    export let offset_scrollbar = false;
    export let gradient_mask = false;

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean;

    let first_element_intersecting: boolean, second_element_intersecting: boolean, first_element: HTMLElement, second_element: HTMLElement;

    $: add_mask_bottom = scroll_area ? scroll_area.scrollHeight > scroll_area.clientHeight : false;

    const handle_scroll = async (event: Event) => {
            const target = event.target as HTMLElement;
            const { scrollHeight, clientHeight, scrollTop } = target;
            add_mask_bottom = clientHeight + scrollTop === scrollHeight ? false : true;
        },
        handle_mouseenter = () => {
            const duration = get_transition_duration_as_ms({ element: scroll_area, ms: true });
            setTimeout(
                () => {
                    if (first_element_intersecting && second_element_intersecting) {
                        add_mask_bottom = false;
                    }
                },
                duration ? duration / 4 : 0
            );
        },
        handle_mouseleave = () => {
            setTimeout(
                () => {
                    if (first_element_intersecting && second_element_intersecting) {
                        add_mask_bottom = true;
                    }
                },
                get_transition_duration_as_ms({ element: scroll_area, ms: true }) ?? 0
            );
        };
</script>

<div
    role="contentinfo"
    bind:this={scroll_area}
    on:scroll={handle_scroll}
    on:mouseenter={handle_mouseenter}
    on:mouseleave={handle_mouseleave}
    class={cn(parent_class, offset_scrollbar && "pr-3 md:pr-[0.75vw]", "flex h-full w-full overflow-y-scroll overscroll-y-contain scrollbar-thin [scrollbar-color:rgba(255,255,255,0.12)transparent]")}
    class:[mask-image:linear-gradient(180deg,rgba(7,5,25,0.95)80%,rgba(0,0,0,0)100%)]={gradient_mask && add_mask_bottom}
>
    <div class={cn(klass)}>
        <IntersectionObserver
            element={first_element}
            bind:intersecting={first_element_intersecting}
            threshold={1}
        >
            <div bind:this={first_element} />
        </IntersectionObserver>

        <slot />

        <IntersectionObserver
            element={second_element}
            bind:intersecting={second_element_intersecting}
            threshold={1}
        >
            <div bind:this={second_element} />
        </IntersectionObserver>
    </div>
</div>
