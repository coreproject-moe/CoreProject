<script lang="ts">
    import { afterNavigate, beforeNavigate } from "$app/navigation";
    // Most of your app wide CSS should be put in this file
    import "../app.postcss";
    // Custom SCSS
    import "../nprogress.scss";
    // Tippy
    import "../tippy.scss";
    import { initializeStores } from "@skeletonlabs/skeleton";
    initializeStores();
    // NProgress
    import NProgress from "nprogress";
    import { beforeUpdate } from "svelte";

    // Local

    // Run after navigation
    beforeNavigate(async function () {
        NProgress.start();
    });
    afterNavigate(async function () {
        NProgress.done();
    });

    // Run first time
    beforeUpdate(async function () {
        // Configure NProgress
        NProgress.configure({
            // Full list: https://github.com/rstacruz/nprogress#configuration
            showSpinner: false,
            minimum: 0.16
        });
    });
</script>

<div class="h-screen w-screen">
    <slot />
</div>
