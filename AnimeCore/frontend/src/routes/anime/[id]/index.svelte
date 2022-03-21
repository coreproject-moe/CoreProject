<script lang="ts">
    import { page } from "$app/stores";
    import { responsiveMode } from "$store/responsive";

    import { projectName } from "$lib/constants/frontend/project";
    import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";

    $: anime_name = "";
</script>

<svelte:head>
    <title>{snakeCaseToTitleCase(anime_name)} | {projectName}</title>
</svelte:head>

<section class="hero is-fullheight-with-navbar">
    <div class="hero-body is-flex-direction-column">
        <div
            class="columns is-desktop container {$responsiveMode === 'mobile'
                ? 'is-flex-direction-column'
                : 'is-flex-direction-row'}"
        >
            <div
                class="column is-align-self-center has-text-white is-flex is-justify-content-center is-flex-direction-column
				{$responsiveMode === 'desktop' || $responsiveMode === 'widescreen' || $responsiveMode === 'fullhd'
                    ? 'is-3'
                    : ''}"
            >
                <div class="columns is-mobile is-centered">
                    <div class="column is-narrow">
                        <div
                            class="progressive replace"
                            data-href="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
                            style="border-radius: 10px;"
                        >
                            <img alt="" src="/placeholder-225x350.avif" class="preview" />
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Name :</div>
                            <div class="column">anime.name</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Score :</div>
                            <div class="column">anime.score</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Episodes :</div>
                            <div class="column">anime.episodes</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Aired :</div>
                            <div class="column">anime.aired</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Studios :</div>
                            <div class="column">anime.studios</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Source :</div>
                            <div class="column">anime.source</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Genres :</div>
                            <div class="column">anime.genres</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Theme :</div>
                            <div class="column">anime.theme</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Duration :</div>
                            <div class="column">anime.duration</div>
                        </div>
                    </div>
                </div>
                <div class="columns mb-0">
                    <div class="column">
                        <div class="columns is-mobile">
                            <div class="column">Rating :</div>
                            <div class="column">anime.rating</div>
                        </div>
                    </div>
                </div>
            </div>
            <div
                class="column is-flex {$responsiveMode === 'desktop' ||
                $responsiveMode === 'widescreen' ||
                $responsiveMode === 'fullhd'
                    ? ''
                    : 'is-align-self-center'}"
            >
                <div class="content has-text-white">
                    <h1 class="has-text-white">Hello World</h1>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan,
                        metus ultrices eleifend gravida, nulla nunc varius lectus, nec rutrum justo
                        nibh eu lectus. Ut vulputate semper dui. Fusce erat odio, sollicitudin vel
                        erat vel, interdum mattis neque. Sub<sub>script</sub> works as well!
                    </p>
                    <h1 class="has-text-white">Episodes :</h1>

                    <div class="grid-container">
                        {#each Array(100) as _, i}
                            <a
                                sveltekit:prefetch
                                href={`/anime/${$page?.params?.id}/episode/${i}`}
                                class="grid-item is-size-6 has-border-white is-clickable is-font-face-roboto has-text-white"
                                on:mouseenter|capture={(e) => {
                                    e?.currentTarget?.classList?.add("grid-item-hover");
                                }}
                                on:mouseleave|capture={(e) => {
                                    e?.currentTarget?.classList?.remove("grid-item-hover");
                                }}
                            >
                                {i}
                            </a>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<style lang="scss">
    .grid-container {
        display: grid;
        align-items: center;
        grid-template-columns: repeat(auto-fit, minmax(4em, 1fr));
        background-color: black;
    }
    .grid-item {
        background-color: black;
        padding: 0.8em;
        text-align: center;
        transition: 0.2s;

        &:global(.grid-item-hover) {
            background-color: hsl(0, 0%, 15%) !important;
        }
    }
</style>
