<script lang="ts">
    //@ts-ignore
    import { LottiePlayer } from "@lottiefiles/svelte-lottie-player";
    
    import AnimeCore from "$icons/AnimeCore/index.svelte";
    import MangaCore from "$icons/MangaCore/Index.svelte";
    import SoundCore from "$icons/SoundCore/Index.svelte";

    import BgLottie from "./lotties/bg-lottie.json";
    import ScrollLottie from "./lotties/scroll.json";
    import SquiggleLottie from "./lotties/squiggle.json";
    import StarLottie from "./lotties/stars.json";
</script>

<div class="bg-secondary overflow-x-hidden relative min-h-dvh">
    <div class="inset-0 overflow-hidden absolute">
        <LottiePlayer
            src={BgLottie}
            autoplay="{true}"
            loop="{false}"
            renderer="svg"
            background="transparent"
            style={{ height: "100%", width: "100%", "object-fit": "contain" }}
        />
    </div>

    <section class="w-full flex flex-col justify-center items-center relative mt-20 md:mt-[10vh]">
        <div class="text-5xl md:text-[8vw] leading-none font-bold text-center flex flex-col md:mt-[3vw]">
            <h2 class="bg-gradient-to-r from-rose-500 from-[35%] to-[65%] to-blue-500 inline-block text-transparent bg-clip-text">Imagine a new</h2>
            <h2 class="bg-gradient-to-r from-blue-500 from-[35%] to-[65%] to-yellow-600 inline-block text-transparent bg-clip-text relative">
                Platform.
                <div class="size-12 md:size-[5vw] -rotate-45 absolute right-3 md:right-[5vw] md:bottom-[2vw] bottom-2">
                    <LottiePlayer
                        src={SquiggleLottie}
                        autoplay="{true}"
                        loop="{false}"
                        mode={"bounce"}
                        speed={0.75}
                        renderer="svg"
                        background="transparent"
                    />
                </div>
            </h2>
        </div>
        <p class="text-base max-w-72 md:text-[1.25vw] mt-2 md:mt-[3vw] md:max-w-[45vw] text-center opacity-90">
            Bridging the gap between streaming and torrenting sites with a modern and clean interface.
        </p>
        <div class="relative flex items-center">
            <a href="#explore-our-trio" class="md:mt-[1vw] mt-4 btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max p-4 text-base rounded-xl md:p-[1.25vw] md:text-[1vw] md:rounded-[1vw] shadow-lg shadow-rose-500/25 leading-none">
                Start Exploring Now!
            </a>
            <div class="size-14 md:size-[4vw] absolute -right-14 md:-right-[4vw]">
                <LottiePlayer
                    src={StarLottie}
                    autoplay="{true}"
                    loop="{false}"
                    renderer="svg"
                    background="transparent"
                />
            </div>
        </div>
        <div class="md:size-[2vw] size-6 mt-5 md:mt-[3vw] opacity-75">
            <LottiePlayer
                src={ScrollLottie}
                autoplay="{true}"
                loop="{true}"
                renderer="svg"
                background="transparent"
            />
        </div>
    </section>

    <section
        id="explore-our-trio"
        class="relative mt-16 md:mt-[10vw] flex flex-col items-center justify-center md:py-[3vw]"
    >
        <h2 class="md:text-[2.5vw] text-2xl font-bold bg-gradient-to-r from-rose-500 from-[35%] to-[65%] to-blue-500 text-transparent bg-clip-text">Explore Our Trio.</h2>
        <div class="flex flex-col md:flex-row items-end justify-center mt-2 p-5 md:mt-[1vw] md:gap-[1.5vw]">
            <div class="relative flex items-center justify-center flex-col bg-secondary md:rounded-[1vw] md:p-[1vw] p-5 md:w-[20vw] gap-2 text-center md:gap-[1vw]">
                <MangaCore class="!text-3xl md:!text-[2.5vw] !m-0" />
                <p class="text-sm line-clamp-3 md:text-[1.1vw] md:leading-[1.5vw] md:line-clamp-4">
                    Dive into the captivating world of manga with our streaming service. Access a diverse collection of manga titles, from timeless classics to the latest releases, and lose yourself in the art of storytelling.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] leading-none p-3 text-lg rounded-xl">
                    Coming soon
                </button>
                <div class="absolute inset-0 bg-secondary/75" />
            </div>
            <div class="flex items-center justify-center flex-col bg-secondary md:border-[0.15vw] md:rounded-[1vw] border-error md:p-[1vw] border-dashed md:w-[25vw] text-center md:gap-[1vw] relative p-5 gap-2 rounded-2xl border-2">
                <AnimeCore class="w-48 md:w-[15vw]" />
                <p class="text-sm md:text-[1.1vw] md:leading-[1.5vw] line-clamp-4">
                    Immerse yourself in a world of endless anime streaming. Explore a vast library of your favorite shows and discover new ones, all at your fingertips.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] shadow-lg shadow-rose-500/25 leading-none p-4 text-lg rounded-xl">
                    Explore
                </button>
                <div class="md:size-[4vw] size-10 absolute md:-right-[1.5vw] right-0 top-0 md:-top-[1.75vw]">
                    <LottiePlayer
                        src={StarLottie}
                        autoplay="{true}"
                        loop="{false}"
                        renderer="svg"
                        background="transparent"
                    />
                </div>
            </div>
            <div class="relative flex items-center justify-center flex-col bg-secondary md:rounded-[1vw] md:p-[1vw] p-5 md:w-[20vw] gap-2 text-center md:gap-[1vw]">
                <SoundCore class="!text-3xl md:!text-[2.5vw] !m-0" />
                <p class="text-sm line-clamp-3 md:text-[1.1vw] md:leading-[1.5vw] md:line-clamp-4">
                    Elevate your auditory experience with our music streaming platform. Explore a rich tapestry of sounds, from chart-toppers to hidden gems, and let the music transport you to new dimensions of sonic bliss.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] leading-none p-3 text-lg rounded-xl">
                    Coming soon
                </button>
                <div class="absolute inset-0 bg-secondary/75" />
            </div>
        </div>
    </section>
</div>
