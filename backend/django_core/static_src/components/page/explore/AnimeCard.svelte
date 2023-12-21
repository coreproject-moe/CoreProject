<script lang="ts">
    export let anime_name: string;
    export let anime_image: string;
    export let anime_total_episodes: number;
    export let anime_synopsis: string;
    export let anime_studio: string[];
    export let anime_genres: string[];

    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import Star from "$icons/Star/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Info from "$icons/Info/Index.svelte";

    // Bindings
    let main_element: HTMLElement,
        dropdown_cont_el: HTMLButtonElement;

    let is_overflowing: boolean;

    // Styles

    // Both of these functions require that parentElement is not changed
    // Please tatoo dont change the position of the element
    function calculate_style() {
        const dropdown_cont_rect = dropdown_cont_el.getBoundingClientRect();
        const main_element_rect = main_element.getBoundingClientRect();
        const parent_element_gap = parseInt((getComputedStyle(main_element.parentElement!)?.gap));

        // udpate position
        is_overflowing = main_element_rect.right + dropdown_cont_rect.width + parent_element_gap > window.innerWidth;
    }
</script>

<div
    class="dropdown dropdown-hover"
    class:dropdown-right={!is_overflowing}
    class:dropdown-left={is_overflowing}
    bind:this={main_element}
>
    <button
        on:mouseenter|preventDefault={calculate_style}
        class="relative"
        tabindex="0"
        aria-expanded={false}
    >
        <div class="h-60 w-full rounded-lg object-cover object-center md:h-[20vw] md:rounded-[0.5vw]">
            <img
                class="h-60 w-full rounded-lg object-cover object-center md:h-[20vw] md:rounded-[0.5vw]"
                src={anime_image}
                alt={anime_name}
                style=""
                loading="lazy"
            />
        </div>
        <div class="absolute inset-x-0 bottom-0 rounded-b-lg backdrop-blur md:rounded-b-[0.5vw]">
            <div class="flex flex-col gap-1 bg-secondary/95 p-3 md:gap-[0.35vw] md:p-[1vw]">
                <ScrollArea
                    gradient_mask
                    offset_scrollbar
                    parent_class="flex md:max-h-[1.35vw] md:leading-[1.35vw] hover:max-h-[10vw] duration-300"
                    class="line-clamp-1 text-sm font-semibold md:line-clamp-none md:text-[1vw]"
                >
                    {anime_name}
                </ScrollArea>
                <span class="text-surface-50 flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                    {anime_studio}
                </span>
            </div>
        </div>
    </button>

    <button
        bind:this={dropdown_cont_el}
        tabindex="0"
        class="dropdown-content top-0 z-10 hidden flex-col leading-none md:flex md:w-[20vw] md:px-[1.5vw]"
    >
        <div class="flex flex-col bg-neutral text-start md:gap-[0.35vw] md:rounded-[0.75vw] md:rounded-t-[0.3vw] md:p-[1vw]">
            <span class="font-semibold text-accent md:text-[1vw] md:leading-[1.25vw]">{anime_name}</span>
            <div class="text-surface-50 flex w-full items-center md:gap-[0.35vw] md:text-[0.8vw]">
                <div class="flex items-center md:gap-[0.5vw]">
                    <Star class="md:w-[0.9vw]" />
                    <span class="text-surface-50 leading-none md:text-[0.8vw]">4.5 rating</span>
                </div>
                <Circle class="w-1 md:w-[0.25vw]" />
                <span>TV</span>
                <Circle class="w-1 md:w-[0.25vw]" />
                <span>{anime_total_episodes} episdoes</span>
            </div>
            <div class="text-surface-50 md:text-[0.75vw]">
                <span>{anime_studio}</span>
            </div>
            <div class="flex items-center md:my-[0.35vw] md:gap-[0.5vw]">
                {#each anime_genres as item}
                    <genre class="bg-warning font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">
                        {item}
                    </genre>
                {/each}
            </div>
            <ScrollArea
                gradient_mask
                offset_scrollbar
                parent_class="md:max-h-[4vw]"
                class="text-surface-50 md:text-[0.8vw] md:leading-[1vw]"
            >
                {anime_synopsis}
            </ScrollArea>
            <div class="divider md:m-0 md:before:h-[0.15vw] md:after:h-[0.15vw]"></div>
            <div class="flex items-center md:gap-[0.5vw]">
                <a
                    href="/anime/mal/1/episode/1"
                    class="btn btn-primary h-[2.75vw] min-h-full flex-1 leading-none text-accent md:rounded-[0.5vw]"
                >
                    <Play class="md:w-[0.9vw]" />
                    <span class="font-semibold md:text-[0.9vw]">Start Watching</span>
                </a>
                <a
                    href="/anime/mal/1"
                    class="btn btn-square h-[2.75vw] min-h-full p-0 leading-none md:rounded-[0.5vw]"
                >
                    <Info class="md:w-[1.2vw]" />
                </a>
            </div>
        </div>
    </button>
</div>
