<script lang="ts">
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Episode from "./Episode.svelte";
    import { reverse } from "$functions/urls";
    import { FETCH_TIMEOUT } from "$constants/fetch";

    type Episodes = {
        id: number;
        cover: string;
        name: string;
        episode_number: string;
        release_date: string;
        synopsis: string;
    }[];

    async function fetch_latest_episodes() {
        const res = await fetch(reverse("anime_latest_episodes"), {
            method: "GET",
            signal: AbortSignal.timeout(FETCH_TIMEOUT),
        });

        return await res.json() as Episodes;
    };

    const fetch_promise = fetch_latest_episodes();
</script>

<ScrollArea
    gradient_mask
    offset_scrollbar
    parent_class="mt-[1vw] w-full max-h-[23vw] snap-y smooth-scroll snap-mandatory"
    class="flex w-full flex-col gap-[1vw]"
>
    {#await fetch_promise then episodes}
        {#each episodes as episode}
            <Episode {episode} />
        {/each}
    {/await}
</ScrollArea>
