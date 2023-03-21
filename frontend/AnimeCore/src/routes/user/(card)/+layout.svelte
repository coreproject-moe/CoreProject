<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import { blur } from "svelte/transition";

    // import AnimeCore from "$icons/AnimeCore.svelte";

    let CHOICE_NUMBER: number;
    let CHOICES: Array<{
        type: string;
        name: string;
        image: string;
        credit?: string;
    }> = [
        {
            type: "anime",
            name: "Demon Slayer",
            image: "/posters/demon-slayer.webp",
            credit: "https://www.reddit.com/r/DemonSlayerAnime/comments/tpgpid/demon_slayer_4k_wallpaper/"
        },
        {
            type: "anime",
            name: "Attack on Titan",
            image: "/posters/attack-on-titan.jpg"
        },
        {
            type: "anime",
            name: "Comic Girls",
            image: "/posters/Comic-Girls-Image.png"
        }
    ];

    const changeIndex = () => {
        const index = Math.floor(Math.random() * CHOICES.length);
        CHOICE_NUMBER = index;
    };
    let interval: NodeJS.Timer | undefined;
    onMount(() => {
        interval = setInterval(() => {
            changeIndex();
        }, 20000);
        changeIndex();
    });
    onDestroy(() => {
        clearInterval(interval);
    });
</script>

<svelte:head>
    {#each CHOICES as item}
        <link
            rel="preload"
            as="image"
            href={item.image}
        />
    {/each}
</svelte:head>

<div class="grid h-screen">
    <!-- Background Image Container -->
    {#each CHOICES as item}
        {#if CHOICES.indexOf(item) == CHOICE_NUMBER}
            {@const type = () => {
                switch (item.type) {
                    case "anime":
                        return "the anime";
                    case "pixiv":
                        return "the artist";
                    default:
                        return "";
                }
            }}

            <div
                transition:blur|local
                class="fixed h-screen bg-black"
                style="grid-area: 1 / 1 / 2 / 2;"
            >
                <div
                    class="h-screen w-screen bg-cover bg-center bg-no-repeat brightness-90"
                    style="background-image:url('{item.image}')"
                />
                <div
                    class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
                />

                <!-- Top animecore logo div  -->
                <!-- <div class="absolute top-8 left-8">
                    <AnimeCore
                        width="164"
                        height="25"
                    />
                </div> -->
                <!-- Background from anime div  -->
                <div class="absolute bottom-8 left-8">
                    <div class="flex flex-col">
                        <p class="text-secondary">Background from {type()}</p>
                        <p class="text-white">
                            {item.name}
                        </p>
                    </div>
                </div>
            </div>
        {/if}
    {/each}
    <div class="absolute inset-0 grid h-screen">
        <div
            style="grid-area: 1 / 1 / 2 / 2"
            class="inline-grid content-center justify-center md:justify-end"
        >
            <div
                class="card mr-0 w-96 bg-base-100 bg-transparent bg-gradient-to-t from-base-100 shadow-xl placeholder:capitalize md:mr-24 md:w-[35vw]"
            >
                <div class="card-body rounded-2xl">
                    <div class="flex justify-center">
                        <div class="flex select-none text-5xl font-bold">
                            <span class="inline-flex text-white">c</span>
                            <span class="inline-flex text-warning">o</span>
                            <span class="inline-flex text-white">r</span>
                            <span class="inline-flex text-white">e</span>
                            &nbsp;
                            <span class="inline-flex text-info">p</span>
                            <span class="inline-flex text-info">r</span>
                            <span class="inline-flex text-info">o</span>
                            <span class="inline-flex text-info">j</span>
                            <span class="inline-flex text-info">e</span>
                            <span class="inline-flex text-info">c</span>
                            <span class="inline-flex text-info">t</span>
                        </div>
                    </div>

                    <slot />
                </div>
            </div>
        </div>
    </div>
</div>

<style lang="scss">
    $border-width: 3px;

    .card {
        border-image: linear-gradient(
                to top,
                transparent 0.1%,
                white 15%,
                transparent,
                rgba(0, 0, 0, 0)
            )
            1 100%;
        border-image-width: $border-width;

        &::before {
            content: "";
            position: absolute;
            bottom: 10.5px;
            right: 0;
            border-left: $border-width solid white;
            border-radius: 9999px;
            width: 1px;
            height: 100px;
            background-color: white;
        }
        &::after {
            content: "";
            position: absolute;
            bottom: 10.5px;
            left: 0;
            border-left: $border-width solid white;
            border-radius: 9999px;
            width: 1px;
            height: 100px;
            background-color: white;
        }
    }
    .card-body {
        z-index: 1;

        &::after {
            position: absolute;
            top: 0px;
            bottom: 0px;
            left: 0px;
            right: 0px;
            z-index: -1;
            box-shadow: inset 0 $border-width * -1 0 0 rgba(250, 250, 250, 0.9);
            content: "";
            border-radius: 16px;
        }
    }
</style>
