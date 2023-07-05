<script lang="ts">
    import Chevron from "$icons/chevron.svelte";
</script>

<section class="grid h-full grid-cols-5 items-end justify-between md:px-[5vw]">
    <radial-gradient
        class="pointer-events-none absolute inset-0 z-10 md:translate-x-[30vw]"
        style="background-image: radial-gradient(circle at center, rgba(117, 105, 225, 0.1) 0%, transparent 100%);"
    />
    <error-context class="col-span-12 flex flex-col items-center leading-none md:col-span-3 md:mb-[12vw] md:items-start md:gap-[1vw]">
        <status-code class="text-7xl font-bold md:text-[7vw]">
            {#each "404".split("") as number}
                <span class="odd:text-warning-400">{number}</span>
            {/each}
        </status-code>
        <status-text class="text-base font-semibold text-primary-300 md:text-[1.25vw]">Oops! Page not found...</status-text>
        <span class="mt-5 text-base font-semibold italic md:mt-[1vw] md:text-[1.2vw]">
            Hi <u>Ealime</u>
            here!
        </span>
        <context class="px-7 text-center text-xs font-semibold italic leading-snug text-surface-50 md:px-0 md:pr-[5vw] md:text-left md:text-[1.1vw] md:leading-[1.5vw]">
            Uh-oh looks like our
            {#each "kokoro-chan".split("") as letter}
                <span class="inline-grid odd:text-warning-400">
                    {letter}
                </span>
            {/each}
            is working really hard for the past few days and now has fall asleep. You can wait for her to wake up by looking at the status page, or come say hi to other fellow
            {#each "kokoro-chan".split("") as letter}
                <span class="inline-grid odd:text-warning-400">
                    {letter}
                </span>
            {/each}
            's worksippers! ah- also let's wish her sweat dreams!
        </context>
        <a
            href="/"
            class="btn mt-5 w-max gap-2 bg-primary-500 py-4 font-semibold leading-none md:mt-0 md:gap-[0.5vw] md:py-[1vw] md:text-[1.1vw]"
        >
            Explore animes
            <Chevron class="w-5 -rotate-90 md:w-[1.1vw]" />
        </a>
    </error-context>
    <character class="col-span-12 flex justify-center md:col-span-2">
        <img
            src="/images/characters/eliane.png"
            alt="Character 1"
            class="h-full w-64 md:w-full"
        />
    </character>
</section>
