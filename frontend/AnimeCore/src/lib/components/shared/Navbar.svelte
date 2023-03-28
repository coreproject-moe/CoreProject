<script lang="ts">
    import { fade } from "svelte/transition";

    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { responsiveMode } from "$store/Responsive";
    import Person from "$icons/Person.svelte";
    import { user_is_logged_in, user_information } from "$store/User";
    import Cross from "$icons/Cross.svelte";
    import PersonLinearGradient from "$icons/Person-Linear-Gradient.svelte";
    import ListLinearGradient from "$icons/List-Linear-Gradient.svelte";
    import MoonLinearGradient from "$icons/Moon-Linear-Gradient.svelte";
    import SettingsLinearGradient from "$icons/Settings-Linear-Gradient.svelte";
    import { UrlMaps } from "$data/urls";
    import { modals } from "$store/Modal";
    import SearchModal from "$components/modals/Search.svelte";
    const backend_mapping = new UrlMaps();

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropdown_open = false;
</script>

<svelte:component this={SearchModal} />

<div class="navbar bg-transparent">
    <div class="navbar-start hidden md:block">
        <label for={$modals.genre}>
            <Search
                class="text-white"
                height={30}
                width={30}
            />
        </label>
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
    <div class="navbar-end">
        {#if $user_is_logged_in}
            {#if $user_information}
                {@const avatar_url = backend_mapping.DOMAIN + $user_information?.avatar}
                <div class="dropdown-end dropdown relative {dropdown_open ? 'dropdown-open' : ''}">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <img
                        alt="{$user_information?.username}'s avatar"
                        class="mask mask-squircle"
                        src={avatar_url}
                        width="50"
                        height="50"
                        on:click={() => {
                            dropdown_open = !dropdown_open;
                        }}
                    />
                    {#if dropdown_open}
                        <div transition:fade|local={{ duration: 100 }}>
                            <span
                                class="absolute left-3 top-16 inline-block rounded-lg border-l-4 border-info"
                                style="height: 60px;"
                            />
                            <span
                                class="absolute right-3 top-16 inline-block rounded-lg border-l-4 border-info"
                                style="height: 33px;"
                            />
                        </div>
                    {/if}
                    <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                    <div
                        class="dropdown-content menu rounded-box mt-24 flex w-[300px] flex-col gap-5 border-4 border-info bg-base-100 px-7 pt-6 pb-16 shadow"
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
                            <a
                                href="/user/logout"
                                class="btn-square btn-xs btn flex items-center bg-base-100"
                            >
                                <Cross
                                    width="16"
                                    height="18"
                                />
                            </a>
                        </div>
                        <div class="flex gap-4">
                            <img
                                alt="{$user_information?.username}'s avatar"
                                class="mask mask-squircle"
                                src={avatar_url}
                                width="50"
                                height="50"
                            />
                            <div>
                                <span class="text-2xl font-bold text-primary">
                                    {$user_information?.username}
                                </span>
                                <span class="font-semibold text-info">
                                    {$user_information?.email}
                                </span>
                            </div>
                        </div>
                        <div class="flex items-center gap-4">
                            <button class="btn-info btn-square btn-sm btn">
                                <PersonLinearGradient />
                            </button>
                            <span class="font-bold text-white">View Profile</span>
                        </div>

                        <div class="flex items-center gap-4">
                            <button class="btn-info btn-square btn-sm btn">
                                <ListLinearGradient />
                            </button>
                            <span class="font-bold text-white">View My List</span>
                        </div>

                        <div class="flex items-center gap-4">
                            <button class="btn-info btn-square btn-sm btn">
                                <MoonLinearGradient />
                            </button>
                            <span class="font-bold text-white">Choose Theme</span>
                        </div>

                        <div class="flex items-center gap-4">
                            <button class="btn-info btn-square btn-sm btn">
                                <SettingsLinearGradient />
                            </button>
                            <span class="font-bold text-white">Change Settings</span>
                        </div>
                    </div>
                </div>
            {:else}
                <button class="loading btn-square btn text-white" />
            {/if}
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
