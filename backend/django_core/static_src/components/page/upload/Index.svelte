<script lang="ts">
    import Upload from "./Upload.svelte";
    import Login from "./Login.svelte";
    import * as _ from "lodash-es";

    let tokens: { [key in "doodstream"]: string };
</script>

{#if tokens}
    <Login
        on:submit={(event) => {
            tokens = event.detail;
        }}
    />
{:else}
    <Upload />
{/if}
