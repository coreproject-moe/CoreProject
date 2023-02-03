<script lang="ts">
    import { fade } from "svelte/transition";

    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import NavbarModal from "$modals/Navbar.svelte";
    import { modals } from "$store/Modal";
    import { navbar_variant } from "$store/Navbar_Variant";
    import { responsiveMode } from "$store/Responsive";

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
                    class="w-[158px] h-[22px]"
                    style="grid-area: 1 / 1 / 2 / 2"
                />
            {/if}
        </div>
    </div>
    <div class="navbar-end">
        <label
            for={$modals.navbar}
            class="btn modal-button bg-transparent hover:bg-transparent px-0 border-transparent"
        >
            <img
                alt=""
                class="mask mask-squircle"
                src="/images/(Avatar)-placeholder.png"
                width="50"
                height="50"
            />
        </label>
    </div>
</div>
