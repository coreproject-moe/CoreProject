<script lang="ts">
    import TextArea from "../minor/TextArea.svelte";

    // Icons
    import Info from "../icons/Info.svelte";

    export const submit_url = "";

    let textarea_value: string;
    async function handle_submit() {
        await fetch(submit_url, {
            method: "POST",
            credentials: "same-origin",
            body: JSON.stringify({ comment: textarea_value }),
            headers: {
                "X-CSRFToken": window.csrfmiddlewaretoken
            }
        });
    }
</script>

<div class="flex flex-col gap-3 md:gap-[0.75vw]">
    <div class="ring-surface-300/25 relative flex flex-col rounded-lg ring-2 transition duration-300 focus-within:ring-primary md:rounded-[0.75vw] md:ring-[0.15vw]">
        <TextArea />
    </div>
    <div class="flex justify-between gap-5 md:gap-[1vw]">
        <comment-alert class="flex items-center gap-3 md:gap-[0.625vw]">
            <Info class="w-10 opacity-75 md:w-[1.2vw]" />
            <p class="text-surface-300 text-[0.65rem] font-light leading-tight md:text-[0.75vw] md:leading-[1.125vw]">
                Please remember to follow our <a
                    href="/"
                    class="text-surface-200 underline"
                >
                    community guidelines
                </a>
                while commenting. Also please refrain from posting spoilers.
            </p>
        </comment-alert>
        <button class="btn btn-primary h-9 min-h-full w-40 rounded text-sm font-semibold text-accent md:h-[2.2vw] md:w-[6vw] md:rounded-[0.375vw] md:text-[0.85vw]">Comment</button>
    </div>
</div>
