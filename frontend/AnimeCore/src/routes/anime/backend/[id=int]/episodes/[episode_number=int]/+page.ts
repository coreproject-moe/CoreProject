import { UrlMaps } from "$data/urls";

import type { PageLoad } from "./$types";

export const load = (async ({
    params
    // ,fetch // Use this if you want Server Side Fetch | https://kit.svelte.dev/docs/hooks#externalfetch
}) => {
    const backend_mapping = new UrlMaps();

    const anime = async () => {
        const url = backend_mapping.id(params.id);
        const res = await fetch(url);
        const data: {
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
        } = await res.json();
        return data;
    };

    const episode = async () => {
        const url = backend_mapping.episode_number(params.id, params.episode_number);
        const res = await fetch(url);
        const data: {
            id: number;
            episode_number: number;
            episode_name: string;
            episode_thumbnail: string;
            episode_summary: string;
            episode_length: number;
            providers: { streamsb: string };
            episode_comments: Array<string>;
            episode_timestamps: Array<string>;
        } = await res.json();
        return data;
    };

    return {
        anime: anime(),
        episode: episode()
    };
}) satisfies PageLoad;
