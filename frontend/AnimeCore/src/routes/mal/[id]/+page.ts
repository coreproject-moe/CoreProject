import type { PageLoad } from "@sveltejs/kit";

// https://kit.svelte.dev/docs/hooks#externalfetch
export const load: PageLoad = async ({ params }) => {
    const id = params.id;
    const url = `https://api.jikan.moe/v4/anime/${id}/full`;

    const response = await fetch(url);
    const data = await response?.json();

    return {
        animeData: data.data,
        error: data.status === 404 && data.message
    };
};
