<script lang="ts">
    export let backgroundImageUrl = "'https://bulma.io/images/placeholders/128x128.png'";
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
                    inset 5em 0 4em 1em #070519;

            "
        >
            <div class="hero-body is-flex-direction-row py-6 px-6">
                <div style="width:18em" class="px-5">
                    <figure class="image is-2by3">
                        <img
                            alt=""
                            style="border-radius:16px"
                            src="https://bulma.io/images/placeholders/256x256.png"
                        />
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
                        <h1 class="has-text-white is-size-2">My Dress Up Darling</h1>
                        <p style="width:70%" class="has-text-white">
                            High schooler Wakana Gojou cares about one thing: making Hina dolls.
                            With nobody to share his obsession, he has trouble finding friends—or
                            even holding conversation. But after the school's most popular girl,
                            Marin Kitagawa, reveals...
                        </p>
                        <div class="buttons">
                            <button
                                class="button is-warning has-border-transparent mx-2"
                                style="border-radius: 12px"
                                ><span class="icon is-small"
                                    ><img
                                        alt=""
                                        src="/icons/play.svg"
                                        width="24"
                                        height="24"
                                    /></span
                                ></button
                            >
                            <button class="button is-warning is-outlined mx-3"
                                ><span class="is-bold">Details</span>
                                <img
                                    alt=""
                                    src="/icons/chevrons-right.svg"
                                    class="s-o8_aYdz83WJL"
                                    width="24"
                                    height="24"
                                /></button
                            >
                            <button class="button is-warning is-outlined mx-2"
                                ><span class="icon is-small"
                                    ><img
                                        alt=""
                                        src="/icons/chevron-left.svg"
                                        width="24"
                                        height="24"
                                    /></span
                                ></button
                            >
                            <button class="button is-warning is-outlined mx-1"
                                ><span class="icon is-small"
                                    ><img
                                        alt=""
                                        src="/icons/chevron-right.svg"
                                        width="24"
                                        height="24"
                                    /></span
                                ></button
                            >
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</section>
