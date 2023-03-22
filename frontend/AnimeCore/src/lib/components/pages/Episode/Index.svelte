<script lang="ts">
    import Navbar from "$components/shared/Navbar.svelte";
    export let data: {
        id: number;
        episode_number: number;
        episode_name: string;
        episode_thumbnail: string;
        episode_summary: string;
        episode_length: number;
        providers: { streamsb: string };
        episode_comments: Array<string>;
        episode_timestamps: Array<string>;
    };

    let htmlIFrameElement: HTMLIFrameElement | undefined = undefined;
    $: {
        if (htmlIFrameElement) {
            // streamsb
            let document = htmlIFrameElement.contentWindow?.document;
            let htmlVidoeElement = document?.querySelector(".jw-video") as HTMLVideoElement;
            htmlVidoeElement.currentTime;
        }
    }
</script>

<div class="relative grid h-screen">
    <div class="absolute inset-0 grid h-screen w-screen">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 pl-6 pb-0 md:pr-[72px] md:pl-20">
                    <Navbar />
                </div>
                <div class="mx-6 mt-0 flex flex-col items-center md:mx-20">
                    {#each Object.entries(data?.providers) as item}
                        {@const key = item[0]}
                        {@const value = item[1]}
                        {#if key === "streamsb"}
                            <iframe
                                bind:this={htmlIFrameElement}
                                class="h-[200px] w-[80vw] md:h-[80vh]"
                                title={data?.episode_name}
                                src="https://sbbrisk.com/e/{value}.html"
                                frameborder="0"
                                marginwidth="0"
                                marginheight="0"
                                scrolling="NO"
                                allowfullscreen
                            />
                        {:else if key === "doodstream"}
                            pass
                        {/if}
                    {/each}
                </div>
            </div>
        </div>
    </div>
</div>
