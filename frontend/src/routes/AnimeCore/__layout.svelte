<script lang="ts">
    import { onMount } from "svelte";

    import { browser } from "$app/env";

    onMount(async () => {
        browser && (await import("bulma-modal-fx/dist/js/modal-fx.js"));
    });
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div style="height:100%">
    <slot />
</div>
