<script lang="ts">
    import type { Swiper as SwiperType } from "swiper";
    import { FreeMode, Mousewheel } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import voca from "voca";

    import continueWatching from "$data/mock/continue_watching.json";
    import latestEpisodes from "$data/mock/latest_episode.json";
    import myList from "$data/mock/my_list.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";
    import LatestEpisode from "./LatestEpisode.svelte";
    import ContinueWatching from "./ContinueWatching.svelte";
    import MyList from "./MyList.svelte";

    // Responsive switches
    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    lastestEpisodeNameWordCount ??= 25;

    let mylistAnimeNameWordCount: number;
    mylistAnimeNameWordCount ??= 25;
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3">
            <LatestEpisode />
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex before:bg-white after:bg-white" />
        <div class="flex flex-col">
            <ContinueWatching />
            <div class="divider hidden md:flex before:bg-white after:bg-white" />
            <MyList />
        </div>
    </div>
</div>
