<script lang="ts">
    import { cn } from "$functions/classnames";

    export let glider_container_class = "";
    export let active_element_class = "";
    export let direction: "horizontal" | "vertical";

    /** vercel effect */
    let hover_glider_element: HTMLElement,
        glider_container_element: HTMLElement,
        GLIDER_TRANSITION_DURATION = 200,
        is_hovered = false, // Boolean switch flag
        mouse_leave_timeout: NodeJS.Timeout | null = null;

    const handle_mouseenter = (event: MouseEvent) => {
            const target = event.target as HTMLElement;
            const target_computed_style = getComputedStyle(target);

            // To make sure our operations are proper we need to make sure that the `position` is set to relative
            glider_container_element.style.position = "relative";

            // Do some magic here to get the target's height and width
            // Don't change the position of this code.
            // It will cause animation jank
            hover_glider_element.style.height = target_computed_style.height;
            hover_glider_element.style.width = target_computed_style.width;

            // We need to make sure that zIndex is not auto
            const target_zindex = parseInt(target_computed_style.zIndex);
            hover_glider_element.style.zIndex = String(target_zindex ? target_zindex - 1 : -1);

            switch (direction) {
                case "vertical":
                    hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;
                    break;
                case "horizontal":
                    hover_glider_element.style.transform = `translateX(${target.offsetLeft}px)`;
                    break;
            }

            if (!is_hovered) {
                GLIDER_TRANSITION_DURATION = 50;
                hover_glider_element.style.opacity = "100";
                is_hovered = true;
            } else {
                GLIDER_TRANSITION_DURATION = 200;
            }

            clearTimeout(mouse_leave_timeout!);
        },
        handle_mouseleave = () => {
            // Delay the mouseleave event to allow time ( GLIDER_TRANSITION_DURATION ) for moving to a sibling element
            mouse_leave_timeout = setTimeout(() => {
                hover_glider_element.style.opacity = "0";
                is_hovered = false;
            }, GLIDER_TRANSITION_DURATION);
        };
</script>

<glider-container
    class={glider_container_class}
    bind:this={glider_container_element}
>
    <active_glider
        bind:this={hover_glider_element}
        class={cn(active_element_class,`absolute opacity-0 ease-in-out duration-${GLIDER_TRANSITION_DURATION}`)}
    />

    <slot
        {handle_mouseleave}
        {handle_mouseenter}
    />
</glider-container>
