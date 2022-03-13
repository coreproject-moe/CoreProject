<script lang="ts">
    export let animeNumber: number;
    export let animeName = "One Piece";

    import tippy from "tippy.js";
    import { SwiperSlide } from "swiper/svelte";
</script>

<SwiperSlide>
    <a
        sveltekit:prefetch
        href="/anime/{animeNumber}"
        class="card"
        style="background-color: black !important;"
    >
        <div class="card-image has-background-black">
            <figure class="image">
                <div
                    style="
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        
                    "
                    data-href="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
                    class="progressive replace"
                >
                    <img src="/placeholder-225x350.avif" class="preview" alt="" />
                </div>
            </figure>
        </div>
        <div
            class="card-content has-background-black-bis"
            style="
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            "
        >
            <div class="media">
                <div class="media-content">
                    <p class="is-size-4 has-text-white">{animeName}</p>
                    <p class="subtitle is-size-6 has-text-white">
                        Episodes : <span>&infin;</span>
                        <br />
                        Duration : total.secnds <br />
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
