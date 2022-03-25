<script context="module" lang="ts">
    import { animeInfoEndpoint } from "$urls/restEndpoints";
    import type { Load } from "@sveltejs/kit";

    export const load: Load = async ({ fetch }) => {
        try {
            if (browser) {
                const res = await fetch(animeInfoEndpoint);
                return {
                    status: res?.status,
                    props: {
                        animes: await res?.json()
                    }
                };
            }
            return {
                status: 400
            };
        } catch {
            return {
                status: 404
            };
        }
    };
</script>

<script lang="ts">
    export let animes: [
        {
            episodes: [
                {
                    episode_comments: [];
                    episode_number: number;
                    episode_name: string;
                    episode_cover: null;
                    episode_file: string;
                    episode_summary: string;
                }
            ];
            anime_name: string;
            mal_id: number;
            updated: string;
        }
    ];
    import anime from "animejs";

    // Import Swiper Svelte components
    import { Swiper } from "swiper/svelte";
    import { EffectCoverflow, Pagination } from "swiper";

    import { responsiveMode } from "$store/responsive";
    import { projectName } from "$lib/constants/frontend/project";

    import WrappedSwiperComponent from "$components/swiper/WrappedSwiperComponent.svelte";
    import AnimeCard from "$components/cards/AnimeCard.svelte";
    import { browser } from "$app/env";

    let animeJSHeartIcon: HTMLElement;
    let animeJSRocketIcon: HTMLElement;
    let animeJSSparkleIcon: HTMLElement;

    let swiperSpacesBetween: number;
    let swiperSlidesPerView: number;

    let activeTab: "trending" | "popular" | "favorite" = "trending";

    $: switch ($responsiveMode) {
        case "mobile":
            swiperSpacesBetween = 15;
            swiperSlidesPerView = 2;
            break;
        case "tablet":
            swiperSpacesBetween = 20;
            swiperSlidesPerView = 4;
            break;
        case "widescreen":
        case "desktop":
        case "fullhd":
            swiperSpacesBetween = 30;
            swiperSlidesPerView = 6;
            break;
    }
</script>

<svelte:head>
    <title>AnimeCore | {projectName}</title>
</svelte:head>

<div class="container">
    <p class="title is-size-5 pt-2 has-text-white" />
    {#if animes?.length}
        <Swiper
            effect={"coverflow"}
            centeredSlides={true}
            speed={100}
            coverflowEffect={{
                rotate: 15,
                stretch: 0,
                depth: 100,
                modifier: 1
            }}
            modules={[EffectCoverflow, Pagination]}
            spaceBetween={swiperSpacesBetween}
            slidesPerView={swiperSlidesPerView}
        >
            {#each animes as { anime_name, mal_id }, i}
                <WrappedSwiperComponent animeName={anime_name} animeNumber={mal_id} />
            {/each}
        </Swiper>
    {:else}
        <section class="hero is-medium">
            <div class="hero-body">
                <div class="columns is-mobile is-centered">
                    <div class="column is-narrow">
                        <button class="button is-loading is-large has-background-black is-ghost" />
                    </div>
                </div>
            </div>
        </section>
    {/if}
</div>
<div class="container">
    <span
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable {activeTab ===
        'trending'
            ? 'hover'
            : ''}"
        on:click|preventDefault={() => {
            activeTab = "trending";
        }}
        on:mouseenter|preventDefault={() => {
            anime({
                targets: [animeJSRocketIcon],
                color: "#6495ed"
            });
        }}
        on:mouseleave|preventDefault={() => {
            anime({
                targets: [animeJSRocketIcon],
                color: "#FFFFFF"
            });
        }}
    >
        <ion-icon name="rocket-outline" class="pr-2" bind:this={animeJSRocketIcon} />Trending
    </span>
    <span
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable {activeTab ===
        'popular'
            ? 'hover'
            : ''}"
        on:click|preventDefault={() => {
            activeTab = "popular";
        }}
        on:mouseenter|preventDefault={() => {
            anime({
                targets: [animeJSSparkleIcon],
                color: "#ffff00"
            });
        }}
        on:mouseleave|preventDefault={() => {
            anime({
                targets: [animeJSSparkleIcon],
                color: "#ffffff"
            });
        }}
    >
        <ion-icon name="sparkles-outline" class="pr-2" bind:this={animeJSSparkleIcon} /> Popular
    </span>
    <span
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable {activeTab ===
        'favorite'
            ? 'hover'
            : ''}"
        on:click|preventDefault={() => {
            activeTab = "favorite";
        }}
        on:mouseenter|preventDefault={() => {
            anime({
                targets: [animeJSHeartIcon],
                color: "#ff0000"
            });
        }}
        on:mouseleave|preventDefault={() => {
            anime({
                targets: [animeJSHeartIcon],
                color: "#ffffff"
            });
        }}
        ><ion-icon name="heart-outline" bind:this={animeJSHeartIcon} class="pr-2" /> Favorite
    </span>
</div>
<div class="container pt-3">
    <div class="grid-container">
        {#if activeTab === "trending"}
            {#each Array(20) as _}
                <div class="grid-item">
                    <AnimeCard />
                </div>
            {/each}
        {:else if activeTab === "favorite"}
            {#each Array(40) as _}
                <div class="grid-item">
                    <AnimeCard />
                </div>
            {/each}
        {:else if activeTab === "popular"}
            {#each Array(60) as _}
                <div class="grid-item">
                    <AnimeCard />
                </div>
            {/each}
        {/if}
    </div>
</div>

<style lang="scss">
    .grid-container {
        display: grid;
        align-items: center;
        gap: 1em;
        grid-template-columns: repeat(auto-fit, minmax(13em, 1fr));
        background-color: black;
    }
    .grid-item {
        padding: 0.8em;
        text-align: center;
        transition: 0.2s;
    }
</style>
