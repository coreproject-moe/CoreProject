<script lang="ts">
    export let status: string;
    export let errorMessage: string;
    export let errorText: string;

    import OverWorked from "$kaomoji/Overworked.svelte";
</script>

<div class="flex items-center justify-center h-screen flex-col text-center gap-12">
    <OverWorked width="387" height="114" />
    <h1 class="text-indigo-700 text-3xl">
        <b>{status}</b>
        -
        <b>{errorMessage}</b>
    </h1>
    <p class="w-[70vw] font-bold">
        {@html errorText}
    </p>
</div>
