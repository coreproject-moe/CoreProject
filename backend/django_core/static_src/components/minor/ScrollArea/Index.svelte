<script lang="ts">
    import IntersectionObserver from "$components/svelte/IntersectionOberser.svelte";
    import { IS_CHROMIUM, IS_FIREFOX } from "$constants/browser";
    import { cn } from "$functions/classname";
    import { string_to_boolean } from "$functions/string_to_bool";

    let klass = "";
    export { klass as class };
    export let remove_gradient_on_mouse_enter: string = "false";
    export let parent_class = "";
    export let offset_scrollbar: string | boolean = "false";
    export let gradient_mask: string | boolean = "false";

    let scroll_area: HTMLElement;
    let add_mask_bottom: boolean,
        expanded = false;

    let first_element_intersecting: boolean, end_element_intersecting: boolean, first_element: HTMLElement, end_element: HTMLElement;

    $: add_mask_bottom = scroll_area ? scroll_area.scrollHeight > scroll_area.clientHeight : false;

    const handle_scroll = async (event: Event) => {
            const target = event.target as HTMLElement;
            const { scrollHeight, clientHeight, scrollTop } = target;
            add_mask_bottom = clientHeight + scrollTop === scrollHeight ? false : true;
        },
        handle_mouseenter = () => {
            expanded = true;

            if (remove_gradient_on_mouse_enter && string_to_boolean(remove_gradient_on_mouse_enter)) {
                add_mask_bottom = false;
            } else {
                scroll_area.addEventListener("transitionend", () => {
                    if (first_element_intersecting && end_element_intersecting) {
                        add_mask_bottom = false;
                    }
                });
            }
        },
        handle_mouseleave = () => {
            if (!expanded) {
                if (remove_gradient_on_mouse_enter && string_to_boolean(remove_gradient_on_mouse_enter)) {
                    scroll_area.addEventListener("transitionend", () => {
                        add_mask_bottom = true;
                    });
                } else {
                    scroll_area.addEventListener("transitionend", () => {
                        if (first_element_intersecting && end_element_intersecting) {
                            add_mask_bottom = true;
                        }
                    });
                }
                expanded = false;
            }
        };
    // TODO: Do AOT ( Ahead of Time ) calculations on `transitionrun` to  prevent flicker
</script>

<div
    role="contentinfo"
    bind:this={scroll_area}
    on:scroll|preventDefault={handle_scroll}
    on:mouseenter|preventDefault={handle_mouseenter}
    on:mouseleave|preventDefault={handle_mouseleave}
    class={cn(
        parent_class,
        string_to_boolean(offset_scrollbar) &&
            // Chromium support for scrollbar sucks
            !IS_CHROMIUM &&
            "pr-3 md:pr-[0.75vw]",

        "flex h-full w-full overflow-y-scroll overscroll-y-contain [scrollbar-color:rgba(255,255,255,0.12)transparent]"
    )}
    class:scrollbar-none={IS_CHROMIUM}
    class:scrollbar-thin={IS_FIREFOX}
    class:[mask-image:linear-gradient(180deg,rgba(7,5,25,0.95)80%,rgba(0,0,0,0)100%)]={string_to_boolean(gradient_mask) && add_mask_bottom}
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
                class="invisible h-0"
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
                class="invisible h-0"
            />
        </IntersectionObserver>
    </div>
</div>
