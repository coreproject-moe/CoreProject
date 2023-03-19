<script lang="ts">
    import { fade } from "svelte/transition";

    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import NavbarModal from "$modals/Navbar.svelte";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { responsiveMode } from "$store/Responsive";
    import { user_is_logged_in } from "$store/User";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

<!-- Init the modal  -->
<svelte:component this={NavbarModal} />

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
    <div class="navbar-end">
        {#if $user_is_logged_in}
            <img
                alt=""
                class="mask mask-squircle"
                src="/images/(Avatar)-placeholder.png"
                width="50"
                height="50"
            />
        {:else}
            <a
                class="glass flex h-[55px] w-[60px] items-center justify-center rounded-lg border-2 border-dashed border-white font-bold hover:border-dashed active:scale-95"
                href="/user/login"
            >
                Log in
            </a>
        {/if}
    </div>
</div>
