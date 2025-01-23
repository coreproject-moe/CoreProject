<script lang="ts">
    import { is_running_on_pyloid } from '@/interface/pyloid';
    import { onMount } from 'svelte';

    const host = 'localhost';
    const port = 10000;

    onMount(async () => {
        const x = await window.pyloid.JSApi.get_server_port();
        console.log(x);
    });
</script>

{#if is_running_on_pyloid()}
    Listening on {host}:{port}
{:else}
    Is pyloid running?
{/if}
