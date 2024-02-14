<script lang="ts">
    import Chevron from "$icons/Chevron/Index.svelte";
    import Settings from "$icons/Settings/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";
    import Recent from "$icons/Recent/Index.svelte";
    import Notification from "$icons/Notification/Index.svelte";
    import Language from "$icons/Language/Index.svelte";
    import Preference from "$icons/Preference/Index.svelte";
    import Moon from "$icons/Moon/Index.svelte";
    import CoreProjectText from "$icons/CoreProjectText/Index.svelte";

    import LatestEpisodes from "$components/specific/LatestEpisodes/Index.svelte";
    import LatestAnimes from "$components/specific/LatestAnimes/Index.svelte";
    import MyAnimeList from "$components/specific/MyAnimeList/Index.svelte";

    export let latest_animes: string;
    export let latest_episodes: string;
    export let my_anime_list: string;
</script>

<div class="mt-16 block md:mt-0 md:p-[1.25vw] md:pr-[3.75vw]">
    <div class="flex flex-col justify-between md:flex-row">
        <LatestAnimes {latest_animes} />

        <div class="hidden w-[21.5625vw] md:block">
            <div class="flex items-center justify-between pr-[0.75vw]">
                <div class="flex items-center gap-[0.625vw]">
                    <span class="text-[1.25vw] font-bold">Latest Episodes</span>
                    <button class="btn btn-secondary hidden min-h-full rounded-[0.1875vw] p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                        <Settings class="w-[0.9vw] opacity-75" />
                    </button>
                </div>
                <button class="btn btn-neutral min-h-max rounded-[0.3vw] p-0 text-[0.9vw] font-semibold md:h-[2vw] md:px-[0.5vw]">
                    <span>Full List</span>
                    <ArrowUpRight class="w-[1vw]" />
                </button>
            </div>
            <LatestEpisodes {latest_episodes} />

            <div class="mt-[0.75vw] flex items-start justify-between gap-[2vw] pr-[0.75vw]">
                <span class="text-[0.75vw] font-semibold md:leading-[1.25vw]">showing recently aired episodes from your Anime List</span>
                <button class="btn btn-secondary p-0 text-[0.75vw] font-semibold text-warning">Change to All</button>
            </div>
        </div>
        <div class="relative mt-[2.75vw] hidden h-[24.5vw] w-[16.625vw] md:block">
            <div class="absolute h-full w-full rounded-[0.875vw] object-cover object-center">
                <img
                    class="absolute h-full w-full rounded-[0.875vw] object-cover object-center"
                    src="https://i.pinimg.com/originals/b7/25/12/b725125aaebafbcbf2fb3886a55d2d6f.jpg"
                    alt=""
                    loading="lazy"
                />
            </div>
            <div class="absolute inset-0 bg-gradient-to-t from-secondary from-[1%] to-secondary/25"></div>
            <div class="absolute inset-0 bg-gradient-to-r from-secondary/50 to-secondary/25"></div>
            <div class="absolute inset-0 flex flex-col justify-between px-[1.875vw] pt-[2vw] text-accent">
                <div class="flex flex-col gap-[0.2w]">
                    <span class="text-[1.5vw] font-bold leading-[1vw]">Welcome</span>
                    <span class="text-[0.875vw] font-semibold leading-[2.5vw]">Jump quickly into</span>
                </div>
                <div class="mt-[1vw] flex flex-col gap-[0.75vw]">
                    <div class="flex items-center gap-[1vw]">
                        <button class="btn btn-warning h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Chat class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <span class="text-[1vw] font-bold">Forums</span>
                    </div>
                    <div class="flex items-center gap-[1vw]">
                        <button class="bg-surface-50 btn btn-warning h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Recent class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <span class="text-[1vw] font-bold">Last watched anime</span>
                    </div>
                    <div class="flex items-center gap-[1vw]">
                        <button class="bg-surface-50 btn btn-warning h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Notification class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <span class="text-[1vw] font-bold">Notifications</span>
                    </div>
                </div>
                <div class="mt-[0.4vw]">
                    <span class="text-[0.9vw] font-semibold leading-none">More</span>
                    <div class="mt-[0.75vw] flex gap-[0.9375vw]">
                        <button class="btn btn-accent h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Language class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <button class="btn btn-accent h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Preference class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <button class="btn btn-accent h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Moon class="text-surface-900 w-[1.25vw]" />
                        </button>
                        <button class="bg-surface-50 btn btn-accent h-[2.5vw] min-h-max w-[2.5vw] rounded-[0.375vw] p-0">
                            <Settings class="text-surface-900 w-[1.25vw]" />
                        </button>
                    </div>
                </div>
                <CoreProjectText />
            </div>
        </div>
    </div>
    <div class="flex flex-col p-4 pt-7 md:mb-[1vw] md:mt-[2.1875vw] md:flex md:w-[68vw] md:p-0">
        <div class="flex items-center gap-[0.625vw]">
            <span class="text-lg font-bold md:text-[1.25vw]">My List</span>
            <button class="btn btn-secondary hidden min-h-full rounded-[0.1875vw] p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                <Settings class="w-[0.9vw] opacity-75" />
            </button>
        </div>
        <div class="flex items-center justify-between">
            <span class="text-surface-50 text-sm md:text-[1vw] md:font-semibold">7 anime in Watching</span>
            <div class="hidden items-center gap-[1vw] md:flex">
                <button class="bg-surface-400 btn btn-neutral h-[2.25vw] min-h-max w-[6.625vw] gap-[0.625vw] rounded-[0.375vw] p-0 text-[0.875vw] font-semibold">
                    Watching
                    <Chevron class="w-[1vw]" />
                </button>
                <button class="bg-surface-400 btn btn-neutral h-[2.25vw] min-h-max w-[5.625vw] gap-[0.625vw] rounded-[0.375vw] p-0 text-[0.875vw] font-semibold">
                    Full List
                    <ArrowUpRight class="w-[1vw]" />
                </button>
            </div>
            <div class="md:hidden">
                <button class="btn btn-secondary h-max min-h-max gap-2 p-0 text-sm">
                    See all
                    <Chevron class="text-primary-400 w-4 -rotate-90" />
                </button>
            </div>
        </div>
        <div class="relative mt-4 grid grid-cols-3 gap-3 md:mt-[1vw] md:grid-cols-5 md:gap-[1.25vw]">
            <MyAnimeList
                {my_anime_list}
                dropdown_class="pl-3"
            />
        </div>
    </div>
</div>
