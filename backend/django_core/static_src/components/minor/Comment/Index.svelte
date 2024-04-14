<script lang="ts">
    import { JSONToTree } from "./json_to_tree";
    import CommentBlock from "./CommentBlock.svelte";
    import CommentSkeleton from "$components/minor/Comment/Skeleton.svelte";
    import Empty from "./Empty.svelte";
    import ErrorSvelteComponent from "./Error.svelte";
    import type { Comment, CommentResponse } from "$types/comment";
    import { comment_needs_update } from "./store";
    import { onDestroy, onMount } from "svelte";
    import IntersectionOberser from "svelte-intersection-observer";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";

    export let api_url: string;
    export let submit_url = "";

    // This is set from backend
    let next_url: string | null;

    let loading_state: "loading" | "error" | "loaded" = "loading",
        error: string | null = null;

    let tree_branch: Comment[] = new Array<Comment>();

    let last_element: HTMLElement;

    let url_params = new URLSearchParams(window.location.search);
    let root_path = url_params.get("comment");

    onMount(() => {
        if (url_params.has("comment")) {
            api_url = `/api/v2/comments/?path=${root_path}`;
        }

        set_comments();
    });

    onDestroy(() => {
        // Clean up
        tree_branch = new Array<Comment>();
    });

    const get_comments = async (url: string) => {
            const res = await fetch(url, {
                method: "GET",
                headers: {
                    "X-CSRFToken": get_csrf_token()
                },
                signal: AbortSignal.timeout(FETCH_TIMEOUT)
            });
            const value = (await res.json()) as CommentResponse;

            switch (res.status) {
                case 200:
                    next_url = value.next;
                    const js_object = {
                        json: value.results
                    };

                    if (tree_branch.length !== 0) Object.assign(js_object, { old_json: tree_branch });
                    if (url_params.has("comment")) Object.assign(js_object, { root_path: root_path });

                    return new JSONToTree(js_object).build() as unknown as Comment[];

                case 404:
                    // No comment exists
                    // Return empty array
                    if (!value?.detail?.toLowerCase().includes("not found")) {
                        throw new Error(`Data fetched from backend contains error`);
                    }
                    return new Array<Comment>();

                default:
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
    {#if tree_branch.length !== 0}
        <div class="flex flex-col gap-5 md:gap-[1.5vw]">
            {#each tree_branch as branch}
                <CommentBlock
                    item={branch}
                    {submit_url}
                />
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
