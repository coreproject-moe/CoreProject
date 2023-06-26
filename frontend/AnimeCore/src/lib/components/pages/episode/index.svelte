<script lang="ts">
    import ForumPosts from "$components/shared/forum_posts.svelte";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import Markdown from "$components/shared/markdown.svelte";
    import TextEditor from "$components/shared/text_editor.svelte";
    import { episode_comments } from "$data/mock/episode_comments";
    import { forum_posts } from "$data/mock/forum_posts";
    import { recommendations } from "$data/mock/recommendations";
    import { FormatDate } from "$functions/format_date";
    import Chevron from "$icons/chevron.svelte";
    import Cross from "$icons/cross.svelte";
    import Download from "$icons/download.svelte";
    import Filter from "$icons/filter.svelte";
    import Heart from "$icons/heart.svelte";
    import Next from "$icons/next.svelte";
    import Warning from "$icons/warning.svelte";
    import type { SvelteComponentDev } from "svelte/internal";
    import tippy from "tippy.js";

    export let episode_number: number | undefined;

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
                component: typeof SvelteComponentDev;
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
</script>

<episode-container class="block md:py-[2vw] md:pl-[1vw] md:pr-[3.75vw]">
    <episode-content class="grid grid-cols-12 md:gap-[5vw]">
        <video-player class="col-span-12 flex flex-col md:col-span-8 md:gap-[0.75vw]">
            <player class="h-64 w-full md:h-[35vw]">
                <!-- adding a image for now -->
                <ImageLoader
                    src="/images/DemonSlayer-episode.webp"
                    alt="Episode image"
                    class="h-full w-full rounded-none object-cover md:rounded-[0.5vw]"
                />
            </player>
            <video-player-options class="flex flex-col gap-2 p-5 md:flex-row md:items-center md:justify-between md:gap-0 md:p-0">
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
                            class="btn flex items-center p-0 text-xs leading-none md:text-[0.9vw]"
                            on:click={() => {
                                button_state_mapping[item[0]] = !button_state_mapping[item[0]];
                            }}
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
                                class="unstyled"
                                class:pointer-events-none={!link}
                                use:tippy={{
                                    content: `<div class='leading-none w-max whitespace-nowrap rounded-lg bg-surface-400 px-2 py-1 text-[0.65rem] text-surface-50 md:px-[0.75vw] md:py-[0.5vw] md:rounded-[0.35vw] md:text-[1vw]'>${text}</div>`,
                                    placement: "bottom",
                                    allowHTML: true,
                                    arrow: false,
                                    offset: [0, 17],
                                    appendTo: document.body,
                                    animation: "shift-away"
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
        <episode-info class="col-span-12 flex flex-col gap-10 p-5 md:col-span-4 md:justify-between md:gap-0 md:p-0">
            <episodes-container class="flex flex-col justify-between gap-3 md:gap-[1.5vw]">
                <header class="flex items-center justify-between">
                    <span class="font-semibold md:text-[1.35vw]">Episodes</span>
                    <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs font-semibold leading-none md:gap-[0.5vw] md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.5vw] md:text-[1vw]">
                        EPS: 1 - 20
                        <Chevron class="w-3 md:w-[1vw]" />
                    </button>
                </header>

                <episodes class="grid grid-cols-6 gap-2 md:gap-[0.75vw]">
                    {#each Array(30) as item, index}
                        {@const actual_index = index + 1}
                        {@const button_active = actual_index === episode_number}
                        <a
                            href="./{actual_index}"
                            class="{button_active ? 'bg-primary-500' : 'bg-surface-400'} unstyled btn rounded py-3 text-sm font-semibold leading-none md:rounded-[0.35vw] md:py-[0.75vw] md:text-[1.2vw]"
                        >
                            {actual_index}
                        </a>
                    {/each}
                </episodes>
            </episodes-container>
            <episode-detail class="relative flex items-end md:gap-[1.5vw]">
                <anime-banner class="relative h-72 w-full md:h-[13vw] md:w-[9vw] md:flex-shrink-0">
                    <ImageLoader
                        class="h-full w-full rounded-lg object-cover object-center md:rounded-[0.5vw]"
                        src="/images/DemonSlayer-bg.avif"
                        alt="Demon Slayer"
                    />
                    <overlay-gradient class="absolute inset-0 bg-gradient-to-t from-surface-900/75 to-surface-900/50 md:from-surface-900/50 md:to-surface-900/25" />
                </anime-banner>
                <episode-main-detail class="absolute bottom-0 flex flex-col p-5 leading-none md:static md:gap-[0.25vw] md:p-0">
                    <anime-title class="text-xl font-bold duration-300 ease-in-out scrollbar-none md:h-auto md:max-h-[1.75vw] md:overflow-hidden md:text-[1.5vw] md:leading-[1.75vw] md:text-surface-50 md:hover:max-h-[5vw] md:hover:overflow-y-scroll">Deamon Slayer</anime-title>

                    <span class="text-base text-surface-50 md:text-[1vw] md:leading-none">currently watching</span>
                    <span class="text-base font-semibold md:my-[0.5vw] md:text-[1.25vw] md:leading-none">Episode: {episode_number}</span>

                    <episode-name class="text-sm duration-300 ease-in-out scrollbar-none md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[1vw] md:leading-[1.25vw] md:text-surface-50 md:hover:max-h-[5vw] md:hover:overflow-y-scroll">A Connected Bond: Daybreak and First Light</episode-name>

                    <button
                        type="button"
                        class="btn mt-2 flex w-max items-center gap-0 rounded-md bg-primary-600 px-3 font-bold text-white md:mt-[1vw] md:h-[3vw] md:w-full md:gap-[0.5vw] md:rounded-[0.5vw] md:p-0"
                    >
                        <span class="text-sm md:text-[1.1vw]">More Details</span>
                        <Chevron class="w-5 -rotate-90 md:w-[1.25vw]" />
                    </button>
                </episode-main-detail>
            </episode-detail>
        </episode-info>
    </episode-content>

    <episode-media class="grid grid-cols-12 p-5 md:mt-[5vw] md:gap-[5vw] md:p-0">
        <comments-section class="col-span-12 flex flex-col md:col-span-7 md:gap-[0.75vw]">
            <span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-base font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]">Comments</span>

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

            <form class="mt-3 md:mt-[1vw]">
                <TextEditor />

                <warning-submit class="mt-4 flex justify-between gap-5 md:mt-[0.75vw] md:gap-[1vw]">
                    <warning class="flex items-center gap-3 md:gap-[0.625vw]">
                        <Warning class="w-10 md:w-[1.2vw]" />
                        <p class="unstyled text-[0.65rem] font-light leading-tight text-surface-300 md:text-[0.75vw] md:leading-[1.125vw]">
                            Please remember to follow our
                            <a
                                href="/"
                                class="unstyled text-surface-200 underline"
                            >
                                community guidelines
                            </a>
                            while commenting. Also please refrain from posting spoilers.
                        </p>
                    </warning>

                    <button class="btn btn-sm h-9 w-40 rounded bg-primary-500 text-sm font-semibold md:h-[2.2vw] md:w-[7vw] md:rounded-[0.375vw] md:text-[0.85vw]">Comment</button>
                </warning-submit>
            </form>

            <comments class="mt-10 flex flex-col gap-5 md:mt-[2vw] md:gap-[1.5vw]">
                {#each episode_comments as comment}
                    <comment class="flex gap-3 md:gap-[1vw]">
                        <a
                            href="/user/"
                            class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
                        >
                            <ImageLoader
                                src={comment.user.profile_pic}
                                alt="Avatar"
                                class="h-full w-full shrink-0 rounded-full object-cover"
                            />
                        </a>
                        <comment-details class="flex flex-col items-start gap-1 md:gap-0">
                            <a
                                href="/user/"
                                class="unstyled text-xs leading-none md:text-[1vw]"
                            >
                                <username>{comment.user.username}</username>
                                <comment-time class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">{new FormatDate(comment.date).format_to_time_from_now}</comment-time>
                            </a>

                            <Markdown
                                class="text-sm leading-snug text-surface-50 md:text-[1vw] md:leading-[1.5vw]"
                                markdown={comment.content}
                            />

                            <button class="btn mt-2 p-0 md:mt-0">
                                <Heart class="w-3 text-surface-300 md:w-[1vw]" />
                                <likes class="text-xs md:text-[0.75vw]">{comment.likes}</likes>
                            </button>
                        </comment-details>
                    </comment>
                {/each}
            </comments>
        </comments-section>
        <forum-recommendations class="col-span-12 mt-10 flex flex-col gap-5 md:col-span-5 md:mt-0 md:gap-[2vw]">
            <forum-posts>
                <span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-base font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]">Forum posts</span>

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
                    <button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                        Load more
                        <Chevron
                            color="surface-50"
                            class="w-4 md:w-[1vw]"
                        />
                    </button>
                </load-more>
            </forum-posts>

            <recommendations-container>
                <span class="font-semibold md:text-[1.35vw]">Recommendations</span>

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
                                <anime-title class="text-sm font-semibold leading-snug duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[1vw] md:leading-[1.25vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll">
                                    {anime.name}
                                </anime-title>
                                <anime-japanese-name class="text-xs leading-none md:text-[0.9vw]">
                                    {anime.japanese_name}
                                </anime-japanese-name>
                                <anime-episodes-count class="text-xs leading-none text-surface-50 duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[0.9vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll">
                                    Episodes: <b>{anime.episodes_count}</b>
                                </anime-episodes-count>
                            </anime-details>

                            <gradient-overlay class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/80 to-surface-900/25" />
                        </a>
                    {/each}
                </container>

                <load-more class=" mt-3 flex w-full justify-center md:mt-[1vw]">
                    <button class="btn btn-sm h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
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
