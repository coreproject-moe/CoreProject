<script lang="ts">
    import { cn } from "$functions/classname";

    let klass = "";
    export { klass as class };
</script>

<div class={cn(klass, "mt-[1vw] items-center justify-center text-[1.5vw]")}>
    <div class="select-none inline-flex gap-[0.35vw] font-bold leading-none">
        <p class="inline-flex">
            <span class="text-accent opacity-75">c</span>
            <span class="text-warning">o</span>
            <span class="text-accent opacity-75">r</span>
            <span class="text-accent opacity-75">e</span>
        </p>
        <p class="inline-flex">
            <span class="text-white">p</span>
            <span class="text-white">r</span>
            <span class="text-white">o</span>
            <span class="text-white">j</span>
            <span class="text-white">e</span>
            <span class="text-white">c</span>
            <span class="text-white">t</span>
        </p>
    </div>
</div>
