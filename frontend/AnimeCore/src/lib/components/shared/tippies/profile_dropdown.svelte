<script lang="ts">
    import List from "$icons/list.svelte";
    import Moon from "$icons/moon.svelte";
    import SettingsOutline from "$icons/settings_outline.svelte";
    import User from "$icons/user.svelte";
    import { Avatar } from "@skeletonlabs/skeleton";
    import type { SvelteComponentDev } from "svelte/internal";
    import voca from "voca";

    let dropdown_icons: {
        [key in string]: {
            name?: string;
            icon: {
                component: typeof SvelteComponentDev;
                class: string;
            };
            url?: string;
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
    <div class="flex items-center gap-[3vw] md:gap-[0.8vw]">
        <Avatar
            rounded="rounded-[1.2vw] md:rounded-[0.375vw]"
            width="w-10 md:w-[2.5vw]"
            src="/images/Avatar.avif"
            initials="SA"
        />
        <div class="flex flex-col md:gap-[0.5vw]">
            <span class="text-base font-semibold md:text-[1vw] md:leading-none">soraamamiya</span>
            <span class="text-xs font-medium md:text-[0.8vw] md:leading-none">{voca.truncate("sora_amamiya@coreproject.moe", 17)}</span>
        </div>
    </div>

    <div class="mt-3 md:mt-[1vw]">
        {#each Object.entries(dropdown_icons) as item}
            {@const item_icon = item[1].icon}
            {@const item_href = item[1].url}
            {@const item_name = item[1].name}

            <a
                href={item_href}
                class="unstyled"
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
