<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import type { Comment } from "../../../types/comment";
    import CommentBox from "$components/specific/CommentBox/Index.svelte";

    export let item: Comment;
    // Import icons
    import Arrow from "$icons/Arrow/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";
    import Share from "$icons/Share/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import { reverse } from "$functions/urls";
    import { onMount } from "svelte";

    // Bindings
    let user_reaction: typeof item.user_reaction,
        ratio: typeof item.ratio,
        reply_shown = false,
        is_comment_highlighted = false;

    onMount(() => {
        const url_params = new URLSearchParams(window.location.search);
        if (url_params.has("comment")) {
            const comment_id = Number(url_params.get("comment")!);
            if (comment_id === item.pk) {
                is_comment_highlighted = true;
                document.querySelector(`#comment-${comment_id}`)?.scrollIntoView({ behavior: "smooth", block: "center" });
            }
        }
        // user actions
        user_reaction = item.user_reaction;
        ratio = item.ratio;
    });

    const fetch_sideeffect = async (res: Response) => {
            const json = await res.json();
            user_reaction = json.user_reaction;
            ratio = json.ratio;
        },
        post_to_reaction_endpoint = async (reaction: "upvote" | "downvote") => {
            const res = await fetch(reverse("comment-reaction-endpoint", item.pk), {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": window.csrfmiddlewaretoken
                },
                body: JSON.stringify({
                    reaction: reaction
                })
            });
            if (res.ok) {
                fetch_sideeffect(res);
            }
        },
        delete_to_reaction_endpoint = async () => {
            const res = await fetch(reverse("comment-reaction-endpoint", item.pk), {
                method: "DELETE",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": window.csrfmiddlewaretoken
                }
            });
            if (res.ok) {
                fetch_sideeffect(res);
            }
        };
</script>

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
        <div
            id={`comment-${item.pk}`}
            class="relative flex flex-col items-start gap-1 md:gap-[0.25vw]"
        >
            <div
                hidden={!is_comment_highlighted}
                class="-z-1 pointer-events-none absolute inset-0 bg-neutral/25 md:-m-[1vw] md:-mb-[0.75vw] md:rounded-[0.5vw]"
            ></div>
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
                <div class="flex items-center md:gap-[0.35vw]">
                    <button
                        on:click|preventDefault={async () => {
                            if (user_reaction === "upvoted") {
                                await delete_to_reaction_endpoint();
                            } else {
                                await post_to_reaction_endpoint("upvote");
                            }
                        }}
                        class="btn btn-secondary min-h-full p-0 md:h-max"
                    >
                        {#if user_reaction === "upvoted"}
                            <Arrow
                                variant="fill"
                                class="text-warning md:w-[1.25vw]"
                            />
                        {:else}
                            <Arrow
                                class="md:w-[1.25vw]"
                                variant="outline"
                            />
                        {/if}
                    </button>
                    <span class="font-semibold text-accent md:text-[0.9vw]">{ratio}</span>
                    <button
                        class="btn btn-secondary min-h-full p-0 md:h-max"
                        on:click={async () => {
                            if (user_reaction === "downvoted") {
                                await delete_to_reaction_endpoint();
                            } else {
                                await post_to_reaction_endpoint("downvote");
                            }
                        }}
                    >
                        {#if user_reaction === "downvoted"}
                            <Arrow
                                class="rotate-180 text-warning md:w-[1.25vw]"
                                variant="fill"
                            />
                        {:else}
                            <Arrow
                                class="rotate-180 md:w-[1.25vw]"
                                variant="outline"
                            />
                        {/if}
                    </button>
                </div>
                <button
                    class="btn min-h-full !bg-transparent p-0 text-xs md:h-max md:gap-[0.35vw] md:text-[0.9vw]"
                    on:click|preventDefault={() => (reply_shown = !reply_shown)}
                >
                    <Chat class="md:w-[1vw]" />
                    <span>Replay</span>
                </button>
                <button class="btn min-h-full !bg-transparent p-0 text-xs md:h-max md:gap-[0.35vw] md:text-[0.9vw]">
                    <Share class="md:w-[1vw]" />
                    <span>Share</span>
                </button>

                <!-- <div class="dropdown">
                <div
                    tabindex="0"
                    role="button"
                    class="btn btn-secondary h-max min-h-max p-0 md:gap-[0.15vw]"
                >
                    {#each Array(3).fill(0) as _}
                        <Dot class="md:w-[0.2vw]" />
                    {/each}
                </div>
                <ul class="dropdown-content z-10 overflow-hidden bg-neutral md:rounded-[0.25vw]">
                    <li class="cursor-pointer transition-colors hover:bg-primary hover:text-accent md:px-[1vw] md:py-[0.5vw] md:text-[1vw]">
                        <span>Report</span>
                    </li>
                </ul>
            </div> -->
            </div>
        </div>
        {#if reply_shown}
            <div class="md:mt-[1vw]">
                <CommentBox />
            </div>
        {/if}

        <!-- Render replies here -->
        {#if item.childrens !== 0}
            <div class="flex flex-col md:mt-[1.5vw] md:gap-[1.5vw]">
                {#each item.child as comment, index}
                    {#if index === 0}
                        <svelte:self item={comment} />
                    {/if}
                {/each}
            </div>
        {/if}
    </div>
</div>

{#if item.childrens > 1}
    <div class="flex items-end md:ml-[0.55vw] md:gap-[0.5vw]">
        <svg
            class="text-neutral md:w-[2vw]"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 15 15"
        >
            <path
                fill="currentColor"
                fill-rule="evenodd"
                d="M9.877 12H11.5a.5.5 0 0 0 0-1H9.9c-1.128 0-1.945 0-2.586-.053c-.637-.052-1.057-.152-1.403-.328a3.5 3.5 0 0 1-1.53-1.53c-.176-.346-.276-.766-.328-1.403C4 7.045 4 6.228 4 5.1V3.5a.5.5 0 0 0-1 0v1.623c0 1.1 0 1.958.056 2.645c.057.698.175 1.265.434 1.775a4.5 4.5 0 0 0 1.967 1.967c.51.26 1.077.377 1.775.434C7.92 12 8.776 12 9.877 12Z"
                clip-rule="evenodd"
            />
        </svg>

        <button class="btn btn-secondary flex h-max min-h-max items-center p-0 md:gap-[0.75vw]">
            <div class="grid rotate-45 place-items-center rounded-full bg-neutral md:h-[1.5vw] md:w-[1.5vw]">
                <Cross class="p-0 text-accent md:w-[1vw]" />
            </div>
            <span class="md:text-[1vw]">{item.child.length - 1} More</span>
        </button>
    </div>
{/if}
