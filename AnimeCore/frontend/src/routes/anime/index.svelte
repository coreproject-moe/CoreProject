<script lang="ts">
    import anime from "animejs";

    // Import Swiper Svelte components
    import { Swiper } from "swiper/svelte";
    import { EffectCoverflow, Pagination } from "swiper";

    import { projectName } from "$lib/constants/frontend/project";

    import { responsiveMode } from "$store/responsive";
    import WrappedSwiperComponent from "$components/swiper/WrappedSwiperComponent.svelte";

    let animeJSHeartIcon: HTMLElement;
    let animeJSRocketIcon: HTMLElement;
    let animeJSSparkleIcon: HTMLElement;

    let swiperSpacesBetween: number;
    let swiperSlidesPerView: number;

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
    <div class="box has-background-black">
        <Swiper
            effect={"coverflow"}
            grabCursor={true}
            centeredSlides={true}
            loop={true}
            speed={50}
            coverflowEffect={{
                rotate: 15,
                stretch: 0,
                depth: 100,
                modifier: 1,
                slideShadows: true
            }}
            modules={[EffectCoverflow, Pagination]}
            spaceBetween={swiperSpacesBetween}
            slidesPerView={swiperSlidesPerView}
        >
            {#each Array(12) as _}
                <WrappedSwiperComponent />
            {/each}
        </Swiper>
    </div>
</div>
<div class="container">
    <span
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable"
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
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable"
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
        class="tag is-black is-rounded has-hover-gray is-size-6 is-clickable is-unselectable"
        on:mouseenter|preventDefault={() => {
            anime({
                targets: [animeJSHeartIcon],
                color: "#ff0000"
            });
        }}
        on:mouseleave|preventDefault={() => {
            anime({
                targets: [animeJSHeartIcon],
                color: "#fffffff"
            });
        }}
        ><ion-icon name="heart-outline" bind:this={animeJSHeartIcon} class="pr-2" /> Trending
    </span>
</div>
