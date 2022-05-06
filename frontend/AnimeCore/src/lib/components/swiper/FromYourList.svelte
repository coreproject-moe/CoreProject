<script lang="ts">
    import { responsiveMode } from "$store/responsive";
    import { SwiperSlide } from "swiper/svelte";

    export let bannerImageUrl = "/images/sono bisque doll banner.jpeg";
    export let animeName = "My Dress Up Darling";
</script>

<SwiperSlide>
    <div class="box is-flex is-flex-direction-column" style="background-color:transparent;">
        <div
            class="box is-flex is-align-self-center"
            style="
                height: {$responsiveMode === 'mobile' ? '14vh' : '32vh'};
                width:15vw;
                background-size: cover;
                background-image: url('{bannerImageUrl}');
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
    </div>
</SwiperSlide>
