<script lang="ts">
    import '../app.css';
    import { type Snippet } from 'svelte';

    const { children }: { children: Snippet } = $props();
</script>

<main class="flex h-screen items-center justify-center">
    {@render children()}
</main>
