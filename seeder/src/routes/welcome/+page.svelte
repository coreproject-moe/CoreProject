<script lang="ts">
    import { Server, Laptop } from 'lucide-svelte';

    import { Separator } from '@/components/ui/separator';

    const items = [
        { name: 'server', icon: Server },
        { name: 'client', icon: Laptop }
    ];
</script>

<div class="flex flex-col">
    <div>Welcome to CoreProject</div>

    <div class="flex items-center justify-center gap-10">
        {#each items as item}
            {@const is_last = item === items.at(-1)}
            <div class="flex flex-col items-center gap-4 p-14 capitalize">
                <div>
                    <svelte:component this={item.icon} />
                </div>
                <div class="text-2xl">
                    {item.name}
                </div>
            </div>
            {#if !is_last}
                <Separator orientation="vertical" />
            {/if}
        {/each}
    </div>
</div>
