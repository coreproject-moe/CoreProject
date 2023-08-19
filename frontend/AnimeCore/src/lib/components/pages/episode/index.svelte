<script lang="ts">
    import Comment from "$components/shared/comment.svelte";
    import ForumPosts from "$components/shared/forum_posts.svelte";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import TextEditor from "$components/shared/text_editor.svelte";
    import { episode_comments } from "$data/mock/episode_comments";
    import { forum_posts } from "$data/mock/forum_posts";
    import { recommendations } from "$data/mock/recommendations";
    import Chevron from "$icons/chevron.svelte";
    import Cross from "$icons/cross.svelte";
    import Download from "$icons/download.svelte";
    import Filter from "$icons/filter.svelte";
    import Next from "$icons/next.svelte";
    import PlayCircle from "$icons/play_circle.svelte";
    import Share from "$icons/share.svelte";
    import Warning from "$icons/warning.svelte";
    import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";
    import type { SvelteComponent } from "svelte";
    import { blur } from "svelte/transition";
    import tippy from "tippy.js";

    /* Comment section logics */
    let comment_body: string;

    /* Video player options */
    const toggle_lights = () => {
        button_state_mapping.lights = !button_state_mapping.lights;
    };

    const button_state_mapping: { [key: string]: boolean } = {
        lights: false
    };

    const video_player_mapping: {
        preferences: {
            [key: string]: {
                text: string;
            };
        };
        options: {
            [key: string]: {
                component: typeof SvelteComponent<{}>;
                link: string;
                class: string;
                text: string;
            };
        };
    } = {
        preferences: {
            lights: {
                text: "Lights"
            }
        },
        options: {
            download: {
                component: Download,
                link: "./",
                class: "w-4 md:w-[1.4vw]",
                text: "Download"
            },
            prev: {
                component: Next,
                link: "./",
                class: "w-4 md:w-[1.4vw] rotate-180",
                text: "Previous Episode"
            },
            next: {
                component: Next,
                link: "./",
                class: "w-4 md:w-[1.4vw]",
                text: "Next Episode"
            }
        }
    };

    /** Episode Contents */
    export let episode_number: number;
    export let episode_details = `The autumn he was twelve, piano prodigy Kousei Arima suddenly found himself unable to play the piano after his mother's death. Ever since then, it's like he's been frozen in time. His childhood friend, Tsubaki Sawabe, watches over him with concern; one day, she invites him on a double date. Kousei's other childhood friend, Ryouta Watari, is being introduced to a certain girl. Kousei reluctantly heads over to the rendezvous spot. There, he sees a girl playing a melodica. This girl, who allegedly has a crush on Watari, is Kaori Miyazono. And she turns out to be a violinist!`;
    export let episode_name = `Monotone/Colorful`;
</script>

{#if button_state_mapping.lights}
    <lights_overlay
        transition:blur={{ duration: 300 }}
        role="presentation"
        class="absolute inset-0 z-20 bg-black/95"
        on:mousedown={toggle_lights}
    />
{/if}

<episode-container class="mt-16 flex flex-col md:mt-0 md:gap-[3.5vw] md:py-[2vw] md:pl-[1vw] md:pr-[3.75vw]">
    <episode-content class="grid grid-cols-12 md:gap-[5vw]">
        <video-player class="col-span-12 flex flex-col md:col-span-8 md:gap-[0.75vw]">
            <player class="relative h-64 w-full md:z-30 md:h-[35vw]">
                <!-- adding a image for now -->
                <ImageLoader
                    src="/images/DemonSlayer-episode.webp"
                    alt="Episode image"
                    class="h-full w-full rounded-none object-cover md:rounded-[0.5vw] "
                />
            </player>
            <video-player-options class="flex flex-col gap-2 px-5 md:flex-row md:items-center md:justify-between md:gap-0 md:p-0">
                <preferences class="flex gap-2 md:items-center md:gap-[1vw]">
                    <sub-dub class="hidden items-center gap-[0.75vw] md:flex">
                        <span class="text-[1vw] font-semibold uppercase">sub/dub:</span>
                        <button class="btn flex items-center gap-[0.5vw] rounded-[0.35vw] bg-surface-400 px-[0.75vw] py-[0.5vw] text-[1vw] leading-none">
                            Vidstreaming (sub)
                            <Chevron class="w-[1vw]" />
                        </button>
                    </sub-dub>

                    {#each Object.entries(video_player_mapping.preferences) as item}
                        {@const text = item[1].text}
                        {@const enabled = button_state_mapping[item[0]]}

                        <button
                            class="btn hidden items-center p-0 text-xs leading-none md:flex md:text-[0.9vw]"
                            on:click={toggle_lights}
                        >
                            <span>{text}:</span>
                            {#if enabled}
                                <status class="font-semibold text-warning-500">On</status>
                            {:else}
                                <status class="font-semibold text-primary-300">Off</status>
                            {/if}
                        </button>
                    {/each}
                </preferences>

                <div class="flex w-full items-center justify-between md:w-auto">
                    <sub-dub class="flex items-center gap-2 md:hidden">
                        <span class="text-xs font-semibold uppercase">sub/dub:</span>
                        <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs leading-none">
                            Vidstreaming (sub)
                            <Chevron class="w-3" />
                        </button>
                    </sub-dub>

                    <video-options class="flex items-center gap-3 md:gap-[0.75vw]">
                        {#each Object.entries(video_player_mapping.options) as item}
                            {@const component = item[1].component}
                            {@const link = item[1].link}
                            {@const klass = item[1].class}
                            {@const text = item[1].text}

                            <a
                                href={link}
                                class:pointer-events-none={!link}
                                use:tippy={{
                                    content: `<div class='leading-none w-max whitespace-nowrap rounded-lg bg-surface-400 px-2 py-1 text-[0.65rem] text-surface-50 md:px-[0.75vw] md:py-[0.5vw] md:rounded-[0.35vw] md:text-[1vw]'>${text}</div>`,
                                    placement: "bottom",
                                    allowHTML: true,
                                    arrow: false,
                                    offset: [0, 17],
                                    appendTo: document.body,
                                    animation: "shift-away",
                                    theme: "elaine"
                                }}
                            >
                                <svelte:component
                                    this={component}
                                    class={klass}
                                />
                            </a>
                        {/each}
                    </video-options>
                </div>
            </video-player-options>
        </video-player>
        <episode-info class="col-span-12 flex flex-col gap-3 p-5 md:col-span-4 md:gap-[1.5vw] md:p-0">
            <header class="flex items-center justify-between">
                <span class="text-lg font-semibold md:text-[1.35vw]">Episodes</span>
                <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs font-semibold leading-none md:gap-[0.5vw] md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.5vw] md:text-[1vw]">
                    EPS: 1 - 60
                    <Chevron class="w-3 md:w-[1vw]" />
                </button>
            </header>

            <episodes class="grid grid-cols-7 gap-2 md:grid-cols-6 md:gap-[0.75vw]">
                {#each Array(60) as item, index}
                    {@const actual_index = index + 1}
                    {@const button_active = actual_index === episode_number}
                    <a
                        href="./{actual_index}"
                        class="{button_active ? 'bg-primary-500' : 'bg-surface-400'} btn rounded py-3 text-sm font-semibold leading-none md:rounded-[0.35vw] md:py-[0.75vw] md:text-[1.2vw]"
                    >
                        {actual_index}
                    </a>
                {/each}
            </episodes>
        </episode-info>
    </episode-content>

    <episode-details class="grid grid-cols-12 gap-5 p-5 md:gap-[5vw] md:p-0">
        <episode-info class="col-span-12 flex flex-col gap-2 md:col-span-8 md:gap-[1vw]">
            <anime-name-options class="flex items-center justify-between">
                <div>
                    <a
                        href="/mal/1"
                        class="flex flex-col gap-1 text-lg leading-none md:gap-[0.25vw] md:text-[1.1vw]"
                    >
                        <span class="font-semibold uppercase">Demon Slayer S1</span>
                        <span class="text-base text-surface-50 md:text-[1vw]">Kimetsu no yaiba</span>
                    </a>
                </div>
                <options>
                    <button class="btn bg-transparent p-0">
                        <Share class="md:w-[1.25vw]" />
                    </button>
                </options>
            </anime-name-options>
            <Accordion
                padding="p-0"
                hover="bg-transparent"
                duration={300}
            >
                <AccordionItem
                    open
                    regionPanel="text-surface-50 text-sm leading-snug md:text-[1vw] md:leading-[1.35vw]"
                    regionControl="text-base text-warning-400 font-semibold md:text-[1.25vw] md:leading-[1vw] md:pb-[1vw]"
                    regionCaret="md:w-[1vw]"
                >
                    <svelte:fragment slot="lead">EP{episode_number}</svelte:fragment>
                    <svelte:fragment slot="summary">{episode_name}</svelte:fragment>
                    <svelte:fragment slot="content">
                        {episode_details}
                    </svelte:fragment>
                </AccordionItem>
            </Accordion>
            <a
                href="/mal/1"
                class="btn w-max rounded-md bg-primary-500 py-3 text-sm font-semibold leading-none md:rounded-[0.5vw] md:py-[0.9vw] md:text-[1vw]"
            >
                <span>View detail</span>
                <Chevron class="w-3 -rotate-90 md:w-[1vw]" />
            </a>
        </episode-info>
        <next-episode class="col-span-4 hidden flex-col md:flex">
            <span class="font-semibold uppercase md:text-[1.1vw]">next episode</span>
            <a
                href="./{episode_number + 1}"
                class="flex md:mt-[0.75vw] md:gap-[1vw]"
            >
                <episode-cover class="relative">
                    <ImageLoader
                        src="/images/episodes/hyouka/Hyouka-ep-6.avif"
                        class="md:w-[12vw] md:rounded-[0.25vw]"
                    />
                    <overlay class="absolute inset-0 flex items-center justify-center bg-surface-900/40">
                        <play class="rounded-full bg-surface-900/50 md:p-[1vw]">
                            <PlayCircle class="md:w-[1.25vw]" />
                        </play>
                    </overlay>
                </episode-cover>
                <episode-info class="flex flex-col justify-between leading-none md:py-[1vw]">
                    <div class="flex flex-col md:gap-[0.5vw]">
                        <span class="text-warning-200 md:text-[1.1vw]">Finally they met</span>
                        <span class="md:text-[1vw]">Episode - {episode_number + 1}</span>
                    </div>

                    <span class="text-surface-50 md:text-[1vw]">23 min</span>
                </episode-info>
            </a>
        </next-episode>
    </episode-details>

    <episode-media class="grid grid-cols-12 p-5 md:gap-[5vw] md:p-0">
        <comments-section class="col-span-12 flex flex-col md:col-span-7 md:gap-[0.75vw]">
            <span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-lg font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]">Comments</span>

            <comments-info class="mt-2 flex items-center justify-between md:hidden">
                <p class="flex items-center gap-1">
                    <span class="text-base font-bold leading-none">69</span>
                    <span class="text-sm font-semibold text-surface-50">comments</span>
                </p>

                <button
                    class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                    aria-label="Filter"
                >
                    <Filter
                        class="w-3 md:w-[1vw]"
                        color="lightgray"
                    />
                </button>
            </comments-info>

            <comment-form class="flex flex-col md:flex-row md:gap-[1vw]">
                <a
                    href="/user/"
                    class="hidden h-7 w-7 flex-shrink-0 md:mt-[0.5vw] md:flex md:h-[2vw] md:w-[2vw]"
                >
                    <ImageLoader
                        src="/images/DemonSlayer-bg.avif"
                        alt="Avatar"
                        class="h-full w-full shrink-0 rounded-full object-cover"
                    />
                </a>
                <form class="mt-3 flex flex-col gap-3 md:mt-[1vw] md:gap-[0.75vw]">
                    <span class="leading-none text-surface-50 md:text-[1vw]">
                        Comment as <strong>Tokito</strong>
                    </span>
                    <TextEditor textarea_value={comment_body} />
                    <warning-submit class="flex justify-between gap-5 md:gap-[1vw]">
                        <warning class="flex items-center gap-3 md:gap-[0.625vw]">
                            <Warning class="w-10 md:w-[1.2vw]" />
                            <p class="text-[0.65rem] font-light leading-tight text-surface-300 md:text-[0.75vw] md:leading-[1.125vw]">
                                Please remember to follow our
                                <a
                                    href="/"
                                    class="text-surface-200 underline"
                                >
                                    community guidelines
                                </a>
                                while commenting. Also please refrain from posting spoilers.
                            </p>
                        </warning>

                        <button class="btn btn-sm h-9 w-40 rounded bg-primary-500 text-sm font-semibold md:h-[2.2vw] md:w-[6vw] md:rounded-[0.375vw] md:text-[0.85vw]">Comment</button>
                    </warning-submit>
                </form>
            </comment-form>

            <comments class="mt-10 flex flex-col gap-5 md:mt-[2vw] md:gap-[1.5vw]">
                {#each episode_comments as comment, index}
                    <Comment
                        comment_user_profile_pic={comment.user.profile_pic}
                        comment_username={comment.user.username}
                        comment_date={comment.date}
                        comment_content={comment.content}
                        comment_likes={comment.likes}
                        comment_replies={comment.replies}
                        open={index === 0}
                    />
                {/each}
            </comments>
        </comments-section>
        <forum-recommendations class="col-span-12 mt-10 flex flex-col gap-5 md:col-span-5 md:mt-0 md:gap-[2vw]">
            <forum-posts>
                <span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-lg font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]">Forum posts</span>

                <forum-options class="mt-3 flex items-center justify-between md:mt-[1.25vw]">
                    <posts-count class="flex items-center gap-1 md:hidden">
                        <span class="text-base font-bold leading-none">106</span>
                        <span class="text-sm font-semibold text-surface-50">posts</span>
                    </posts-count>

                    <forum-buttons class="flex items-center gap-2 md:w-full md:justify-between">
                        <button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                            <Cross
                                color="surface-50"
                                class="w-4 rotate-45 md:w-[1vw]"
                            />
                            Create New
                        </button>

                        <button
                            class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                            aria-label="Filter"
                        >
                            <Filter
                                class="w-3 md:w-[1vw]"
                                color="lightgray"
                            />
                        </button>
                    </forum-buttons>
                </forum-options>

                <posts class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1vw] md:flex md:gap-[1vw]">
                    {#each forum_posts as post}
                        <ForumPosts
                            post_title={post.title}
                            post_banner={post.banner}
                            post_description={post.description}
                            author={post.author}
                            posted_on_date={post.posted_on}
                            link={post.link}
                            responses={Number(post.responses)}
                        />
                    {/each}
                </posts>

                <load-more class="mt-3 flex w-full justify-center md:mt-[1vw]">
                    <button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-3 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                        Load more
                        <Chevron
                            color="surface-50"
                            class="w-4 md:w-[1vw]"
                        />
                    </button>
                </load-more>
            </forum-posts>

            <recommendations-container>
                <span class="text-lg font-semibold md:text-[1.35vw]">Recommendations</span>

                <container class="mt-3 grid grid-cols-3 gap-4 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1vw]">
                    {#each recommendations as anime}
                        <a
                            href="/myanimelist/{anime.mal_id}"
                            class="card relative col-span-1 h-44 w-full overflow-hidden md:h-[15vw] md:rounded-[0.75vw]"
                        >
                            <ImageLoader
                                src={anime.cover}
                                class="h-full w-full object-cover object-center"
                            />

                            <anime-details class="absolute bottom-3 z-10 flex w-full flex-col items-center gap-1 px-[0.5vw] text-center md:bottom-[1vw] md:gap-[0.25vw]">
                                <anime-title class="text-sm font-semibold leading-snug duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[1vw] md:leading-[1.25vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">
                                    {anime.name}
                                </anime-title>
                                <anime-japanese-name class="text-xs leading-none md:text-[0.9vw]">
                                    {anime.japanese_name}
                                </anime-japanese-name>
                                <anime-episodes-count class="text-xs leading-none text-surface-50 duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[0.9vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">
                                    Episodes: <b>{anime.episodes_count}</b>
                                </anime-episodes-count>
                            </anime-details>

                            <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/80 to-surface-900/25" />
                        </a>
                    {/each}
                </container>

                <load-more class="mt-3 flex w-full justify-center md:mt-[1vw]">
                    <button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-3 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                        Load more
                        <Chevron
                            color="surface-50"
                            class="w-4 md:w-[1vw]"
                        />
                    </button>
                </load-more>
            </recommendations-container>
        </forum-recommendations>
    </episode-media>
</episode-container>
