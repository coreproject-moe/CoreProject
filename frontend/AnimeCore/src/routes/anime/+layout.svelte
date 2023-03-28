<script lang="ts">
    import GenreModal from "$components/modals/Genre.svelte";
    import SearchModal from "$components/modals/Search.svelte";
</script>

<!-- Modals  -->
<svelte:component this={SearchModal} />
<svelte:component this={GenreModal} />

<slot />
