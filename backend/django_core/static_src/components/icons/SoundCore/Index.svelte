<script lang="ts">
    import { cn } from "$functions/classname";

    let klass = "";
    export { klass as class };
</script>

<div class={cn(klass, "mt-[1vw] items-center justify-center text-[1.5vw]")}>
    <div class="select-none inline-flex gap-[0.25vw] font-bold leading-none">
        <p class="inline-flex">
            <span class="text-white">s</span>
            <span class="text-white">o</span>
            <span class="text-white">u</span>
            <span class="text-white">n</span>
            <span class="text-white">d</span>
        </p>
        <p class="inline-flex">
            <span class="text-accent opacity-75">c</span>
            <span class="text-warning">o</span>
            <span class="text-accent opacity-75">r</span>
            <span class="text-accent opacity-75">e</span>
        </p>
    </div>
</div>