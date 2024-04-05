<script lang="ts">
    import { cn } from "$functions/classname";
    import { createEventDispatcher } from "svelte";
    // Icons
    import Chat from "$icons/Chat/Index.svelte";

    const dispatch = createEventDispatcher();
    export const handle_mobile = () => console.log(1);

    const handle_mobile_click = () => {
            dispatch("mobile_reply");
        },
        handle_tablet_click = () => {
            dispatch("tablet_reply");
        },
        handle_desktop_click = () => {
            dispatch("desktop_reply");
        };

    const button_mapping = [
        {
            action: handle_mobile_click,
            class: "sm:hidden"
        },
        {
            action: handle_tablet_click,
            class: "hidden sm:flex md:hidden"
        },
        {
            action: handle_desktop_click,
            class: "hidden md:flex"
        },
    ];
</script>

{#each button_mapping as item}
    <button
        on:click={item.action}
        class={cn(item.class, "btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw]")}
    >
        <Chat class="w-4 md:w-[1vw]" />
        <span>Replay</span>
    </button>
{/each}
