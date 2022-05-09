<script lang="ts">
    import { SwiperSlide } from "swiper/svelte";

    import { responsiveMode } from "$store/responsive";

    export let bannerImageUrl = "/images/sono bisque doll banner.jpeg";
    export let animeName = "My Dress Up Darling";
</script>

<SwiperSlide>
    <div class="box is-flex is-flex-direction-column pt-6" style="background-color:transparent;">
        <div
            class="box is-flex is-align-self-center"
            style="
                border-radius: 1em;
                height: {$responsiveMode === 'mobile' ? '14vh' : '35vh'};
                width:  {$responsiveMode === 'mobile' ? '14vw' : '200px'};
                background-size: cover;
                background-image: url('{bannerImageUrl}');
                box-shadow:
                    inset 0px -65px 25px -20px rgba(7, 5, 25, .9),
                    inset 0px -70px 75px -20px rgba(7, 5, 25, .8),
                    inset 0px -75px 75px -20px rgba(7, 5, 25, .7)
                ;
            "
        >
            <div
                class="is-size-7 has-text-white is-align-self-flex-end has-text-weight-semibold"
                style="width: 15vw; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"
            >
                {animeName}
            </div>
        </div>
    </div>
</SwiperSlide>
