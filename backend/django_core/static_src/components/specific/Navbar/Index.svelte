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
        }
    };
</script>

{#if window.user_authenticated}
    <div class="dropdown dropdown-end flex">
        <div
            tabindex="0"
            role="button"
            class="avatar btn border-none !bg-transparent p-0"
        >
            <div class="w-12 rounded-lg md:w-[3vw] md:rounded-[0.5vw]">
                <img
                    alt=""
                    src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg"
                />
            </div>
        </div>
        <div
            role="button"
            tabindex="0"
            class="z-1 menu dropdown-content top-14 min-w-48 rounded-lg bg-base-100 p-4 md:top-[4vw] md:min-w-[12vw] md:rounded-[0.75vw] md:p-[0.5vw] md:text-[0.9vw]"
        >
            <div class="flex flex-col items-start gap-2 leading-none md:gap-[0.35vw] md:p-[0.75vw] md:py-[0.5vw]">
                <span class="font-bold capitalize md:text-[1vw]">sora_amamiya#4444</span>
                <span class="md:text-[0.75vw]">sora_amamiya@coreproject.moe</span>
            </div>
            <div class="divider mb-0 mt-1 md:mb-[0.1vw]"></div>
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
                            class="flex items-center gap-3 !bg-transparent px-0 leading-none !text-white md:gap-[0.5vw] md:p-[0.75vw]"
                        >
                            <svelte:component
                                this={item.icon}
                                class="w-4 md:w-[1vw]"
                            />
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
            class="btn btn-neutral h-max min-h-max leading-none md:rounded-[0.5vw] md:p-[0.9vw] md:text-[1vw]"
        >
            Register
        </a>
        <a
            href="/user/login"
            class="btn btn-primary h-max min-h-max leading-none text-accent md:rounded-[0.5vw] md:p-[0.9vw] md:text-[1vw]"
        >
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
                <img
                    alt=""
                    src="https://i.pinimg.com/1200x/a8/2d/aa/a82daa4b726d8f02d8ce28f3e3b3677a.jpg"
                />
            </div>
        </div>
        <div
            role="button"
            tabindex="0"
            class="z-1 menu dropdown-content top-14 flex min-w-36 flex-col gap-3 rounded-lg bg-base-100 p-4"
        >
            <li>
                <a
                    href="/user/login"
                    class="flex items-center gap-3 !bg-transparent p-0 leading-none !text-white"
                >
                    <Login class="w-4 md:w-[1vw]" />
                    Log in
                </a>
            </li>
            <li>
                <a
                    href="/user/register"
                    class="flex items-center gap-3 !bg-transparent p-0 leading-none !text-white"
                >
                    <Register class="w-4 md:w-[1vw]" />
                    Register
                </a>
            </li>
        </div>
    </div>
{/if}
