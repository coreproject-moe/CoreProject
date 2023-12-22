<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";
    import CommentSkeleton from "$components/minor/Comment/Skeleton.svelte";
    import Empty from "./Empty.svelte";
    import ErrorSvelteComponent from "./Error.svelte";
    import type { Comment } from "../../../types/comment";
    import { comment_needs_update } from "./store";
    import { onMount } from "svelte";
    import * as _ from "lodash-es";
    import IntersectionOberser from "$components/svelte/IntersectionOberser.svelte";
    import { get_csrf_token } from "$functions/get_csrf_token";

    export let api_url: string;

    interface CommentResponse {
        detail?: string;
        count: number;
        next: null | string;
        previous: null | string;
        results: Comment[];
    }
    // This is set from backend
    let next_url: string | null;

    let loading_state: "loading" | "error" | "loaded" = "loading",
        error: string | null = null;

    let tree_branch: Comment[] = new Array<Comment>();

    let last_element: HTMLElement;

    onMount(() => {
        set_comments();
    });

    const get_comments = async (url: string) => {
            const res = await fetch(url, {
                method: "GET",
                headers: {
                    "X-CSRFToken": get_csrf_token()
                }
            });
            const value = (await res.json()) as CommentResponse;

            if (res.status === 200) {
                next_url = value.next;

                return new JSONToTree({
                    json: value.results,
                    old_json: tree_branch
                }).build() as unknown as Comment[];
            } else if (res.status === 404) {
                // No comment exists
                // Return empty array
                if (!value?.detail?.toLowerCase().includes("not found")) {
                    throw new Error(`Data fetched from backend contains error`);
                }
                return new Array<Comment>();
            } else {
                throw new Error(await res.text());
            }
        },
        set_comments = async () => {
            get_comments(api_url)
                .then((res) => {
                    tree_branch = res;
                    loading_state = "loaded";
                })
                .catch((err: string) => {
                    loading_state = "error";
                    error = err as string;
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
            // This should not trigger tree loading thing;
            get_comments(api_url)
                .then((res) => {
                    tree_branch = res;
                })
                .catch((err: string) => {
                    loading_state = "error";
                    error = err as string;
                });
            comment_needs_update.set(false);
        }
    });
</script>

{#if loading_state === "loading"}
    <div class="flex flex-col md:gap-[1.5vw]">
        <CommentSkeleton />
    </div>
{:else if loading_state === "error"}
    {#if error}
        <ErrorSvelteComponent {error} />
    {/if}
{:else if loading_state === "loaded"}
    {#if !_.isEmpty(tree_branch)}
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
