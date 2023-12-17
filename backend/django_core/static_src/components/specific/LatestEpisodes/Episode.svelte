<script lang="ts">
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import { FormatDate } from "$functions/format_date";
    import Play from "$icons/Play/Index.svelte";
    import { slide } from "svelte/transition";
    import { onMount } from "svelte";

    type Episode = {
        id: number;
        cover: string;
        name: string;
        episode_number: string;
        release_date: string;
        synopsis: string;
    };

    export let episode: Episode;

    /* Bindings */
    let ANIMATION_DURATION = 300;
    let scroll_area_element: HTMLElement | null = null,
        anime_episode: HTMLElement | null = null;

    let show_more_info = false;

    /** Bindings */
    onMount(() => (scroll_area_element = anime_episode?.parentElement?.parentElement!));

    function handle_mouseenter() {
        show_more_info = true;
    }

    function handle_mouseleave() {
        show_more_info = false;
    }

    function handle_animationstart() {
        const parent_element = anime_episode?.parentElement!;

        // Declare rects
        const parent_rect = parent_element?.getBoundingClientRect(), // taking parent not scroll_area_element
            anime_episode_rect = anime_episode?.getBoundingClientRect();

        const scroll_area_center = scroll_area_element?.offsetHeight! / 2;
        const anime_episode_center =
            anime_episode_rect?.top! - parent_rect?.top + anime_episode_rect?.height! / 2;
        const target_scroll_top =
            anime_episode_center -
                scroll_area_center +
                parseInt(getComputedStyle(parent_element)?.gap) || 0;

        scroll_area_element?.scroll({
            top: target_scroll_top,
            behavior: "smooth"
        });
    }

    const formated_episode_number = String(episode.episode_number).padStart(2, "0"),
        formated_release_date = new FormatDate(episode.release_date).format_to_time_from_now;
</script>

<div
    bind:this={anime_episode}
    on:mouseenter={handle_mouseenter}
    on:mouseleave={handle_mouseleave}
    role="group"
    class="group relative h-[5vw] shrink-0 duration-300 ease-in-out hover:h-[16vw]"
>
    <img
        src={episode.cover}
        alt=""
        class="absolute h-full w-full rounded-[0.75vw] object-cover object-center"
    />
    <div class="gradient absolute inset-0 bg-gradient-to-t from-secondary/75 to-transparent" />
    <div class="gradient absolute inset-0 bg-gradient-to-r from-secondary/50 to-transparent" />

    <div class="absolute inset-0 flex items-start justify-between p-[1.3125vw]">
        <div class="flex flex-col gap-[0.25vw]">
            <div class="text-[1vw] font-semibold leading-[1.1875vw] text-white">
                {episode.name}
            </div>
            <div class="flex items-center gap-[0.35vw] text-[0.8vw] text-accent">
                <span class="font-semibold">
                    Ep {formated_episode_number}
                </span>
                <span>
                    aired {formated_release_date}
                </span>
            </div>
        </div>
        <a
            href="/mal/{episode.id}/episode/{episode.episode_number}"
            class="btn btn-warning h-[2.5vw] min-h-max w-[2.5vw] rounded-full p-0 transition-colors duration-300 group-hover:btn-accent"
        >
            <Play class="w-[1vw]" />
        </a>
    </div>

    {#if show_more_info}
        <div
            in:slide={{ duration: ANIMATION_DURATION, delay: ANIMATION_DURATION * (2 / 3) }}
            out:slide={{ duration: ANIMATION_DURATION * (2 / 3) }}
            on:animationstart={handle_animationstart}
            class="absolute inset-x-0 bottom-0 flex flex-col gap-[0.5vw] p-[1.3125vw]"
        >
            <genres class="flex items-center md:my-[0.35vw] md:gap-[0.5vw]">
                {#each ["Action", "Romance", "Hentai"] as genre}
                    <genre
                        class="bg-accent font-semibold leading-none text-secondary md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]"
                    >
                        {genre}
                    </genre>
                {/each}
            </genres>
            <ScrollArea
                offset_scrollbar
                gradient_mask
                class="h-[6vw] text-[0.8vw] leading-[1vw] text-accent"
            >
                {episode.synopsis}
            </ScrollArea>
        </div>
    {/if}
</div>
