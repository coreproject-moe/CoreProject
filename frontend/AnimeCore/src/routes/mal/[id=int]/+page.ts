import { MAL_URL } from "$data/urls";

import type { PageLoad } from "./$types";

// https://kit.svelte.dev/docs/hooks#externalfetch

export const load: PageLoad = async ({
    params
    // ,fetch // Use this if you want Server Side Fetch
}) => {
    const id = params.id;
    const url = MAL_URL.replace("{id}", id);

    const response = await fetch(url);
    const data = await response?.json();

    const animeData: Partial<{
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
    }> = data.data;

    const errorMessage: string = data.status === 404 && data.message;

    return {
        animeData: animeData,
        error: errorMessage
    };
};
