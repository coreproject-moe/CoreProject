<script lang="ts">
    // Import Swiper Svelte components
    import { Swiper } from "swiper/svelte";
    import { projectName } from "$lib/constants/frontend/project";

    import { responsiveMode } from "$store/responsive";
    import WrappedSwiperComponent from "$components/swiper/WrappedSwiperComponent.svelte";

    let swiperSpacesBetween: number;
    let swiperSlidesPerView: number;

    $: switch ($responsiveMode) {
        case "mobile":
            swiperSpacesBetween = 10;
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
    <p class="title is-size-5 pt-6 has-text-white">
        <span class="pr-3 pl-3"
            ><ion-icon name="rocket-outline" style="transform: translateY(5px)" /></span
        >
        Recent Uploads :
    </p>
    <div class="box" style="background-color: black; border: 1px dotted white">
        <Swiper spaceBetween={swiperSpacesBetween} slidesPerView={swiperSlidesPerView}>
            {#each Array(12) as _}
                <WrappedSwiperComponent />
            {/each}
        </Swiper>
    </div>
</div>
