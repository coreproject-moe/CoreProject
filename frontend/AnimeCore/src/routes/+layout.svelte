<script lang="ts">
    import "../app.scss";

    import { fade } from "svelte/transition";

    import NavigationBar from "$components/shared/NavigationBar.svelte";
    import navigationState from "$store/Navigation_State";
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
