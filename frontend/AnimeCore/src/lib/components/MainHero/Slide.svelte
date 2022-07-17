<script lang="ts">
    import Navbar from "$components/common/Navbar.svelte";

    export let animeTitle: string;
    export let animeSummary: string;
    export let animeEpisodeCount:number;
    export let animeStudio:string;
    export let animeAirTime:string;
    export let backgroundImage:string;
    export let backgroundBanner:string;
    export let tags:string[];
</script>

<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url(https://placeimg.com/1000/800/arch);"
>
    <div class="hero-overlay bg-opacity-60">
        <div class="pt-8 pr-[72px] pl-[48px] pb-0">
            <Navbar />
        </div>
    </div>
    <div class="hero-content text-center text-neutral-content justify-self-start">
        <div class="max-w-md">
            <h1 class="mb-5 text-5xl font-bold">Hello there</h1>
            <p class="mb-5">
                Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi
                exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.
            </p>
            <button class="btn btn-primary">Get Started</button>
        </div>
    </div>
</div>
