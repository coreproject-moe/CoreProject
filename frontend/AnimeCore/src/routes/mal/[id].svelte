<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";

    // https://kit.svelte.dev/docs/hooks#externalfetch
    export const load: Load = async ({ params }) => {
        const id = params.id;
        const url = `https://api.jikan.moe/v4/anime/${id}/full`;

        const response = await fetch(url);
        const data = await response?.json();

        return {
            props: {
                animeData: data.status === 200 && data.data,
                error: data.status === 404 && data.message
            }
        };
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
    export let error: string;
    console.log(error);
</script>
