<script lang="ts">
    import { dev } from '$app/environment';
    import Button from '$lib/components/ui/button/button.svelte';

    let page_shown = $state(false);
    let links_shown = $state(false);
</script>

{#if dev}
    {#if !(page_shown || links_shown)}
        <div class="flex flex-col gap-5">
            <Button
                variant="outline"
                class="capitalize"
                onclick={() => {
                    links_shown = true;
                }}
            >
                Show links
            </Button>
            <Button
                variant="outline"
                class="capitalize"
                onclick={() => {
                    page_shown = true;
                }}
            >
                Show page
            </Button>
        </div>
    {:else if links_shown}
        <div class="flex flex-col items-center">
            <a href="#/welcome">welcome</a>
            <a href="#/server">server</a>
        </div>
    {/if}
{/if}
