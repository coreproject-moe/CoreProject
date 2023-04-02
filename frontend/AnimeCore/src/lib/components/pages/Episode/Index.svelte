<script lang="ts">
    import { page } from "$app/stores";

    import Navbar from "$components/shared/Navbar.svelte";
    import { UrlMaps } from "$data/urls";
    import ChevronsRight from "$icons/Chevrons-Right.svelte";
    import { responsiveMode } from "$store/Responsive";
    import MaximizeInward from "$icons/Maximize-Inward.svelte";
    import MaximizeOutward from "$icons/Maximize-Outward.svelte";

    import { video_player_width } from "$store/VideoPlayerWidth";

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
    const backend_mapping = new UrlMaps();

    let htmlIFrameElement: HTMLIFrameElement | undefined = undefined;
    $: {
        if (htmlIFrameElement) {
            // streamsb
            let document = htmlIFrameElement.contentWindow?.document;
            // get value from localStorage
            // format is domain.id
        }
    }

    let mobile: boolean;

    $: mobile = $responsiveMode === "mobile";

    const widthMapping = {
        wide: {
            height: "80vh",
            width: "89vw"
        },
        normal: {
            height: "50vh",
            width: "50vw"
        },
        mobile: {
            height: "30vh",
            width: "89vw"
        }
    };
</script>

<div class="relative grid h-screen items-center overflow-x-hidden">
    <div class="absolute inset-0 grid h-screen w-screen">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pb-0 pl-6 pr-6 pt-8 md:pl-20 md:pr-[72px]">
                    <Navbar />
                </div>
                <div
                    class="mx-6 mt-0 flex items-start md:mx-20 {$video_player_width === 'normal'
                        ? 'mt-20 flex-row'
                        : 'mt-2 flex-col'}"
                    style="min-height:{widthMapping[$video_player_width ?? 'normal']['height']}"
                >
                    <div class="flex flex-col">
                        {#each Object.entries(episode_data?.providers) as item}
                            {@const key = item[0]}
                            {@const value = item[1]}
                            {@const player_height =
                                widthMapping[$video_player_width ?? "normal"]["height"]}
                            {@const player_width =
                                widthMapping[$video_player_width ?? "normal"]["width"]}
                            {#if key === "streamsb"}
                                {@const url = `https://sbbrisk.com/e/${value}.html`}
                                <iframe
                                    title={episode_data?.episode_name}
                                    src={url}
                                    class="self-center rounded-lg bg-black"
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
                        <div
                            class="mt-6 flex h-10 max-h-10 w-full items-center justify-between rounded-lg bg-info px-4 font-semibold"
                        >
                            <div class="flex gap-7">
                                <a
                                    href={Number($page.params.episode_number) !== 1
                                        ? `./${Number($page.params.episode_number) - 1}`
                                        : "javascript:void(0)"}
                                    class="flex gap-2 {Number($page.params.episode_number) !== 1
                                        ? 'text-black'
                                        : 'pointer-events-none text-zinc-500'}"
                                >
                                    <ChevronsRight
                                        class="rotate-180"
                                        width="24"
                                        height="24"
                                    />
                                    Previous
                                </a>
                            </div>

                            <div class="flex gap-4 text-black">
                                {#if $video_player_width === "wide"}
                                    <p class="flex items-center">Shrink</p>
                                    <button
                                        class="btn-square btn-xs btn"
                                        on:click={() => {
                                            $video_player_width = "normal";
                                        }}
                                    >
                                        <MaximizeInward
                                            width="20"
                                            height="20"
                                        />
                                    </button>
                                {:else if $video_player_width === "normal"}
                                    <p class="flex items-center">Expand</p>
                                    <button
                                        class="btn-square btn-xs btn"
                                        on:click={() => {
                                            $video_player_width = "wide";
                                        }}
                                    >
                                        <MaximizeOutward
                                            width="25"
                                            height="25"
                                        />
                                    </button>
                                {/if}
                            </div>

                            <div class="flex gap-7">
                                <a
                                    href={Number($page.params.episode_number) !==
                                    anime_data?.episodes_count
                                        ? `./${Number($page.params.episode_number) + 1}`
                                        : "javascript:void(0)"}
                                    class="flex gap-2 {Number($page.params.episode_number) !==
                                    anime_data?.episodes_count
                                        ? 'text-black'
                                        : 'pointer-events-none text-zinc-500'}"
                                >
                                    Next
                                    <ChevronsRight
                                        width="24"
                                        height="24"
                                    />
                                </a>
                            </div>
                        </div>
                    </div>
                    {#if $video_player_width === "normal"}
                        <div
                            class="divider divider-horizontal ml-24 h-[250px] self-center before:bg-info after:bg-info"
                        />
                    {/if}

                    <div
                        class="flex {$video_player_width === 'normal'
                            ? 'ml-24 flex-col'
                            : 'mt-16 w-full flex-row justify-between'}"
                    >
                        <div class="flex flex-col">
                            <span class="font-bold text-white">Episodes</span>
                            <div
                                class="mt-8 grid {$video_player_width === 'normal'
                                    ? 'w-[340px] grid-cols-8'
                                    : $video_player_width === 'wide'
                                    ? 'w-[490px] grid-cols-12'
                                    : $video_player_width === 'mobile'
                                    ? 'w-full grid-cols-12'
                                    : ''} gap-x-2 gap-y-4 self-start"
                            >
                                {#each Array(anime_data?.episodes_count).fill(0) as _, index}
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
                        {#if $video_player_width === "normal"}
                            <div
                                class="divider mb-16 mt-10 w-[200px] self-center before:bg-info after:bg-info"
                            />
                        {:else if $video_player_width === "wide"}
                            <div
                                class="divider divider-horizontal mb-16 mt-10 h-[200px] self-center before:bg-info after:bg-info"
                            />
                        {/if}
                        <div class="hidden flex-row md:flex">
                            <anime-image-card class="card flex h-[150px] w-[100px] self-center">
                                <img
                                    class="rounded-lg object-contain"
                                    src={backend_mapping.DOMAIN + anime_data?.banner}
                                    alt="{anime_data.name} banner image"
                                    width="100"
                                    height="150"
                                />
                            </anime-image-card>
                            <anime-info
                                class="ml-9 w-36 {$video_player_width === 'wide'
                                    ? 'self-center'
                                    : ''} :"
                            >
                                <p class="self-end text-lg font-bold leading-5 text-white">
                                    {anime_data?.name}
                                </p>
                                <p class="text-default mt-3 text-sm font-bold">
                                    currently watching
                                </p>
                                <p class="mt-2 font-bold">Episode {$page.params.episode_number}</p>
                                <a
                                    href="../"
                                    class="btn-primary btn mt-6"
                                >
                                    <span class="font-bold text-white">Details</span>
                                    <ChevronsRight
                                        width={18}
                                        height={18}
                                        color="white"
                                    />
                                </a>
                            </anime-info>
                            <div
                                class="divider divider-horizontal h-[30px] self-center before:bg-secondary after:bg-secondary"
                            />
                            <div class="flex flex-col gap-3 self-center">
                                {#each [{ Score: 79 }, { Status: "Watching" }, { Episode: `${$page.params.episode_number}/${anime_data?.episodes_count}` }, { "Your Score": "Not Rated" }] as item}
                                    <div class="flex flex-row gap-1 text-xs">
                                        <p class="font-bold capitalize text-white">
                                            {Object.keys(item)}:
                                        </p>
                                        <p class="font-bold text-warning">
                                            {Object.values(item)}
                                        </p>
                                    </div>
                                {/each}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
