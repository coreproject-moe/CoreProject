<script lang="ts">
    import { dev } from '$app/environment';
    import { onMount } from 'svelte';

    onMount(async () => {
        const x = await window.pyloid.JSApi.start_websocket_server();
        console.log(x);
    });
</script>

{#if dev}
    <div class="flex flex-col items-center">
        <a href="#/welcome">welcome</a>
        <a href="#/server">server</a>
    </div>
{/if}
