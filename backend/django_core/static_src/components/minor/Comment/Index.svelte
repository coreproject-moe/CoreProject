<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";
    import CommentSkeleton from "$components/minor/Comment/Skeleton.svelte";
    import Empty from "./Empty.svelte";
    import type { Comment } from "../../../types/comment";
    import { comment_needs_update } from "./store";
    import { onMount } from "svelte";
    import IntersectionOberser from "$components/svelte/IntersectionOberser.svelte";

    export let api_url: string;

    interface CommentResponse {
        count: number;
        next: null | string;
        previous: null | string;
        results: Comment[];
    }
    // This is set from backend
    let next_url: string | null;

    let loading_state: "loading" | "error" | "loaded",
        error = "";

    let tree_branch: Comment[] = new Array<Comment>();

    let last_element: HTMLElement;

    onMount(() => {
        set_comments();
    });

    const get_comments = async (url: string) => {
            const res = await fetch(url, {
                method: "GET",
                headers: {
                    "X-CSRFToken": window.csrfmiddlewaretoken
                }
            });
            const value = (await res.json()) as CommentResponse;
            next_url = value.next;

            const formated_json = new JSONToTree({
                json: value.results,
                old_json: tree_branch
            }).build() as unknown as Comment[];
            if (res.ok) {
                return formated_json;
            } else {
                throw new Error(await res.text());
            }
        },
        set_comments = () => {
            loading_state = "loading";
            get_comments(api_url)
                .then((res) => {
                    tree_branch = res;
                    loading_state = "loaded";
                })
                .catch((err) => {
                    loading_state = "error";
                    error = err;
                });
        },
        get_next_comments = async () => {
            if (next_url) {
                get_comments(next_url).then((res) => {
                    tree_branch = res;
                });
            }
        };

    // Store to trigger updates
    comment_needs_update.subscribe(async (val) => {
        if (val === true) {
            set_comments();
            comment_needs_update.set(false);
        }
    });
</script>

{#if loading_state === "loading"}
    <div class="flex flex-col md:gap-[1.5vw]">
        <CommentSkeleton />
    </div>
{:else if loading_state === "error"}
    Something is wrong Error : {@html error}
{:else if loading_state === "loaded"}
    {#if tree_branch}
        <div class="flex flex-col md:gap-[1.5vw]">
            {#each tree_branch as branch}
                <CommetBlock item={branch} />
            {/each}
        </div>
    {:else}
        <Empty />
    {/if}

    <!-- Intersection observer must be at last  -->
    {#if next_url !== null}
        <IntersectionOberser
            on:intersect={() => {
                get_next_comments();
            }}
            element={last_element}
        >
            <div bind:this={last_element} />
        </IntersectionOberser>
    {/if}
{/if}
