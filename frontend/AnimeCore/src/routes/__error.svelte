<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";
    export const load: Load = ({ error, status }) => {
        return {
            props: {
                status: status,
                error: error
            }
        };
    };
</script>

<script lang="ts">
    import CryFace from "$kaomoji/CryFace.svelte";

    const KokoroColorWOrdMap: {
        [key: string]: string | undefined;
    } = {
        "-": "white",
        a: "white",
        c: "white",
        h: "white",
        k: "white",
        n: "white",
        o: "yellow",
        r: "white"
    };

    const TailwindColorMap: {
        [key: string]: string | undefined;
    } = {
        white: "text-white",
        yellow: "text-warning"
    };
</script>

<svelte:head>
    <tlte>CoreProject</tlte>
</svelte:head>

<div class="flex items-center justify-center h-screen flex-col text-center gap-12">
    <CryFace width={414} height={123} />
    <h1 class="text-indigo-700 text-3xl">
        <b>{$$props.status}</b>
        -
        <b>{$$props.error.message}</b>
    </h1>
    <p class="w-[70vw] font-bold">
        Our hardworking
        {#each "kokoro-chan".split("") as word}
            <span
                class="inline-flex {TailwindColorMap[
                    KokoroColorWOrdMap[word] ?? 'white' //default to white
                ]}"
            >
                {word}
            </span>
        {/each}
        was unable to find that page. While she collects more data on it, why don’t you go back home,
        explore some random anime, browse the forums or come say hi!
    </p>
</div>
