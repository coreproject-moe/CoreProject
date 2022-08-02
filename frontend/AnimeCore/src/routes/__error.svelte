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

    import FourZeroFour from "$components/errors/[404].svelte";
    import FiveZeroZero from "$components/errors/[500].svelte";

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
            </span>`
                .replace(/\s+/g, " ")
                .trim();
        });
        input = input.replaceAll(kokoroRegex, coloredWrappedWords.join("").toString());
        return input;
    }

    const errorPages = [
        {
            status: 404,
            text: formatKokoroColor(
                `Our hardworking kokoro-chan was unable to find that page. While she collects more data on it, why don’t you go back home, explore some random anime, browse the forums or come say hi!`
            ),
            component: FourZeroFour
        },
        {
            status: 500,
            text: formatKokoroColor(
                `Uh-oh, looks like our cute kokoro-chan worked really hard for the past few days and has now fallen asleep. You can wait for her to wake up by looking at the status page, or come say hi to other fellow kokoro-chan worshippers! ah- also let’s wish her sweet dreams!`
            ),
            component: FiveZeroZero
        }
    ];

    let errorPage = errorPages.find((item) => item.status === status);
</script>

<svelte:head>
    <title>CoreProject</title>
</svelte:head>

<svelte:component
    this={errorPage?.component}
    {status}
    errorMessage={error?.message}
    errorText={errorPage?.text}
/>
