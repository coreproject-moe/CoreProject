<script lang="ts">
    import { fade } from "svelte/transition";

    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { responsiveMode } from "$store/Responsive";
    import Person from "$icons/Person.svelte";
    import { user_is_logged_in } from "$store/User";
    import Cross from "$icons/Cross.svelte";
    import PersonLinearGradient from "$icons/Person-Linear-Gradient.svelte";
    import ListLinearGradient from "$icons/List-Linear-Gradient.svelte";
    import MoonLinearGradient from "$icons/Moon-Linear-Gradient.svelte";
    import SettingsLinearGradient from "$icons/Settings-Linear-Gradient.svelte";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    const closeDropdown = () => {
        let element = document.activeElement as HTMLDivElement;
        element?.blur();
    };
</script>

<div class="navbar bg-transparent">
    <div class="navbar-start hidden md:block">
        <Search
            height={30}
            width={30}
        />
    </div>
    <div
        class="navbar-center glass rounded-md"
        style="--glass-reflex-degree:90;"
    >
        <div class="inline-grid py-1 md:py-2">
            {#if $navbar_variant == "black" || $navbar_variant == undefined || mobile}
                <div
                    transition:fade|local
                    style="grid-area: 1 / 1 / 2 / 2"
                >
                    <Logo
                        variant="black"
                        width={158}
                        height={22}
                    />
                </div>
            {:else if $navbar_variant == "white" || !mobile}
                <div
                    transition:fade|local
                    style="grid-area: 1 / 1 / 2 / 2"
                >
                    <Logo
                        variant="white"
                        width={158}
                        height={22}
                    />
                </div>
            {:else}
                <!-- placeholder to remove layout shift  -->
                <div
                    transition:fade|local
                    class="h-[22px] w-[158px]"
                    style="grid-area: 1 / 1 / 2 / 2"
                />
            {/if}
        </div>
    </div>
    <div class="navbar-end ">
        {#if $user_is_logged_in}
            <div class="dropdown-end dropdown">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                <label tabindex="0">
                    <img
                        alt=""
                        class="mask mask-squircle"
                        src="/images/(Avatar)-placeholder.png"
                        width="50"
                        height="50"
                    />
                </label>
                <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                <ul
                    tabindex="0"
                    class="dropdown-content menu rounded-box flex w-[275px] flex-col gap-5 border-4 border-info bg-base-100 px-7 pt-6 pb-16 shadow"
                >
                    <div class="flex justify-between">
                        <div class="flex items-center gap-1">
                            <Person
                                color="white"
                                width="12"
                                height="12"
                            />
                            <span class="text-xs font-bold text-white">Profile View</span>
                        </div>
                        <button
                            class="btn-square btn-xs btn flex items-center bg-base-100"
                            on:click={closeDropdown}
                        >
                            <Cross
                                width="16"
                                height="18"
                            />
                        </button>
                    </div>
                    <div class="flex gap-4">
                        <img
                            alt="Name"
                            class="mask mask-squircle"
                            src="/images/(Avatar)-placeholder.png"
                            width="50"
                            height="50"
                        />
                        <div>
                            <span class="text-2xl font-bold">Username</span>
                            <span class="font-semibold">email@domain</span>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <button class="btn-info btn-square btn-sm btn">
                            <PersonLinearGradient />
                        </button>
                        <span class="font-bold">View Profile</span>
                    </div>

                    <div class="flex items-center gap-4">
                        <button class="btn-info btn-square btn-sm btn">
                            <ListLinearGradient />
                        </button>
                        <span class="font-bold">View My List</span>
                    </div>

                    <div class="flex items-center gap-4">
                        <button class="btn-info btn-square btn-sm btn">
                            <MoonLinearGradient />
                        </button>
                        <span class="font-bold">Choose Theme</span>
                    </div>

                    <div class="flex items-center gap-4">
                        <button class="btn-info btn-square btn-sm btn">
                            <SettingsLinearGradient />
                        </button>
                        <span class="font-bold">Change Settings</span>
                    </div>
                </ul>
            </div>
        {:else}
            <a
                class="glass flex h-[55px] w-[60px] items-center justify-center rounded-lg border-2 border-dashed font-bold text-white hover:border-dashed active:scale-95"
                href="/user/login"
            >
                Log in
            </a>
        {/if}
    </div>
</div>
