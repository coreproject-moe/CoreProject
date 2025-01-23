<script lang="ts">
    import { is_running_on_pyloid } from '@/interface/pyloid';
    import { onMount } from 'svelte';

    let host = $state<null | string>(null);
    let port = $state<null | number>(null);

    onMount(async () => {
        const response = await window.pyloid.JSApi.get_server_port();
        host = response['host'];
        port = response['port'];
    });
</script>

{#if is_running_on_pyloid()}
    Listening on {host}:{port}
{:else}
    Is pyloid running?
{/if}
