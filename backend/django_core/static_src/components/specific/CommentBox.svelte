<script lang="ts">
    import TextArea from '../minor/TextArea.svelte';

    // Icons
    import Info from '../icons/info.svelte';
</script>

<div class="mt-3 flex flex-col gap-3 md:mt-[1vw] md:gap-[0.75vw]">
    <div
        class="relative rounded-lg ring-2 ring-surface-300/25 transition duration-300 focus-within:ring-primary md:rounded-[0.75vw] md:ring-[0.15vw] flex flex-col"
    >
        <TextArea />
    </div>
    <div class="flex justify-between gap-5 md:gap-[1vw]">
        <comment-alert class="flex items-center gap-3 md:gap-[0.625vw]">
            <Info class="w-10 md:w-[1.2vw] opacity-75" />
            <p
                class="text-[0.65rem] font-light leading-tight text-surface-300 md:text-[0.75vw] md:leading-[1.125vw]"
            >
                Please remember to follow our <a
                    href="/"
                    class="text-surface-200 underline">community guidelines</a
                > while commenting. Also please refrain from posting spoilers.
            </p>
        </comment-alert>
        <button
            class="btn btn-primary text-accent min-h-full h-9 w-40 rounded text-sm font-semibold md:h-[2.2vw] md:w-[6vw] md:rounded-[0.375vw] md:text-[0.85vw]"
            >Comment</button
        >
    </div>
</div>
