<script lang="ts">
    export let status: string;
    export let errorMessage: string;
    export let errorText: string;

    import HowCouldYouDoIt from "$kaomoji/HowCouldYouDoIt.svelte";
</script>

<div class="flex items-center justify-center h-screen flex-col text-center gap-12">
    <HowCouldYouDoIt width="309" height="108" />
    <h1 class="text-indigo-700 text-3xl">
        <b>{status}</b>
        -
        <b>{errorMessage}</b>
    </h1>
    <p class="w-[70vw] font-bold">
        {@html errorText}
    </p>
</div>
