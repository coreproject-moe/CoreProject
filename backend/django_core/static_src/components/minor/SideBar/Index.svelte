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
    import VercelHover from "$components/svelte/VercelHover.svelte";

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
</script>

<VercelHover
    glider_container_class="mt-[2.8125vw] flex flex-col items-center gap-[0.75vw]"
    active_element_class="rounded-[0.75vw] bg-white/10"
    direction="vertical"
    GLIDER_TRANSITION_DURATION={200}
    let:handle_mouseenter
    let:handle_mouseleave
>
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
</VercelHover>
