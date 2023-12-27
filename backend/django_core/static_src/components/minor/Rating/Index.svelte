<script lang="ts">
    import { cn } from "$functions/classname";

    const klass = "md:w-[0.75vw] md:h-[1.5vw]";
    export {klass as class};

    let RATING_COUNT = 5;
</script>

<div class="rating rating-half">
    {#each Array(RATING_COUNT) as _}
        {@const common_classes = "bg-accent checked:!bg-accent border-none mask mask-star-2"}

        <input type="radio" name="rating-10" class={cn(klass, common_classes, "mask-half-1")} />
        <input type="radio" name="rating-10" class={cn(klass, common_classes, "mask-half-2")} />
    {/each}
</div>
