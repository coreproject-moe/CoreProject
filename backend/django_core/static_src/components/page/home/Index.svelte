<script lang="ts">
    import Sky from "../../../public/images/paralax/sky.svg";
	import BackGround from "../../../public/images/paralax/back-ground.svg"
	import MidGround from "../../../public/images/paralax/mid-ground.svg";
	import Floating1 from "../../../public/images/paralax/floating-1.svg";
	import Floating2 from "../../../public/images/paralax/floating-2.svg";
	import { onMount } from "svelte";

    // @ts-ignore
    import Typewriter from "typewriter-effect/dist/core";

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

	let sky_el: HTMLImageElement,
		background_el: HTMLImageElement,
		mid_ground_el: HTMLImageElement,
		floating_1_el: HTMLImageElement,
		floating_2_el: HTMLImageElement,
		gradient_el: HTMLDivElement,
		content_el: HTMLDivElement;

	function handle_window_scroll(e: Event) {
		let value = window.scrollY;
		
		sky_el.style.top = value * 0.75 + "px";
		content_el.style.marginTop = value * 0.85 + "px";

		background_el.style.bottom = value * 0.15 + "px";
		mid_ground_el.style.bottom = value * 0 + "px";
		floating_1_el.style.marginTop = value * 0.5 + "px";
		floating_2_el.style.marginTop = value * 0.25 + "px";
	};
</script>

<svelte:window on:scroll={handle_window_scroll} />

<main class="bg-secondary">
	<section class="h-screen relative overflow-hidden">
		<div bind:this={gradient_el} class="bg-gradient-to-b from-[#2A1E80] to-[#EA76B3] absolute inset-0" />
		<img bind:this={sky_el} class="sky absolute top-0 inset-x-0 w-4/5 mx-auto" src={Sky} alt="Sky" />
		
		<div bind:this={content_el} class="absolute inset-0 flex flex-col items-center top-[5vw] leading-none gap-[0.75vw]">
			<h2 class="text-white text-[5vw] font-bold">Imagine a new platform.</h2>
			<p class="text-[2.5vw] text-accent" id="typing_text"></p>
			<button class="btn btn-neutral p-[1.1vw] text-[1.1vw] uppercase min-h-max h-max rounded-[1vw]">Get Started</button>
		</div>

		<img bind:this={floating_1_el} class="floating pointer-events-none floating-1 absolute top-1/4 left-[15vw] inset-x-0 w-[10vw]" src={Floating1} alt="Floating1" />
		<img bind:this={background_el} class="pointer-events-none background absolute bottom-0 inset-x-0 w-full" src={BackGround} alt="Background" />
		<img bind:this={floating_2_el} class="floating pointer-events-none floating-2 absolute top-2/4 left-2/4 inset-x-0 w-[7vw]" src={Floating2} alt="Floating2" />
		<img bind:this={mid_ground_el} class="pointer-events-none mid-ground absolute bottom-0 inset-x-0 w-full" src={MidGround} alt="MidGround" />
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
    50%  { transform: translate(0, 15px); }
    100%   { transform: translate(0, -0px); }    
}
</style>