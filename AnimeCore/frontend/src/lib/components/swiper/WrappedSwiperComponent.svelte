<script lang="ts">
    export let animeNumber: number;
    export let animeName: string;
    export let animePosterImage: string;

    import { SwiperSlide } from "swiper/svelte";
    import tippy, { followCursor, animateFill } from "tippy.js";
</script>

<SwiperSlide>
    <a sveltekit:prefetch href="/anime/{animeNumber}" style="z-index:999999" class="card">
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
                <div class="media-content is-clipped">
                    <p class="is-size-5 has-text-white">
                        <span
                            class="anime_name"
                            use:tippy={{
                                content: `<p class='is-size-7'>${animeName}</p>`,
                                allowHTML: true,
                                theme: "black",
                                maxWidth: 150,
                                placement: "top",
                                animateFill: true,
                                followCursor: "horizontal",
                                plugins: [followCursor, animateFill]
                            }}
                        >
                            {animeName}
                        </span>
                    </p>
                    <p class="subtitle has-text-white mb-0">
                        <span class="is-size-7"
                            ><ion-icon
                                name="tv-outline"
                                class="is-size-5"
                                style="color:firebrick;transform:translateY(5px)"
                            />
                        </span>
                        <span
                            class="is-size-5"
                            use:tippy={{
                                content: "<p class='is-size-7'>No End Reached 😱</p>",
                                allowHTML: true,
                                theme: "black",
                                offset: [0, -5],
                                maxWidth: 130,
                                placement: "top",
                                animateFill: true,
                                followCursor: "horizontal",
                                plugins: [followCursor, animateFill]
                            }}
                        >
                            ∞
                        </span>

                        <span class="is-size-7"
                            ><ion-icon
                                name="star-outline"
                                class="is-size-5"
                                style="color:yellow;transform:translateY(5px)"
                            />
                        </span>
                        <span
                            class="is-size-5"
                            use:tippy={{
                                content: "<p class='is-size-7'>No End Reached 😱</p>",
                                allowHTML: true,
                                theme: "black",
                                offset: [0, -5],
                                maxWidth: 130,
                                placement: "top",
                                animateFill: true,
                                followCursor: "horizontal",
                                plugins: [followCursor, animateFill]
                            }}
                        >
                            ∞
                        </span>
                    </p>
                    <br />

                    <div
                        class="field is-grouped is-grouped-multiline is-flex is-justify-content-start"
                    >
                        <div class="control">
                            <div class="tags has-addons">
                                <span
                                    class="tag is-black has-border-blue"
                                    use:tippy={{
                                        content:
                                            "<p class='is-size-7'>This anime has English <b>Subtitles</b>🥳</p>",
                                        allowHTML: true,
                                        theme: "black",
                                        maxWidth: 140,
                                        placement: "top",
                                        animateFill: true,
                                        followCursor: "horizontal",
                                        plugins: [followCursor, animateFill]
                                    }}
                                >
                                    Sub
                                </span>
                                <span
                                    class="tag is-black has-border-green"
                                    use:tippy={{
                                        content:
                                            "<p class='is-size-7'>This anime has English <b>Audio</b>🥳</p>",
                                        allowHTML: true,
                                        theme: "black",
                                        maxWidth: 120,
                                        placement: "top",
                                        animateFill: true,
                                        followCursor: "horizontal",
                                        plugins: [followCursor, animateFill]
                                    }}
                                >
                                    Dub
                                </span>
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
