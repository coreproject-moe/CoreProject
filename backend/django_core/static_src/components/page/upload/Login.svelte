<script lang="ts">
    import { createEventDispatcher } from "svelte";
    import Chevron from "$icons/Chevron/Index.svelte";
    import Info from "$icons/Info/Index.svelte";

    const dispatch = createEventDispatcher();

    let doodsteam_token = "";
    const handle_submit = () => {
        dispatch("submit", {
            doodstream: doodsteam_token
        });
    };
</script>

<div class="h-screen w-screen md:grid md:grid-cols-[2fr_1fr] md:gap-[5vw] md:px-[5vw] md:pt-[5vw]">
    <form
        class="h-full w-full"
        on:submit|preventDefault={handle_submit}
    >
        <span class="text-2xl font-semibold md:text-[1.5vw] md:leading-[1.5vw]">
            Paste your
            <span class="text-warning-400 inline-flex">API</span>
            token
        </span>
        <span class="text-surface-50 text-xl md:text-[1vw] md:leading-[2vw]">for seamless integration</span>

        <div class="mt-10 flex md:mt-[5vw]">
            <div class="flex w-full flex-col md:gap-[0.35vw]">
                <span class="text-xl font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Doodstream Token</span>
                <div class="flex justify-between gap-5 md:gap-[1vw]">
                    <input
                        name="doodstream"
                        bind:value={doodsteam_token}
                        placeholder="Doodstream token"
                        class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.5vw] md:rounded-[0.6vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                    />
                    <button
                        type="submit"
                        class="btn btn-primary font-semibold leading-none md:h-[3.5vw] md:w-[9vw] md:rounded-[0.6vw] md:text-[1vw]"
                    >
                        <span>Continue</span>
                        <Chevron class="w-4 -rotate-90 md:w-[1.25vw]" />
                    </button>
                </div>
                <div class="flex items-center gap-2 md:gap-[0.5vw]">
                    <Info class="w-3 opacity-70 md:w-[1vw]"></Info>

                    <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.9vw]">Insert your unique API token here to unlock the full potential of Doodsteam's video services</span>
                </div>
            </div>
        </div>
    </form>
    <div class="flex flex-col items-end justify-end">
        <gradient class="pointer-events-none absolute [background:var(--mobile-gradient)] md:[background:var(--desktop-gradient)]"></gradient>

        <img
            src="https://github-production-user-asset-6210df.s3.amazonaws.com/114811070/281985715-a3a0f410-bf85-4d99-b736-6a386cba716d.png"
            alt="Fish"
        />
    </div>
</div>
