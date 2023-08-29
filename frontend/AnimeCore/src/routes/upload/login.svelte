<script lang="ts">
    import { fish_mapping } from "$data/fish_mapping";
    import Chevron from "$icons/chevron.svelte";
    import { ValidationMessage, reporter } from "@felte/reporter-svelte";
    import { validator } from "@felte/validator-zod";
    import { focusTrap } from "@skeletonlabs/skeleton";
    import { createForm } from "felte";
    import { sample } from "lodash";
    import { createEventDispatcher, onMount } from "svelte";
    import { blur } from "svelte/transition";
    import { z } from "zod";

    let mapping: (typeof fish_mapping)[0] | undefined; // This logically can't be undefined or null

    // to prevent double mounting
    onMount(() => {
        mapping = sample(fish_mapping);
    });

    // form validation
    const dispatch = createEventDispatcher();

    const schema = z.object({
        streamsb: z.string().min(20, "Please provide a valid API token")
    });

    const { form } = createForm<z.infer<typeof schema>>({
        initialValues: {
            streamsb: ""
        },
        onSubmit: async (values) => {
            dispatch("submit", values);
        },
        extend: [reporter, validator({ schema })]
    });
</script>

{#if mapping}
    <login-container
        transition:blur
        class="{mapping.class} flex h-full w-full grid-cols-12 flex-col justify-end md:grid md:items-start md:gap-[5vw] md:pl-[3.75vw]"
    >
        <form
            use:form
            use:focusTrap={true}
            class="col-span-12 mb-32 flex flex-col p-5 md:col-span-7 md:mb-0 md:mt-[2vw] md:p-0"
        >
            <span class="text-2xl font-semibold md:text-[1.5vw] md:leading-[1.5vw]">
                Paste your
                <span class="inline-flex text-warning-400">API</span>
                token
            </span>
            <span class="text-xl text-surface-50 md:text-[1vw] md:leading-[2vw]">for seamless integration</span>

            <providers class="mt-10 md:mt-[5vw]">
                <streamsb class="flex flex-col md:gap-[0.25vw]">
                    <span class="text-xl font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Stream SB</span>
                    <token-input class="flex justify-between gap-5 md:gap-[1vw]">
                        <input
                            name="streamsb"
                            placeholder="StreamSB token"
                            class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.6vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                        />
                        <button
                            type="submit"
                            class="btn bg-primary-500 font-semibold leading-none md:rounded-[0.6vw] md:px-[1vw] md:py-[0.5vw] md:text-[1vw]"
                        >
                            <span>Continue</span>
                            <Chevron class="w-4 -rotate-90 md:w-[1vw]" />
                        </button>
                    </token-input>
                    <ValidationMessage
                        for="streamsb"
                        let:messages={message}
                    >
                        <span class="text-lg leading-snug text-surface-50 md:text-[1vw] md:leading-[1.25vw]">
                            {@html message}
                        </span>
                        <span
                            slot="placeholder"
                            class="text-lg leading-snug text-surface-50 md:text-[1vw] md:leading-[1.25vw]"
                        >
                            Insert your unique API token here to unlock the full potential of Streamsb's video services
                        </span>
                    </ValidationMessage>
                </streamsb>
            </providers>
        </form>
        <character-image
            class="relative col-span-12 flex items-end justify-center md:col-span-5"
            style="--mobile-gradient:{mapping.gradient.mobile}; --desktop-gradient:{mapping.gradient.desktop}"
        >
            <gradient class="{mapping.gradient.class} pointer-events-none absolute [background:var(--mobile-gradient)] md:[background:var(--desktop-gradient)]" />

            <img
                src={mapping.image.src}
                alt={mapping.image.alt}
                class="{mapping.image.class ?? ''} relative h-[40dvh] object-contain object-bottom md:h-[90dvh]"
            />
        </character-image>
    </login-container>
{/if}
