<script lang="ts">
    import { cn } from "$functions/classname";
    import { DeviceEnum } from "$types/device";
    import { createEventDispatcher } from "svelte";
    
    // Icons
    import Chat from "$icons/Chat/Index.svelte";

    const dispatch = createEventDispatcher();

    const button_mapping = [
        {
            device: DeviceEnum.Mobile,
            class: "sm:hidden"
        },
        {
            device: DeviceEnum.Tablet,
            class: "hidden sm:flex md:hidden"
        },
        {
            device: DeviceEnum.Desktop,
            class: "hidden md:flex"
        },
    ]

    const handle_click = (device: DeviceEnum) => {
        dispatch("reply", device);
    };
</script>

{#each button_mapping as item}
    <button
        on:click={() => handle_click(item.device)}
        class={cn(item.class, "btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw]")}
    >
        <Chat class="w-4 md:w-[1vw]" />
        <span>Replay</span>
    </button>
{/each}
