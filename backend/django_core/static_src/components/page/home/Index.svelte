<script lang="ts">
    import Sky from "./paralax/sky.svg";
    import BackGround from "./paralax/back-ground.svg";
    import ForeGround from "./paralax/fore-ground.svg";
    import Floating1 from "./paralax/floating-1.svg";
    import Floating2 from "./paralax/floating-2.svg";

    // @ts-ignore
    import Typewriter from "typewriter-effect/dist/core";
    import { blur } from "svelte/transition";

    let typewritter_element: HTMLParagraphElement,
        sky_element: HTMLDivElement,
        background_element: HTMLDivElement,
        fore_ground_element: HTMLDivElement,
        floating_1_element: HTMLImageElement,
        floating_2_element: HTMLImageElement,
        gradient_element: HTMLDivElement,
        content_element: HTMLDivElement,
        heavy_svg_element: HTMLImageElement;

    let loading_state = {
        sky_element: false,
        fore_ground_element: false,
        floating_1_element: false,
        floating_2_element: false,
        heavy_svg_element: false
    };

    function handle_window_scroll(e: Event) {
        let value = window.scrollY;

        sky_element.style.top = value * 0.75 + "px";
        content_element.style.marginTop = value * 0.85 + "px";
        gradient_element.style.top = value * 0.75 + "px";

        background_element.style.bottom = value * -0.5 + "px";
        fore_ground_element.style.bottom = value * 0 + "px";
        floating_1_element.style.marginTop = value * 0.75 + "px";
        floating_2_element.style.marginTop = value * 0.5 + "px";
    }
    let loaded = false;
    $: loaded = Object.values(loading_state).every((item) => item === true);

    $: {
        if (typewritter_element) {
            let app = document.getElementById("typing_text");
            console.log(app);
            let typewriter = new Typewriter(app, {
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
        }
    }
</script>

<svelte:window on:scroll={handle_window_scroll} />

<div class="bg-secondary">
    <div class="relative h-dvh w-screen overflow-hidden">
        <div
            bind:this={gradient_element}
            class="absolute inset-0 bg-gradient-to-b from-[#2A1E80] to-[#EA76B3]"
        />
        <div
            bind:this={sky_element}
            class="sky absolute inset-x-0 left-1/2 mx-auto w-[75rem] -translate-x-1/2 transform md:w-full"
        >
            <img
                on:load={() => {
                    loading_state.sky_element = true;
                }}
                class="w-full"
                src={Sky}
                alt="Sky"
            />
        </div>

        {#if loaded}
            <div
                transition:blur={{ duration: 500 }}
                bind:this={content_element}
                class="absolute inset-0 top-1/4 flex flex-col items-center gap-3 text-center md:top-[5vw] md:gap-[0.75vw] md:leading-none"
            >
                <h2 class="text-5xl font-bold text-white md:text-[5vw]">Imagine a new platform.</h2>
                <p
                    class="text-2xl text-accent md:text-[2.5vw]"
                    id="typing_text"
                    bind:this={typewritter_element}
                />
                <button class="btn btn-neutral h-max min-h-max p-4 text-lg leading-none md:rounded-[1vw] md:p-[1.1vw] md:text-[1.1vw]">Get Started</button>
            </div>
        {/if}

        <img
            bind:this={floating_1_element}
            on:load={() => {
                loading_state.floating_1_element = true;
            }}
            class="floating pointer-events-none absolute inset-x-0 left-10 top-[28rem] w-32 [animation-delay:0s] md:left-[15vw] md:top-1/4 md:w-[10vw]"
            src={Floating1}
            alt="Floating1"
        />
        <!-- this is the heaviest svg -->
        <div
            bind:this={background_element}
            class="background pointer-events-none absolute -left-20 bottom-0 w-[75rem] md:inset-x-0 md:left-0 md:w-full"
        >
            <img
                on:load={() => {
                    loading_state.heavy_svg_element = true;
                }}
                bind:this={heavy_svg_element}
                class="w-full"
                src={BackGround}
                alt="Background"
            />
        </div>
        <img
            bind:this={floating_2_element}
            class="floating pointer-events-none absolute inset-x-0 left-64 top-[37rem] w-20 [animation-delay:1s] md:left-2/4 md:top-2/4 md:w-[7vw]"
            src={Floating2}
            alt="Floating2"
            on:load={() => {
                loading_state.floating_2_element = true;
            }}
        />
        <div
            bind:this={fore_ground_element}
            class="mid-ground pointer-events-none absolute inset-x-0 -left-20 bottom-0 w-[90rem] md:left-0 md:w-full"
        >
            <img
                on:load={() => {
                    loading_state.fore_ground_element = true;
                }}
                class="w-full"
                src={ForeGround}
                alt="ForeGround"
            />
        </div>
    </div>
    <div class="h-screen"></div>
</div>

<style lang="scss">
    .floating {
        animation-name: floating;
        animation-duration: 3s;
        animation-iteration-count: infinite;
        animation-timing-function: ease-in-out;
        margin-left: 30px;
        margin-top: 5px;
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
