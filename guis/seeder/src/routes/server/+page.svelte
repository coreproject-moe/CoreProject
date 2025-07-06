<script lang="ts">
    import { JSApi } from '$lib/interface/pyloid';
    import { onMount } from 'svelte';

    let host = $state<null | string>(null);
    let port = $state<null | number>(null);

    onMount(async () => {
        const api = new JSApi();
        const response = await api.get_server_port();
        if (response === null) return;

        host = response['host'];
        port = response['port'];
    });
</script>

{#if host || port}
    Listening on {host}:{port}
{:else}
    Is pyloid running?
{/if}
