<script lang="ts">
    import { cn } from "$functions/classname";
    import * as _ from "lodash-es";

    let hover_glider_element: HTMLElement | null = null,
        glider_container_element: HTMLElement | null = null;

    export let glider_container_class: string | null = null,
        active_element_class: string | null = null;

    export let direction: "horizontal" | "vertical" = "horizontal",
        GLIDER_TRANSITION_DURATION = 200;

    let mouse_leave_timeout: NodeJS.Timeout,
        is_hovered_from_prev_el = false;

    const handle_mouseenter = (event: Event) => {
            const target = event.target as HTMLElement;
            const target_computed_style = getComputedStyle(target);
            if (_.isNull(glider_container_element) || _.isNull(hover_glider_element)) return;

            glider_container_element.style.position = "relative";

            hover_glider_element.style.height = target_computed_style.height;
            hover_glider_element.style.width = target_computed_style.width;

            const target_zindex = parseInt(target_computed_style.zIndex);
            glider_container_element.style.zIndex = String(target_zindex ?? 0);
            hover_glider_element.style.zIndex = String(target_zindex - 1 ?? -1);

            switch (direction) {
                case "vertical":
                    hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;
                    break;
                case "horizontal":
                    hover_glider_element.style.transform = `translateX(${target.offsetLeft}px)`;
                    break;
                default:
                    throw Error("Method Not Implemented");
            }

            if (is_hovered_from_prev_el) {
                GLIDER_TRANSITION_DURATION = 200;
                hover_glider_element.style.transitionDuration = `${GLIDER_TRANSITION_DURATION}ms`;
            } else {
                GLIDER_TRANSITION_DURATION = 100;
                hover_glider_element.style.transitionDuration = `${GLIDER_TRANSITION_DURATION}ms`;
                setTimeout(() => {
                    if (hover_glider_element) {
                        hover_glider_element.style.opacity = "100";
                    }
                }, GLIDER_TRANSITION_DURATION);
                is_hovered_from_prev_el = true;
            }

            clearTimeout(mouse_leave_timeout);
        },
        handle_mouseleave = () => {
            mouse_leave_timeout = setTimeout(() => {
                if (hover_glider_element) {
                    hover_glider_element.style.opacity = "0";
                }
                is_hovered_from_prev_el = false;
            }, GLIDER_TRANSITION_DURATION);
        };
</script>

<div
    bind:this={glider_container_element}
    class={glider_container_class}
>
    <div
        bind:this={hover_glider_element}
        class={cn(active_element_class, "absolute opacity-0 duration-200 ease-in-out")}
    />
    <slot
        {handle_mouseenter}
        {handle_mouseleave}
    />
</div>
