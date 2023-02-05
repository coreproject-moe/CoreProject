<script lang="ts">
    import "../app.scss";

    import { afterUpdate } from "svelte";
    import { fade } from "svelte/transition";

    import NavigationBar from "$components/shared/NavigationBar.svelte";
    import navigationState from "$store/Navigation_State";
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
