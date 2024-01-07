<script lang="ts">
    import VercelHover from "$components/svelte/VercelHover.svelte";
    import User from "$icons/User/Index.svelte";
    import List from "$icons/List/Index.svelte";
    import Preference from "$icons/Preference/Index.svelte";
    import Settings from "$icons/Settings/Index.svelte";
    import Login from "$icons/Login/Index.svelte";
    import Register from "$icons/Register/Index.svelte";
    import { goto } from "$functions/urls";

    const profile_mapping = {
        profile: {
            href: "/profile",
            icon: User,
            text: "Profile"
        },
        my_list: {
            href: "/my-list",
            icon: List,
            text: "My List"
        },
        prefernce: {
            href: "/prefernce",
            icon: Preference,
            text: "Preference"
        },
        settings: {
            href: "/settings",
            icon: Settings,
            text: "Settings"
        },
    };
</script>

{#if window.user_authenticated}
    <div class="dropdown dropdown-end flex">
        <div tabindex="0" role="button" class="avatar btn border-none !bg-transparent p-0">
            <div class="w-12 rounded-lg md:w-[3vw] md:rounded-[0.5vw]">
                <img alt="" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
            </div>
        </div>
        <div role="button" tabindex="0" class="dropdown-content z-1 menu min-w-48 md:min-w-[12vw] top-14 md:top-[4vw] md:text-[0.9vw] md:p-[0.5vw] p-4 bg-base-100 md:rounded-[0.75vw] rounded-lg">
            <div class="md:p-[0.75vw] md:py-[0.5vw] flex flex-col items-start leading-none md:gap-[0.35vw] gap-2">
                <span class="md:text-[1vw] font-bold capitalize">
                    sora_amamiya#4444
                </span>
                <span class="md:text-[0.75vw]">
                    sora_amamiya@coreproject.moe
                </span>
            </div>
            <div class="divider md:mb-[0.1vw] mb-0 mt-1"></div>
            <VercelHover
                glider_container_class="flex flex-col"
                active_element_class="rounded-[0.5vw] bg-primary"
                direction="vertical"
                GLIDER_TRANSITION_DURATION={200}
                let:handle_mouseenter
                let:handle_mouseleave
            >
                {#each Object.values(profile_mapping) as item}
                    <li
                        on:mouseenter|preventDefault={handle_mouseenter}
                        on:mouseleave|preventDefault={handle_mouseleave}
                    >
                        <button
                            on:click={() => {
                                goto({ target: "#page", url: item.href, verb: "GET" });
                            }}
                            class="flex items-center gap-3 md:gap-[0.5vw] px-0 md:p-[0.75vw] leading-none !text-white !bg-transparent"
                        >
                            <svelte:component this={item.icon} class="w-4 md:w-[1vw]" />
                            {item.text}
                        </button>
                    </li>
                {/each}
            </VercelHover>
        </div>
    </div>
{:else}
    <div class="hidden md:flex md:gap-[0.75vw]">
        <a
            href="/user/register"
            class="btn btn-neutral md:p-[0.9vw] md:text-[1vw] h-max min-h-max leading-none md:rounded-[0.5vw]">
            Register
        </a>
        <a
            href="/user/login"
            class="btn btn-primary text-accent md:p-[0.9vw] md:text-[1vw] h-max min-h-max leading-none md:rounded-[0.5vw]">
            Log in
        </a>
    </div>

    <div class="dropdown dropdown-end flex md:hidden">
        <div
            tabindex="0"
            role="button"
            class="avatar btn border-none !bg-transparent p-0"
        >
            <div class="w-12 rounded-lg md:w-[3vw] md:rounded-[0.5vw]">
                <img alt="" src="https://i.pinimg.com/1200x/a8/2d/aa/a82daa4b726d8f02d8ce28f3e3b3677a.jpg" />
            </div>
        </div>
        <div
            role="button"
            tabindex="0"
            class="dropdown-content z-1 min-w-36 top-14 p-4 bg-base-100 menu rounded-lg flex flex-col gap-3"
        >
            <li>
                <a
                    href="/user/login"
                    class="flex items-center gap-3 p-0 leading-none !text-white !bg-transparent"
                >
                    <Login class="w-4 md:w-[1vw]" />
                    Log in
                </a>
            </li>
            <li>
                <a
                    href="/user/register"
                    class="flex items-center gap-3 p-0 leading-none !text-white !bg-transparent"
                >
                    <Register class="w-4 md:w-[1vw]" />
                    Register
                </a>
            </li>
        </div>
    </div>
{/if}