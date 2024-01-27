<script lang="ts">
    import Upload from "./Upload.svelte";
    import Login from "./Login.svelte";
    import * as _ from "lodash-es";
    import { provider } from "./store/provider";
</script>

{#if !_.some($provider, _.isEmpty)}
    <Login />
{:else}
    <Upload />
{/if}
