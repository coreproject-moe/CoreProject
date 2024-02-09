<script lang="ts">
    //@ts-ignore
    import { LottiePlayer } from "@lottiefiles/svelte-lottie-player";

    import AnimeCore from "$icons/AnimeCore/index.svelte";
    import MangaCore from "$icons/MangaCore/Index.svelte";
    import SoundCore from "$icons/SoundCore/Index.svelte";

    const products_mapping = [
        {
            icon: MangaCore,
            div_class: "order-2 md:order-1",
            icon_class: "!text-3xl md:!text-[2.5vw] !m-0",
            description:
                "Dive into the captivating world of manga with our streaming service. Access a diverse collection of manga titles, from timeless classics to the latest releases, and lose yourself in the art of storytelling.",
            href: "/manga",
            available: false
        },
        {
            icon: AnimeCore,
            div_class: "order-1 md:order-2",
            icon_class: "w-48 md:w-[15vw]",
            description: "Immerse yourself in a world of endless anime streaming. Explore a vast library of your favorite shows and discover new ones, all at your fingertips.",
            href: "/anime",
            available: true
        },
        {
            icon: SoundCore,
            div_class: "order-3 md:order-3",
            icon_class: "!text-3xl md:!text-[2.5vw] !m-0",
            description:
                "Elevate your auditory experience with our music streaming platform. Explore a rich tapestry of sounds, from chart-toppers to hidden gems, and let the music transport you to new dimensions of sonic bliss.",
            href: "/sound",
            available: false
        }
    ];
</script>

<div class="relative min-h-dvh overflow-x-hidden bg-secondary">
    <div class="absolute inset-0 overflow-hidden">
        {#await import("./lotties/bg-lottie.json") then item}
            <LottiePlayer
                src={item.default}
                autoplay={true}
                loop={false}
                renderer="svg"
                background="transparent"
                style={{ height: "100%", width: "100%", "object-fit": "contain" }}
            />
        {/await}
    </div>

    <section class="relative mt-20 flex w-full flex-col items-center justify-center md:mt-[10vh]">
        <div class="flex flex-col text-center text-5xl font-bold leading-none md:mt-[3vw] md:text-[8vw]">
            <h2 class="inline-block bg-gradient-to-r from-rose-500 from-[35%] to-blue-500 to-[65%] bg-clip-text text-transparent">Imagine a new</h2>
            <h2 class="relative inline-block bg-gradient-to-r from-blue-500 from-[35%] to-yellow-600 to-[65%] bg-clip-text text-transparent">
                Platform.
                <div class="absolute bottom-2 right-3 size-12 -rotate-45 md:bottom-[2vw] md:right-[5vw] md:size-[5vw]">
                    {#await import("./lotties/squiggle.json") then item}
                        <LottiePlayer
                            src={item.default}
                            autoplay={true}
                            loop={false}
                            mode={"bounce"}
                            speed={0.75}
                            renderer="svg"
                            background="transparent"
                        />
                    {/await}
                </div>
            </h2>
        </div>
        <p class="mt-2 max-w-72 text-center text-base opacity-90 md:mt-[3vw] md:max-w-[45vw] md:text-[1.25vw]">
            Bridging the gap between streaming and torrenting sites with a modern and clean interface.
        </p>
        <div class="relative flex items-center">
            <a
                href="#explore-our-trio"
                class="btn mt-4 h-max min-h-max rounded-xl border-none bg-gradient-to-r from-rose-500 to-blue-500 p-4 text-base leading-none text-accent shadow-lg shadow-rose-500/25 md:mt-[1vw] md:rounded-[1vw] md:p-[1.25vw] md:text-[1vw]"
            >
                Start Exploring Now!
            </a>
            <div class="absolute -right-14 size-14 md:-right-[4vw] md:size-[4vw]">
                {#await import("./lotties/stars.json") then item}
                    <LottiePlayer
                        src={item.default}
                        autoplay={true}
                        loop={false}
                        renderer="svg"
                        background="transparent"
                    />
                {/await}
            </div>
        </div>
        <div class="mt-5 size-6 opacity-75 md:mt-[3vw] md:size-[2vw]">
            {#await import("./lotties/scroll.json") then item}
                <LottiePlayer
                    src={item.default}
                    autoplay={true}
                    loop={true}
                    renderer="svg"
                    background="transparent"
                />
            {/await}
        </div>
    </section>

    <section
        id="explore-our-trio"
        class="relative mt-16 flex flex-col items-center justify-center md:mt-[10vw] md:py-[3vw]"
    >
        <h2 class="bg-gradient-to-r from-rose-500 from-[35%] to-blue-500 to-[65%] bg-clip-text text-2xl font-bold leading-none text-transparent md:text-[2.5vw]">Explore Our Trio.</h2>
        <div class="mt-2 flex flex-col items-end justify-center p-5 md:mt-[1vw] md:flex-row md:gap-[1.5vw]">
            {#each products_mapping as item}
                <div
                    class="relative flex flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed border-error bg-secondary p-5 text-center md:w-[20vw] md:gap-[1vw] md:rounded-[1vw] md:border-[0.15vw] md:p-[1vw]"
                    class:md:!w-[25vw]={item.available}
                    class:!border-none={!item.available}
                >
                    <svelte:component
                        this={item.icon}
                        class={item.icon_class}
                    />
                    <p class="line-clamp-3 text-sm md:line-clamp-4 md:text-[1.1vw] md:leading-[1.5vw]">
                        {item.description}
                    </p>
                    {#if item.available}
                        <a
                            href={item.href}
                            class="btn relative h-max min-h-max w-full rounded-xl border-none bg-gradient-to-r from-rose-500 to-blue-500 p-4 text-lg leading-none text-accent shadow-lg shadow-rose-500/25 md:rounded-[1vw] md:p-[1.25vw] md:text-[1.25vw]"
                        >
                            Explore
                        </a>
                    {:else}
                        <a
                            href="/"
                            class="btn relative h-max min-h-max w-full rounded-xl border-none bg-gradient-to-r from-rose-500 to-blue-500 p-3 text-lg leading-none text-accent md:rounded-[1vw] md:p-[1.25vw] md:text-[1.25vw]"
                        >
                            Coming soon
                        </a>
                        <div class="absolute inset-0 bg-secondary/75" />
                    {/if}
                </div>
            {/each}
        </div>
    </section>
</div>
