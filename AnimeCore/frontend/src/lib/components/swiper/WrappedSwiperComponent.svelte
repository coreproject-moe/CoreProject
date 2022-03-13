<script lang="ts">
    export let animeNumber: number | string = "∞";
    export let animeName =
        "One Piece Hello world Hdassad fafdsa One Piece Hello world Hdassad fafdsa One Piece Hello world Hdassad fafdsa";
    export let animePosterImage = "https://cdn.myanimelist.net/images/anime/6/73245.jpg";

    import { SwiperSlide } from "swiper/svelte";
    import { onDestroy, onMount } from "svelte";
    import tippy, { followCursor, animateFill, type Instance } from "tippy.js";

    let tippyJsAnimeNumberElement: HTMLElement & { _tippy?: Instance };
    let tippyJsAnimeNameElement: HTMLElement & { _tippy?: Instance };
    let tippyJsSubElement: HTMLElement & { _tippy?: Instance };
    let tippyJsDubElement: HTMLElement & { _tippy?: Instance };

    onMount(async () => {
        if (animeNumber === "∞") {
            tippy(tippyJsAnimeNumberElement, {
                content: "<p class='is-size-7'>No End Reached 😱</p>",
                allowHTML: true,
                theme: "black",
                offset: [0, -5],
                maxWidth: 130,
                placement: "top",
                animateFill: true,
                followCursor: "horizontal",
                plugins: [followCursor, animateFill]
            });
        }
        tippy(tippyJsAnimeNameElement, {
            content: `<p class='is-size-7'>${animeName}</p>`,
            allowHTML: true,
            theme: "black",
            maxWidth: 150,
            placement: "top",
            animateFill: true,
            followCursor: "horizontal",
            plugins: [followCursor, animateFill]
        });
        tippy(tippyJsSubElement, {
            content: "<p class='is-size-7'>This anime has English <b>Subtitles</b>🥳</p>",
            allowHTML: true,
            theme: "black",
            maxWidth: 140,
            placement: "top",
            animateFill: true,
            followCursor: "horizontal",
            plugins: [followCursor, animateFill]
        });
        tippy(tippyJsDubElement, {
            content: "<p class='is-size-7'>This anime has English <b>Audio</b>🥳</p>",
            allowHTML: true,
            theme: "black",
            maxWidth: 120,
            placement: "top",
            animateFill: true,
            followCursor: "horizontal",
            plugins: [followCursor, animateFill]
        });
    });
    onDestroy(async () => {
        tippyJsAnimeNumberElement?._tippy?.destroy();
        tippyJsAnimeNameElement?._tippy?.destroy();
        tippyJsDubElement?._tippy?.destroy();
        tippyJsSubElement?._tippy?.destroy();
    });
</script>

<SwiperSlide>
    <a sveltekit:prefetch href="/anime/{animeNumber}" class="card">
        <div class="card-image has-background-black">
            <figure class="image">
                <div
                    style="border-top-left-radius: 10px;border-top-right-radius: 10px;"
                    data-href={animePosterImage}
                    class="progressive replace"
                >
                    <img src="/placeholder-225x350.avif" class="preview" alt="" />
                </div>
            </figure>
        </div>
        <div
            class="card-content has-background-black-bis"
            style="border-bottom-left-radius: 10px;border-bottom-right-radius: 10px;"
        >
            <div class="media">
                <div class="media-content">
                    <p class="is-size-5 has-text-white">
                        <span class="anime_name" bind:this={tippyJsAnimeNameElement}
                            >{animeName}</span
                        >
                    </p>
                    <p class="subtitle has-text-white mb-0">
                        <span class="is-size-7">Episodes :</span>
                        <span class="is-size-5" bind:this={tippyJsAnimeNumberElement}
                            >{animeNumber}</span
                        >
                    </p>
                    <br />

                    <div
                        class="field is-grouped is-grouped-multiline is-flex is-justify-content-start"
                    >
                        <div class="control">
                            <div class="tags has-addons">
                                <span
                                    class="tag is-black"
                                    style="border:1px solid cornflowerblue"
                                    bind:this={tippyJsSubElement}>Sub</span
                                >
                                <span
                                    class="tag is-black"
                                    style="border:1px solid springgreen"
                                    bind:this={tippyJsDubElement}>Dub</span
                                >
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </a>
</SwiperSlide>

<style lang="scss">
    .anime_name {
        overflow: hidden !important;
        width: 6em !important;
        display: block ruby;
        text-overflow: ellipsis;
    }
</style>
