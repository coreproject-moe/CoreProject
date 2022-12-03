<script lang="ts">
    export const trailingSlash = "always";

    import "../app.scss";
    // NProgress css
    import "nprogress/nprogress.css";

    import NProgress from "nprogress";
    import { afterUpdate, SvelteComponent } from "svelte";

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

    afterUpdate(async () => {
        document
            ?.querySelectorAll<HTMLDivElement | HTMLStyleElement>("#loader")
            ?.forEach((e) => e.remove());
        document?.querySelector<HTMLElement>(".root")?.style.removeProperty("display");
    });
</script>

<slot />
