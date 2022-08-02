<script lang="ts">
    export let status: string;
    export let errorMessage: string;
    export let errorText: string;

    import Confused from "$kaomoji/Confused.svelte";
</script>

<div class="flex items-center justify-center h-screen flex-col text-center gap-12">
    <Confused width={414} height={123} />
    <h1 class="text-indigo-700 text-3xl">
        <b>{status}</b>
        -
        <b>{errorMessage}</b>
    </h1>
    <p class="w-[70vw] font-bold">
        {@html errorText}
    </p>
</div>
