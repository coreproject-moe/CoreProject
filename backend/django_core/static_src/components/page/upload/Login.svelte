<script lang="ts">
    import Chevron from "$icons/Chevron/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import FishGradient from "../../../public/images/fish/fish-gradient.png?url";

    import { provider } from "./store/provider";

    let doodsteam_token = "";
    const handle_submit = () => {
        provider.set({
            doodstream: doodsteam_token
        });
    };
</script>

<div class="flex min-h-screen w-screen flex-col justify-between gap-20 bg-secondary p-5 !pb-0 md:grid md:grid-cols-2 md:gap-0 md:p-[5vw]">
    <form
        class="w-full md:h-full"
        on:submit|preventDefault={handle_submit}
    >
        <div class="flex flex-col md:gap-[0.2vw]">
            <span class="text-2xl font-semibold md:text-[1.5vw] md:leading-[1.5vw]">
                Paste your
                <span class="inline-flex text-warning">API</span>
                token
            </span>
            <span class="text-base md:text-[1.1vw] md:leading-[2vw]">for seamless integration</span>
        </div>

        <div class="mt-10 flex md:mt-[3vw]">
            <div class="flex w-full flex-col gap-1 md:gap-[0.35vw]">
                <span class="text-lg font-semibold leading-none md:text-[1.25vw] md:leading-[1.5vw]">Doodstream Token</span>
                <div class="flex justify-between gap-3 md:gap-[0.75vw]">
                    <input
                        name="doodstream"
                        bind:value={doodsteam_token}
                        placeholder="Doodstream token"
                        class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-lg border-2 bg-transparent px-5 text-base font-medium text-white outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.5vw] md:rounded-[0.6vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                    />
                    <button
                        type="submit"
                        class="btn btn-primary min-h-full font-semibold leading-none md:h-[3.5vw] md:rounded-[0.6vw] md:text-[1vw]"
                    >
                        <span>Continue</span>
                        <Chevron class="w-4 -rotate-90 md:w-[1.25vw]" />
                    </button>
                </div>
                <div class="flex items-center gap-2 md:gap-[0.5vw]">
                    <Info class="w-5 opacity-70 md:w-[1vw]"></Info>

                    <span class="text-surface-300 text-[0.7rem] leading-snug md:text-[0.9vw]">Insert your unique API token here to unlock the full potential of Doodsteam's video services</span>
                </div>
            </div>
        </div>
    </form>
    <div class="flex flex-col items-end justify-end self-end">
        <img
            src={FishGradient}
            alt="Fish"
        />
    </div>
</div>
