<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import type { Comment } from "../../../types/comment";

    export let item: Comment;
    console.log(item);
</script>

<div>
    <div class="flex gap-3 md:gap-[0.75vw]">
        <div class="flex flex-col items-center md:gap-[1vw]">
            <a
                href="/user/"
                class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
            >
                <img
                    alt=""
                    src={item.user.avatar ?? item.user.avatar_url}
                    class="h-full w-full shrink-0 rounded-full object-cover"
                />
            </a>
            <button class="group flex h-full cursor-pointer justify-center transition-transform active:scale-95 md:w-full">
                <div class="h-full rounded-full bg-neutral transition-colors group-hover:bg-warning md:w-[0.15vw] group-hover:md:w-[0.2vw]" />
            </button>
        </div>
        <div class="flex flex-col items-start gap-1 md:gap-[0.25vw]">
            <a
                href="/user/"
                class="flex flex-col text-xs leading-none md:text-[1vw]"
            >
                <div class="flex items-center md:gap-[0.5vw]">
                    <div class="text-white">{`${item.user.first_name} ${item.user.last_name}`}</div>
                    <div class="md:text-[0.75vw]">{item.user.username}</div>
                </div>
                <div class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">{new FormatDate(item.created_at).format_to_time_from_now}</div>
            </a>
            <div class="text-sm leading-snug text-accent md:text-[1vw] md:leading-[1.5vw]">
                <Markdown markdown={item.text} />
            </div>
            <div class="flex items-center gap-3 md:gap-[0.75vw]">
                <button class="btn min-h-full !bg-transparent p-0 md:h-max">
                    <!-- {% include "icons/like.html" with class="w-3 text-surface-300 md:w-[1vw]" %} -->
                    <div class="text-xs md:text-[0.75vw]">106</div>
                </button>
                <button class="text-surface-50 btn min-h-full !bg-transparent p-0 text-xs uppercase md:h-max md:text-[0.8vw]">Replay</button>
            </div>

            <!-- Render replies here -->
            {#if item.children !== 0}
                <div class="flex flex-col md:mt-[1.5vw] md:gap-[1.5vw]">
                    {#each Object.entries(item) as [key, obj]}
                        <!-- Avoid user object -->
                        {#if typeof obj === "object" && key !== "user"}
                            <svelte:self item={obj} />
                        {/if}
                    {/each}
                </div>
            {/if}
        </div>
    </div>
</div>
