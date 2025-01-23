<script lang="ts">
    import type { Snippet } from 'svelte';
    const { children }: { children: Snippet } = $props();
</script>

<div class="flex h-full flex-col items-center justify-center">
    {@render children()}
</div>
