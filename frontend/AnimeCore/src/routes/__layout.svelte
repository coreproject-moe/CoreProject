<script lang="ts">
    import "../app.scss";
    import "animate.css/animate.css";

    import OptionModal from "$components/modals/OptionModal.svelte";
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div style="height:100%">
    <OptionModal />
    <slot />
</div>
