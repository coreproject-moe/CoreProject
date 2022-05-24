<script lang="ts">
    import "../app.scss";
// NProgress css
    import "nprogress/nprogress.css";

    import NProgress from "nprogress";
    import Modal from "svelte-simple-modal";

    import { navigating } from "$app/stores";

    NProgress.configure({
        // Full list: https://github.com/rstacruz/nprogress#configuration
        minimum: 0.16
    });

    $: {
        if ($navigating) {
            NProgress.start();
        }
        if (!$navigating) {
            NProgress.done();
        }
    }
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div style="height:100%">
    <Modal>
        <slot />
    </Modal>
</div>
