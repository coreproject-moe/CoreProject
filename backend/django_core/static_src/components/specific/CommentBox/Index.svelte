<script lang="ts">
    import TextArea from "$components/minor/TextArea/Index.svelte";
    import { cn } from "$functions/classname";
    import { comment_needs_update } from "../../minor/Comment/store";
    // Icons
    import Info from "$icons/Info/Index.svelte";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";

    export let submit_url = "";

    let textarea_value = "";

    const handle_submit = async () => {
        if (!submit_url) {
            throw new Error("`submit_url` is needed");
        }
        if (!textarea_value) {
            throw new Error("`textarea_value` is empty");
        }

        const res = await fetch(submit_url, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": get_csrf_token()
            },
            body: JSON.stringify({
                text: textarea_value
            }),
            signal: AbortSignal.timeout(FETCH_TIMEOUT)
        });
        if (res.ok) {
            comment_needs_update.set(true);
            textarea_value = "";
        }
    };
</script>

<div class="flex flex-col gap-3 md:gap-[0.75vw]">
    <div class="ring-surface-300/25 relative flex flex-col rounded-lg ring-2 transition duration-300 focus-within:ring-primary md:rounded-[0.75vw] md:ring-[0.15vw]">
        <TextArea bind:textarea_value />
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
        <button
            on:click|preventDefault={async () => {
                await handle_submit();
            }}
            class={cn(textarea_value || "btn-disabled", "btn btn-primary h-9 min-h-full w-24 rounded-md text-sm font-semibold text-accent md:h-[2.2vw] md:w-[6vw] md:rounded-[0.375vw] md:text-[0.85vw]")}
        >
            Comment
        </button>
    </div>
</div>
