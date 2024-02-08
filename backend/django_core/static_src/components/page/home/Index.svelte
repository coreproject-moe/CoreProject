<script lang="ts">
    //@ts-ignore
    import { LottiePlayer } from "@lottiefiles/svelte-lottie-player";
    import Navbar from "$components/specific/Navbar/Index.svelte";
    
    import CoreProjectIcon from "$icons/CoreProject/Index.svelte";
    import CoreProjectText from "$icons/CoreProjectText/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
    import AnimeCore from "$icons/AnimeCore/index.svelte";
    import MangaCore from "$icons/MangaCore/Index.svelte";
    import SoundCore from "$icons/SoundCore/Index.svelte";

    import BgLottie from "./lotties/bg-lottie.json";
    import ScrollLottie from "./lotties/scroll.json";
    import SquiggleLottie from "./lotties/squiggle.json";
    import StarLottie from "./lotties/stars.json";
</script>

<div class="bg-secondary overflow-x-hidden relative">
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

    <navbar class="fixed inset-x-0 top-0 flex h-[4.5rem] items-center justify-between bg-secondary/95 p-3 backdrop-blur-3xl md:h-[8.5vh] md:p-[1vw] z-[999]">
        <a href="/">
            <CoreProjectIcon class="w-9 md:w-[2.25vw] md:pt-[0.75vw]" />
        </a>
        <div class="relative flex items-center md:static">
            <div class="absolute left-1/2 -translate-x-1/2">
                <a href="/anime" class="hidden md:flex">
                    <CoreProjectText class="!text-[1.75vw] !m-0" />
                </a>
                <form class="relative flex h-12 w-[65vw] items-center md:hidden">
                    <button class="btn absolute left-4 p-0 !bg-transparent border-none" aria-label="Search">
                        <Search class="w-5 text-neutral-content/75" />
                    </button>
                    <input
                        type="text"
                        placeholder="Search for animes, mangas..."
                        class="h-full w-full rounded-lg border-none bg-neutral/75 pl-12 text-base font-semibold text-accent shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-200"
                    />
                </form>
            </div>
        </div>
        <Navbar />
    </navbar>

    <section class="w-full flex flex-col justify-center items-center relative md:mt-[10vh]">
        <div class="md:text-[8vw] leading-none font-bold text-center flex flex-col md:mt-[3vw]">
            <h2 class="bg-gradient-to-r from-rose-500 from-[35%] to-[65%] to-blue-500 inline-block text-transparent bg-clip-text">Imagine a new</h2>
            <h2 class="bg-gradient-to-r from-blue-500 from-[35%] to-[65%] to-yellow-600 inline-block text-transparent bg-clip-text relative">
                Platform.
                <div class="size-[5vw] -rotate-45 absolute right-[5vw] bottom-[2vw]">
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
        <p class="md:text-[1.25vw] md:mt-[3vw] md:max-w-[45vw] text-center opacity-90">
            Bridging the gap between streaming and torrenting sites with a modern and clean interface.
        </p>
        <div class="relative flex items-center">
            <a href="#explore-our-trio" class="md:mt-[1vw] btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1vw] md:rounded-[1vw] shadow-lg shadow-rose-500/25 leading-none">
                Start Exploring Now!
            </a>
            <div class="size-[4vw] absolute -right-[4vw]">
                <LottiePlayer
                    src={StarLottie}
                    autoplay="{true}"
                    loop="{false}"
                    renderer="svg"
                    background="transparent"
                />
            </div>
        </div>
        <div class="size-[2vw] md:mt-[3vw] opacity-75">
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
        class="relative md:mt-[10vw] flex flex-col items-center justify-center bg-secondary/75s md:py-[3vw]"
    >
        <h2 class="md:text-[2.5vw] font-bold bg-gradient-to-r from-rose-500 from-[35%] to-[65%] to-blue-500 inline-block text-transparent bg-clip-text">Explore Our Trio.</h2>
        <div class="flex items-end justify-center md:mt-[1vw] md:gap-[1.5vw]">
            <div class="relative flex items-center justify-center flex-col bg-secondary md:rounded-[1vw] md:p-[1vw] md:w-[20vw] text-center md:gap-[1vw]">
                <MangaCore class="!text-[2.5vw] !m-0" />
                <p class="md:text-[1.1vw] md:leading-[1.5vw] md:line-clamp-4">
                    Dive into the captivating world of manga with our streaming service. Access a diverse collection of manga titles, from timeless classics to the latest releases, and lose yourself in the art of storytelling.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] leading-none">
                    Coming soon
                </button>
                <div class="absolute inset-0 bg-secondary/75" />
            </div>
            <div class="flex items-center justify-center flex-col bg-secondary border-[0.15vw] md:rounded-[1vw] border-error md:p-[1vw] border-dashed md:w-[25vw] text-center md:gap-[1vw] relative">
                <AnimeCore class="md:w-[15vw]" />
                <p class="md:text-[1.1vw] md:leading-[1.5vw]">
                    Immerse yourself in a world of endless anime streaming. Explore a vast library of your favorite shows and discover new ones, all at your fingertips.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] shadow-lg shadow-rose-500/25 leading-none">
                    Explore
                </button>
                <div class="size-[4vw] absolute -right-[1.5vw] -top-[1.75vw]">
                    <LottiePlayer
                        src={StarLottie}
                        autoplay="{true}"
                        loop="{false}"
                        renderer="svg"
                        background="transparent"
                    />
                </div>
            </div>
            <div class="relative flex items-center justify-center flex-col bg-secondary md:rounded-[1vw] md:p-[1vw] md:w-[20vw] text-center md:gap-[1vw]">
                <SoundCore class="!text-[2.5vw] !m-0" />
                <p class="md:text-[1.1vw] md:leading-[1.5vw] md:line-clamp-4">
                    Elevate your auditory experience with our music streaming platform. Explore a rich tapestry of sounds, from chart-toppers to hidden gems, and let the music transport you to new dimensions of sonic bliss.
                </p>
                <button class="relative w-full btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1.25vw] md:rounded-[1vw] leading-none">
                    Coming soon
                </button>
                <div class="absolute inset-0 bg-secondary/75" />
            </div>
        </div>
    </section>
</div>
