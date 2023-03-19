<script lang="ts">
    import "../app.scss";

    import { onMount } from "svelte";
    import { fade } from "svelte/transition";

    import NavigationBar from "$components/shared/NavigationBar.svelte";
    import navigationState from "$store/Navigation_State";
    onMount(async () => {
        document
            ?.querySelectorAll<HTMLDivElement | HTMLStyleElement>("#loader")
            ?.forEach((e) => e.remove());
        document?.querySelector<HTMLElement>(".root")?.style.removeProperty("display");
    });

    import { dev } from "$app/environment";
    import { inject } from "@vercel/analytics";

    inject({ mode: dev ? "development" : "production" });
</script>

<svelte:window
    on:sveltekit:navigation-start={() => {
        $navigationState = "loading";
    }}
    on:sveltekit:navigation-end={() => {
        $navigationState = "loaded";
    }}
/>

{#if $navigationState === "loading"}
    <div out:fade={{ delay: 500 }}>
        <NavigationBar />
    </div>
{/if}

<slot />
