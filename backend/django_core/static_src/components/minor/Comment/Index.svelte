<script lang="ts">
    import { JSONToTree } from "$functions/json_to_tree";
    import CommetBlock from "./CommetBlock.svelte";

    export let api_url: string;

    type CommentResult = {
        created_at: string;
        user: {
            username: string;
            first_name: string;
            last_name: string;
            avatar: null | string;
            avatar_url: string;
        };
        text: string;
        path: string;
        children: number;
    }

    interface Comment {
        count: number;
        next: null | number;
        previous: null | number;
        results: CommentResult[];
    }
    async function get_comments() {
        const res = await fetch(api_url, {
            method: "GET",
            headers: {
                "X-CSRFToken": window.csrfmiddlewaretoken
            }
        });
        const value = (await res.json()) as Comment;
        const formated_json = new JSONToTree(value.results).to_tree() as CommentResult[];

        // clear results
        value.results.length = 0;
        if (typeof formated_json === "object" && formated_json !== null) {
            Object.values(formated_json).forEach((item) => {
                value.results.push(item);
            })
        }

        if (res.ok) {
            return value;
        } else {
            throw new Error(await res.text());
        }
    }
</script>

{#await get_comments()}
    Loading...
{:then comment}
    <div class="flex flex-col md:gap-[1.5vw]">
        {#each comment.results as item}
            <CommetBlock {item} />
        {/each}
    </div>
{/await}
