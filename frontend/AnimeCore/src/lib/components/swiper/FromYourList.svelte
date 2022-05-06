<script lang="ts">
    import { createEventDispatcher } from "svelte";
    import { responsiveMode } from "$store/responsive";
    import { SwiperSlide } from "swiper/svelte";

    export let backgroundImageUrl = "/images/Sono Bisque Doll.jpg";
    export let bannerImageUrl = "/images/sono bisque doll banner.jpeg";
    export let slideNumber = "01";
    export let animeName = "My Dress Up Darling";

    const dispatch = createEventDispatcher();

    const onBackClick = () => {
        dispatch("backClick", {});
    };

    const onForwardClick = () => {
        dispatch("forwardClick", {});
    };
</script>

<SwiperSlide>
    <div class="box" style="background-color:transparent;">
        <div
            class="box is-flex"
            style="
                background-size: cover;
                background-image:url('{bannerImageUrl}');
                box-shadow:
                    inset 0px -65px 25px -20px rgba(7, 5, 25, 1),
                    inset 0px -70px 75px -20px rgba(7, 5, 25, .8),
                    inset 0px -75px 75px -20px rgba(7, 5, 25, .7)
                ;
            "
        >
            <div
                class="is-size-7 has-text-white is-align-self-flex-end has-text-weight-semibold"
                style="width: 100px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"
            >
                {animeName}
            </div>
        </div>
        <div class="has-text-white has-text-weight-bold has-text-centered">
            {slideNumber}
        </div>
    </div>
</SwiperSlide>
