<script lang="ts">
    /** @type {import('./$types').PageData} */
    export let data;
    
    export let animeData: {
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
    };
    export let error: string;
    console.log(animeData);
</script>

<svelte:head>
    <title>{animeData.title_english}</title>
</svelte:head>
