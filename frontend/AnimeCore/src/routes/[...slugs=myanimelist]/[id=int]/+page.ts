import dayjs from "dayjs";

import { MAL } from "$data/urls";

import type { PageLoad } from "./$types";

export const load = (async ({
    params
    // ,fetch // Use this if you want Server Side Fetch | https://kit.svelte.dev/docs/hooks#externalfetch
}) => {
    const mal_id = new MAL();
    const data_url = mal_id.id(params.id);

    const data_response = await fetch(data_url);
    const data = await data_response?.json();

    const jikan_data: Partial<{
        mal_id: number;
        url: string;
        images: {
            jpg: {
                image_url: string;
                small_image_url: string;
                large_image_url: string;
            };
            webp: {
                image_url: string;
                small_image_url: string;
                large_image_url: string;
            };
        };
        trailer: {
            youtube_id: string;
            url: string;
            embed_url: string;
        };
        approved: true;
        titles: [
            {
                type: string;
                title: string;
            }
        ];
        title: string;
        title_english: string;
        title_japanese: string;
        title_synonyms: [string];
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
                string: string;
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
            string: string;
        };
        producers: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        licensors: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        studios: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        genres: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        explicit_genres: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        themes: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        demographics: [
            {
                mal_id: number;
                type: string;
                name: string;
                url: string;
            }
        ];
        relations: [
            {
                relation: string;
                entry: [
                    {
                        mal_id: number;
                        type: string;
                        name: string;
                        url: string;
                    }
                ];
            }
        ];
        theme: {
            openings: [string];
            endings: [string];
        };
        external: [
            {
                name: string;
                url: string;
            }
        ];
        streaming: [
            {
                name: string;
                url: string;
            }
        ];
    }> = data.data;

    console.log(data.data);

    const jikan_remapped_to_backend: Partial<{
        mal_id: number;
        episodes: [
            {
                episode_number: number;
            }
        ];
        title_english: string;
        title_japanese: string;
        anime_source: string;
        anime_aired_from: Date;
        anime_aired_to: Date;
        anime_cover: string; // Image
        anime_synopsis: string;
        anime_background: string;
        anime_rating: string;
        updated: Date;
    }> = {
        mal_id: jikan_data?.mal_id ?? 0,
        episodes: [{ episode_number: data?.episodes }],
        title_english: jikan_data?.title_english ?? "",
        title_japanese: jikan_data?.title_japanese ?? "",
        anime_source: jikan_data?.source ?? "",
        anime_aired_from: dayjs(jikan_data?.aired?.from, "YYYY-MM-DD").toDate(),
        anime_aired_to: dayjs(jikan_data?.aired?.to, "YYYY-MM-DD").toDate(),
        anime_cover: jikan_data?.images?.webp.image_url ?? jikan_data?.images?.jpg?.image_url ?? "",
        anime_synopsis: jikan_data?.synopsis ?? "",
        anime_background: jikan_data?.background ?? "",
        updated: new Date()
    };

    const errorMessage: string = data.status === 404 && data.message;

    return {
        animeData: jikan_remapped_to_backend,
        error: errorMessage
    };
}) satisfies PageLoad;
