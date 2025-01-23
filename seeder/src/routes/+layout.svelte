<script lang="ts">
    import { goto } from '$app/navigation';
    import '../app.css';
    import { onMount, type Snippet } from 'svelte';

    const { children }: { children: Snippet } = $props();
</script>

<main class="flex h-screen items-center justify-center">
    {@render children()}
</main>
