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

    let loading_state: "loading" | "loaded" | "errored" = "loading",
        error = "",
        tree_branch: Comment[] = new Array<Comment>();

    onMount(() => {
        set_comments();
    });

    const get_comments = async () => {
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
        },
        set_comments = () => {
            get_comments()
                .then((res) => {
                    tree_branch = res;
                    loading_state = "loaded";
                })
                .catch((err) => {
                    loading_state = "errored";
                    error = err;
                });
        };

    comment_needs_update.subscribe(async (val) => {
        if (val === true) {
            set_comments();
            comment_needs_update.set(false);
        }
    });
</script>

{#if loading_state === "loading"}
    Loading
{:else if loading_state === "errored"}
    Something is wrong
{:else if loading_state === "loaded"}
    <div class="flex flex-col md:gap-[1.5vw]">
        {#each tree_branch as branch}
            <CommetBlock item={branch} />
        {/each}
    </div>
{/if}
