<script lang="ts">
    import Chevron from "$icons/Chevron/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import Edit from "$icons/Edit/Index.svelte";

    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";

    import { swipe } from "svelte-gestures";
    import { Timer as EasyTimer} from "easytimer.js";
    import { tweened } from "svelte/motion";
    import { FormatDate } from "$functions/format_date";
    import { blur } from "svelte/transition";

    export let latest_animes: {
        id: number;
        name: string;
        type: string;
        episodes: number;
        status: string;
        release_date: string;
        studio: string;
        genres: string[];
        synopsis: string;
        image: string;
    }[];

    const slider_delay = 10,
        timer = new EasyTimer({
            target: {
                seconds: slider_delay
            },
            precision: "secondTenths"
        }),
        slide_buttons = [
            { background: "bg-accent", border: "border-accent" },
            { background: "bg-info", border: "border-info" },
            { background: "bg-warning", border: "border-warning" },
            { background: "bg-white", border: "border-white" },
            { background: "bg-primary", border: "border-primary" },
            { background: "bg-error", border: "border-error" }
        ];

        /* Slider codes */
    let main_hero_slider_element: HTMLElement,
        main_hero_slide_active_index = 0;

    const add_one_to_main_hero_slide_active_index = () => {
            if (main_hero_slide_active_index + 1 === latest_animes.length) {
                main_hero_slide_active_index = 0;
                return;
            }
            main_hero_slide_active_index += 1;
        },
        minus_one_to_main_hero_slide_active_index = () => {
            if (main_hero_slide_active_index === 0) {
                main_hero_slide_active_index = latest_animes.length - 1;
                return;
            }
            main_hero_slide_active_index -= 1;
        },
        swipe_handler = (event: CustomEvent) => {
            const direction = event.detail.direction;
            timer.reset();

            if (direction === "left") {
                add_one_to_main_hero_slide_active_index();
            } else if (direction === "right") {
                minus_one_to_main_hero_slide_active_index();
            }
        };

    // Progress bar code //
    let progress_value = 0,
        tweened_progress_value = tweened(progress_value);
    $: tweened_progress_value.set(progress_value);

    timer.on("targetAchieved", () => {
        // change slider
        add_one_to_main_hero_slide_active_index();
        timer.reset();
    });

    timer.on("secondTenthsUpdated", () => {
        const time = timer.getTotalTimeValues().secondTenths,
            value = (100 / slider_delay) * (time / 10);

        progress_value = value;
    });
</script>

<latest-anime-swiper
    class="relative h-96 w-full md:h-[27.875vw] md:w-[42.1875vw]"
    use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: "pan-y" }}
    on:swipe={swipe_handler}
    bind:this={main_hero_slider_element}
>
    {#each latest_animes as anime, index}
        {@const active = index === main_hero_slide_active_index}
        {@const formated_aired_on = new FormatDate(anime.release_date).format_to_season}

        {#if active}
            <anime-slides
                role="presentation"
                class="absolute inset-0 md:bottom-[2vw]"
                transition:blur
                on:mouseenter={() => {
                    timer?.pause();
                }}
                on:mouseleave={() => {
                    timer?.start();
                }}
                on:touchstart={() => {
                    timer?.pause();
                }}
                on:touchend={() => {
                    timer?.start();
                }}
            >
                <img
                    src={anime.image}
                    alt=""
                    class="absolute h-full w-full object-cover object-center md:rounded-t-[0.875vw]"
                />

                <div class="absolute inset-0 bg-gradient-to-t from-secondary/90 to-secondary/50 md:to-surface-900/25" />
                <div class="absolute inset-0 hidden bg-gradient-to-r from-surface-900 to-surface-900/25 md:flex md:from-surface-900/50" />

                <div class="absolute bottom-7 left-7 flex flex-col md:bottom-0 md:left-0 md:px-[3.75vw] md:py-[2.625vw]">
                    <span class="text-white text-3xl font-bold md:text-[2vw] md:leading-[2.375vw]">{anime.name}</span>
                    <div class="text-base uppercase font-semibold text-white/90 md:hidden md:text-[2vw] md:leading-[2.375vw]">
                        { anime.name }
                    </div>
                    <div class="py-2 md:pb-0 flex flex-wrap items-center gap-2 md:pt-4 text-xs font-semibold text-white/90 md:gap-[0.65vw] md:pt-[0.5vw] md:text-[0.9375vw]">
                        <span class="leading-[1.125vw]">
                            {anime.type}
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">
                            {anime.episodes} eps
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">Completed</span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="capitalize leading-[1.125vw]">
                            {formated_aired_on}
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">
                            {anime.studio}
                        </span>
                    <div>

                    <anime-genres class="flex gap-2 pb-2 pt-3 md:gap-[0.5vw] md:pt-0">
                        {#each anime.genres as genre}
                            <span
                                class="rounded-lg bg-secondary p-2 px-3 text-xs md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.4vw] md:text-[0.75vw] md:font-semibold capitalize leading-none"
                            >
                                { genre }
                            </span>
                        {/each}
                    </anime-genres>

                    <ScrollArea
                        gradient_mask
                        offset_scrollbar
                        parent_class="max-h-16 md:max-h-[6vw] hidden md:flex"
                        class="text-xs font-medium leading-4 text-surface-200 md:pt-[0.75vw] md:text-[0.85vw] md:leading-[1.1vw]"
                    >
                        {anime.synopsis}
                    </ScrollArea>

                    <div class="mb-2 mt-5 flex items-center gap-2 md:mb-0 md:mt-[1.5vw] md:gap-[1vw]">
                        <button
                            class="btn btn-warning leading-none flex px-6 py-4 md:py-[1vw] md:px-[1.25vw] min-h-max h-max justify-center gap-2 rounded-xl text-base text-secondary font-bold md:rounded-[0.625vw] md:text-[0.875vw] md:gap-[0.5vw]"
                        >
                            <Play class="w-4 text-surface-900 md:w-[1vw]" />
                            <span>Ep 1</span>
                        </button>
                        <a href="/anime/mal/40748">
                            <button
                                class="btn btn-secondary leading-none flex px-6 py-4 md:py-[1vw] md:px-[1.25vw] min-h-max h-max items-center justify-center rounded-xl text-base font-semibold md:gap-[0.5vw] md:rounded-[0.5vw] md:text-[0.875vw] md:font-bold"
                            >
                                <Info class="w-5 text-surface-50 md:w-[1.25vw]" />
                                <span>Details</span>
                            </button>
                        </a>
                        <button
                            class="btn btn-secondary leading-none p-4 md:p-[0.9vw] min-h-max h-max rounded-xl bg-surface-900 text-[3vw] font-bold text-surface-50s md:rounded-[0.5vw] md:text-[0.875vw]"
                        >
                            <Edit class="w-4 text-surface-50 md:w-[1.25vw]" />
                        </button>
                    </div>
                </div>
            </anime-slides>
        {/if}
    {/each}

    <div class="absolute bottom-0 flex w-full flex-col">
        <div
            class="bg-warning h-[0.2rem] md:h-[0.145vw] {slide_buttons[main_hero_slide_active_index].background}"
            style="width: {$tweened_progress_value}%;"
        />

        <div class="hidden w-full grid-cols-6 gap-[0.9375vw] md:mt-[1.25vw] md:grid">
            {#each latest_animes as _, index}
                <button
                    class="col-span-1 h-[0.625vw] w-full rounded-[0.1875vw] border-[0.15vw] {slide_buttons[index].border} transition duration-300 hover:border-surface-50/50 {index === main_hero_slide_active_index ? slide_buttons[index].background : ''}"
                    on:click={() => {
                        timer?.reset();
                        timer?.start();
                        main_hero_slide_active_index = index;
                    }}
                />
            {/each}
        </div>
    </div>

    <button
        class="btn btn-primary text-accent min-h-max p-0 absolute -left-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] md:flex"
        on:click={() => {
            timer?.reset();
            timer?.start();
            minus_one_to_main_hero_slide_active_index();
        }}
    >
        <Chevron class="w-[1.25vw] rotate-90" />
    </button>
    <button
        class="btn btn-primary text-accent min-h-max p-0 absolute -right-[1vw] top-[12vw] z-20 hidden h-[2.25vw] w-[2.25vw] rounded-[0.375vw] bg-secondary-800 md:flex"
        on:click={async () => {
            timer?.reset();
            timer?.start();
            add_one_to_main_hero_slide_active_index();
        }}
    >
        <Chevron class="w-[1.25vw] -rotate-90" />
    </button>
</latest-anime-swiper>