<script lang="ts">
    export let animeNumber: number | string = "∞";
    export let animeName = "One Piece";
    export let animePosterImage = "https://cdn.myanimelist.net/images/anime/6/73245.jpg";

    import tippy, { type Instance } from "tippy.js";
    import { SwiperSlide } from "swiper/svelte";
    import { onDestroy, onMount } from "svelte";

    let tippyjsAnimeNumberElement: HTMLElement & { _tippy?: Instance };

    onMount(async () => {
        if (animeNumber === "∞") {
            tippy(tippyjsAnimeNumberElement, {
                content: "This anime is probably ongoing",
                theme: "black",
                maxWidth: 120,
                placement: "top"
            });
        }
    });
    onDestroy(async () => {
        tippyjsAnimeNumberElement?._tippy?.destroy();
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
                    <p class="is-size-4 has-text-white">{animeName}</p>
                    <p class="subtitle is-size-6 has-text-white">
                        Episodes : <span
                            style="text-decoration:underline"
                            bind:this={tippyjsAnimeNumberElement}>{animeNumber}</span
                        >
                        <br />
                    </p>
                    <div
                        class="field is-grouped is-grouped-multiline is-flex is-justify-content-center"
                    >
                        <div class="control">
                            <div class="tags has-addons">
                                <span class="tag is-dark heading">sub</span>
                                <span class="tag is-info heading">dub</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </a>
</SwiperSlide>
