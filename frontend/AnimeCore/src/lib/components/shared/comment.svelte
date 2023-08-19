<script lang="ts">
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import Markdown from "$components/shared/markdown.svelte";
    import { FormatDate } from "$functions/format_date";
    import Chevron from "$icons/chevron.svelte";
    import Heart from "$icons/heart.svelte";
    import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";

    export let comment_user_profile_pic: string;
    export let comment_username: string;
    export let comment_date: string;
    export let comment_content: string;
    export let comment_likes: number;
    export let comment_replies: Array<{
        user: {
            username: string;
            profile_pic: string;
        };
        date: string;
        content: string;
        likes: number;
    }>;
    export let open: boolean;
</script>

<comment class="flex gap-3 md:gap-[1vw]">
    <a
        href="/user/"
        class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
    >
        <ImageLoader
            src={comment_user_profile_pic}
            alt="Avatar"
            class="h-full w-full shrink-0 rounded-full object-cover"
        />
    </a>
    <comment-details class="flex flex-col items-start gap-1 md:gap-0">
        <a
            href="/user/"
            class="text-xs leading-none md:text-[1vw]"
        >
            <username>{comment_username}</username>
            <comment-time class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">{new FormatDate(comment_date).format_to_time_from_now}</comment-time>
        </a>

        <Markdown
            class="text-sm leading-snug text-surface-50 md:text-[1vw] md:leading-[1.5vw]"
            markdown={comment_content}
        />

        <options class="mt-2 flex items-center gap-3 md:mt-[0.75vw] md:gap-[0.75vw]">
            <button class="btn p-0">
                <Heart class="w-3 text-surface-300 md:w-[1vw]" />
                <likes class="text-xs md:text-[0.75vw]">{comment_likes}</likes>
            </button>
            <button class="btn p-0 text-xs uppercase text-surface-50 md:text-[0.8vw]">Replay</button>
        </options>

        {#if Array.isArray(comment_replies) && comment_replies.length}
            <replies-section class="md:mt-[0.35vw]">
                <Accordion
                    padding="p-0"
                    hover="bg-transparent"
                >
                    <AccordionItem
                        {open}
                        regionPanel="text-surface md:text-[1vw] md:leading-[1.35vw] items-start justify-start"
                        regionControl="text-sm text-warning-400 font-semibold md:text-[0.9vw] md:leading-[1vw] pb-2 md:pb-[0.75vw] w-max"
                        regionCaret="md:w-[0.75vw] items-start justify-start"
                    >
                        <svelte:fragment slot="summary">Replies</svelte:fragment>
                        <svelte:fragment slot="content">
                            {#each comment_replies as reply}
                                <reply class="flex gap-3 md:gap-[1vw]">
                                    <a
                                        href="/user/"
                                        class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
                                    >
                                        <ImageLoader
                                            src={reply.user.profile_pic}
                                            alt="Avatar"
                                            class="h-full w-full shrink-0 rounded-full object-cover"
                                        />
                                    </a>
                                    <reply-details class="flex flex-col items-start gap-1 md:gap-0">
                                        <a
                                            href="/user/"
                                            class="text-xs leading-none md:text-[1vw]"
                                        >
                                            <username>{reply.user.username}</username>
                                            <reply-time class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">{new FormatDate(reply.date).format_to_time_from_now}</reply-time>
                                        </a>

                                        <Markdown
                                            class="text-sm leading-snug text-surface-50 md:text-[1vw] md:leading-[1.5vw]"
                                            markdown={reply.content}
                                        />

                                        <options class="mt-2 flex items-center md:mt-[0.75vw] md:gap-[0.75vw]">
                                            <button class="btn p-0">
                                                <Heart class="w-3 text-surface-300 md:w-[1vw]" />
                                                <likes class="text-xs md:text-[0.75vw]">{reply.likes}</likes>
                                            </button>
                                        </options>
                                    </reply-details>
                                </reply>
                            {/each}
                        </svelte:fragment>
                    </AccordionItem>
                </Accordion>
            </replies-section>
        {/if}
    </comment-details>
</comment>
