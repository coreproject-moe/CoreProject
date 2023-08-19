<script lang="ts">
    import { page } from "$app/stores";
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import MyListAnimeDetails from "$components/tippies/my_list_anime_details.svelte";
    import { latest_animes } from "$data/mock/latest_animes";
    import { latest_episodes } from "$data/mock/latest_episodes";
    import { my_list } from "$data/mock/my_list";
    import { FormatDate } from "$functions/format_date";
    import { OpengraphGenerator } from "$functions/opengraph";
    import ArrowUpRight from "$icons/arrow_up_right.svelte";
    import Chevron from "$icons/chevron.svelte";
    import Circle from "$icons/circle.svelte";
    import CoreProject from "$icons/core_project.svelte";
    import Caption from "$icons/caption.svelte";
    import Edit from "$icons/edit.svelte";
    import Forum from "$icons/forum.svelte";
    import Info from "$icons/info.svelte";
    import Language from "$icons/language.svelte";
    import Moon from "$icons/moon.svelte";
    import Notifications from "$icons/notifications.svelte";
    import Play from "$icons/play.svelte";
    import PlayCircle from "$icons/play_circle.svelte";
    import Preference from "$icons/preference.svelte";
    import Recent from "$icons/recent.svelte";
    import SettingsOutline from "$icons/settings_outline.svelte";
    import { timer as timerStore } from "$store/timer";
    import { Timer as EasyTimer } from "easytimer.js";
    import { onDestroy, onMount } from "svelte";
    import type { SvelteComponent } from "svelte";
    import { swipe } from "svelte-gestures";
    import { tweened } from "svelte/motion";
    import { blur } from "svelte/transition";
    import Mic from "$icons/mic.svelte";
    import tippy from "tippy.js";

    /* Slider codes */
    let main_hero_slider_element: HTMLElement;
    let main_hero_slide_active_index = 0;

    const add_one_to_main_hero_slide_active_index = () => {
        if (main_hero_slide_active_index + 1 === latest_animes.length) {
            main_hero_slide_active_index = 0;
            return;
        }
        main_hero_slide_active_index += 1;
    };

    const minus_one_to_main_hero_slide_active_index = () => {
        if (main_hero_slide_active_index === 0) {
            main_hero_slide_active_index = latest_animes.length - 1;
            return;
        }
        main_hero_slide_active_index -= 1;
    };

    const swipe_handler = (event: CustomEvent) => {
        const direction = event.detail.direction;
        timer.reset();
        if (direction === "left") {
            add_one_to_main_hero_slide_active_index();
        } else if (direction === "right") {
            minus_one_to_main_hero_slide_active_index();
        }
    };

    // Progress bar code //
    const slider_delay = 10;
    let progress_value = 0;

    let tweened_progress_value = tweened(progress_value);
    $: tweened_progress_value.set(progress_value);

    let timer = new EasyTimer({
        target: {
            seconds: slider_delay
        },
        precision: "secondTenths"
    });

    timer.on("targetAchieved", () => {
        // change slider
        add_one_to_main_hero_slide_active_index();
        timer.reset();
    });

    timer.on("secondTenthsUpdated", () => {
        const time = timer.getTotalTimeValues().secondTenths;
        const value = (100 / slider_delay) * (time / 10);
        progress_value = value;
    });

    $: {
        switch ($timerStore) {
            case "start":
                timer?.start();
                break;
            case "pause":
                timer?.pause();
                break;
            case "reset":
                timer?.reset();
                timer?.start();
                break;
        }
    }

    // Controls timer according to element visibility on viewport
    onMount(() => {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                $timerStore = "start";
            } else {
                $timerStore = "pause";
            }
        });

        observer.observe(main_hero_slider_element);
        return () => observer.unobserve(main_hero_slider_element);
    });

    onDestroy(() => {
        timer.reset();
        timer.stop();
    });

    /* slide buttons colors */
    let slide_buttons = [
        { background: "bg-surface-50", border: "border-surface-50" },
        { background: "bg-secondary-300", border: "border-secondary-300" },
        { background: "bg-warning-400", border: "border-warning-400" },
        { background: "bg-white", border: "border-white" },
        { background: "bg-primary-300", border: "border-primary-300" },
        { background: "bg-error-200", border: "border-error-200" }
    ];

    /* Icons */
    const icon_mapping: {
        [key: string]: {
            [key: string]: {
                title?: string;
                icon: {
                    component: typeof SvelteComponent<{}>;
                    class: string;
                };
            };
        };
    } = {
        left: {
            forums: {
                title: "Forums",
                icon: {
                    component: Forum,
                    class: "text-surface-900 w-[1.25vw]"
                }
            },
            last_watched: {
                title: "Last watched anime",
                icon: {
                    component: Recent,
                    class: "text-surface-900 w-[1.25vw]"
                }
            },
            notifications: {
                title: "Notifications",
                icon: {
                    component: Notifications,
                    class: "text-surface-900 w-[1.25vw]"
                }
            }
        },
        bottom: {
            language: {
                icon: {
                    component: Language,
                    class: "text-surface-900 w-[1.25vw]"
                }
            },
            preferences: {
                icon: {
                    component: Preference,
                    class: "text-surface-900 w-[1.25vw]"
                }
            },
            theme: {
                icon: {
                    component: Moon,
                    class: "text-surface-900 w-[1.25vw]"
                }
            },
            settings: {
                icon: {
                    component: SettingsOutline,
                    class: "text-surface-900 w-[1.25vw]"
                }
            }
        }
    };

    const opengraph_html = new OpengraphGenerator({
        title: "AnimeCore - A modern anime streaming site",
        site_name: "CoreProject",
        image_url: "", // Use Opengraph later
        url: $page.url.href,
        locale: "en_US",
        description: "The most modern anime streaming site"
    }).generate_opengraph();
</script>

<svelte:window
    on:focus={() => {
        $timerStore = "start";
    }}
    on:blur={() => {
        $timerStore = "pause";
    }}
/>

<svelte:head>
    {@html opengraph_html}
</svelte:head>

<home-container class="mt-16 block md:mt-0 md:p-[1.25vw] md:pr-[3.75vw]">
    <hero-section class="flex flex-col justify-between md:flex-row">
        <latest-animes-slider
            class="relative h-96 w-full md:h-[27.875vw] md:w-[42.1875vw]"
            use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: "pan-y" }}
            on:swipe={swipe_handler}
            bind:this={main_hero_slider_element}
        >
            {#each latest_animes as anime, index}
                {@const active = index === main_hero_slide_active_index}
                {@const slide_button_background = slide_buttons[main_hero_slide_active_index].background}

                {#if active}
                    <anime-slide
                        role="presentation"
                        class="absolute inset-0 md:bottom-[2vw]"
                        transition:blur
                        on:mouseenter={() => {
                            $timerStore = "pause";
                        }}
                        on:mouseleave={() => {
                            $timerStore = "start";
                        }}
                        on:touchstart={() => {
                            $timerStore = "pause";
                        }}
                        on:touchend={() => {
                            $timerStore = "start";
                        }}
                    >
                        <ImageLoader
                            src={anime.cover}
                            class="absolute h-full w-full object-cover object-center md:rounded-t-[0.875vw]"
                        />

                        <gradient-overlay class="absolute inset-0 bg-gradient-to-t from-surface-900/90 to-surface-900/50 md:to-surface-900/25" />
                        <gradient-overlay class="absolute inset-0 hidden bg-gradient-to-r from-surface-900 to-surface-900/25 md:flex md:from-surface-900/50" />

                        <anime-details class="absolute bottom-7 left-7 flex flex-col md:bottom-0 md:left-0 md:px-[3.75vw] md:py-[2.625vw]">
                            <anime-name class="text-3xl font-bold md:text-[2vw] md:leading-[2.375vw]">
                                {anime.name}
                            </anime-name>
                            <japanese-name class="text-base font-semibold text-white/90 md:hidden md:text-[2vw] md:leading-[2.375vw]">
                                {anime.japanese_name}
                            </japanese-name>
                            <anime-infos class="flex flex-wrap items-center gap-2 pt-4 text-xs font-semibold text-white/90 md:gap-[0.65vw] md:pt-[0.5vw] md:text-[0.9375vw]">
                                <span class="leading-[1.125vw]">
                                    {anime.type}
                                </span>
                                <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                <span class="leading-[1.125vw]">
                                    {anime.episodes_count} eps
                                </span>
                                <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                <span class="leading-[1.125vw]">Completed</span>
                                <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                <span class="capitalize leading-[1.125vw]">
                                    {new FormatDate(anime.aired_from).format_to_season}
                                </span>
                                <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                                <span class="leading-[1.125vw]">
                                    {anime.studios[0]}
                                </span>
                            </anime-infos>

                            <anime-genres class="flex gap-2 pb-2 pt-3 md:gap-[0.5vw] md:pt-[0.5vw]">
                                {#each anime.genres as item}
                                    <span class="rounded-lg bg-surface-900 p-2 px-3 text-xs md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.4vw] md:text-[0.75vw] md:font-semibold">{item}</span>
                                {/each}
                            </anime-genres>

                            <ScrollArea
                                gradientMask
                                offsetScrollbar
                                parentClass="max-h-16 md:max-h-[6vw] hidden md:flex"
                                class="text-xs font-medium leading-4 text-surface-200 md:pt-[0.75vw] md:text-[0.85vw] md:leading-[1.1vw]"
                            >
                                {anime.synopsis}
                            </ScrollArea>

                            <options class="mb-2 mt-5 flex gap-3 md:mb-0 md:mt-[1.5vw] md:gap-[1vw]">
                                <button class="{slide_button_background} btn btn-icon flex h-14 w-24 justify-center gap-1 rounded-xl text-base font-bold text-surface-900 md:h-[3.125vw] md:w-[5.4375vw] md:rounded-[0.625vw] md:text-[0.875vw]">
                                    <PlayCircle class="w-4 text-surface-900 md:w-[1vw]" />
                                    <span>Ep 1</span>
                                </button>

                                <a href="./mal/{anime.mal_id}">
                                    <button class="btn btn-icon flex h-14 w-28 items-center justify-center rounded-xl bg-surface-900 text-base font-semibold text-surface-50 md:h-[3.125vw] md:w-[6.5vw] md:rounded-[0.5vw] md:text-[0.875vw] md:font-bold">
                                        <Info class="w-5 text-surface-50 md:w-[1.25vw]" />
                                        <span>Details</span>
                                    </button>
                                </a>

                                <button class="btn btn-icon h-14 w-14 rounded-xl bg-surface-900 text-[3vw] font-bold text-surface-50 md:h-[3.125vw] md:w-[3.125vw] md:rounded-[0.5vw] md:text-[0.875vw]">
                                    <Edit
                                        variant="with_underline_around_pencil"
                                        class="w-4 text-surface-50 md:w-[1.25vw]"
                                    />
                                </button>
                            </options>
                        </anime-details>
                    </anime-slide>
                {/if}
            {/each}

            <slide-progress class="absolute bottom-0 flex w-full flex-col">
                <progress-bar
                    class="h-[0.2rem] md:h-[0.145vw] {slide_buttons[main_hero_slide_active_index].background}"
                    style="width: {$tweened_progress_value}%;"
                />

                <animes-boxes class="hidden w-full grid-cols-6 gap-[0.9375vw] md:mt-[1.25vw] md:grid">
                    {#each latest_animes as _, index}
                        <button
                            class="col-span-1 h-[0.625vw] w-full rounded-[0.1875vw] border-[0.15vw] {slide_buttons[index].border} transition duration-300 hover:border-surface-50/50 {index === main_hero_slide_active_index ? slide_buttons[index].background : ''}"
                            on:click={() => {
                                timer?.reset();
                                timer?.start();
                                main_hero_slide_active_index = index;
                            }}
                        />
                    {/each}
                </animes-boxes>
            </slide-progress>

            <button
                class="btn btn-icon absolute -left-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] bg-secondary-800 md:flex"
                on:click={() => {
                    timer?.reset();
                    timer?.start();
                    minus_one_to_main_hero_slide_active_index();
                }}
            >
                <Chevron
                    color="text-white"
                    class="w-[1.25vw] rotate-90"
                />
            </button>
            <button
                class="btn btn-icon absolute -right-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] bg-secondary-800 md:flex"
                on:click={async () => {
                    timer?.reset();
                    timer?.start();
                    add_one_to_main_hero_slide_active_index();
                }}
            >
                <Chevron
                    color="text-white"
                    class="w-[1.25vw] -rotate-90"
                />
            </button>
        </latest-animes-slider>

        <latest-episodes class="hidden w-[21.5625vw] md:block">
            <section-header class="flex items-center justify-between pr-[0.75vw]">
                <header-title class="flex items-center gap-[0.625vw]">
                    <span class="text-[1.25vw] font-bold">Latest Episodes</span>
                    <button class="btn btn-icon h-[1.7vw] w-[1.7vw] rounded-[0.3vw] bg-surface-400">
                        <SettingsOutline class="w-[0.8vw]" />
                    </button>
                </header-title>
                <button class="btn btn-icon h-[1.75vw] w-[6vw] rounded-[0.3vw] bg-surface-400 text-[0.9vw] font-semibold">
                    <span>Full List</span>
                    <ArrowUpRight class="w-[0.9vw]" />
                </button>
            </section-header>

            <ScrollArea
                offsetScrollbar
                parentClass="mt-[1vw] max-h-[22.25vw]"
                class="flex flex-col gap-[1vw]"
            >
                {#each latest_episodes as anime}
                    <anime-episode class="relative h-[5vw]">
                        <ImageLoader
                            src={anime.cover}
                            class="absolute h-full w-full rounded-[0.75vw] object-cover object-center"
                        />
                        <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-t from-surface-900/75 to-surface-900/0" />
                        <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-r from-surface-900/50 to-surface-900/0" />

                        <episode-info class="absolute inset-0 flex items-start justify-between p-[1.3125vw]">
                            <div class="flex flex-col gap-[0.25vw]">
                                <episode-name class="text-[1vw] font-semibold leading-[1.1875vw] text-white">
                                    {anime.name}
                                </episode-name>
                                <episode-dates class="flex items-center gap-[0.35vw] text-[0.8vw] text-surface-50">
                                    <span class="font-semibold">
                                        Ep {String(anime.episode_number).padStart(2, "0")}
                                    </span>
                                    <span>
                                        aired {new FormatDate(anime.release_date).format_to_time_from_now}
                                    </span>
                                </episode-dates>
                            </div>
                            <button class="btn btn-icon h-[2.5vw] w-[2.5vw] rounded-full bg-warning-400 text-surface-900">
                                <Play class="w-[1.25vw]" />
                            </button>
                        </episode-info>
                    </anime-episode>
                {/each}
            </ScrollArea>

            <section-bottom class="mt-[0.75vw] flex items-start justify-between gap-[2vw] pr-[0.75vw]">
                <span class="text-[0.75vw] font-semibold md:leading-[1.25vw]">showing recently aired episodes from your Anime List</span>
                <button class="btn p-0 text-[0.75vw] font-semibold text-warning-400">Change to All</button>
            </section-bottom>
        </latest-episodes>

        <navigation-card class="relative mt-[2.75vw] hidden h-[24.5vw] w-[16.625vw] md:block">
            <ImageLoader
                src="/images/NavigationBox-bg.avif"
                class="absolute h-full w-full rounded-[0.875vw] object-cover object-center"
            />

            <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-t from-surface-900 from-[1%] to-surface-900/25" />
            <gradient-overlay class="gradient absolute inset-0 bg-gradient-to-r from-surface-900/50 to-surface-900/25" />

            <navigation-content class="absolute inset-0 flex flex-col justify-between px-[1.875vw] pt-[2vw]">
                <section-header class="flex flex-col gap-[0.2w]">
                    <span class="text-[1.5vw] font-bold leading-[1vw]">Welcome</span>
                    <span class="text-[0.875vw] font-semibold leading-[2.5vw]">Jump quickly into</span>
                </section-header>

                <navigation-left-buttons class="mt-[1vw] flex flex-col gap-[0.75vw]">
                    {#each Object.entries(icon_mapping.left) as item}
                        {@const item_title = item[1].title}
                        {@const item_icon = item[1].icon}

                        <div class="flex items-center gap-[1vw]">
                            <button class="btn h-[2.5vw] w-[2.5vw] rounded-[0.375vw] bg-surface-50 p-0">
                                <svelte:component
                                    this={item_icon.component}
                                    class={item_icon.class}
                                />
                            </button>
                            <span class="text-[1vw] font-bold">{item_title}</span>
                        </div>
                    {/each}
                </navigation-left-buttons>

                <navigation-right-buttons class="mt-[0.4vw]">
                    <span class="text-[0.9vw] font-semibold leading-none">More</span>
                    <div class="mt-[0.75vw] flex gap-[0.9375vw]">
                        {#each Object.entries(icon_mapping.bottom) as item}
                            {@const item_icon = item[1].icon}

                            <button class="btn h-[2.5vw] w-[2.5vw] rounded-[0.375vw] bg-surface-50 p-0">
                                <svelte:component
                                    this={item_icon.component}
                                    class={item_icon.class}
                                />
                            </button>
                        {/each}
                    </div>
                </navigation-right-buttons>

                <coreproject-logo class="mt-[1vw] flex items-center justify-center">
                    <CoreProject />
                </coreproject-logo>
            </navigation-content>
        </navigation-card>
    </hero-section>

    <my-list class="flex flex-col p-4 pt-7 md:mb-[1vw] md:mt-[2.1875vw] md:flex md:w-[68vw] md:p-0">
        <section-header class="flex items-center gap-[0.625vw]">
            <header-title class="text-lg font-bold md:text-[1.25vw]">My List</header-title>
            <button class="btn btn-icon hidden h-[1.7vw] w-[1.7vw] rounded-[0.3vw] bg-surface-400 md:flex">
                <SettingsOutline class="w-[0.9vw]" />
            </button>
        </section-header>

        <my-list-info class="flex items-center justify-between">
            <span class="text-sm text-surface-50 md:text-[1vw] md:font-semibold">
                {my_list.length} anime in Watching
            </span>

            <my-list-options class="hidden items-center gap-[1vw] md:flex">
                <button class="btn btn-icon h-[2.25vw] w-[6.625vw] gap-[0.625vw] rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw] font-semibold">
                    Watching
                    <Chevron class="w-[1vw]" />
                </button>
                <button class="btn btn-icon h-[2.25vw] w-[5.625vw] gap-[0.625vw] rounded-[0.375vw] bg-surface-400 p-0 text-[0.875vw] font-semibold">
                    Full List
                    <ArrowUpRight class="w-[1vw]" />
                </button>
            </my-list-options>

            <see-all class="md:hidden">
                <button class="btn gap-2 p-0 text-sm">
                    See all
                    <Chevron class="w-4 -rotate-90 text-primary-400" />
                </button>
            </see-all>
        </my-list-info>

        <my-list-animes class="relative mt-4 grid grid-cols-3 gap-3 md:mt-[1vw] md:grid-cols-5 md:gap-[1.25vw]">
            {#each my_list as anime}
                <a
                    href="/mal/{anime.id}/episode/{anime.current_episode}"
                    class="relative col-span-1 flex flex-col gap-2 md:gap-[0.5vw]"
                >
                    <div
                        class="relative"
                        use:tippy={{
                            arrow: false,
                            allowHTML: true,
                            placement: "right-start",
                            animation: "scale",
                            duration: [150, 10],
                            interactive: true,
                            appendTo: document.body,
                            onTrigger: async (instance) => {
                                const node = document.createElement("div");
                                new MyListAnimeDetails({
                                    target: node,
                                    props: {
                                        anime_id: anime.id,
                                        anime_name: anime.name,
                                        anime_type: anime.type,
                                        anime_genres: anime.genres,
                                        anime_studios: anime.studios,
                                        anime_episodes_count: anime.episodes_count,
                                        anime_synopsis: anime.synopsis,
                                        anime_current_episode: anime.current_episode,
                                        anime_release_date: anime.release_date
                                    }
                                });

                                instance.setContent(node);
                            }
                        }}
                    >
                        <ImageLoader
                            src={anime.cover}
                            alt={anime.name}
                            class="h-52 w-full rounded-md object-cover object-center md:h-[18vw] md:rounded-[0.35vw]"
                        />
                        <overlay class="absolute inset-0 flex items-end bg-gradient-to-t from-surface-900/75 to-transparent p-2 leading-none md:p-[0.5vw]">
                            <div class="flex gap-1 overflow-hidden rounded md:gap-[0.2vw] md:rounded-[0.3vw]">
                                <subs class="flex items-center gap-1 bg-warning-400 p-1 text-black md:gap-[0.25vw] md:px-[0.35vw] md:py-[0.25vw]">
                                    <Caption class="h-4 md:h-[1.25vw]" />
                                    <span class="text-xs font-semibold md:text-[0.8vw]">{anime.episodes_count}</span>
                                </subs>
                                <dubs class="flex items-center gap-1 bg-white/25 p-1 backdrop-blur md:gap-[0.25vw] md:px-[0.45vw] md:py-[0.25vw]">
                                    <Mic class="h-3 md:h-[0.8vw]" />
                                    <span class="text-xs font-semibold md:text-[0.8vw]">{anime.episodes_count}</span>
                                </dubs>
                            </div>
                        </overlay>
                    </div>

                    <anime-details class="flex flex-col gap-2 text-surface-50 md:gap-[0.5vw]">
                        <anime_name class="line-clamp-1 text-xs font-semibold leading-none md:text-[1vw]">{anime.name}</anime_name>
                        <anime_info class="flex items-center gap-2 text-xs leading-none text-surface-50 md:gap-[0.5vw] md:text-[0.8vw]">
                            <span>Watching</span>
                            <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                            <span>{anime.current_episode}/{anime.episodes_count} eps</span>
                        </anime_info>
                    </anime-details>
                </a>
            {/each}
        </my-list-animes>
    </my-list>
</home-container>
