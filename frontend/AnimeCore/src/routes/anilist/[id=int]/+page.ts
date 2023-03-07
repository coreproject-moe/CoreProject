import { UrlMaps } from "$data/urls";

import type { PageLoad } from "./$types";

export const load = (async ({
    params,
    fetch // Use this if you want Server Side Fetch | https://kit.svelte.dev/docs/hooks#externalfetch
}) => {
    const backend_mapping = new UrlMaps();

    const anime = async () => {
        const url = backend_mapping.anilist_id(params.id);
        console.log(url);
        const data_response = await fetch(url);
        const data: {
            items: {
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
                episodes: string;
                recommendations: [number];
                episodes_count: number;
            }[];
        } = await data_response?.json();

        const backend_data: {
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
            episodes: string;
            recommendations: [number];
            episodes_count: number;
        } = data?.["items"]?.[0] ?? {
            id: 0,
            mal_id: 0,
            anilist_id: 0,
            kitsu_id: 0,
            name: "",
            name_japanese: "",
            source: "",
            aired_from: "",
            aired_to: "",
            banner: "",
            cover: "",
            banner_background_color: "",
            cover_background_color: "",
            synopsis: "",
            background: "",
            rating: "",
            theme_openings: "",
            theme_endings: "",
            updated: "",
            name_synonyms: [],
            genres: "",
            themes: "",
            studios: "",
            producers: "",
            characters: "",
            episodes: "",
            recommendations: [0],
            episodes_count: 0
        };

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
            genres: string;
            episodes: string;
            episodes_count: number;
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
            genres: backend_data?.genres ?? "",
            episodes: backend_data?.episodes ?? "",
            episodes_count: backend_data?.episodes_count ?? 0
        };

        return backend_remapped_to_frontend;
    };

    return {
        animeData: anime()
    };
}) satisfies PageLoad;
