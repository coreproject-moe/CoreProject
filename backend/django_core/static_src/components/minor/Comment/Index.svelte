<script lang="ts">
    export let api_url: string;

    interface Comment {
        count: number;
        next: null | number;
        previous: null | number;
        results: {
            user: string;
            text: string;
            path: string;
        }[];
    }

    async function get_comments() {
        const res = await fetch(api_url, {
            method: "GET",
            headers: {
                "X-CSRFToken": window.csrfmiddlewaretoken
            }
        });
        const value = (await res.json()) as Comment;

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
    {#each comment.results as item}
        <div class="flex gap-3 md:gap-[1vw]">
            <a
                href="/user/"
                class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
            >
                <img
                    alt=""
                    src="https://avatars.githubusercontent.com/u/114811070?s=40&v=4"
                    class="h-full w-full shrink-0 rounded-full object-cover"
                />
            </a>
            <div class="flex flex-col items-start gap-1 md:gap-0">
                <a
                    href="/user/"
                    class="flex flex-col text-xs leading-none md:text-[1vw]"
                >
                    <div class="flex items-center md:gap-[0.5vw]">
                        <div class="text-white">Tokitouq</div>
                        <div class="md:text-[0.75vw]">{item.user}</div>
                    </div>
                    <div class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">10 months ago</div>
                </a>
                <div class="text-sm leading-snug text-accent md:text-[1vw] md:leading-[1.5vw]">{item.text}</div>
                <div class="mt-2 flex items-center gap-3 md:mt-[0.5vw] md:gap-[0.75vw]">
                    <button class="btn !bg-transparent p-0">
                        <!-- {% include "icons/like.html" with class="w-3 text-surface-300 md:w-[1vw]" %} -->
                        <likes class="text-xs md:text-[0.75vw]">106</likes>
                    </button>
                    <button class="text-surface-50 btn !bg-transparent p-0 text-xs uppercase md:text-[0.8vw]">Replay</button>
                </div>
            </div>
        </div>
    {/each}
{/await}
