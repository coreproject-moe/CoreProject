<script lang="ts">
    import { afterNavigate, beforeNavigate } from "$app/navigation";
    import { page } from "$app/stores";
    import SearchPanel from "$components/shared/search_panel.svelte";
    import VercelHover from "$components/shared/vercel_hover.svelte";
    import ProfileDropdown from "$components/tippies/profile_dropdown.svelte";
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
    // Most of your app wide CSS should be put in this file
    import "../app.postcss";
    // Custom SCSS
    import "../nprogress.scss";
    // Tippy
    import "../tippy.scss";
    import { AppShell, Avatar } from "@skeletonlabs/skeleton";
    import { Modal } from "@skeletonlabs/skeleton";
    import { initializeStores } from "@skeletonlabs/skeleton";
    initializeStores();
    import { getModalStore } from "@skeletonlabs/skeleton";
    import type { ModalComponent, ModalSettings } from "@skeletonlabs/skeleton";
    // NProgress
    import NProgress from "nprogress";
    import { beforeUpdate } from "svelte";
    import type { SvelteComponent } from "svelte";
    import { blur } from "svelte/transition";
    import tippy from "tippy.js";

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

            explore: {
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
    const modalStore = getModalStore();
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
</script>

<div class="relative h-[100dvh]">
    <Modal />

    <AppShell>
        <svelte:fragment slot="header">
            <navbar class="absolute top-0 flex h-[4.5rem] w-full items-center justify-between bg-surface-900/95 px-4 backdrop-blur-3xl md:static md:h-[10vh] md:bg-surface-900 md:py-[0.9375vw] md:pl-[2.1vw] md:pr-[3.75vw]">
                {#if ["form", "logo"].includes($navbar_middle_section_variant)}
                    <a href="/">
                        <Logo class="w-9 md:w-[2.25vw] md:pt-[0.75vw]" />
                    </a>

                    <div class="relative flex items-center">
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
                                class="absolute left-1/2 -translate-x-1/2"
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
                            theme: "elaine",
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

                    <VercelHover
                        direction="vertical"
                        glider_container_class="mt-[2.8125vw] flex flex-col items-center gap-[0.75vw]"
                        active_element_class="rounded-[0.75vw] bg-white/10"
                        let:handle_mouseenter
                        let:handle_mouseleave
                    >
                        {#each Object.entries(icon_mapping.middle) as item}
                            {@const item_name = item[0]}
                            {@const item_icon = item[1].icon}
                            {@const item_href = item[1].url}

                            {@const component = item_icon.component}

                            {@const is_active = $page.url.pathname === item_href}

                            <a
                                on:mouseenter={handle_mouseenter}
                                on:mouseleave={handle_mouseleave}
                                href={item_href}
                                type="button"
                                class:pointer-events-none={!item_href}
                                class="{is_active ? 'relative bg-secondary-100 before:absolute before:-left-[0.15vw] before:z-10 before:h-[1.25vw] before:w-[0.25vw] before:rounded-full before:bg-primary-500' : 'bg-initial'} btn btn-icon relative w-[4vw] rounded-[0.75vw] p-0"
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
                    </VercelHover>
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
            <div class="flex h-24 items-center justify-center md:hidden">
                <div class="flex items-start justify-center gap-5">
                    {#each Object.entries(icon_mapping.middle).filter(([_, value]) => value.show_on_mobile) as item}
                        {@const item_name = item[0]}
                        {@const item_icon = item[1].icon}
                        {@const item_href = item[1].url}

                        {@const component = item_icon.component}
                        {@const klass = "w-5"}

                        {@const is_active = $page.url.pathname === item_href}

                        <a
                            href={item_href ?? "javascript:void(0)"}
                            type="button"
                            class="flex flex-col items-center gap-[0.5vh]"
                        >
                            <div class="{is_active ? 'bg-primary-500' : 'bg-initial'} btn btn-icon h-12 w-20 rounded-xl p-0">
                                <div transition:blur>
                                    {#if is_active}
                                        <svelte:component
                                            this={component}
                                            class={klass}
                                        />
                                    {:else}
                                        <svelte:component
                                            this={component}
                                            class={klass}
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
