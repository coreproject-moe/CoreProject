<script lang="ts">
    import { responsiveMode } from "$store/responsive";

    export let backgroundImageUrl = "'/images/Sono Bisque Doll.jpg'";
    export let bannerImageUrl = "/images/sono bisque doll banner.jpeg";
</script>

<section class="hero is-fullheight">
    <div class="hero-body is-align-self-center is-flex-direction-column">
        <div class="title pb-5 is-size-2 has-text-white">
            <div class="columns is-mobile" style="width:90vw">
                <div class="column is-narrow">
                    <span class="is-align-self-center"> TRENDING </span>
                </div>
                <div class="column is-flex">
                    <div
                        class="is-align-self-center"
                        style="
                            width: 100%;
                            display: inline-block;
                            border-top: 10px solid;
                        "
                    />
                </div>
            </div>
        </div>
        {#if $responsiveMode === "mobile"}
            <div class="card">
                <div class="card-image">
                    <figure class="image is-4by3">
                        <img
                            src="https://bulma.io/images/placeholders/1280x960.png"
                            alt="Placeholder image"
                        />
                    </figure>
                </div>
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure class="image is-48x48">
                                <img
                                    src="https://bulma.io/images/placeholders/96x96.png"
                                    alt="Placeholder image"
                                />
                            </figure>
                        </div>
                        <div class="media-content">
                            <p class="title is-4">John Smith</p>
                            <p class="subtitle is-6">@johnsmith</p>
                        </div>
                    </div>

                    <div class="content">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
                        iaculis mauris. <a>@bulmaio</a>.
                        <a href="#">#css</a> <a href="#">#responsive</a>
                        <br />
                        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                    </div>
                </div>
            </div>
        {:else}
            <section
                class="hero is-large"
                style="
           width: 100%;
           border-radius:18px;
           border-color: #070519;
           background-image:url({backgroundImageUrl});
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
                            <h1 class="has-text-white is-size-2 my-2">My Dress Up Darling</h1>
                            <p style="width:70%" class="has-text-white">
                                High schooler Wakana Gojou cares about one thing: making Hina dolls.
                                With nobody to share his obsession, he has trouble finding
                                friends—or even holding conversation. But after the school's most
                                popular girl, Marin Kitagawa, reveals...
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
            <div class="pt-6">
                <div class="field is-grouped ">
                    <button
                        class="button is-medium has-border-warning-light is-warning is-outlined mx-5"
                    >
                        <span class="icon is-small">
                            <img alt="" src="/icons/chevron-left.svg" height={24} width={24} />
                        </span>
                    </button>

                    <button
                        class="button is-medium is-warning has-text-white mx-0 has-text-weight-medium"
                    >
                        03
                    </button>

                    <button
                        class="button is-medium has-border-warning-light is-warning is-outlined mx-5"
                    >
                        <span class="icon is-small">
                            <img alt="" src="/icons/chevron-right.svg" height={24} width={24} />
                        </span>
                    </button>
                </div>
            </div>
        {/if}
    </div>
</section>

<style lang="scss">
    .button {
        border-radius: 16px;
        border-width: 5px;
        height: 32px;
    }
</style>
