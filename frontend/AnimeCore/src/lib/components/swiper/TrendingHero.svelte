<script lang="ts">
    import { SwiperSlide } from "swiper/svelte";

    import { responsiveMode } from "$store/responsive";

    export let backgroundImageUrl = "/images/Sono Bisque Doll.jpg";
    export let bannerImageUrl = "/images/sono bisque doll banner.jpeg";
    export let slideNumber = "01";
    export let animeName = "My Dress Up Darling";
</script>

<SwiperSlide>
    {#if $responsiveMode === "mobile"}
        <div class="box is-flex is-flex-direction-column" style="background-color:transparent;">
            <div
                class="box is-flex is-align-self-center mb-0"
                style="
                    border-radius: 1em;
                    height: 14vh;
                    width: 15vw;
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
                    style="width: 15vw; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"
                >
                    {animeName}
                </div>
            </div>
            <div class="has-text-white has-text-weight-bold has-text-centered">
                {slideNumber}
            </div>
        </div>
    {:else}
        <section
            class="hero"
            style="
                min-height: 60vh;
                width: 100%;
                border-radius:18px;
                border-color: #070519;
                background-image:url('{backgroundImageUrl}');
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
                box-shadow:
                    inset 5vw 0px 10px -20px rgba(7, 5, 25, 1),
                    inset 10vw 0px 100px -20px rgba(7, 5, 25, .9),
                    inset 25vw 0px 100px -20px rgba(7, 5, 25, .7),
                    inset 35vw 0px 100px -20px rgba(7, 5, 25, .6),
                    inset 50vw 0px 100px -20px rgba(7, 5, 25, .4)
                ;
            "
        >
            <div
                class="hero-body is-flex-direction-row px-6"
                style="padding-top:7.5rem !important; padding-bottom:7.5rem !important;"
            >
                <div style="width:18em" class="px-5">
                    <figure class="image is-2by3">
                        <img alt="" style="border-radius:16px" src={bannerImageUrl} />
                    </figure>
                </div>
                <div class="px-5">
                    <div class="content">
                        <div class="has-text-warning is-size-6">
                            <div class="columns is-mobile">
                                <div class="column is-narrow px-1">
                                    <span class="is-align-self-center">#3 Most Popular</span>
                                </div>
                                <div class="column is-flex px-1">
                                    <div
                                        class="is-align-self-center"
                                        style="width: 14vw; display: inline-block; border-top: 4px solid;"
                                    />
                                </div>
                            </div>
                        </div>
                        <h1 class="has-text-white is-size-2 my-2">{animeName}</h1>
                        <p style="width:70%" class="has-text-white">
                            High schooler Wakana Gojou cares about one thing: making Hina dolls.
                            With nobody to share his obsession, he has trouble finding friends—or
                            even holding conversation. But after the school's most popular girl,
                            Marin Kitagawa, reveals...
                        </p>
                        <div class="buttons are-medium">
                            <button
                                class="button is-warning has-border-transparent mx-2"
                                style="border-radius: 12px"
                            >
                                <span class="icon is-small">
                                    <img alt="" src="/icons/play.svg" width="24" height="24" />
                                </span>
                            </button>
                            <button class="button is-warning is-outlined mx-4 is-flex">
                                <span class="has-text-weight-semibold">Details</span>
                                <img
                                    class="is-align-self-flex-end"
                                    alt=""
                                    src="/icons/chevrons-right.svg"
                                    height={26}
                                    width={26}
                                />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    {/if}
</SwiperSlide>

<style lang="scss">
    .button {
        border-radius: 16px;
        border-width: 5px;
    }
</style>
