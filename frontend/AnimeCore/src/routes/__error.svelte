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
    export let status: number;
    export let error: { message: string };

    import Confused from "$kaomoji/Confused.svelte";
    import Overworked from "$kaomoji/Overworked.svelte";

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

    function formatKokoroColor(input: string) {
        const kokoroRegex = new RegExp(/kokoro-chan/gm);

        // There is no kokoro-chan in the input ( which is odd )
        if (!kokoroRegex.exec(input)) {
            return input;
        }

        const coloredWrappedWords = "kokoro-chan".split("").map((word) => {
            return `<span
                class="inline-flex ${
                    TailwindColorMap[
                        KokoroColorWOrdMap[word] ?? "white" //default to white
                    ]
                }"
                >
                    ${word}
            </span>`;
        });
        input = input.replaceAll(kokoroRegex, coloredWrappedWords.join("").toString());
        return input;
    }
</script>

<svelte:head>
    <title>CoreProject</title>
</svelte:head>

{#if status === 404}
    <div class="flex items-center justify-center h-screen flex-col text-center gap-12">
        <Confused width={414} height={123} />
        <h1 class="text-indigo-700 text-3xl">
            <b>{status}</b>
            -
            <b>{error.message}</b>
        </h1>
        <p class="w-[70vw] font-bold">
            {@html formatKokoroColor(
                `Our hardworking kokoro-chan was unable to find that page. While she collects more data on it, why don’t you go back home, explore some random anime, browse the forums or come say hi!`
            )}
        </p>
    </div>
{:else if status === 500}
    <div class="flex items-center justify-center h-screen flex-col text-center gap-12">
        <Overworked width="387" height="114" />
        <h1 class="text-indigo-700 text-3xl">
            <b>{status}</b>
            -
            <b>{error.message}</b>
        </h1>
        <p class="w-[70vw] font-bold">
            {@html formatKokoroColor(
                `Uh-oh, looks like our cute kokoro-chan worked really hard for the past few days and has now fallen asleep. You can wait for her to wake up by looking at the status page, or come say hi to other fellow kokoro-chan worshippers! ah- also let’s wish her sweet dreams!`
            )}
        </p>
    </div>
{/if}
