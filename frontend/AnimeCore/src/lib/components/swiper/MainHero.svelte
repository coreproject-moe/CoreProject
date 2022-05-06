<script lang="ts">
    import { responsiveMode } from "$store/responsive";
    import Navbar from "$components/common/Navbar.svelte";
    import { SwiperSlide } from "swiper/svelte";

    export let backgroundImageUrl: string;
    export let animeName: string;
</script>

<SwiperSlide>
    <section
        class="hero {$responsiveMode === 'mobile' ? 'is-halfheight' : 'is-fullheight'}"
        style="
            background-image: url({backgroundImageUrl});
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            box-shadow:
                inset 0 4px 1800px rgb(7, 5, 25),
                inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
                inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
                inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
                inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)
            ;
"
    >
        <!-- Hero head: will stick at the top -->
        <div class="hero-head">
            <Navbar />
        </div>

        <!-- Hero content: will be in the middle -->
        <div class="hero-body is-align-items-self-end">
            <div class="container">
                <div
                    class="title has-text-warning  container mb-0 {$responsiveMode === 'mobile'
                        ? 'is-size-7'
                        : 'is-size-4'}"
                >
                    <div class="is-flex">
                        <span class="pr-2 is-align-self-center">Featured</span>
                        <div
                            class="is-align-self-center"
                            style="display: inline-block;width: 4em;border-top: 6px solid;"
                        />
                    </div>
                </div>
                <div
                    class="title has-text-white is-bold mb-0 {$responsiveMode === 'mobile'
                        ? 'is-size-2'
                        : 'is-size-1'}"
                >
                    {animeName}
                </div>
                <div
                    class="subtitle has-text-white pt-5 {$responsiveMode === 'mobile'
                        ? 'is-size-7'
                        : 'is-size-6'}"
                    style={$responsiveMode === "mobile" ? "width: 100%;" : "width: 60%;"}
                >
                    Energy-conservative high school student Houtarou Oreki ends up with more than he
                    bargained for when he signs up for the Classic Literature Club at his
                    sister&apos;s behest especially when he realizes how deep-rooted the club&apos;s
                    history really is. Begrudgingly, Oreki is dragged into an...
                </div>
                <!-- Tags -->
                <div class="subtitle is-hidden-mobile">
                    <span class="tag is-size-6 mx-1 is-bold is-black"> Mystery </span>
                    <span class="tag is-size-6 mx-1 is-bold is-black"> Slice of Life </span>
                </div>

                <div class="subtitle">
                    <div class="buttons are-medium">
                        <button
                            class="button is-warning has-border-transparent mx-3"
                            style="border-radius: 12px"
                        >
                            <img alt="" src="/icons/play.svg" />
                            <span class="has-text-weight-bold is-size-6 is-hidden-desktop mx-1"
                                >Watch</span
                            >
                        </button>
                        <button class="button is-warning is-outlined mx-4 is-flex">
                            <span class="has-text-weight-semibold mx-1">Details</span>
                            <img
                                class="is-align-self-flex-center"
                                alt=""
                                src="/icons/chevrons-right.svg"
                            />
                        </button>
                        <button
                            class="button has-border-warning-light is-warning is-outlined mx-4 is-hidden-mobile mainhero__previous__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-left.svg" height={24} width={24} />
                            </span>
                        </button>
                        <button
                            class="button has-border-warning-light is-warning is-outlined mx-1 is-hidden-mobile mainhero__next__el"
                        >
                            <span class="icon is-small">
                                <img alt="" src="/icons/chevron-right.svg" height={24} width={24} />
                            </span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Hero footer: will stick at the bottom -->
        <div class="hero-foot is-hidden-mobile">
            <nav class="tabs is-clipped">
                <div class="container has-text-white">
                    <div class="columns is-mobile is-centered">
                        <div class="column is-narrow px-1">
                            <img src="/icons/arrow-down.svg" alt="" height={24} width={24} />
                        </div>
                        <div class="column is-narrow px-1">scroll below</div>
                    </div>
                </div>
            </nav>
        </div>
    </section>
</SwiperSlide>

<style lang="scss">
    .button {
        border-radius: 16px !important;
        border-width: 5px;
        height: 32px;
    }
</style>
