<script lang="ts">
    import { format_kokoro_color } from "$functions/format_kokoro";
    import Chevron from "$icons/chevron.svelte";
    import sample from "lodash/sample";
    import { onMount } from "svelte";
    import { blur } from "svelte/transition";
    import { fish_mapping } from "$data/fish_mapping";

    let mapping: (typeof fish_mapping)[0] | undefined;

    // onMount is here to prevent double mount of this.
    onMount(() => {
        mapping = sample(fish_mapping);
    });
</script>

<svelte:head>
    <link
        href={mapping?.image.src}
        rel="preload"
        as="image"
    />
    <style>
        #page {
            overflow: hidden;
        }
    </style>
</svelte:head>

{#if mapping}
    {@const is_image_left_or_right = sample(mapping.position)}
    {@const on_left = is_image_left_or_right === "left"}
    {@const on_right = is_image_left_or_right === "right"}

    <section
        transition:blur
        class:md:flex-row-reverse={on_left}
        class:md:flex-row={on_right}
        class="{mapping.class} relative flex h-full flex-col justify-end gap-20 md:items-end md:gap-0"
    >
        <error-context class="flex flex-col items-center leading-none md:mb-[13vw] md:w-[70dvw] md:items-start md:gap-[1vw] md:pl-[5vw]">
            <status-code class="text-7xl font-bold md:text-[7vw]">
                {#each "404".split("") as number}
                    <span class="odd:text-warning-400">{number}</span>
                {/each}
            </status-code>
            <status-text class="text-base font-semibold text-primary-300 md:text-[1.25vw]">Oops! Page not found...</status-text>
            <span class="mt-5 text-base font-semibold italic md:mt-[1vw] md:text-[1.2vw]">
                Hi <u>{mapping.image.alt}</u>
                here!
            </span>
            <context class="select-none px-7 text-center text-xs font-semibold italic leading-snug text-surface-50 md:px-0 md:pr-[5vw] md:text-left md:text-[1.1vw] md:leading-[1.5vw]">
                {@html format_kokoro_color(`Uh-oh looks like our kokoro-chan is working really hard for the past few days and now has fall asleep. You can wait for her to wake up by looking at the status page, or come say hi to other fellow kokoro-chan's worksippers! ah- also let's wish her sweat dreams!`)}
            </context>
            <a
                href="/explore"
                class="btn mt-5 w-max gap-2 bg-primary-500 py-4 font-semibold leading-none md:mt-0 md:gap-[0.5vw] md:py-[1vw] md:text-[1.1vw]"
            >
                Explore animes
                <Chevron class="w-5 -rotate-90 md:w-[1.1vw]" />
            </a>
        </error-context>
        <character-image
            class="pointer-events-none relative flex items-end justify-center md:w-[45dvw]"
            style="--mobile-gradient:{mapping.gradient.mobile}; --desktop-gradient:{mapping.gradient.desktop}"
        >
            <gradient
                class:md:ml-[8vw]={on_left}
                class="{mapping.gradient.class ?? ''} absolute [background:var(--mobile-gradient)] md:[background:var(--desktop-gradient)]"
            />

            <img
                src={mapping.image.src}
                alt={mapping.image.alt}
                class="{mapping.image.class ?? ''} relative h-[40dvh] object-contain object-bottom md:h-[100dvh]"
            />
        </character-image>
    </section>
{/if}
