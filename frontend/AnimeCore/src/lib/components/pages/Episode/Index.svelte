<script lang="ts">
    import { page } from "$app/stores";
    import Navbar from "$components/shared/Navbar.svelte";
    export let episode_data: {
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
    export let anime_data: {
        id: number;
        mal_id: number;
        anilist_id: number;
        kitsu_id: number;
        name: string;
        name_japanese: string;
        source: string;
        aired_from: string;
        aired_to: string;
        banner: string;
        cover: string;
        banner_background_color: string;
        cover_background_color: string;
        synopsis: string;
        background: string;
        rating: string;
        theme_openings: string;
        theme_endings: string;
        updated: string;
        name_synonyms: [];
        genres: string;
        themes: string;
        studios: string;
        producers: string;
        characters: string;
        episodes: string;
        recommendations: [number];
        episodes_count: number;
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
            height: "800px",
            width: "1280px"
        },
        normal: {
            height: "50vh",
            width: "50vw"
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
                    style="height:{widthMapping[videoPlayerWidth]['height']}"
                >
                    {#each Object.entries(episode_data?.providers) as item}
                        {@const key = item[0]}
                        {@const value = item[1]}
                        {@const url = "https://google.com" ?? `https://sbbrisk.com/e/${value}.html`}
                        {@const player_height = widthMapping[videoPlayerWidth]["height"]}
                        {@const player_width = widthMapping[videoPlayerWidth]["width"]}
                        {#if key === "streamsb"}
                            <iframe
                                title={episode_data?.episode_name}
                                src={url}
                                class="bg-black"
                                style="height:{player_height}; width:{player_width};"
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
                            class="divider divider-horizontal ml-24 h-[250px] self-center before:bg-info after:bg-info"
                        />
                    {/if}
                    <div
                        class="flex text-white {videoPlayerWidth === 'normal'
                            ? 'ml-24 flex-col'
                            : 'flex-row'}"
                    >
                        <div class="flex flex-col">
                            <span class="font-bold">Episodes</span>
                            <div class="mt-8 grid grid-cols-8 gap-4">
                                {#each Array(anime_data?.episodes_count + 10).fill(0) as _, index}
                                    {@const actual_index = index >= 0 ? index + 1 : index}
                                    {@const button_active =
                                        Number($page.params.episode_number) === actual_index}
                                    <a
                                        href="./{actual_index}"
                                        class="group btn-square btn-sm btn hover:border-2 hover:border-secondary hover:bg-transparent {button_active
                                            ? 'border-2 border-secondary bg-transparent'
                                            : 'bg-[#87849e]'}"
                                    >
                                        <span
                                            class="font-bold group-hover:text-white {button_active
                                                ? 'text-white'
                                                : 'text-zinc-700'}"
                                        >
                                            {actual_index}
                                        </span>
                                    </a>
                                {/each}
                            </div>
                        </div>
                        <div
                            class="divider mt-10 w-[200px] self-center before:bg-info after:bg-info"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
