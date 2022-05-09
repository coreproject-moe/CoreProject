<script lang="ts">
    import { SwiperSlide } from "swiper/svelte";

    import Navbar from "$components/common/Navbar.svelte";
    import { truncateString } from "$lib/functions/truncateText";
    import { responsiveMode } from "$store/responsive";

    export let backgroundImageUrl: string;
    export let animeName: string;
    export let backgroundBannerUrl = "https://media.kitsu.io/anime/poster_images/6686/large.jpg";
    export let animeSummary = `High school freshman Houtarou Oreki has but one goal: to lead a gray life while conserving as much energy as he can. Unfortunately, his peaceful days come to an end when his older sister, Tomoe, forces him to save the memberless Classics Club from disbandment. Luckily, Oreki's predicament seems to be over when he heads to the clubroom and discovers that his fellow first-year, Eru Chitanda, has already become a member. However, despite his obligation being fulfilled, Oreki finds himself entangled by Chitanda's curious and bubbly personality, soon joining the club of his own volition. Hyouka follows the four members of the Classics Club—including Oreki's friends Satoshi Fukube and Mayaka Ibara—as they, driven by Chitanda's insatiable curiosity, solve the trivial yet intriguing mysteries that permeate their daily lives.`;

    let wordCount: number;

    $: {
        switch ($responsiveMode) {
            case "mobile":
                wordCount = 100;
                break;
            case "tablet":
                wordCount = 350;
                break;

            case "desktop":
            case "widescreen":
            case "fullhd":
                wordCount = 500;
                break;
            default:
                break;
        }
    }
</script>

<SwiperSlide>
    <section
        class="hero {$responsiveMode === 'mobile'
            ? 'is-halfheight mobile-shadow'
            : 'is-fullheight desktop-shadow'}"
        style="
            background-image: url({$responsiveMode === 'mobile'
            ? backgroundBannerUrl
            : backgroundImageUrl});
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        "
    >
        <!-- Hero head: will stick at the top -->
        <div class="hero-head">
            <Navbar />
        </div>

        <!-- Hero content: will be in the middle -->
        <div class="hero-body is-align-items-self-end">
            <div class="container pb-6">
                <div
                    class="title has-text-warning  container {$responsiveMode === 'mobile'
                        ? 'is-size-7 mb-0'
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
                    class="title has-text-white is-bold {$responsiveMode === 'mobile'
                        ? 'is-size-2 mb-0'
                        : 'is-size-1'}"
                >
                    {animeName}
                </div>
                <div
                    class="subtitle has-text-white pt-5 {$responsiveMode === 'mobile'
                        ? 'is-size-7'
                        : 'is-size-6'}"
                    style={$responsiveMode === "mobile" ? "width: 100%;" : "width: 70%;"}
                >
                    {truncateString(animeSummary, wordCount)}
                </div>
                <!-- Tags -->
                <div class="subtitle is-hidden-mobile">
                    <span class="tag is-size-6 mx-1 is-bold is-black"> Mystery </span>
                    <span class="tag is-size-6 mx-1 is-bold is-black"> Slice of Life </span>
                </div>

                <div class="buttons {$responsiveMode === 'mobile' ? 'are-small' : 'are-medium'}">
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
        border-radius: 10px !important;
        border-width: 5px;

        @media screen and (max-width: 768px) {
            border-width: 3px;
            border-radius: 8px !important;
        }
    }
    .desktop-shadow {
        box-shadow: inset 0 4px 1800px rgb(7, 5, 25), inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7), inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2);
    }
    .mobile-shadow {
        box-shadow: inset 0px -30px 12px -2px rgba(7, 5, 25, 0.95),
            inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.8), inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2);
    }
</style>
