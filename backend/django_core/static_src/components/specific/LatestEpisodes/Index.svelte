<script lang="ts">
    import JSON5 from "json5";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Episode from "./Episode.svelte";
    import { reverse } from "$functions/urls";
    import { FETCH_TIMEOUT } from "$constants/fetch";
    import { get_csrf_token } from "$functions/get_csrf_token";

    type Episodes = {
        id: number;
        cover: string;
        name: string;
        episode_number: string;
        release_date: string;
        synopsis: string;
    }[];

    async function fetch_latest_episodes() {
        try {
            const res = await fetch(reverse("anime_latest_episodes"), {
                method: "GET",
                signal: AbortSignal.timeout(FETCH_TIMEOUT),
            });

            return await res.json() as Episodes;
        } catch (err) {
            console.log(err);
        };
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
        {#if episodes}
            {#each episodes as episode}
                <Episode {episode} />
            {/each}
        {/if}
    {/await}
</ScrollArea>
