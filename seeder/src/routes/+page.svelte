<script lang="ts">
    import { dev } from '$app/environment';
</script>

{#if dev}
    <div class="flex flex-col items-center">
        <a href="#/welcome">welcome</a>
        <a href="#/server">server</a>
    </div>
{/if}
