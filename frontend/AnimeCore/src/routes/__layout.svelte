<script lang="ts">
    import "../app.scss";

    import Modal from "svelte-simple-modal";
</script>

<svelte:head>
    <title>AnimeCore</title>
</svelte:head>

<div style="height:100%">
    <Modal>
        <slot />
    </Modal>
</div>
