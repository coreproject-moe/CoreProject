<script lang="ts">
    import "../app.scss";

    import { onMount } from "svelte";

    import { browser } from "$app/env";
    import OptionModal from "$components/modals/OptionModal.svelte";

    onMount(async () => {
        browser && (await import("bulma-modal-fx/dist/js/modal-fx.js"));
    });
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div style="height:100%">
    <OptionModal />
    <slot />
</div>
