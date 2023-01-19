<script lang="ts">
    import { fade } from "svelte/transition";

    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import NavbarModal from "$modals/Navbar.svelte";
    import { navbar_variant } from "$store/Navbar_Variant";
</script>

<!-- Init the modal  -->
<svelte:component
    this={NavbarModal}
    id="nabar__modal"
/>

<div class="navbar bg-transparent">
    <div class="navbar-start hidden md:block">
        <Search
            height={30}
            width={30}
        />
    </div>
    <div class="navbar-center">
        <div class="inline-grid">
            {#if $navbar_variant == "black"}
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
            {:else if $navbar_variant == "white"}
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
                    style="grid-area: 1 / 1 / 2 / 2;"
                >
                    <placeholder class="w-[170px] h-[22px] inline-block" />
                </div>
            {/if}
        </div>
    </div>
    <div class="navbar-end">
        <label
            for="nabar__modal"
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
