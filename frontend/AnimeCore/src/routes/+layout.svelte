<script lang="ts">
    export const trailingSlash = "always";

    import "../app.scss";
    import navigationState from "$store/Navigation_State";

    import { afterUpdate } from "svelte";
    import { fade } from "svelte/transition";
    import NavigationBar from "$components/shared/NavigationBar.svelte";
    afterUpdate(async () => {
        document
            ?.querySelectorAll<HTMLDivElement | HTMLStyleElement>("#loader")
            ?.forEach((e) => e.remove());
        document?.querySelector<HTMLElement>(".root")?.style.removeProperty("display");
    });
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
