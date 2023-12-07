<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";
    import type { Comment } from "../../../types/comment";
    import { comment_needs_update } from "../../../stores/comment";

    export let api_url: string;

    interface CommentResponse {
        count: number;
        next: null | number;
        previous: null | number;
        results: Comment[];
    }

    let tree = get_comments();

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

    comment_needs_update.subscribe((val) => {
        if (val === true) {
            tree = get_comments();
            comment_needs_update.set(false);
        }
    });
</script>

{#key tree}
    {#await tree}
        Loading...
    {:then tree_branch}
        <div class="flex flex-col md:gap-[1.5vw]">
            {#each tree_branch as branch}
                <CommetBlock item={branch} />
            {/each}
        </div>
    {:catch e}
        Something is wrong {e}
    {/await}
{/key}
