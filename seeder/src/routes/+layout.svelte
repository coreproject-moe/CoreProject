<script lang="ts">
    import '../app.css';
    import { type Snippet } from 'svelte';

    const { children }: { children: Snippet } = $props();
</script>

{@render children()}
