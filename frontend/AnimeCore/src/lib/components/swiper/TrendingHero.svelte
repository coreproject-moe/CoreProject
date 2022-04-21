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
            <div class="hero-body">
                <p class="title">Large hero</p>
                <p class="subtitle">Large subtitle</p>
            </div>
        </section>
    </div>
</section>
