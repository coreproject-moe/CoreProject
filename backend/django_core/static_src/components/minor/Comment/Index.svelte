<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";
    import type { Comment } from "../../../types/comment";
    import { comment_needs_update } from "../../../stores/comment";
    import { onMount } from "svelte";

    export let api_url: string;

    interface CommentResponse {
        count: number;
        next: null | number;
        previous: null | number;
        results: Comment[];
    }

    let loading_state: "loading" | "error" | "loaded";
    let tree_branch: Comment[] = new Array<Comment>();

    onMount(() => {
        loading_state = "loading";
        get_comments()
            .then((res) => {
                tree_branch = res;
                loading_state = "loaded";
            })
            .catch((err) => {
                loading_state = "error";
            });
    });

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

    comment_needs_update.subscribe(async (val) => {
        if (val === true) {
            tree_branch = await get_comments();
            comment_needs_update.set(false);
        }
    });
</script>

{#if loading_state === "loading"}
    Loading..
{:else if loading_state === "error"}
    Something is wrong
{:else if loading_state === "loaded"}
    {#if tree_branch}
        <div class="flex flex-col md:gap-[1.5vw]">
            {#each tree_branch as branch}
                <CommetBlock item={branch} />
            {/each}
        </div>
    {:else}
        No comments
    {/if}
{/if}
