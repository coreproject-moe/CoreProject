<script lang="ts">
    import { cn } from "$functions/classname";
    import { goto, reverse } from "$functions/urls";
    import * as _ from "lodash-es";
    import { blur } from "svelte/transition";
    import { url } from "../../../stores/url";

    // Import Icons
    import Home from "$icons/Home/Index.svelte";
    import Compass from "$icons/Compass/Index.svelte";
    import List from "$icons/List/Index.svelte";
    import Calender from "$icons/Calender/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";

    let hover_glider_element: HTMLElement | null = null,
        glider_container_element: HTMLElement | null = null;

    export let glider_container_class: string | null = null,
        active_element_class: string | null = null;
    export let direction: "horizontal" | "vertical" = "horizontal",
        GLIDER_TRANSITION_DURATION = 200;

    let mouse_leave_timeout: NodeJS.Timeout,
        is_hovered_from_prev_el = false;

    const mappings = [
        {
            icon: {
                component: Home,
                class: `w-[1.25vw]`
            },
            label: "home",
            href: reverse("anime_home_view")
        },
        {
            icon: {
                component: Compass,
                class: `w-[1.25vw]`
            },

            label: "explore",
            href: "/anime/explore/"
        },
        {
            icon: {
                component: List,
                class: `w-[1.25vw]`
            },
            label: "list",
            href: "/anime/list/"
        },
        {
            icon: {
                component: Calender,
                class: `w-[1.25vw]`
            },
            href: "/anime/shedule",
            label: "schedule"
        },
        {
            icon: {
                component: Chat,
                class: `w-[1.25vw]`
            },
            href: "/anime/forum",
            label: "forum"
        }
    ];

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
                    hover_glider_element!.style.opacity = "100";
                }, GLIDER_TRANSITION_DURATION);
                is_hovered_from_prev_el = true;
            }

            clearTimeout(mouse_leave_timeout);
        },
        handle_mouseleave = () => {
            mouse_leave_timeout = setTimeout(() => {
                hover_glider_element!.style.opacity = "0";
                is_hovered_from_prev_el = false;
            }, GLIDER_TRANSITION_DURATION);
        };
</script>

<glider-container
    bind:this={glider_container_element}
    class={glider_container_class}
>
    <active-glider
        bind:this={hover_glider_element}
        class={cn(active_element_class, "absolute opacity-0 duration-200 ease-in-out")}
    />
    {#each mappings as item}
        {@const is_active = item.href === $url}
        <button
            on:mouseenter|preventDefault={handle_mouseenter}
            on:mouseleave|preventDefault={handle_mouseleave}
            on:click={() => {
                goto({ target: "#page", url: item.href, verb: "GET" });
            }}
            type="button"
            class="{cn(
                'btn relative h-[4vw] w-[4vw] rounded-[0.75vw] border-none p-0',
                is_active ? 'relative !bg-accent before:absolute before:-left-[0.15vw] before:z-10 before:h-[1.25vw] before:w-[0.25vw] before:rounded-full before:bg-primary' : '!bg-transparent'
            )} "
        >
            <div class="inline-grid">
                {#if is_active}
                    <div
                        transition:blur
                        class="absolute inset-0 flex flex-col items-center justify-center gap-[0.5vw]"
                    >
                        <icon class={cn("!text-secondary")}>
                            <svelte:component
                                this={item.icon.component}
                                class={item.icon.class}
                            />
                        </icon>
                    </div>
                {:else}
                    <div
                        transition:blur
                        class="absolute inset-0 flex flex-col items-center justify-center gap-[0.5vw]"
                    >
                        <icon class={cn("!text-white")}>
                            <svelte:component
                                this={item.icon.component}
                                class={item.icon.class}
                            />
                        </icon>

                        <span class="text-[0.75vw] font-semibold capitalize leading-[1.05vw]">{item.label}</span>
                    </div>
                {/if}
            </div>
        </button>
    {/each}
</glider-container>
