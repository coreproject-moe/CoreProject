<script lang="ts">
    import { cn } from "$functions/classname";
    import Chat from "$icons/Chat/Index.svelte";
    import { DeviceEnum } from "$types/device";
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    const handle_click = (device: DeviceEnum) => {
        dispatch("reply", device);
    };
</script>

<button
    on:click={() => handle_click(DeviceEnum.Mobile)}
    class={cn(`btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw] sm:hidden`)}
>
    <Chat class="w-4 md:w-[1vw]" />
    <span>Replay mob</span>
</button>

<button
    on:click={() => handle_click(DeviceEnum.Tablet)}
    class={cn(`btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw] hidden sm:flex md:hidden`)}
>
    <Chat class="w-4 md:w-[1vw]" />
    <span>Replay tab</span>
</button>

<button
    on:click={() => handle_click(DeviceEnum.Desktop)}
    class={cn(`btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw] hidden md:flex`)}
>
    <Chat class="w-4 md:w-[1vw]" />
    <span>Replay desk</span>
</button>
