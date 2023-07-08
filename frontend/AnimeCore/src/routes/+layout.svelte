<script lang="ts">
    import { afterNavigate, beforeNavigate } from "$app/navigation";
    import { page } from "$app/stores";
    import SearchPanel from "$components/shared/search_panel.svelte";
    import ProfileDropdown from "$components/shared/tippies/profile_dropdown.svelte";
    // import icons
    import AnimeCore from "$icons/anime_core.svelte";
    import Explore from "$icons/explore.svelte";
    import Forum from "$icons/forum.svelte";
    import Home from "$icons/home.svelte";
    import List from "$icons/list.svelte";
    import Logo from "$icons/logo.svelte";
    import Misc from "$icons/misc.svelte";
    import Schedule from "$icons/schedule.svelte";
    import Search from "$icons/search.svelte";
    import Settings from "$icons/settings.svelte";
    import { navbar_middle_section_variant } from "$store/navbar";
    import { theme } from "$store/theme";
    import { AppShell, Avatar } from "@skeletonlabs/skeleton";
    import { Modal, modalStore } from "@skeletonlabs/skeleton";
    import type { ModalComponent, ModalSettings } from "@skeletonlabs/skeleton";
    // This contains the bulk of Skeletons required styles:
    import "@skeletonlabs/skeleton/styles/all.css";
    // NProgress
    import NProgress from "nprogress";
    import { beforeUpdate } from "svelte";
    import type { SvelteComponent } from "svelte";
    import { blur, slide } from "svelte/transition";
    import tippy from "tippy.js";

    // Most of your app wide CSS should be put in this file
    import "../app.css";
    // Custom SCSS
    import "../nprogress.scss";
    // Tippy
    import "../tippy.postcss";

    // Local
    const icon_mapping: {
        // Top,middle,bottom
        [key in "top" | "middle" | "bottom"]: {
            // Icon name
            [key in string]: {
                name?: string;
                icon: {
                    component: typeof SvelteComponent<{}>;
                    class: string;
                };
                url?: string;
                show_on_mobile?: boolean | undefined;
            };
        };
    } = {
        top: {
            search: {
                icon: {
                    component: Search,
                    class: "w-[1.25vw] text-black"
                }
            }
        },
        middle: {
            home: {
                icon: {
                    component: Home,
                    class: "w-[1.25vw] text-white"
                },
                url: "/",
                show_on_mobile: true
            },

            discover: {
                icon: {
                    component: Explore,
                    class: "w-[1.25vw] text-white"
                },
                url: "/explore",
                show_on_mobile: true
            },
            list: {
                icon: {
                    component: List,
                    class: "w-[1.7vw] text-white"
                },
                url: "/list",
                show_on_mobile: false
            },
            schedule: {
                icon: {
                    component: Schedule,
                    class: "w-[1.25vw] text-white"
                },
                url: "/shedule",
                show_on_mobile: false
            },
            forum: {
                icon: {
                    component: Forum,
                    class: "w-[1.25vw] text-white"
                },
                url: "/forum",
                show_on_mobile: true
            }
        },
        bottom: {
            settings: {
                icon: {
                    component: Settings,
                    class: "w-[1.25vw] text-white"
                },
                url: undefined
            },
            "misc.": {
                icon: {
                    component: Misc,
                    class: "w-[1.25vw] text-white"
                },
                url: undefined
            }
        }
    };

    // Run after navigation
    beforeNavigate(async function () {
        NProgress.start();
    });
    afterNavigate(async function () {
        NProgress.done();
    });

    // Run first time
    beforeUpdate(async function () {
        // Configure NProgress
        NProgress.configure({
            // Full list: https://github.com/rstacruz/nprogress#configuration
            showSpinner: false,
            minimum: 0.16
        });
    });

    /** search panel */
    async function show_search_modal(): Promise<void> {
        const search_component: ModalComponent = { ref: SearchPanel };
        const search_modal: ModalSettings = {
            type: "component",
            component: search_component,
            backdropClasses: "!bg-surface-900/95",
            position: "items-start"
        };
        modalStore.trigger(search_modal);
    }

    /** vercel effect */
    let hover_glider_element: HTMLDivElement;
    let GLIDER_TRANSITION_DURATION = 100;

    function handle_mouseenter(event: MouseEvent) {
        const target = event.target as HTMLAnchorElement;
        hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;

        if (getComputedStyle(hover_glider_element).getPropertyValue("opacity") === "0") {
            setTimeout(() => {
                hover_glider_element.style.opacity = "100";
            }, GLIDER_TRANSITION_DURATION);
        } else {
            hover_glider_element.style.opacity = "100";
        }
    }
</script>

{#if $theme == "kokoro"}
    <style lang="scss">
        :root {
            /* =~= Theme Properties =~= */
            --theme-font-family-base: "Kokoro", sans-serif;
            --theme-font-family-heading: "Kokoro", sans-serif;
            --theme-font-color-base: 0 0 0;
            --theme-font-color-dark: 255 255 255;
            --theme-rounded-base: 8px;
            --theme-rounded-container: 8px;
            --theme-border-base: 1px;
            /* =~= Theme On-X Colors =~= */
            --on-primary: 0 0 0;
            --on-secondary: 255 255 255;
            --on-tertiary: 0 0 0;
            --on-success: 0 0 0;
            --on-warning: 0 0 0;
            --on-error: 255 255 255;
            --on-surface: var(--color-primary-200);
            /* =~= Theme Colors  =~= */
            /* primary | #7569E1 */
            --color-primary-50: 234 233 251; /* ⬅ #eae9fb */
            --color-primary-100: 227 225 249; /* ⬅ #e3e1f9 */
            --color-primary-200: 221 218 248; /* ⬅ #dddaf8 */
            --color-primary-300: 200 195 243; /* ⬅ #c8c3f3 */
            --color-primary-400: 158 150 234; /* ⬅ #9e96ea */
            --color-primary-500: 117 105 225; /* ⬅ #7569E1 */
            --color-primary-600: 105 95 203; /* ⬅ #695fcb */
            --color-primary-700: 88 79 169; /* ⬅ #584fa9 */
            --color-primary-800: 70 63 135; /* ⬅ #463f87 */
            --color-primary-900: 57 51 110; /* ⬅ #39336e */
            /* secondary | #4F46E5 */
            --color-secondary-50: 229 227 251; /* ⬅ #e5e3fb */
            --color-secondary-100: 220 218 250; /* ⬅ #dcdafa */
            --color-secondary-200: 211 209 249; /* ⬅ #d3d1f9 */
            --color-secondary-300: 185 181 245; /* ⬅ #b9b5f5 */
            --color-secondary-400: 132 126 237; /* ⬅ #847eed */
            --color-secondary-500: 79 70 229; /* ⬅ #4F46E5 */
            --color-secondary-600: 71 63 206; /* ⬅ #473fce */
            --color-secondary-700: 59 53 172; /* ⬅ #3b35ac */
            --color-secondary-800: 47 42 137; /* ⬅ #2f2a89 */
            --color-secondary-900: 39 34 112; /* ⬅ #272270 */
            /* tertiary | #0EA5E9 */
            --color-tertiary-50: 219 242 252; /* ⬅ #dbf2fc */
            --color-tertiary-100: 207 237 251; /* ⬅ #cfedfb */
            --color-tertiary-200: 195 233 250; /* ⬅ #c3e9fa */
            --color-tertiary-300: 159 219 246; /* ⬅ #9fdbf6 */
            --color-tertiary-400: 86 192 240; /* ⬅ #56c0f0 */
            --color-tertiary-500: 14 165 233; /* ⬅ #0EA5E9 */
            --color-tertiary-600: 13 149 210; /* ⬅ #0d95d2 */
            --color-tertiary-700: 11 124 175; /* ⬅ #0b7caf */
            --color-tertiary-800: 8 99 140; /* ⬅ #08638c */
            --color-tertiary-900: 7 81 114; /* ⬅ #075172 */
            /* success | #84cc16 */
            --color-success-50: 237 247 220; /* ⬅ #edf7dc */
            --color-success-100: 230 245 208; /* ⬅ #e6f5d0 */
            --color-success-200: 224 242 197; /* ⬅ #e0f2c5 */
            --color-success-300: 206 235 162; /* ⬅ #ceeba2 */
            --color-success-400: 169 219 92; /* ⬅ #a9db5c */
            --color-success-500: 132 204 22; /* ⬅ #84cc16 */
            --color-success-600: 119 184 20; /* ⬅ #77b814 */
            --color-success-700: 99 153 17; /* ⬅ #639911 */
            --color-success-800: 79 122 13; /* ⬅ #4f7a0d */
            --color-success-900: 65 100 11; /* ⬅ #41640b */
            /* warning | #E3BD49 */
            --color-warning-50: 251 245 228; /* ⬅ #fbf5e4 */
            --color-warning-100: 249 242 219; /* ⬅ #f9f2db */
            --color-warning-200: 248 239 210; /* ⬅ #f8efd2 */
            --color-warning-300: 244 229 182; /* ⬅ #f4e5b6 */
            --color-warning-400: 237 214 141; /* ⬅ #EDD68D */
            --color-warning-500: 227 189 73; /* ⬅ #E3BD49 */
            --color-warning-600: 204 170 66; /* ⬅ #ccaa42 */
            --color-warning-700: 170 142 55; /* ⬅ #aa8e37 */
            --color-warning-800: 136 113 44; /* ⬅ #88712c */
            --color-warning-900: 111 93 36; /* ⬅ #6f5d24 */
            /* error | #D41976 */
            --color-error-50: 249 221 234; /* ⬅ #f9ddea */
            --color-error-100: 246 209 228; /* ⬅ #f6d1e4 */
            --color-error-200: 244 198 221; /* ⬅ #f4c6dd */
            --color-error-300: 238 163 200; /* ⬅ #eea3c8 */
            --color-error-400: 225 94 159; /* ⬅ #e15e9f */
            --color-error-500: 212 25 118; /* ⬅ #D41976 */
            --color-error-600: 191 23 106; /* ⬅ #bf176a */
            --color-error-700: 159 19 89; /* ⬅ #9f1359 */
            --color-error-800: 127 15 71; /* ⬅ #7f0f47 */
            --color-error-900: 104 12 58; /* ⬅ #680c3a */
            /* surface | #070519 */
            --color-surface-50: 218 218 221; /* ⬅ #dadadd */
            --color-surface-100: 205 205 209; /* ⬅ #cdcdd1 */
            --color-surface-200: 193 193 198; /* ⬅ #c1c1c6 */
            --color-surface-300: 156 155 163; /* ⬅ #9c9ba3 */
            --color-surface-400: 30 32 54; /* ⬅ #1E2036 */
            --color-surface-500: 7 5 25; /* ⬅ #070519 */
            --color-surface-600: 6 5 23; /* ⬅ #060517 */
            --color-surface-700: 5 4 19; /* ⬅ #050413 */
            --color-surface-800: 4 3 15; /* ⬅ #04030f */
            --color-surface-900: 3 2 12; /* ⬅ #03020c */
        }
    </style>
{/if}

<div class="relative h-[100dvh]">
    <Modal />

    <AppShell>
        <svelte:fragment slot="header">
            <navbar class="absolute top-0 flex h-[4.5rem] w-full items-center justify-between bg-surface-900/95 px-[3vw] backdrop-blur-3xl md:static md:h-[10vh] md:bg-surface-900 md:py-[0.9375vw] md:pl-[2.1vw] md:pr-[3.75vw]">
                {#if ["form", "logo"].includes($navbar_middle_section_variant)}
                    <a href="/">
                        <Logo class="w-9 md:w-[2vw]" />
                    </a>

                    <div class="relative">
                        {#if $navbar_middle_section_variant === "logo"}
                            <a
                                href="/"
                                class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform"
                                transition:blur
                            >
                                <AnimeCore class="w-36 md:w-[10vw]" />
                            </a>
                        {:else if $navbar_middle_section_variant === "form"}
                            <div
                                transition:blur
                                class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform"
                            >
                                <a
                                    href="/"
                                    class="hidden md:flex"
                                >
                                    <AnimeCore class="w-[10vw]" />
                                </a>

                                <search-form>
                                    <form class="relative flex h-12 w-[65vw] items-center md:hidden">
                                        <button
                                            class="btn absolute left-4 p-0"
                                            aria-label="Search"
                                        >
                                            <Search class="w-5 opacity-75" />
                                        </button>
                                        <input
                                            type="text"
                                            placeholder="Search for animes, mangas..."
                                            class="h-full w-full rounded-[0.4rem] border-none bg-surface-400 pl-12 text-sm font-semibold text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-200"
                                        />
                                    </form>
                                </search-form>
                            </div>
                        {/if}
                    </div>

                    <button
                        class="avatar"
                        aria-label="Avatar"
                        use:tippy={{
                            trigger: "click",
                            arrow: false,
                            allowHTML: true,
                            placement: "bottom-end",
                            offset: [0, 10],
                            animation: "shift-away",
                            appendTo: document.body,
                            interactive: true,
                            onTrigger: async (instance) => {
                                const node = document.createElement("div");
                                new ProfileDropdown({
                                    target: node
                                });

                                instance.setContent(node);
                            }
                        }}
                    >
                        <Avatar
                            rounded="rounded-[0.4rem] md:rounded-[0.375vw]"
                            width="w-12 md:w-[3.125vw]"
                            src="/images/Avatar.avif"
                            initials="JD"
                        />
                    </button>
                {/if}
            </navbar>
        </svelte:fragment>
        <svelte:fragment slot="sidebarLeft">
            <div class="hidden h-full w-[6.25vw] flex-col justify-between py-[2vw] md:flex">
                <div>
                    <div class="flex flex-col items-center gap-5">
                        {#each Object.entries(icon_mapping.top) as item}
                            {@const item_icon = item[1].icon}
                            <button
                                type="button"
                                class="btn btn-icon w-[2.5vw] rounded-[0.375vw] bg-warning-400 p-0"
                                on:click={show_search_modal}
                            >
                                <svelte:component
                                    this={item_icon.component}
                                    class={item_icon.class}
                                />
                            </button>
                        {/each}
                    </div>

                    <div class="relative mt-[2.8125vw] flex flex-col items-center gap-[0.75vw]">
                        <active_glider
                            bind:this={hover_glider_element}
                            class="absolute h-[4vw] w-[4vw] rounded-[0.75vw] bg-white/10 opacity-0 ease-in-out duration-{GLIDER_TRANSITION_DURATION}"
                        />

                        {#each Object.entries(icon_mapping.middle) as item}
                            {@const item_name = item[0]}
                            {@const item_icon = item[1].icon}
                            {@const item_href = item[1].url}

                            {@const component = item_icon.component}

                            {@const is_active = $page.url.pathname === item_href}

                            <a
                                href={item_href}
                                type="button"
                                class:pointer-events-none={!item_href}
                                class="{is_active ? 'relative bg-secondary-100 before:absolute before:-left-[0.15vw] before:z-10 before:h-[1.25vw] before:w-[0.25vw] before:rounded-full before:bg-primary-500' : 'bg-initial'} btn btn-icon relative w-[4vw] rounded-[0.75vw] p-0"
                                on:mouseenter={handle_mouseenter}
                                on:mouseleave={() => (hover_glider_element.style.opacity = "0")}
                            >
                                <div class="inline-grid">
                                    {#if is_active}
                                        <div
                                            class="absolute inset-0 flex items-center justify-center"
                                            transition:blur
                                        >
                                            <svelte:component
                                                this={component}
                                                class="!text-black {item_icon.class}"
                                            />
                                        </div>
                                    {:else}
                                        <div
                                            class="absolute inset-0 flex flex-col items-center justify-center gap-[0.35vw]"
                                            transition:blur
                                        >
                                            <svelte:component
                                                this={component}
                                                class={item_icon.class}
                                            />
                                            <span class="text-[0.75vw] font-semibold capitalize leading-[1.05vw]">
                                                {item_name}
                                            </span>
                                        </div>
                                    {/if}
                                </div>
                            </a>
                        {/each}
                    </div>
                </div>

                <div class="flex flex-col-reverse items-center gap-[1vw]">
                    {#each Object.entries(icon_mapping.bottom) as item}
                        {@const item_name = item[0]}
                        {@const item_icon = item[1].icon}
                        <button
                            type="button"
                            class="bg-initial btn btn-icon w-[3.375vw] flex-col justify-center gap-[0.45vw] p-0 text-sm"
                        >
                            <svelte:component
                                this={item_icon.component}
                                class={item_icon.class}
                            />
                            <span class="!m-0 text-[0.75vw] font-semibold capitalize leading-[1.05vw]">
                                {item_name}
                            </span>
                        </button>
                    {/each}
                </div>
            </div>
        </svelte:fragment>

        <svelte:fragment slot="footer">
            <div class="flex h-20 items-center justify-center md:hidden">
                <div class="flex items-start justify-center gap-4 md:gap-[5vw]">
                    {#each Object.entries(icon_mapping.middle).filter(([_, value]) => value.show_on_mobile) as item}
                        {@const item_name = item[0]}
                        {@const item_icon = item[1].icon}
                        {@const item_href = item[1].url}

                        {@const component = item_icon.component}

                        {@const is_active = $page.url.pathname === item_href}

                        <a
                            href={item_href ?? "javascript:void(0)"}
                            type="button"
                            class="unstyled flex flex-col items-center gap-[0.5vh]"
                        >
                            <div class="{is_active ? 'bg-secondary-100' : 'bg-initial'} btn btn-icon relative h-11 w-[4.5rem] rounded-[0.75rem] p-0">
                                <div transition:blur>
                                    {#if is_active}
                                        <svelte:component
                                            this={component}
                                            class="w-5 text-surface-900"
                                        />
                                    {:else}
                                        <svelte:component
                                            this={component}
                                            class="w-5 text-white"
                                        />
                                    {/if}
                                </div>
                            </div>
                            <span class="text-xs font-bold capitalize text-surface-50">
                                {item_name}
                            </span>
                        </a>
                    {/each}
                </div>
            </div>
        </svelte:fragment>

        <div class="h-full">
            <slot />
        </div>
    </AppShell>
</div>
