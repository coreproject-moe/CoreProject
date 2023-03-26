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

    // let htmlIFrameElement: HTMLIFrameElement | undefined = undefined;
    // $: {
    //     if (htmlIFrameElement) {
    //         // streamsb
    //         let document = htmlIFrameElement.contentWindow?.document;
    //         let htmlVidoeElement = document?.querySelector(".jw-video") as HTMLVideoElement;
    //         htmlVidoeElement.currentTime;
    //     }
    // }

    const widthMapping = {
        wide: {
            height: 800,
            width: 1280
        },
        normal: {
            height: 500,
            width: 800
        }
    };
    const videoPlayerWidth: keyof typeof widthMapping = "normal";
</script>

<div class="relative grid h-screen ">
    <div class="absolute inset-0 grid h-screen w-screen">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 pl-6 pb-0 md:pr-[72px] md:pl-20">
                    <Navbar />
                </div>
                <div
                    class="mx-6 mt-0 flex items-start md:mx-20 {videoPlayerWidth === 'normal'
                        ? 'flex-row'
                        : 'flex-col'}"
                    style="height:{widthMapping[videoPlayerWidth]['height']}px"
                >
                    {#each Object.entries(data?.providers) as item}
                        {@const key = item[0]}
                        {@const value = item[1]}
                        {@const url = "https://google.com" ?? `https://sbbrisk.com/e/${value}.html`}
                        {@const player_height = widthMapping[videoPlayerWidth]["height"]}
                        {@const player_width = widthMapping[videoPlayerWidth]["width"]}
                        {#if key === "streamsb"}
                            <iframe
                                title={data?.episode_name}
                                src={url}
                                class="bg-black"
                                style="height:{player_height}px; width:{player_width}px;"
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
                    {#if videoPlayerWidth === "normal"}
                        <div
                            class="divider divider-horizontal ml-24 h-[250px] self-center before:bg-white after:bg-white"
                        />
                    {/if}
                    <div class="flex">ga</div>
                </div>
            </div>
        </div>
    </div>
</div>
