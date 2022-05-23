<script lang="ts">
    import { activeModal } from "$store/modals";
</script>

<div
    class="modal animate__animated {$activeModal.option
        ? 'is-active animate__fadeInUp'
        : 'animate__fadeInDown'}"
>
    <div class="modal-background" />
    <div class="modal-content">
        <section class="hero is-medium">
            <!-- Hero head: will stick at the top -->
            <div class="hero-head">
                <div class="container pt-6 px-6" style="max-width:95vw">
                    <div class="title is-size-2 has-text-white">
                        <div class="columns is-mobile">
                            <div class="column is-narrow">
                                <span class="is-align-self-center"> Options </span>
                            </div>
                            <div class="column is-flex has-warning-light">
                                <div
                                    class="is-align-self-center"
                                    style="
                                        width: 100%;
                                        display: inline-block;
                                        border-top: 6px solid;
                                    "
                                />
                            </div>
                            <div class="column is-flex has-border-warning-light is-narrow">
                                <button
                                    class="button is-medium has-border-warning-light is-warning is-outlined px-2 py-4 modal-button-close"
                                    style="border-width:6px;border-radius:12px;"
                                    on:click={() => {
                                        $activeModal.option = false;
                                    }}
                                >
                                    <button
                                        class="delete is-large"
                                        style="background-color:transparent !important"
                                    />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Hero content: will be in the middle -->
            <div class="hero-body">
                <div class="container has-text-centered">
                    <p class="title">Title</p>
                    <p class="subtitle">Subtitle</p>
                </div>
            </div>

            <!-- Hero footer: will stick at the bottom -->
            <div class="hero-foot">
                <nav class="tabs">
                    <div class="container">
                        <ul>
                            <li class="is-active"><a>Overview</a></li>
                            <li><a>Modifiers</a></li>
                            <li><a>Grid</a></li>
                            <li><a>Elements</a></li>
                            <li><a>Components</a></li>
                            <li><a>Layout</a></li>
                        </ul>
                    </div>
                </nav>
            </div>
        </section>
    </div>
</div>

<style lang="scss">
    .hero {
        border-radius: 25px;
        background-color: #070519;
    }
    .animate__animated.animate__fadeInUp {
        --animate-duration: 0.2s;
    }
</style>
