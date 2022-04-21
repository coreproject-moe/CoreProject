<script lang="ts">
    export let backgroundImageUrl = "'https://bulma.io/images/placeholders/128x128.png'";
</script>

<section class="hero is-fullheight">
    <div class="hero-body is-align-self-center">
        <div>
            <div class="title pb-5 is-size-2 has-text-white">
                <div class="is-flex">
                    <span class="pr-5 is-align-self-center"> TRENDING </span>
                    <div
                        class="is-align-self-center"
                        style="display: inline-block;width: 26em;border-top: 10px solid;"
                    />
                </div>
            </div>
            <section
                class="hero is-large"
                style="
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
                <div class="hero-body">
                    <p class="title">Large hero</p>
                    <p class="subtitle">Large subtitle</p>
                </div>
            </section>
        </div>
    </div>
</section>
