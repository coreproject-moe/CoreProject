<script lang="ts">
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import TextEditor from "$components/shared/text_editor.svelte";
    import { forum_posts } from "$data/mock/forum_posts";
    import { FormatDate } from "$functions/format_date";
    import { FormatTime } from "$functions/format_time";
    import { round_to_nearest_zero_point_five } from "$functions/math";
    import Chevron from "$icons/chevron.svelte";
    import Circle from "$icons/circle.svelte";
    import Cross from "$icons/cross.svelte";
    import Download from "$icons/download.svelte";
    import Edit from "$icons/edit.svelte";
    import ExternalLink from "$icons/external_link.svelte";
    import Filter from "$icons/filter.svelte";
    import Listen from "$icons/listen.svelte";
    import MessageCircle from "$icons/message_circle.svelte";
    import PlayCircle from "$icons/play_circle.svelte";
    import Read from "$icons/read.svelte";
    import Search from "$icons/search.svelte";
    import SettingsOutline from "$icons/settings_outline.svelte";
    import Share from "$icons/share.svelte";
    import Star from "$icons/star.svelte";
    import TrendingUp from "$icons/trending_up.svelte";
    import Video from "$icons/video.svelte";
    import Warning from "$icons/warning.svelte";
    import { Ratings } from "@skeletonlabs/skeleton";
    import type { SvelteComponentDev } from "svelte/internal";

    export let anime_name: string;
    export let japanese_name: string;
    export let anime_episodes_count: number;
    export let anime_date: string;
    export let anime_synopsis: string;
    export let anime_banner: string;
    export let anime_cover: string;

    export let anime_episodes: any;

    const anime_details = {
        format: "TV",
        episodes: "22",
        "episode Duration": "26 Minutes",
        status: "finished",
        "start date": new FormatDate("2012-04-23").format_to_human_readable_form,
        "end date": new FormatDate("2012-09-16").format_to_human_readable_form,
        season: new FormatDate("2012-4").format_to_season,
        studios: "Kyoto Animation",
        producers: ["Lantis", "Kadokawa Shoten", "Klock Worx", "chara-ani.com", "Animation Do"],
        source: "Night Novel"
        //tags: []
    };

    const icon_mapping: {
        [key: string]: {
            [key: string]: {
                icon: {
                    component: typeof SvelteComponentDev;
                    class: string;
                    color?: string;
                    variant?: boolean | string;
                    label?: string;
                };
            };
        };
    } = {
        anime_options: {
            read: {
                icon: {
                    component: Read,
                    class: "w-4 md:w-[1.5vw] text-surface-500"
                }
            },
            listen: {
                icon: {
                    component: Listen,
                    class: "w-4 md:w-[1.5vw] text-surface-500"
                }
            }
        },
        user_options_icons: {
            video: {
                icon: {
                    component: Video,
                    variant: false,
                    class: "w-4 md:w-[1.125vw]"
                }
            },
            edit: {
                icon: {
                    component: Edit,
                    variant: "with_underline_around_pencil",
                    class: "w-4 md:w-[1.125vw]"
                }
            },
            download: {
                icon: {
                    component: Download,
                    class: "w-4 md:w-[1.125vw]"
                }
            },
            share: {
                icon: {
                    component: Share,
                    class: "w-4 md:w-[1.125vw]"
                }
            }
        }
    };
</script>

<div class="anime_info relative">
    <div class="relative h-screen bg-cover">
        <ImageLoader
            src={anime_cover ?? ""}
            class="absolute hidden h-full w-full select-none rounded-tl-[1.5vw] object-cover object-center md:flex"
        />

        <div class="gradient absolute inset-0 bg-gradient-to-t from-surface-900 to-surface-900/50" />
        <div class="absolute inset-0 md:p-[5vw]">
            <div class="grid grid-cols-12 items-start p-5 pt-10 md:p-0">
                <div class="col-span-12 md:col-span-10 md:pr-[4vw]">
                    <div class="grid grid-cols-12 items-end justify-between">
                        <div class="relative col-span-12 grid grid-cols-12 gap-5 md:col-span-7 md:flex md:w-full md:items-end md:gap-[2vw] md:pr-[2vw]">
                            <anime-banner class="relative col-span-12 h-96 md:h-[18.25vw] md:w-[13vw] md:flex-shrink-0">
                                <radial-gradient
                                    class="pointer-events-none absolute inset-0 z-10 h-[150%] w-[125%] -translate-x-8 -translate-y-28 md:hidden"
                                    style="
                                        background-image: radial-gradient(circle at center, rgba(255, 255, 255, 0.1) 0%, transparent 100%);
                                        mask-image: linear-gradient(to bottom, rgba(7, 5, 25, 0.95) 80%, rgba(0, 0, 0, 0) 100%);
                                    "
                                />
                                <ImageLoader
                                    class="h-full w-full rounded-xl object-cover object-center md:rounded-[1vw]"
                                    src={anime_banner}
                                    alt={anime_name}
                                />
                                <overlay-gradient class="gradient absolute inset-0 bg-gradient-to-t from-surface-900/75 to-surface-900/25 md:hidden" />
                            </anime-banner>
                            <div class="absolute bottom-0 col-span-12 p-5 md:static md:p-0">
                                <anime-name class="text-2xl font-bold md:text-[2vw] md:leading-[2.7vw]">{anime_name}</anime-name>

                                <anime-japanese-name class="unstyled flex flex-wrap gap-x-2 pt-2 text-xs font-semibold uppercase tracking-wider text-surface-50 md:gap-x-[0.25vw] md:pt-[0.625vw] md:text-[0.75vw] md:leading-[0.9vw]">
                                    {japanese_name}
                                </anime-japanese-name>

                                <p class="mt-1 flex flex-wrap items-center gap-2 text-xs font-semibold md:mt-[0.25vw] md:gap-[0.5vw] md:pt-[0.5vw] md:text-[0.75vw] md:leading-[0.75vw]">
                                    <span>TV</span>
                                    <Circle class="w-[0.35rem] opacity-50" />

                                    <span>
                                        {anime_episodes_count} eps
                                    </span>
                                    <Circle class="w-[0.35rem] opacity-50" />

                                    <span>Completed</span>
                                    <Circle class="w-[0.35rem] opacity-50" />

                                    <span class="capitalize">
                                        {new FormatDate(anime_date).format_to_season}
                                    </span>
                                    <Circle class="w-[0.35rem] opacity-50" />

                                    <span class="uppercase tracking-wider">Kuschio animation</span>
                                </p>

                                <div class="mt-3 flex items-center gap-3 md:mt-[1.5vw] md:gap-[0.75vw]">
                                    <button
                                        type="button"
                                        class="btn h-14 w-[6.5rem] rounded-lg bg-primary-500 font-bold text-white md:h-[4.3vw] md:w-[7vw] md:rounded-[0.625vw]"
                                    >
                                        <div class="flex gap-3 md:gap-[0.7vw]">
                                            <PlayCircle class="w-5 md:w-[1.875vw]" />
                                            <div class="flex flex-col items-start gap-1">
                                                <span class="text-sm leading-none md:text-[0.87vw]">Watch</span>
                                                <span class="text-xs font-bold leading-none text-surface-50 md:text-[0.625vw]">Ep 01</span>
                                            </div>
                                        </div>
                                    </button>

                                    {#each Object.entries(icon_mapping.anime_options) as item}
                                        {@const item_name = item[0]}
                                        {@const item_icon = item[1].icon}
                                        {@const component = item_icon.component}
                                        {@const component_class = item_icon.class}

                                        <button
                                            type="button"
                                            class="btn h-14 w-14 rounded-lg bg-secondary-100 capitalize text-surface-500 md:h-[4.3vw] md:w-[4.3vw] md:rounded-[0.625vw] md:text-[0.87vw] md:font-semibold"
                                            disabled
                                        >
                                            <div class="flex flex-col items-center gap-2 md:gap-[0.68vw]">
                                                <svelte:component
                                                    this={component}
                                                    class={component_class}
                                                />
                                                <span class="leading-none">{item_name}</span>
                                            </div>
                                        </button>
                                    {/each}
                                </div>

                                <div class="mt-3 flex gap-2 md:mt-[0.75vw] md:gap-[0.75vw]">
                                    {#each Object.entries(icon_mapping.user_options_icons) as item}
                                        {@const item_label = item[0]}
                                        {@const item_icon = item[1].icon}
                                        {@const component = item_icon.component}
                                        {@const component_class = item_icon.class}
                                        {@const component_variant = item_icon.variant}

                                        <button
                                            type="button"
                                            aria-label={item_label}
                                            class="btn btn-icon w-7 rounded bg-warning-400 p-0 text-surface-500 md:w-[1.875vw] md:rounded-[0.25vw]"
                                        >
                                            <svelte:component
                                                this={component}
                                                class={component_class}
                                                variant={component_variant}
                                            />
                                        </button>
                                    {/each}
                                </div>
                            </div>
                        </div>

                        <div class="col-span-12 mt-10 md:col-span-5 md:mt-0">
                            <div class="flex gap-[0.75vw]">
                                <span class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Synopsis</span>
                                <button class="btn btn-icon hidden rounded-[0.1875vw] bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                    <SettingsOutline class="w-[0.9vw] opacity-75" />
                                </button>
                            </div>

                            <ScrollArea
                                offsetScrollbar
                                gradientMask
                                parentClass="mt-3 md:mt-[1.25vw]"
                                class="h-40 text-justify text-xs md:h-[10.25vw] md:text-[0.75vw] md:leading-[1vw]"
                            >
                                {anime_synopsis}
                            </ScrollArea>

                            <div class="hidden gap-[0.5vw] text-white md:mt-[1vw] md:flex md:text-[0.75vw] md:leading-[0.9vw]">
                                <span class="rounded bg-surface-900 px-[0.95vw] md:py-[0.375vw]">Mystery</span>
                                <span class="rounded bg-surface-900 px-[0.95vw] md:py-[0.375vw]">Romance</span>
                                <span class="rounded bg-surface-900 px-[0.95vw] md:py-[0.375vw]">Horror</span>
                            </div>

                            <div class="hidden w-max gap-[0.75vw] rounded-[0.25vw] bg-surface-50/10 backdrop-blur-lg md:mt-[0.5vw] md:flex md:px-[0.75vw] md:py-[0.375vw] md:text-[0.65vw] md:leading-[0.75vw]">
                                <div class="flex gap-[0.25vw]">
                                    <span>Score:</span>
                                    <span class="text-warning-400">79</span>
                                </div>
                                <div class="flex gap-[0.25vw]">
                                    <span>Status:</span>
                                    <span class="text-warning-400">Watching</span>
                                    <Chevron class="w-[0.625vw] text-warning-400" />
                                </div>
                                <div class="flex gap-[0.25vw]">
                                    <span>Episode:</span>
                                    <span class="text-warning-400">0/{anime_episodes_count}</span>
                                </div>
                                <div class="flex gap-[0.25vw]">
                                    <span>Your Score:</span>
                                    <span class="text-warning-400">Not Rated</span>
                                    <Chevron class="w-[0.625vw] text-warning-400" />
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="my-7 md:my-[6vw]">
                        <div class="flex border-b-2 border-surface-50/50 pb-1 md:gap-x-[0.75vw] md:border-none md:pb-0">
                            <span class="text-lg font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Episodes</span>
                            <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                <SettingsOutline class="w-[0.9vw] opacity-75" />
                            </button>
                        </div>

                        <div class="mt-2 flex flex-col justify-between gap-y-5 md:mt-0 md:flex-row md:gap-y-0">
                            <div class="hidden items-end gap-2 md:flex md:gap-[1.25vw]">
                                <p class="flex items-center gap-1 md:gap-[0.75vw]">
                                    <span class="text-base font-bold leading-none md:text-[2vw] md:leading-[1.9vw]">23</span>
                                    <span class="text-xs font-semibold md:text-[1vw]">episodes</span>
                                    <Circle class="w-[0.4vw] opacity-50" />
                                </p>

                                <div>
                                    <div class="flex w-full items-center gap-2 leading-4 md:gap-[1vw] md:leading-[1.5vw]">
                                        <span class="flex-shrink-0 text-[0.5rem] font-medium md:text-[0.75vw]">Available in</span>
                                        <div class="h-[0.1rem] w-full bg-surface-50/25 md:h-[0.08vw] md:bg-surface-300" />
                                    </div>

                                    <div>
                                        <div class="flex h-5 gap-2 text-[0.5rem] font-bold md:h-[1.8vw] md:gap-[0.75vw] md:text-[0.75vw]">
                                            {#each ["sub", "dub"] as item}
                                                <span class="flex h-full place-items-center rounded bg-surface-400 px-2 uppercase leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">
                                                    {item}
                                                </span>
                                            {/each}

                                            <Circle class="w-[0.4vw] opacity-50" />

                                            {#each ["1080p", "720p", "480p"] as resolution}
                                                <span class="flex h-full place-items-center rounded bg-surface-400 px-2 leading-[0.9vw] md:rounded-[0.25vw] md:px-[0.9vw]">
                                                    {resolution}
                                                </span>
                                            {/each}
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="flex items-center justify-between gap-2 md:items-end md:gap-[0.75vw]">
                                <p class="flex items-center gap-1 md:hidden">
                                    <span class="text-base font-bold leading-none">23</span>
                                    <span class="text-sm font-semibold text-surface-50">episodes</span>
                                </p>

                                <div class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]">
                                    <span class="text-[0.65rem] leading-[0.9vw] text-surface-50 transition-colors duration-300 group-hover:text-white md:text-[0.75vw]">Type</span>
                                    <button class="btn h-7 rounded bg-surface-400 px-3 text-[0.65rem] font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw] md:leading-[0.9vw]">
                                        <span>Subbed</span>
                                        <Chevron
                                            class="w-3 md:w-[1vw]"
                                            color="lightgray"
                                        />
                                    </button>
                                </div>

                                <div class="group hidden flex-col gap-2 md:flex md:gap-[0.5vw]">
                                    <span class="text-[0.65rem] leading-[0.9vw] text-surface-50 transition-colors duration-300 group-hover:text-white md:text-[0.75vw]">Display Mode</span>
                                    <button class="btn h-7 rounded bg-surface-400 px-3 text-[0.65rem] font-semibold leading-[0.9vw] md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.9vw]">
                                        <span>Thumbnails</span>
                                        <Chevron
                                            class="w-3 md:w-[1vw]"
                                            color="lightgray"
                                        />
                                    </button>
                                </div>
                                <button
                                    class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]"
                                    aria-label="Search"
                                >
                                    <Search
                                        class="w-3 md:w-[1vw]"
                                        color="lightgray"
                                    />
                                </button>
                            </div>
                        </div>

                        <div class="mt-4 grid grid-cols-12 gap-5 md:mt-[2.5vw] md:gap-[2.5vw]">
                            {#each anime_episodes as episode}
                                {@const thumbnail = episode.thumbnail}
                                {@const title = episode.title}
                                {@const episode_number = episode.number}
                                {@const japanese_name = episode.japanese_title}
                                {@const duration = episode.duration}

                                <a
                                    href="./watch/{episode_number}"
                                    class="unstyled relative col-span-12 grid grid-cols-12 gap-4 md:col-span-4"
                                >
                                    <div class="relative col-span-5 h-full w-full md:col-span-12 md:h-[19vw]">
                                        <div class="h-24 md:h-[12vw] md:w-full">
                                            <ImageLoader
                                                src={thumbnail ?? ""}
                                                class="h-full w-full shrink-0 rounded-lg bg-cover bg-center md:rounded-t-[0.625vw]"
                                            />
                                        </div>
                                        <overlay-effect class="absolute inset-0 hidden bg-gradient-to-t from-surface-900/75 to-transparent md:flex md:h-[12vw]" />

                                        <div class="absolute bottom-0 flex h-max w-full justify-between p-1 md:top-0 md:p-[0.5vw]">
                                            <p class="rounded bg-surface-900/75 p-1 text-xs font-bold tracking-wider text-surface-50 md:bg-surface-900/50 md:p-[0.45vw] md:text-[0.8vw]">
                                                EP {episode_number < 10 ? `0${episode_number}` : episode_number}
                                            </p>
                                            <p class="unstyled rounded bg-surface-900/75 p-1 py-0 text-[0.7rem] font-semibold tracking-wider text-surface-50 md:bg-surface-900/50 md:px-[0.45vw] md:py-[0.1vw] md:text-[0.75vw]">
                                                {new FormatTime(duration).format_seconds_to_time_stamp_duration}
                                            </p>
                                        </div>
                                    </div>

                                    <episode-info-card class="col-span-7 flex h-full w-full flex-col items-start justify-between md:absolute md:bottom-0 md:col-span-12 md:h-auto md:gap-[0.75vw] md:rounded-b-[0.625vw] md:bg-surface-900 md:p-[1vw]">
                                        <div class="relative flex w-full flex-col items-start gap-1 md:gap-[0.25vw]">
                                            <episode-name class="md:hover:overflow-scroll-y max-h-9 w-full overflow-hidden text-[0.8rem] font-light leading-snug text-white duration-500 ease-in-out md:max-h-[1.25vw] md:bg-surface-900 md:text-[0.9vw] md:leading-[1.25vw] md:text-surface-50/90 md:hover:max-h-[18vw] md:hover:text-surface-50">
                                                {title}
                                            </episode-name>

                                            <episode-japanese-name class="md:hover:overflow-scroll-y max-h-4 w-full overflow-hidden text-[0.8rem] font-light leading-snug text-white duration-500 ease-in-out md:max-h-[1.3vw] md:bg-surface-900 md:text-[0.9vw] md:leading-[1.25vw] md:text-surface-50/90 md:hover:max-h-[18vw] md:hover:text-surface-50">
                                                {japanese_name}
                                            </episode-japanese-name>
                                        </div>
                                        <div class="relative flex w-full items-center gap-2 md:mt-[0.25vw] md:gap-[0.65vw]">
                                            <formats class="flex gap-2 leading-none md:gap-[0.65vw]">
                                                {#each episode.formats as format}
                                                    <span class="rounded text-[0.6rem] font-semibold uppercase tracking-wider text-surface-50 md:bg-surface-400/50 md:p-[0.45vw] md:text-[0.8vw]">{format}</span>
                                                {/each}
                                            </formats>
                                            <Circle class="w-1 opacity-50 md:w-[0.25vw]" />
                                            <resolutions class="flex gap-2 leading-none md:gap-[0.65vw]">
                                                {#each episode.resolutions as episode_resolution}
                                                    {@const resolution = (() => {
                                                        switch (episode_resolution) {
                                                            case "720p": {
                                                                return "hd";
                                                            }
                                                            case "1080p": {
                                                                return "fhd";
                                                            }
                                                            default: {
                                                                return "sd";
                                                            }
                                                        }
                                                    })()}

                                                    <span class="text-[0.6rem] font-semibold uppercase tracking-wider text-surface-50 md:rounded md:bg-surface-400/25 md:p-[0.45vw] md:text-[0.8vw]">
                                                        {resolution}
                                                    </span>
                                                {/each}
                                            </resolutions>
                                        </div>
                                    </episode-info-card>
                                </a>
                            {/each}
                        </div>

                        <div class="mt-10 flex grid-cols-5 flex-col gap-10 md:mt-[3vw] md:grid md:gap-[4.375vw]">
                            <comment-box class="md:col-span-3">
                                <div class="flex gap-2 border-b-2 border-surface-50/50 pb-1 md:gap-[0.75vw] md:border-none md:pb-0">
                                    <span class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Comments</span>
                                    <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                        <SettingsOutline class="w-[0.9vw] opacity-75" />
                                    </button>
                                </div>

                                <div class="mt-2 flex items-center justify-between md:hidden">
                                    <p class="flex items-center gap-1 md:hidden">
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
                                </div>

                                <form class="mt-3 md:mt-[1vw]">
                                    <div class="relative">
                                        <TextEditor />
                                    </div>

                                    <div class="mt-4 flex justify-between gap-5 md:mt-[0.75vw] md:gap-[1vw]">
                                        <div class="flex items-center gap-3 md:gap-[0.625vw]">
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
                                        </div>

                                        <button class="btn btn-sm h-9 w-40 rounded bg-primary-500 text-sm font-semibold md:h-[2.2vw] md:w-[7vw] md:rounded-[0.375vw] md:text-[0.85vw]">Comment</button>
                                    </div>
                                </form>
                            </comment-box>
                            <forum-posts class="md:col-span-2">
                                <div class="flex gap-2 border-b-2 border-surface-50/50 pb-1 md:gap-[0.75vw] md:border-none md:pb-0">
                                    <span class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Forum Posts</span>
                                    <button class="btn btn-icon hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                                        <SettingsOutline class="w-[0.9vw] opacity-75" />
                                    </button>
                                </div>

                                <div class="mt-2 md:mt-[0.75vw]">
                                    <div class="flex items-center justify-between">
                                        <p class="flex items-center gap-1 md:hidden">
                                            <span class="text-base font-bold leading-none">106</span>
                                            <span class="text-sm font-semibold text-surface-50">posts</span>
                                        </p>

                                        <div class="flex items-center gap-2 md:w-full md:justify-between">
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
                                        </div>
                                    </div>

                                    <posts class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1.25vw] md:flex md:gap-[1vw]">
                                        {#each forum_posts as post}
                                            <a
                                                href="/"
                                                class="card w-full grid-cols-7 overflow-hidden rounded-lg !bg-surface-400 md:grid md:rounded-[0.625vw]"
                                            >
                                                <div class="col-span-2 h-16 md:h-full md:w-full">
                                                    <ImageLoader
                                                        src={post.banner}
                                                        alt={post.title}
                                                        class="h-full w-full object-cover object-center"
                                                    />
                                                </div>

                                                <div class="flex h-36 flex-col justify-between p-3 md:col-span-5 md:h-full md:gap-[0.375vw] md:p-[1vw]">
                                                    <div>
                                                        <span class="line-clamp-2 text-xs font-extrabold md:text-[0.875vw] md:leading-[1.25vw]">
                                                            {post.title}
                                                        </span>
                                                        <span class="mt-2 line-clamp-3 text-[0.6rem] font-medium leading-snug text-surface-50 md:mt-[0.5vw] md:line-clamp-2 md:text-[0.75vw] md:leading-[1.125vw]">
                                                            {post.description}
                                                        </span>
                                                    </div>

                                                    <div class=" flex items-end justify-between text-[0.6rem] leading-none md:mt-[0.75vw] md:items-center md:text-[0.75vw]">
                                                        <div class="flex flex-col gap-1 md:flex-row md:items-center md:gap-[0.25vw]">
                                                            <span>
                                                                Posted by <span class="text-[0.65rem] font-semibold md:text-[0.85vw]">{post.author}</span>
                                                            </span>
                                                            <span class="text-surface-50">
                                                                {new FormatDate(post.posted_on).format_to_time_from_now}
                                                            </span>
                                                        </div>

                                                        <div class="flex items-center gap-1 md:gap-[0.25vw]">
                                                            <MessageCircle class="w-3 md:w-[1vw]" />
                                                            <span>{post.responses}</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </a>
                                        {/each}
                                    </posts>
                                </div>
                            </forum-posts>
                        </div>
                    </div>
                </div>

                <div class="hidden md:col-span-2 md:flex">
                    <div>
                        <div class="flex gap-[0.75vw]">
                            <span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Ratings</span>
                            <button class="btn btn-icon rounded-[0.1875vw] bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">
                                <SettingsOutline class="w-[0.9vw] opacity-75" />
                            </button>
                        </div>

                        <div class="md:mt-[1.56vw]">
                            <div class="flex items-center gap-[0.5vw]">
                                <span class="border-b-2 border-surface-50/50 pb-[0.5vw] font-bold md:text-[2vw] md:leading-[1.5vw]">92%</span>
                                <span class="divider-vertical m-0 !border-surface-50/50 font-semibold text-surface-50 md:pl-1 md:text-[0.75vw] md:leading-[0.8vw]">2.8k ratings</span>
                            </div>

                            <div class="md:mt-[1.125vw]">
                                <div class="flex items-center md:gap-[0.25vw]">
                                    <span class="md:text-[1vw] md:leading-[1.5vw]">#80</span>
                                    <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Trending of all time</span>
                                </div>
                                <div class="flex items-center md:gap-[0.25vw]">
                                    <span class="md:text-[1vw] md:leading-[1.5vw]">#108</span>
                                    <span class="text-surface-50 md:text-[0.75vw] md:leading-[0.75vw]">Most popular anime</span>
                                </div>
                            </div>

                            <button class="btn bg-secondary-100 text-surface-500 md:mt-[1.125vw] md:h-[1.5vw] md:w-[9vw] md:rounded-[0.18vw] md:text-[0.75vw] md:leading-[0.9vw]">
                                <div class="flex place-items-center gap-[0.25vw]">
                                    <TrendingUp class="w-[1vw]" />
                                    Detailed Distribution
                                </div>
                            </button>

                            <div class="md:mt-[0.4vw]">
                                <span class="font-semibold md:text-[0.9vw] md:leading-[0.9vw]">Your rating</span>
                                <div class="flex items-center gap-[0.75vw] md:mt-[0.25vw]">
                                    <ratings>
                                        <Ratings
                                            value={round_to_nearest_zero_point_five(4.5)}
                                            max={5}
                                        >
                                            <svelte:fragment slot="empty">
                                                <Star
                                                    color="white"
                                                    variant="empty"
                                                    fill_color="white"
                                                    class="w-[1.25vw]"
                                                />
                                            </svelte:fragment>
                                            <svelte:fragment slot="half">
                                                <Star
                                                    color="white"
                                                    variant="half"
                                                    fill_color="white"
                                                    class="w-[1.25vw]"
                                                />
                                            </svelte:fragment>
                                            <svelte:fragment slot="full">
                                                <Star
                                                    color="white"
                                                    variant="full"
                                                    fill_color="white"
                                                    class="w-[1.25vw]"
                                                />
                                            </svelte:fragment>
                                        </Ratings>
                                    </ratings>
                                    <span class="font-bold leading-none md:text-[0.95vw]">92%</span>
                                    <button class="btn btn-icon bg-secondary-100 p-[0.3vw] text-surface-500 md:w-[1.375vw] md:rounded-[0.19vw]">
                                        <Edit
                                            variant="without_underline_around_pencil"
                                            color="bg-surface-500"
                                            style="width: 0.75vw;"
                                        />
                                    </button>
                                </div>
                            </div>

                            <button class="btn btn-sm flex gap-[0.5vw] p-0 md:mt-[1vw] md:text-[0.8vw] md:leading-[0.9vw]">
                                Add a review
                                <ExternalLink class="w-[0.8vw]" />
                            </button>
                        </div>

                        <div class="flex gap-[0.75vw] md:mt-[6vw]">
                            <span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Details</span>
                            <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">
                                <SettingsOutline class="w-[0.9vw] opacity-75" />
                            </button>
                        </div>

                        <div class="md:mt-[1.25vw]">
                            <animedetails class="flex flex-col gap-[1.125vw] capitalize">
                                {#each Object.entries(anime_details) as details_item}
                                    {@const key = details_item[0]}
                                    {@const value = details_item[1]}

                                    {#if Array.isArray(value)}
                                        <!-- Only handle producers in this array field  -->
                                        <div class="flex flex-col gap-[0.75vw] text-[0.9375vw] leading-none text-surface-50">
                                            <p class="font-semibold text-white">{key}</p>
                                            {#each value.sort() as item}
                                                <p>{item}</p>
                                            {/each}
                                        </div>
                                    {:else}
                                        <!-- Handle everything else here  -->
                                        <div class="flex flex-col gap-[0.5vw] text-[0.9375vw] leading-none text-surface-50">
                                            <p class="font-semibold text-white">{key}</p>
                                            <p>{value}</p>
                                        </div>
                                    {/if}
                                {/each}
                            </animedetails>

                            <voiceovercase>
                                <div class="mt-[2.5vw]">
                                    <div class="flex gap-[0.75vw]">
                                        <span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Voiceover Cast</span>
                                        <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">
                                            <SettingsOutline class="w-[0.9vw] opacity-75" />
                                        </button>
                                    </div>

                                    <div class="mt-[1vw] flex flex-col">
                                        <span class="text-[0.9375vw] text-surface-50">VAs</span>
                                        <button class="btn btn-sm mt-[0.3vw] h-[2.25vw] w-[6.625vw] gap-1 rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw]">
                                            Japanese
                                            <Chevron class="w-[0.9vw]" />
                                        </button>
                                    </div>

                                    <casts>
                                        <div class="mt-[1vw]">
                                            <div class="relative grid h-[7.5vw] w-[12.5vw] grid-cols-2 gap-[2px] overflow-hidden rounded-[0.75vw]">
                                                <div class="relative col-span-1 w-full bg-cover">
                                                    <ImageLoader
                                                        src="https://s4.anilist.co/file/anilistcdn/character/large/b55131-ypodHQCyHbzD.png"
                                                        class="absolute h-full w-full object-cover object-center"
                                                    />

                                                    <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1.25vw]">Houtarou Oreki</span>
                                                </div>
                                                <div class="relative col-span-1 w-full bg-cover">
                                                    <ImageLoader
                                                        src="https://cdn.myanimelist.net/images/voiceactors/1/74056.jpg"
                                                        class="absolute h-full w-full object-cover object-center"
                                                    />

                                                    <span class="absolute bottom-[0.3vw] z-10 w-full text-center text-[0.9vw] font-bold leading-[1.25vw]">Yuuichi Nakamura</span>
                                                </div>
                                                <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25" />
                                            </div>

                                            <div class="mt-[1.5vw] flex flex-col">
                                                <div class="btn-group flex h-[2.25vw] w-1/2 rounded-[0.5vw] bg-surface-400">
                                                    <button class="h-full w-full bg-surface-400 !p-0 font-semibold">
                                                        <Chevron class="w-[1vw] rotate-180" />
                                                    </button>
                                                    <button class="h-full w-full bg-surface-400 !p-0 !text-[0.9vw] font-bold">01</button>
                                                    <button class="h-full w-full bg-surface-400 !p-0 font-semibold">
                                                        <Chevron class="w-[1vw]" />
                                                    </button>
                                                </div>
                                                <span class="mt-[1vw] text-[0.75vw] leading-none text-surface-50">Showing 1-5, out of 58 Voiceover Casts</span>
                                            </div>
                                        </div>
                                    </casts>
                                </div>
                            </voiceovercase>

                            <recommendations>
                                <div class="mt-[2.5vw]">
                                    <div class="flex gap-3">
                                        <span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Recommendations</span>
                                        <button class="btn btn-icon rounded bg-surface-400 p-0 md:h-[1.5vw] md:w-[1.5vw]">
                                            <SettingsOutline class="w-[0.9vw] opacity-75" />
                                        </button>
                                    </div>

                                    <div class="mt-[1vw]">
                                        <div class="grid grid-cols-2 gap-[1vw]">
                                            <a
                                                href="/myanimelist/1"
                                                class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover bg-center"
                                            >
                                                <ImageLoader
                                                    src="https://wallup.net/wp-content/uploads/2017/10/27/112470-Yahari_Ore_no_Seishun_Love_Comedy_wa_Machigatteiru-Yuigahama_Yui-Hikigaya_Hachiman.jpg"
                                                    class="absolute h-full w-full object-cover object-center"
                                                />

                                                <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw]">Yahari Ore no Seishun Love Come wa Machigatteiru.</span>
                                                <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25" />
                                            </a>

                                            <a
                                                href="/myanimelist/1"
                                                class="card relative col-span-1 h-[9.375vw] w-full overflow-hidden rounded-[0.75vw] bg-cover"
                                            >
                                                <ImageLoader
                                                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyHBqVsDb9uqO0weu_Hi4DdFs-AywgumizkZnLQys-TJc19oks1tofYGDqijII7qDxzZEMqVdstNg&usqp=CAU&ec=48665698"
                                                    class="absolute h-full w-full object-cover object-center"
                                                />

                                                <span class="absolute bottom-[0.3vw] z-10 line-clamp-2 w-full px-[0.5vw] text-center text-[0.9vw] font-semibold leading-[1.25vw]">Suzumiya Haruhi no Yuuutsu</span>
                                                <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-surface-900/75 to-surface-900/25" />
                                            </a>
                                        </div>

                                        <div class="mt-[1.5vw] flex flex-col">
                                            <div class="btn-group flex h-[2.25vw] w-1/2 rounded-[0.5vw] bg-surface-400">
                                                <button class="h-full w-full bg-surface-400 !p-0 font-semibold">
                                                    <Chevron class="w-[1vw] rotate-180" />
                                                </button>
                                                <button class="h-full w-full bg-surface-400 !p-0 !text-[0.9vw] font-bold">01</button>
                                                <button class="h-full w-full bg-surface-400 !p-0 font-semibold">
                                                    <Chevron class="w-[1vw]" />
                                                </button>
                                            </div>
                                            <span class="mt-[1vw] text-[0.75vw] leading-none text-surface-50">Showing 1-8, out of 47 Recommendations</span>
                                        </div>
                                    </div>
                                </div>
                            </recommendations>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style lang="scss">
    episode-japanese-name,
    episode-name {
        scrollbar-width: none;

        &:not(:hover) {
            /* if we need to change the width, we should change the 90% to higher  */
            mask-image: linear-gradient(90deg, rgba(7, 5, 25, 0.95) 90%, rgba(0, 0, 0, 0) 100%);
            mask-position: right;
        }

        @media (max-width: 767px) {
            display: -webkit-box;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 2;
        }
    }
</style>
