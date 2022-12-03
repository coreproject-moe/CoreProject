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

    let KokoroFont: typeof SvelteComponent | null = null;

    const mountKokoroFont = async () => {
        await import("$lib/fonts/Kokoro.svelte")
            .then((res) => (KokoroFont = res.default))
            .then(() => {
                document
                    ?.querySelectorAll<HTMLDivElement | HTMLStyleElement>("#loader")
                    ?.forEach((e) => e.remove());
                document?.querySelector<HTMLElement>(".root")?.style.removeProperty("display");
            });
    };

    afterUpdate(async () => {
        await mountKokoroFont();
    });
</script>

<svelte:component this={KokoroFont} />
<slot />
