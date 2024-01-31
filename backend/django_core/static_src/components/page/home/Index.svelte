<script lang="ts">
    import Sky from "../../../public/images/paralax/sky.svg";
	import BackGround from "../../../public/images/paralax/back-ground.svg"
	import ForeGround from "../../../public/images/paralax/fore-ground.svg";
	import Floating1 from "../../../public/images/paralax/floating-1.svg";
	import Floating2 from "../../../public/images/paralax/floating-2.svg";
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
        var app = document.getElementById('typing_text');

        var typewriter = new Typewriter(app, {
            loop: true,
            delay: 75,
        });

        typewriter
            .typeString('For watching <b>Animes.</b>')
            .pauseFor(2000)
            .deleteChars(16)
            .typeString('reading <b>Mangas.</b>')
            .pauseFor(2000)
            .deleteChars(15)
            .typeString('listening to <b>Musics.</b>')
            .pauseFor(2000)
            .deleteAll()
            .typeString('Welcome to <b>CoreProject.</b>')
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
	};
</script>

<svelte:window on:scroll={handle_window_scroll} />

{#if !svg_loaded}
	<div transition:blur class="fixed inset-0 bg-secondary z-[999] grid place-items-center">
		<div class="p-[0.25vw] bg-gradient-to-tr animate-spin from-green-500 to-blue-500 via-purple-500 rounded-full">
			<div class="bg-secondary rounded-full">
				<div class="size-[7vw] rounded-full"></div>
			</div>
		</div>
	</div>
{/if}

<main class="bg-secondary w-screen h-screen">
	<section class="h-full w-full relative overflow-hidden">
		<div bind:this={gradient_el} class="bg-gradient-to-b from-[#2A1E80] to-[#EA76B3] absolute inset-0" />
		<div
			bind:this={sky_el}
			class="sky absolute inset-x-0 mx-auto transform -translate-x-1/2 left-1/2 w-[75rem] md:w-full"
		>
			<img
				class="w-full"
				src={Sky} alt="Sky"
			/>
		</div>
		
		<div bind:this={content_el} class="absolute inset-0 flex flex-col items-center top-1/4 md:top-[5vw] md:leading-none gap-3 md:gap-[0.75vw] text-center">
			<h2 class="text-white text-5xl md:text-[5vw] font-bold">Imagine a new platform.</h2>
			<p class="text-2xl md:text-[2.5vw] text-accent" id="typing_text"></p>
			<button class="btn btn-neutral md:p-[1.1vw] p-4 leading-none text-lg md:text-[1.1vw] min-h-max h-max md:rounded-[1vw]">Get Started</button>
		</div>

		<img bind:this={floating_1_el} class="floating pointer-events-none floating-1 absolute top-[28rem] md:top-1/4 left-10 md:left-[15vw] inset-x-0 w-32 md:w-[10vw]" src={Floating1} alt="Floating1" />
		<!-- this is the heaviest svg -->
		<div
			bind:this={background_el}
			class="pointer-events-none background absolute bottom-0 -left-20 md:left-0 md:inset-x-0 w-[75rem] md:w-full"
		>
			<img
				bind:this={heavy_svg}
				on:load={handle_svg_load}
				class="w-full"
				src={BackGround} alt="Background"
			/>
		</div>
		<img bind:this={floating_2_el} class="floating pointer-events-none floating-2 absolute top-[37rem] md:top-2/4 left-64 md:left-2/4 inset-x-0 w-20 md:w-[7vw]" src={Floating2} alt="Floating2" />
		<div
			bind:this={fore_ground_el}
			class="pointer-events-none mid-ground absolute bottom-0 -left-20 md:left-0 inset-x-0 w-[90rem] md:w-full"
		>
			<img
				class="w-full"
				src={ForeGround} alt="ForeGround"
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
    0% { transform: translate(0,  0px); }
    50%  { transform: translate(0, 1rem); }
    100%   { transform: translate(0, -0px); }    
}
</style>