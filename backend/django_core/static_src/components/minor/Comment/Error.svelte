<script lang="ts">
    export let error: string;
</script>

<div class="flex w-full items-center justify-center md:gap-[1vw]">
    <img
        src="/static/public/images/gifs/sad.gif"
        alt=""
        class="md:h-[10vw]"
    />
    <div class="flex flex-col md:gap-[0.1vw]">
        <span class="font-semibold md:text-[1.5vw]">Something went wrong!</span>
        <span class="italic md:text-[1.15vw]">Error: {error}</span>
    </div>
</div>
