<script lang="ts">
    import Sky from "./paralax/sky.svg";
    import BackGround from "./paralax/back-ground.svg";
    import ForeGround from "./paralax/fore-ground.svg";
    import Floating1 from "./paralax/floating-1.svg";
    import Floating2 from "./paralax/floating-2.svg";
    import { onMount } from "svelte";
    // @ts-ignore
    import Typewriter from "typewriter-effect/dist/core";
    import { blur } from "svelte/transition";

    let sky_el: HTMLDivElement,
        background_el: HTMLDivElement,
        fore_ground_el: HTMLDivElement,
        floating_1_el: HTMLImageElement,
        floating_2_el: HTMLImageElement,
        gradient_el: HTMLDivElement,
        content_el: HTMLDivElement,
        heavy_svg: HTMLImageElement;

    let svg_loaded = false;

    onMount(() => {
        var app = document.getElementById("typing_text");

        var typewriter = new Typewriter(app, {
            loop: true,
            delay: 75
        });

        typewriter
            .typeString("For watching <b>Animes.</b>")
            .pauseFor(2000)
            .deleteChars(16)
            .typeString("reading <b>Mangas.</b>")
            .pauseFor(2000)
            .deleteChars(15)
            .typeString("listening to <b>Musics.</b>")
            .pauseFor(2000)
            .deleteAll()
            .typeString("Welcome to <b>CoreProject.</b>")
            .pauseFor(5000)
            .start();
    });

    const handle_svg_load = (e: Event) => {
        console.log("Loaded");
        svg_loaded = true;
    };

    function handle_window_scroll(e: Event) {
        let value = window.scrollY;

        sky_el.style.top = value * 0.75 + "px";
        content_el.style.marginTop = value * 0.85 + "px";
        gradient_el.style.top = value * 0.75 + "px";

        background_el.style.bottom = value * 0.15 + "px";
        fore_ground_el.style.bottom = value * 0 + "px";
        floating_1_el.style.marginTop = value * 0.5 + "px";
        floating_2_el.style.marginTop = value * 0.25 + "px";
    }
</script>

<svelte:window on:scroll={handle_window_scroll} />

{#if !svg_loaded}
    <div
        transition:blur
        class="fixed inset-0 z-[999] grid place-items-center bg-secondary"
    >
        <div class="animate-spin rounded-full bg-gradient-to-tr from-green-500 via-purple-500 to-blue-500 p-[0.25vw]">
            <div class="rounded-full bg-secondary">
                <div class="size-[7vw] rounded-full"></div>
            </div>
        </div>
    </div>
{/if}

<main class="h-screen w-screen bg-secondary">
    <section class="relative h-full w-full overflow-hidden">
        <div
            bind:this={gradient_el}
            class="absolute inset-0 bg-gradient-to-b from-[#2A1E80] to-[#EA76B3]"
        />
        <div
            bind:this={sky_el}
            class="sky absolute inset-x-0 left-1/2 mx-auto w-[75rem] -translate-x-1/2 transform md:w-full"
        >
            <img
                class="w-full"
                src={Sky}
                alt="Sky"
            />
        </div>

        <div
            bind:this={content_el}
            class="absolute inset-0 top-1/4 flex flex-col items-center gap-3 text-center md:top-[5vw] md:gap-[0.75vw] md:leading-none"
        >
            <h2 class="text-5xl font-bold text-white md:text-[5vw]">Imagine a new platform.</h2>
            <p
                class="text-2xl text-accent md:text-[2.5vw]"
                id="typing_text"
            ></p>
            <button class="btn btn-neutral h-max min-h-max p-4 text-lg leading-none md:rounded-[1vw] md:p-[1.1vw] md:text-[1.1vw]">Get Started</button>
        </div>

        <img
            bind:this={floating_1_el}
            class="floating floating-1 pointer-events-none absolute inset-x-0 left-10 top-[28rem] w-32 md:left-[15vw] md:top-1/4 md:w-[10vw]"
            src={Floating1}
            alt="Floating1"
        />
        <!-- this is the heaviest svg -->
        <div
            bind:this={background_el}
            class="background pointer-events-none absolute -left-20 bottom-0 w-[75rem] md:inset-x-0 md:left-0 md:w-full"
        >
            <img
                bind:this={heavy_svg}
                on:load={handle_svg_load}
                class="w-full"
                src={BackGround}
                alt="Background"
            />
        </div>
        <img
            bind:this={floating_2_el}
            class="floating floating-2 pointer-events-none absolute inset-x-0 left-64 top-[37rem] w-20 md:left-2/4 md:top-2/4 md:w-[7vw]"
            src={Floating2}
            alt="Floating2"
        />
        <div
            bind:this={fore_ground_el}
            class="mid-ground pointer-events-none absolute inset-x-0 -left-20 bottom-0 w-[90rem] md:left-0 md:w-full"
        >
            <img
                class="w-full"
                src={ForeGround}
                alt="ForeGround"
            />
        </div>
    </section>
    <section class="h-screen"></section>
</main>

<style>
    .floating {
        animation-name: floating;
        animation-duration: 3s;
        animation-iteration-count: infinite;
        animation-timing-function: ease-in-out;
        margin-left: 30px;
        margin-top: 5px;
    }

    .floating-1 {
        animation-delay: 0s;
    }

    .floating-2 {
        animation-delay: 1s;
    }

    @keyframes floating {
        0% {
            transform: translate(0, 0px);
        }
        50% {
            transform: translate(0, 1rem);
        }
        100% {
            transform: translate(0, -0px);
        }
    }
</style>
