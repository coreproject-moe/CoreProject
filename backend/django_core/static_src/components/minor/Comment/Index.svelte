<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";
    import type { Comment } from "../../../types/comment";

    export let api_url: string;

    interface CommentResponse {
        count: number;
        next: null | number;
        previous: null | number;
        results: Comment[];
    }

    async function get_comments() {
        const res = await fetch(api_url, {
            method: "GET",
            headers: {
                "X-CSRFToken": window.csrfmiddlewaretoken
            }
        });
        const value = (await res.json()) as CommentResponse;
        const formated_json = new JSONToTree(value.results).to_tree() as unknown as Comment[];
        if (res.ok) {
            return formated_json;
        } else {
            throw new Error(await res.text());
        }
    }
</script>

{#await get_comments()}
    Loading...
{:then tree_branch}
    <div class="flex flex-col md:gap-[1.5vw]">
        {#each tree_branch as branch}
            <CommetBlock item={branch} />
        {/each}
    </div>
{/await}
