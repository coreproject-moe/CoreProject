<script lang="ts">
    //@ts-ignore
    import { LottiePlayer } from "@lottiefiles/svelte-lottie-player";
    import Navbar from "$components/specific/Navbar/Index.svelte";
    
    import CoreProjectIcon from "$icons/CoreProject/Index.svelte";
    import CoreProjectText from "$icons/CoreProjectText/Index.svelte";
    import Search from "$icons/Search/Index.svelte";

    import BgLottie from "./lotties/bg-lottie.json";
    import ScrollLottie from "./lotties/scroll.json";
    import SquiggleLottie from "./lotties/squiggle.json";
    import StarLottie from "./lotties/stars.json";
</script>

<div class="bg-secondary min-h-dvh w-screen overflow-x-hidden">
    <div class="w-full h-[100vh] overflow-hidden absolute">
        <LottiePlayer
            src={BgLottie}
            autoplay="{true}"
            loop="{false}"
            renderer="svg"
            background="transparent"
            style={{ height: "100%", width: "100%", "object-fit": "contain" }}
        />
    </div>

    <navbar class="absolute inset-x-0 top-0 flex h-[4.5rem] items-center justify-between bg-secondary/95 p-3 backdrop-blur-3xl md:h-[8.5vh] md:p-[1vw] z-[999]">
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
            <button class="md:mt-[1vw] btn border-none bg-gradient-to-r from-rose-500 to-blue-500 text-accent h-max min-h-max md:p-[1.25vw] md:text-[1vw] md:rounded-[1vw] shadow-lg shadow-rose-500/25 leading-none">
                Start Exploring Now!
            </button>
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
</div>
