<script lang="ts">
    import List from "$icons/list.svelte";
    import Moon from "$icons/moon.svelte";
    import SettingsOutline from "$icons/settings_outline.svelte";
    import User from "$icons/user.svelte";
    import { Avatar } from "@skeletonlabs/skeleton";
    import type { SvelteComponent } from "svelte";
    // Bindings
    let email_element_scroll_percent = 0,
        username_element_scroll_percent = 0;

    function mouseenter(el: HTMLElement) {
        document.body.classList.add("select-none");
        el.classList.add("select-text");
    }

    function mouseleave(el: HTMLElement) {
        el.classList.remove("select-text");
        document.body.classList.remove("select-none");
    }
    // Icons
    let dropdown_icons: {
        [key in string]: {
            name: string;
            icon: {
                component: typeof SvelteComponent<{}>;
                class: string;
            };
            url: string | undefined;
            show_on_mobile?: boolean | undefined;
        };
    } = {
        profile: {
            name: "Profile",
            url: undefined,
            icon: {
                component: User,
                class: "w-[1.25vw] text-white"
            }
        },
        my_list: {
            name: "My List",
            url: undefined,
            icon: {
                component: List,
                class: "w-[1.5vw] text-white"
            }
        },
        theme: {
            name: "Theme",
            url: undefined,
            icon: {
                component: Moon,
                class: "w-[1.1vw] text-white"
            }
        },
        settings: {
            name: "Settings",
            url: undefined,
            icon: {
                component: SettingsOutline,
                class: "w-[1.1vw] text-white"
            }
        }
    };
</script>

<div class="w-48 rounded-lg bg-surface-400 p-4 shadow-lg shadow-surface-900/50 md:w-[12vw] md:rounded-[0.5vw] md:px-[0.75vw] md:py-[1.125vw]">
    <div class="grid grid-cols-12 items-center gap-[3vw] md:gap-[0.8vw]">
        <avatar class="col-span-3">
            <Avatar
                rounded="rounded-[1.2vw] md:rounded-[0.375vw]"
                width="w-full"
                src="/images/Avatar.avif"
                initials="SA"
            />
        </avatar>
        <div class="col-span-9 line-clamp-1 flex flex-col md:gap-[0.25vw]">
            <p
                class="overflow-x-scroll text-base font-semibold scrollbar-none md:text-[1vw] md:leading-none"
                class:mask-right={username_element_scroll_percent <= 10 && username_element_scroll_percent >= 0}
                class:mask-left-and-right={username_element_scroll_percent < 90 && username_element_scroll_percent >= 10}
                class:mask-left={username_element_scroll_percent <= 100 && username_element_scroll_percent >= 90}
                on:mouseenter={(event) => mouseenter(event.currentTarget)}
                on:mouseleave={(event) => mouseleave(event.currentTarget)}
                on:scroll={(event) => {
                    const el = event.currentTarget;
                    username_element_scroll_percent = globalThis.Math.round((el.scrollLeft / (el.scrollWidth - el.clientWidth)) * 100);
                }}
            >
                soraamamiya#0001
            </p>
            <p
                class="overflow-x-scroll text-xs font-medium scrollbar-none md:text-[0.8vw]"
                class:mask-right={email_element_scroll_percent <= 10 && email_element_scroll_percent >= 0}
                class:mask-left-and-right={email_element_scroll_percent < 90 && email_element_scroll_percent >= 10}
                class:mask-left={email_element_scroll_percent <= 100 && email_element_scroll_percent >= 90}
                on:mouseenter={(event) => mouseenter(event.currentTarget)}
                on:mouseleave={(event) => mouseleave(event.currentTarget)}
                on:scroll={(event) => {
                    const el = event.currentTarget;
                    email_element_scroll_percent = globalThis.Math.round((el.scrollLeft / (el.scrollWidth - el.clientWidth)) * 100);
                }}
            >
                sora_amamiya@coreproject.moe
            </p>
        </div>
    </div>

    <div class="mt-3 md:mt-[1vw]">
        {#each Object.entries(dropdown_icons) as item}
            {@const item_icon = item[1].icon}
            {@const item_href = item[1].url}
            {@const item_name = item[1].name}

            <a
                href={item_href}
                class=""
                class:pointer-events-none={!item_href}
            >
                <div class="flex cursor-pointer items-center gap-2 rounded-[0.2vw] p-[0.4rem] transition duration-100 md:gap-[0.75vw] md:p-[0.5vw] md:py-[0.5vw] md:hover:bg-surface-300/20">
                    <svelte:component
                        this={item_icon.component}
                        class="hidden basis-[12%] md:flex {item_icon.class}"
                    />
                    <svelte:component
                        this={item_icon.component}
                        class="flex w-5 basis-[12%] md:hidden"
                    />
                    <span class=" text-xs font-medium text-white md:text-[0.9vw]">
                        {item_name}
                    </span>
                </div>
            </a>
        {/each}
    </div>
</div>

<style>
    .mask-right {
        mask-image: linear-gradient(to right, rgba(7, 5, 25) 75%, rgba(0, 0, 0, 0) 100%);
    }
    .mask-left-and-right {
        mask-image: linear-gradient(to right, rgba(0, 0, 0, 0) 0%, rgba(7, 5, 25) 25%, rgba(7, 5, 25) 75%, rgba(0, 0, 0, 0) 100%);
    }
    .mask-left {
        mask-image: linear-gradient(to left, rgba(7, 5, 25) 75%, rgba(0, 0, 0, 0) 100%);
    }
</style>
