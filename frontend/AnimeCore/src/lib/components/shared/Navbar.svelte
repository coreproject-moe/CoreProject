<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";

    export const load: Load = ({ session }) => {
        return {
            props: {
                logged_in: session.authenticated
            }
        };
    };
</script>

<script lang="ts">
    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
    import NavbarModal from "$modals/Navbar.svelte";
</script>

<!-- Init the modal  -->
<svelte:component this={NavbarModal} />

<div class="navbar bg-transparent">
    <div class="navbar-start hidden md:block">
        <Search height={30} width={30} />
    </div>
    <div class="navbar-center">
        <Logo variant="black" width={158} height={22} />
    </div>
    <div class="navbar-end">
        <label
            for="my-modal-4"
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
