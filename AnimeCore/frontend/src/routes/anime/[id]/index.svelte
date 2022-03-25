<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";

    export const load: Load = async ({ fetch, params }) => {
        const res = await fetch(`https://api.jikan.moe/v4/anime/${params.id}`);
        return {
            props: {
                animeData: await res?.json()
            }
        };
    };
</script>

<script lang="ts">
    export let animeData: {
        data: {
            mal_id: number;
            url: string;
            images: {
                jpg: {
                    image_url: string;
                    small_image_url: string;
                    large_image_url: "";
                };
                webp: {
                    image_url: string;
                    small_image_url: string;
                    large_image_url: "";
                };
            };
            trailer: {
                youtube_id: string;
                url: string;
                embed_url: "";
            };
            title: string;
            title_english: string;
            title_japanese: string;
            title_synonyms: [""];
            type: string;
            source: string;
            episodes: number;
            status: string;
            airing: true;
            aired: {
                from: string;
                to: string;
                prop: {
                    from: {
                        day: number;
                        month: number;
                        year: number;
                    };
                    to: {
                        day: number;
                        month: number;
                        year: number;
                    };
                    string: "";
                };
            };
            duration: string;
            rating: string;
            score: number;
            scored_by: number;
            rank: number;
            popularity: number;
            members: number;
            favorites: number;
            synopsis: string;
            background: string;
            season: string;
            year: number;
            broadcast: {
                day: string;
                time: string;
                timezone: string;
                string: "";
            };
            producers: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            licensors: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            studios: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            genres: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            explicit_genres: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            themes: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
            demographics: [
                {
                    mal_id: number;
                    type: string;
                    name: string;
                    url: "";
                }
            ];
        };
    };
    import dayjs from "dayjs";

    import { page } from "$app/stores";
    import { responsiveMode } from "$store/responsive";

    import { projectName } from "$lib/constants/frontend/project";
    import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";

    // @fix-me
    // Better logic
    let animeStudios: string[] = [];
    $: animeData?.data?.studios?.forEach((items) => {
        animeStudios.push(items.name ?? "");
    });

    let animeGenres: string[] = [];
    $: animeData?.data?.genres?.forEach((items) => {
        animeGenres.push(items.name ?? "");
    });

    let animeTheme: string[] = [];
    $: animeData?.data?.themes?.forEach((items) => {
        animeTheme.push(items.name ?? "");
    });
</script>

<svelte:head>
    <title>{snakeCaseToTitleCase(animeData?.data?.title ?? "undefined")} | {projectName}</title>
</svelte:head>

{#if animeData.data === undefined}
    <section class="hero is-fullheight-with-navbar">
        <div class="hero-body is-justify-content-center">
            <div class="">
                <div class="columns is-mobile is-centered">
                    <div class="column is-narrow">
                        <img src="/crying_raiden.png" alt="crying_raiden" width={150} />
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
                    class="column is-align-self-flex-start has-text-white is-flex is-justify-content-center is-flex-direction-column
				{$responsiveMode === 'desktop' || $responsiveMode === 'widescreen' || $responsiveMode === 'fullhd'
                        ? 'is-3'
                        : ''}"
                >
                    <div class="columns is-mobile is-centered">
                        <div class="column is-narrow">
                            <img
                                alt=""
                                style="border-radius: 10px;"
                                src={animeData?.data?.images?.webp?.image_url}
                            />
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Name :</div>
                                <div class="column">{animeData?.data?.title}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Score :</div>
                                <div class="column">{animeData?.data?.score}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Episodes :</div>
                                <div class="column">{animeData?.data?.episodes}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Aired From :</div>
                                <div class="column">
                                    {dayjs(animeData?.data?.aired?.from).format(
                                        "MMMM D, YYYY - h:mm A"
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Aired To :</div>
                                <div class="column">
                                    {dayjs(animeData?.data?.aired?.to)?.format(
                                        "MMMM D, YYYY - h:mm A"
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Studios :</div>
                                <div class="column">
                                    {animeStudios?.toString()}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Source :</div>
                                <div class="column">{animeData?.data?.source}</div>
                            </div>
                        </div>
                    </div>
                    <div class="columns mb-0">
                        <div class="column">
                            <div class="columns is-mobile">
                                <div class="column">Genres :</div>
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
                                <div class="column">Theme :</div>
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
                                <div class="column">Duration :</div>
                                <div class="column">{animeData?.data?.duration}</div>
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
                        <h1 class="has-text-white">Synopsis</h1>
                        <p>
                            {animeData?.data?.synopsis}
                        </p>
                        <h1 class="has-text-white">Episodes :</h1>

                        <div class="grid-container">
                            {#each Array(100) as _, i}
                                <a
                                    href={`/anime/${$page?.params?.id}/episode/${i}`}
                                    sveltekit:prefetch
                                    class="button has-text-white is-black has-border-gray has-hover-gray is-rounded mx-3 my-1"
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
{/if}

<style lang="scss">
    .grid-container {
        display: grid;
        align-items: center;
        grid-template-columns: repeat(auto-fit, minmax(3em, 1fr));
    }
    .grid-item {
        background-color: black;
        text-align: center;
        transition: 0.2s;
    }
</style>
