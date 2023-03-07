import { UrlMaps } from "$data/urls";

import type { PageLoad } from "./$types";

export const load = (async ({
    params
    // ,fetch // Use this if you want Server Side Fetch | https://kit.svelte.dev/docs/hooks#externalfetch
}) => {
    const backend_mapping = new UrlMaps();

    const anime = async () => {
        const url = backend_mapping.id(params.id);
        const data_response = await fetch(url);
        const data = await data_response?.json();

        const backend_data: Partial<{
            id: number;
            mal_id: number;
            anilist_id: number;
            kitsu_id: number;
            name: string;
            name_japanese: string;
            source: string;
            aired_from: string;
            aired_to: string;
            banner: string;
            cover: string;
            banner_background_color: string;
            cover_background_color: string;
            synopsis: string;
            background: string;
            rating: string;
            theme_openings: string;
            theme_endings: string;
            updated: string;
            name_synonyms: [];
            genres: string;
            themes: string;
            studios: string;
            producers: string;
            characters: string;
            recommendations: [number];
            episodes: [number];
        }> = data;

        const backend_remapped_to_frontend: Partial<{
            mal_id: number;
            title_english: string;
            title_japanese: string;
            anime_source: string;
            anime_aired_from: string;
            anime_aired_to: string;
            anime_banner: string; // image
            anime_cover: string; // Image
            anime_synopsis: string;
            anime_background: string;
            anime_rating: string;
            genres: () => Promise<{ id: number; mal_id: number; name: string; type: string }[]>;
            episodes: () => Promise<
                {
                    id: number;
                    episode_number: number;
                    episode_name: string;
                    episode_thumbnail: string;
                    episode_summary: string;
                    providers: Array<object>;
                }[]
            >;
        }> = {
            mal_id: backend_data?.mal_id ?? 0,
            title_english: backend_data?.name ?? "",
            title_japanese: backend_data?.name_japanese ?? "",
            anime_source: backend_data?.source ?? "",
            anime_aired_from: backend_data?.aired_from ?? "",
            anime_aired_to: backend_data?.aired_to ?? "",
            anime_banner: backend_data?.banner ?? "",
            anime_cover: backend_data?.cover ?? "",
            anime_synopsis: backend_data?.synopsis ?? "",
            anime_background: backend_data?.background ?? "",

            genres: async () => {
                const res = await fetch(backend_mapping.DOMAIN + String(backend_data.genres));
                const res_json = await res.json();
                const data: Array<{
                    id: number;
                    mal_id: number;
                    name: string;
                    type: string;
                }> = res_json;
                return data;
            },

            episodes: async () => {
                const res = await fetch(backend_mapping.DOMAIN + String(backend_data.episodes));
                const res_json = await res.json();
                const data: Array<{
                    id: number;
                    episode_number: number;
                    episode_name: string;
                    episode_thumbnail: string;
                    episode_summary: string;
                    providers: Array<object>;
                }> = res_json;
                return data;
            }
        };

        return backend_remapped_to_frontend;
    };

    return {
        animeData: anime()
    };
}) satisfies PageLoad;
