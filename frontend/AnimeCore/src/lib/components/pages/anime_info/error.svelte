<script lang="ts">
    import { format_kokoro_color } from "$functions/format_kokoro";
    import Chevron from "$icons/chevron.svelte";
    import sample from "lodash/sample";

    const items: Array<{
        image: { src: string; alt: string; class?: string };
        class?: string;
        gradient: { mobile: string; desktop: string; class?: string };
    }> = [
        {
            image: {
                src: "/images/characters/eliane/eliane.png",
                alt: "Elaine"
            },
            gradient: {
                class: "h-[50dvh] w-[100dvw] md:h-[40dvw] md:w-[calc(100%*2)]",
                mobile: "radial-gradient(50dvh circle at center, rgba(218, 202, 207, 0.25) 0%, transparent 50%)",
                desktop: "radial-gradient(40dvw circle at center, rgba(218, 202, 207, 0.25) 0%, transparent 50%)"
            }
        },
        {
            image: {
                src: "/images/characters/ichigo/ichigo.png",
                alt: "Ichigo",
                class: "ml-auto"
            },
            class: "items-end",
            gradient: {
                class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
                mobile: "radial-gradient(45dvh circle at center, rgba(137, 155, 206, 0.25) 0%, transparent 50%)",
                desktop: "radial-gradient(45dvw circle at center, rgba(137, 155, 206, 0.25) 0%, transparent 50%)"
            }
        },
        {
            image: {
                src: "/images/characters/sasha/sasha.png",
                alt: "Sasha"
            },
            gradient: {
                class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
                mobile: "radial-gradient(50dvh circle at center, rgba(181, 124, 82, 0.25) 0%, transparent 50%)",
                desktop: "radial-gradient(45dvw circle at center, rgba(181, 124, 82, 0.25) 0%, transparent 50%)"
            }
        },
        {
            image: {
                src: "/images/characters/laura/laura.png",
                alt: "Laura"
            },
            gradient: {
                class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
                mobile: "radial-gradient(50dvh circle at center, rgba(243, 243, 243, 0.25) 0%, transparent 50%)",
                desktop: "radial-gradient(45dvw circle at center, rgba(243, 243, 243, 0.25) 0%, transparent 50%)"
            }
        }
    ];
    const mapping: {
        image: { src: string; alt: string; class?: string };
        class?: string;
        gradient: { mobile: string; desktop: string; class?: string };
    } = sample(items)!; // This logically can't be undefined or null
</script>

<svelte:head>
    <link
        href={mapping.image.src}
        rel="preload"
        as="image"
    />
    <style>
        #page {
            overflow: hidden;
        }
    </style>
</svelte:head>

<section class="{mapping.class} relative flex h-full grid-cols-5 flex-col justify-end gap-20 md:grid md:items-end md:gap-0">
    <error-context class="col-span-5 flex flex-col items-center leading-none md:col-span-3 md:mb-[13vw] md:items-start md:gap-[1vw] md:pl-[5vw]">
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
        class="relative col-span-5 flex items-end justify-center md:col-span-2"
        style="--mobile-gradient:{mapping.gradient.mobile}; --desktop-gradient:{mapping.gradient.desktop}"
    >
        <gradient class="{mapping.gradient.class} absolute [background:var(--mobile-gradient)] md:[background:var(--desktop-gradient)]" />

        <img
            src={mapping.image.src}
            alt={mapping.image.alt}
            class="{mapping.image.class ?? ''} relative h-[40dvh] object-contain object-bottom md:h-[100dvh]"
        />
    </character-image>
</section>
