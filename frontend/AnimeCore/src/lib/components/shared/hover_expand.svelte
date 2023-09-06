<script lang="ts">
    import { cn } from "$functions/classnames";
    import ScrollArea from "./scroll_area.svelte";

    let klass: string = "";
    export { klass as class };
    export let height: string = "";
    export let duration: string = "duration-300";
    export let line_clamp: string = "line-clamp-1";
</script>

<ScrollArea class={cn(klass, height, duration, "overflow-hidden ease-in-out scrollbar-none hover:overflow-y-scroll")}>
    <span class={cn(line_clamp, "md:line-clamp-none [&:not(:hover)]:[mask-image:_linear-gradient(90deg,_rgba(7,5,25)_75%,_rgba(0,0,0,0)_100%)]")}>
        <slot />
    </span>
</ScrollArea>