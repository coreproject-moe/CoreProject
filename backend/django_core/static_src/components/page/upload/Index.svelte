<script lang="ts">
    import Upload from "./Upload.svelte";
    import Login from "./Login.svelte";
    import { provider } from "./store/provider";

    let is_empty = Object.values($provider).some((value) => value === null || value === "" || (typeof value === "object" && Object.keys(value).length === 0));
</script>

{#if is_empty}
    <Login />
{:else}
    <Upload />
{/if}
