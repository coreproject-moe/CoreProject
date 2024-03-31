<script lang="ts">
    export let item: Comment;
    export let submit_url = "";

    import Markdown from "$components/minor/Markdown/Index.svelte";
    import CommentBox from "$components/specific/CommentBox/Index.svelte";

    import type { Comment } from "$types/comment";
    import { FETCH_TIMEOUT } from "$constants/fetch";
    import * as _ from "lodash-es";
    import { onMount } from "svelte";
    import { user_authenticated } from "$stores/user";

    // Functions
    import { cn } from "$functions/classname";
    import { reverse } from "$functions/urls";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FormatDate } from "$functions/format_date";

    // import Images
    import DefaultAvatar from "../../../public/images/defaults/avatar.png";

    // Import icons
    import Arrow from "$icons/Arrow/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";
    import Share from "$icons/Share/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Expand from "$icons/Expand/Index.svelte";
    import { breakpoint } from "$stores/breakpoints";

    // Bindings
    let user_reaction: typeof item.user_reaction,
        ratio: typeof item.ratio,
        reply_shown = false,
        comment_reply_dialog_el: HTMLDialogElement,
        icon_mapping = ["upvote", "downvote"],
        reply_type: "box" | "modal" | "link" = "box";

    onMount(async () => {
        // user actions
        user_reaction = item["user_reaction"];
        ratio = item["ratio"];

        // reply type
        const is_small_screen = $breakpoint?.sm;
        const is_medium_screen = $breakpoint?.md;
        const is_large_screen = $breakpoint?.lg || $breakpoint?.xl || $breakpoint?.["2xl"];

        if (is_small_screen && item.depth > 1) reply_type = "modal";
        else if (is_medium_screen && item.depth > 5) reply_type = "link";
        else if (is_large_screen && item.depth > 4) reply_type = "link";
    });

    const apply_fetch_sideeffect = async (res: Response) => {
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
                    "X-CSRFToken": get_csrf_token()
                },
                signal: AbortSignal.timeout(FETCH_TIMEOUT),
                body: JSON.stringify({
                    reaction: reaction
                })
            });
            if (res.ok) {
                apply_fetch_sideeffect(res);
            }
        },
        delete_to_reaction_endpoint = async () => {
            const res = await fetch(reverse("comment-reaction-endpoint", item.pk), {
                method: "DELETE",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": get_csrf_token()
                }
            });
            if (res.ok) {
                apply_fetch_sideeffect(res);
            }
        };

    const handle_reaction_button_click = async (reaction: string /**upvote | downvote*/) => {
        if (!reaction && (reaction !== "upvote" || "downvote")) throw new Error("Sanity Error");

        if (user_reaction === `${reaction}d` /** ${upvote}d | ${downvote}d */) {
            await delete_to_reaction_endpoint();
        } else {
            await post_to_reaction_endpoint(reaction as "upvote" | "downvote");
        }
    };

    const handle_more_click = () => {
        console.log("CLicked");
    };
</script>

<div
    class="flex gap-2 duration-300 md:gap-[0.75vw]"
    class:md:pl-[2vw]={item.collapse}
    class:pl-7={item.collapse}
>
    <div
        class="relative flex items-center gap-4 md:gap-[1vw]"
        class:flex-col={!item.collapse}
        class:flex-row-reverse={item.collapse}
    >
        <a
            href="/user/"
            class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
        >
            <img
                alt=""
                src={item.deleted ? DefaultAvatar : item?.user?.avatar_url}
                class="h-full w-full shrink-0 rounded-full object-cover"
            />
        </a>
        <button
            on:click={() => (item.collapse = !item.collapse)}
            class="group flex h-full w-full cursor-pointer justify-center transition-transform active:scale-95"
            class:absolute={item.collapse}
            class:md:-left-[2.25vw]={item.collapse}
            class:-left-7={item.collapse}
        >
            {#if item.collapse}
                <Expand class="w-5 -rotate-45 text-neutral-content/75 transition-colors hover:text-warning md:w-[1.25vw]" />
            {:else}
                <div class="h-full w-[0.15rem] rounded-full bg-neutral transition-colors group-hover:bg-warning md:w-[0.15vw] group-hover:md:w-[0.2vw]" />
            {/if}
        </button>
    </div>
    <div class="flex flex-col items-start gap-1 md:gap-[0.25vw]">
        <div
            id={`comment-${item.pk}`}
            class="relative flex flex-col items-start gap-3 md:gap-[0.25vw]"
        >
            <a
                href="/user/"
                class="flex flex-col gap-1 text-xs leading-none md:gap-0 md:text-[1vw]"
            >
                <div class="flex items-center gap-2 md:gap-[0.5vw]">
                    {#if item.deleted}
                        <div class="md:text-[0.9vw]">[deleted]</div>
                    {:else}
                        <div class="text-white">
                            {`${item?.user?.first_name ?? ""} ${item?.user?.last_name ?? ""}`}
                        </div>
                        <div class="md:text-[0.75vw]">{item?.user?.username}</div>
                    {/if}
                </div>
                <div class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">
                    {new FormatDate(item.created_at).format_to_time_from_now}
                </div>
            </a>
            <div
                class="text-sm leading-snug text-accent md:text-[1vw] md:leading-[1.5vw]"
                class:hidden={item.collapse}
            >
                <Markdown markdown={item.text} />
            </div>
            <div
                class="flex items-center gap-3 md:gap-[0.75vw]"
                class:hidden={item.collapse}
            >
                <div class="flex items-center gap-1 md:gap-[0.35vw]">
                    {#each icon_mapping as item, index}
                        {@const is_first = index === 0}
                        {@const is_last = index === icon_mapping.length - 1}
                        <button
                            on:click|preventDefault={() => handle_reaction_button_click(item)}
                            class={cn("btn btn-secondary h-max min-h-full p-0", is_first && "order-1", is_last && "order-3", $user_authenticated || "btn-disabled")}
                        >
                            <div class:rotate-180={item === "downvote"}>
                                {#if user_reaction === `${item}d`}
                                    <Arrow
                                        variant="fill"
                                        class="w-4 text-warning md:w-[1.25vw]"
                                    />
                                {:else}
                                    <Arrow
                                        class="w-4 md:w-[1.25vw]"
                                        variant="outline"
                                    />
                                {/if}
                            </div>
                        </button>
                    {/each}
                    <span class="order-2 text-sm font-semibold text-accent md:text-[0.9vw]">{ratio}</span>
                </div>
                <button
                    class={cn(`btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw]`)}
                    on:click|preventDefault={() => {
                        switch(reply_type) {
                            case "box":
                                reply_shown = !reply_shown;
                                break;
                            case "modal":
                                comment_reply_dialog_el.showModal();
                                break;
                            case "link":
                                // navigate to specific comment url with open query
                                break;
                            default:
                                break;
                        };
                    }}
                >
                    <Chat class="w-4 md:w-[1vw]" />
                    <span>Replay</span>
                </button>
                <button
                    disabled
                    class="btn h-max min-h-full !bg-transparent p-0 text-xs md:gap-[0.35vw] md:text-[0.9vw]"
                >
                    <Share class="w-4 md:w-[1vw]" />
                    <span>Share</span>
                </button>
            </div>
        </div>

        {#if reply_shown && reply_type === "box"}
            <div class="md:mt-[1vw]">
                <CommentBox
                    on:submit={() => {
                        reply_shown = false;
                    }}
                    {submit_url}
                    path={item.path ?? ""}
                />
            </div>
        {/if}

        <!-- Render replies here -->
        {#if !_.isEmpty(item.child) && item.childrens !== 0 && !item.collapse}
            <div class="mt-5 flex flex-col gap-5 md:mt-[1.5vw] md:gap-[1.5vw]">
                {#each item.child as comment}
                    <svelte:self
                        {submit_url}
                        item={comment}
                    />
                {/each}
            </div>
        {/if}
    </div>
</div>

{#if _.isEmpty(item.child) && item.childrens !== 0 && !item.collapse}
    <div class="flex items-end ml-2 md:ml-[0.55vw] md:gap-[0.5vw]">
        <svg
            class="text-neutral w-7 md:w-[2vw]"
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

        <button
            on:click={handle_more_click}
            class="btn btn-secondary flex h-max min-h-max items-center p-0 gap-2 md:gap-[0.75vw]"
        >
            <div class="grid rotate-45 place-items-center rounded-full bg-neutral size-5 md:size-[1.5vw]">
                <Cross class="p-0 text-accent w-4 md:w-[1vw]" />
            </div>
            <span class="md:text-[1vw]">{item.childrens} More</span>
        </button>
    </div>
{/if}

{#if reply_type === "modal"}
    <dialog
        bind:this={comment_reply_dialog_el}
        class="modal modal-bottom"
    >
        <div class="modal-box overflow-x-hidden rounded-xl bg-secondary p-4">
            <span class="text-sm text-warning">Reply to:</span>
            <div class="mt-2 flex w-full gap-2">
                <a
                    href="/user/"
                    class="h-7 w-7 flex-shrink-0"
                >
                    <img
                        alt=""
                        src={item.deleted ? DefaultAvatar : item?.user?.avatar_url}
                        class="h-full w-full shrink-0 rounded-full object-cover"
                    />
                </a>
                <div class="flex w-full flex-col items-start gap-2">
                    <a
                        href="/user/"
                        class="flex flex-col gap-1 text-xs leading-none"
                    >
                        <div class="flex items-center gap-2">
                            {#if item.deleted}
                                <div>[deleted]</div>
                            {:else}
                                <div class="text-white">
                                    {`${item?.user?.first_name ?? ""} ${item?.user?.last_name ?? ""}`}
                                </div>
                                <div>{item?.user?.username}</div>
                            {/if}
                        </div>
                        <div class="text-surface-300">
                            {new FormatDate(item.created_at).format_to_time_from_now}
                        </div>
                    </a>
                    <div class="text-sm leading-snug text-accent">
                        <Markdown markdown={item.text} />
                    </div>
                </div>
            </div>
            <div class="mt-5 flex w-full">
                <CommentBox
                    on:submit={() => {
                        reply_shown = false;
                    }}
                    {submit_url}
                    path={item.path ?? ""}
                />
            </div>
        </div>
        <form
            method="dialog"
            class="modal-backdrop"
        >
            <button>close</button>
        </form>
    </dialog>
{/if}