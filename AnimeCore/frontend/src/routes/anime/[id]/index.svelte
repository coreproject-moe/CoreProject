<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";

    export const load: Load = async ({ fetch, params }) => {
        try {
            if (browser) {
                const res = await fetch(`${animeInfoEndpoint}${params.id}`);
                return {
                    status: res.status,
                    props: {
                        animeData: await res?.json()
                    }
                };
            }
            return {};
        } catch {
            return {
                status: 404
            };
        }
    };
</script>

<script lang="ts">
    export let animeData: {
        mal_id: number;
        episodes: [
            {
                episode_number: number;
            }
        ];
        anime_name: string;
        anime_name_japanese: string;
        anime_source: string;
        anime_aired_from: Date;
        anime_aired_to: Date;
        anime_cover: string; // Image
        anime_synopsis: string;
        anime_background: string;
        anime_rating: string;
        updated: Date;
    };

    import dayjs from "dayjs";

    import { page } from "$app/stores";
    import { responsiveMode } from "$store/responsive";

    import { projectName } from "$lib/constants/frontend/project";
    import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";
    import { animeInfoEndpoint } from "$urls/restEndpoints";
    import { browser } from "$app/env";

    // @fix-me
    // Better logic
    let animeStudios: string[] = [];
    // $: animeData?.studios?.forEach((items) => {
    //     animeStudios.push(items.name ?? "");
    // });

    let animeGenres: string[] = [];
    // $: animeData?.genres?.forEach((items) => {
    //     animeGenres.push(items.name ?? "");
    // });

    let animeTheme: string[] = [];
    // $: animeData?.themes?.forEach((items) => {
    //     animeTheme.push(items.name ?? "");
    // });
</script>

<svelte:head>
    <title>{snakeCaseToTitleCase(animeData?.anime_name ?? "undefined")} | {projectName}</title>
</svelte:head>

{#if !animeData}
    <section class="hero is-fullheight-with-navbar">
        <div class="hero-body is-justify-content-center">
            <div class="">
                <div class="columns is-mobile is-centered">
                    <div class="column is-narrow">
                        <img src="/images/crying_raiden.png" alt="crying_raiden" width={150} />
                    </div>
                </div>
                <p class="subtitle has-text-white has-text-centered">This anime is unavailable</p>
            </div>
        </div>
    </section>
{:else}
    <section class="hero is-fullheight-with-navbar">
        <div class="hero-body is-flex-direction-column">
            <div
                class="columns is-desktop container {$responsiveMode === 'mobile'
                    ? 'is-flex-direction-column'
                    : 'is-flex-direction-row'}"
            >
                <div
                    class="column is-justify-content-start has-text-white is-flex is-justify-content-center is-flex-direction-column
				{$responsiveMode === 'desktop' || $responsiveMode === 'widescreen' || $responsiveMode === 'fullhd'
                        ? 'is-3'
                        : ''}"
                >
                    <div class="columns is-mobile is-centered">
                        <div class="column is-narrow">
                            <img alt="" style="border-radius: 10px;" src={animeData?.anime_cover} />
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">MyAnimeList:</div>
                                <div class="column">
                                    <a
                                        class="has-text-white is-underlined"
                                        href="https://myanimelist.net/anime/{animeData?.mal_id}"
                                        >{animeData?.mal_id}
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Name:</div>
                                <div class="column">{animeData?.anime_name}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Japanese Name:</div>
                                <div class="column">{animeData?.anime_name_japanese}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Score:</div>
                                <div class="column">{"Score"}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Episodes:</div>
                                <div class="column">{animeData?.episodes?.length}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Aired From:</div>
                                <div class="column">
                                    {dayjs(animeData?.anime_aired_from)?.format(
                                        "MMMM D, YYYY - h:mm A"
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Aired To:</div>
                                <div class="column">
                                    {dayjs(animeData?.anime_aired_to)?.format(
                                        "MMMM D, YYYY - h:mm A"
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Studios:</div>
                                <div class="column">
                                    {animeStudios?.toString()}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Source:</div>
                                <div class="column">{animeData?.anime_source}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Genres:</div>
                                <div
                                    class="column"
                                    style="display: inline;overflow: hidden;text-overflow: ellipsis;width:0px"
                                >
                                    {animeGenres?.toString()}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Theme:</div>
                                <div
                                    class="column"
                                    style="display: inline;overflow: hidden;text-overflow: ellipsis;width:0px"
                                >
                                    {animeTheme?.toString()}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Duration:</div>
                                <div class="column">{"animeData?.duration"}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div
                    class="column is-flex is-justify-content-end {$responsiveMode === 'desktop' ||
                    $responsiveMode === 'widescreen' ||
                    $responsiveMode === 'fullhd'
                        ? ''
                        : 'is-align-self-center'}"
                >
                    <div class="content has-text-white">
                        <h1 class="has-text-white">Synopsis</h1>
                        <p>
                            {animeData?.anime_synopsis}
                        </p>

                        {#if animeData?.anime_background}
                            <h1 class="has-text-white">Background</h1>
                            <p>
                                {animeData?.anime_background}
                            </p>
                        {/if}

                        <h1 class="has-text-white">Episodes</h1>

                        {#if animeData?.episodes?.length}
                            <div class="grid-container">
                                {#each animeData?.episodes as i}
                                    <a
                                        href={`/anime/${$page?.params?.id}/episode/${i?.episode_number}`}
                                        sveltekit:prefetch
                                        style="width:30px"
                                        class="button has-text-white is-black has-border-gray has-hover-gray is-rounded mx-3 my-1"
                                    >
                                        {i?.episode_number}
                                    </a>
                                {/each}
                            </div>
                        {:else}
                            <div>
                                <div class="columns is-mobile is-centered is-flex-direction-column">
                                    <div class="column is-narrow is-flex is-justify-content-center">
                                        <img
                                            src="/images/crying_raiden_2.png"
                                            alt="crying_raiden"
                                            width={150}
                                        />
                                    </div>
                                    <div class="column is-narrow has-text-centered">
                                        There are no episodes available for this anime
                                    </div>
                                </div>
                            </div>
                        {/if}
                    </div>
                </div>
            </div>
        </div>
    </section>
{/if}

<style lang="scss">
    .grid-container {
        display: grid;
        align-items: center;
        grid-template-columns: repeat(auto-fill, minmax(3em, 1fr));
    }
</style>
