<script lang="ts">
    export let anime_name: string;
    export let anime_status: string;
    export let anime_image: string;
    export let anime_current_episodes: string;
    export let anime_total_episodes: string;

    // Pass styles
    export let dropdown_class: string;

    import { afterUpdate } from "svelte";
    import Dot from "$icons/Dot.svelte";
    import ScrollArea from "$components/minor/ScrollArea.svelte";
    import { cn } from "$functions/classname";

    let main_element: HTMLElement;

    // Styles
    let style_left: string;

    // Both of these functions require that parentElement is not changed
    // Please tatoo dont change the position of the element
    function calculate_style() {
        style_left = window.getComputedStyle(main_element).width;
    }

    afterUpdate(() => {
        calculate_style();
    });
</script>

<svelte:window
    on:resize={() => {
        calculate_style();
    }}
/>

<div
    class="dropdown dropdown-hover"
    bind:this={main_element}
>
    <button
        class="relative"
        tabindex="0"
        aria-expanded="false"
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
                    gradient_mask={true}
                    parent_class="flex self-start md:max-h-[1.35vw] md:leading-[1.35vw] hover:max-h-[10vw] duration-300"
                    class="line-clamp-1 text-sm font-semibold md:line-clamp-none md:text-[1vw]"
                >
                    {anime_name}
                </ScrollArea>
                <div class="text-surface-50 flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                    <span class="hidden capitalize md:flex">
                        {anime_status}
                    </span>
                    <Dot class="hidden opacity-75 md:flex md:w-[0.25vw]" />
                    <span>
                        {`${anime_current_episodes}/${anime_total_episodes}`}
                    </span>
                </div>
            </div>
        </div>
    </button>

    <button
        tabindex="0"
        class={cn(dropdown_class, "dropdown-content top-0 z-10 hidden flex-col leading-none md:flex md:w-[20vw]")}
        style="left:{style_left};"
    >
        <div class="flex flex-col bg-neutral md:gap-[0.35vw] md:rounded-[0.75vw] md:rounded-t-[0.3vw] md:p-[1vw]">
            <anime-name class="font-semibold text-accent md:text-[1vw] md:leading-[1.25vw]">
                {{ anime_name }}
            </anime-name>
            <div class="text-surface-50 flex items-center md:gap-[0.35vw] md:text-[0.8vw]">
                <rating class="flex items-center md:gap-[0.5vw]">
                    <svg
                        width="30"
                        height="30"
                        viewBox="0 0 30 30"
                        fill="yellow"
                        xmlns="http://www.w3.org/2000/svg"
                        color="yellow"
                        class="h-[1.1vw] w-[1.1vw]"
                    >
                        <path
                            d="M15 2.5L18.8625 10.325L27.5 11.5875L21.25 17.675L22.725 26.275L15 22.2125L7.275 26.275L8.75 17.675L2.5 11.5875L11.1375 10.325L15 2.5Z"
                            stroke="currentColor"
                            stroke-width="3"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        ></path>
                    </svg>
                    <span class="text-surface-50 leading-none md:text-[0.8vw]">4.5 rating</span>
                </rating>
                <svg
                    class="opacity-50 md:w-[0.25vw]"
                    viewBox="0 0 10 10"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <circle
                        cx="5"
                        cy="5"
                        r="5"
                        fill="currentColor"
                    ></circle>
                </svg>
                <anime-type>TV</anime-type>
                <svg
                    class="opacity-50 md:w-[0.25vw]"
                    viewBox="0 0 10 10"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <circle
                        cx="5"
                        cy="5"
                        r="5"
                        fill="currentColor"
                    ></circle>
                </svg>
                <episodes-count>
                    {{ anime_total_episodes }} episdoes
                </episodes-count>
            </div>
            <studio class="text-surface-50 md:text-[0.75vw]">
                <span>Bibury Animation Studios</span>
            </studio>
            <genres class="flex items-center md:my-[0.35vw] md:gap-[0.5vw]">
                <genre class="bg-warning font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">Action</genre>
                <genre class="bg-warning font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">Ecchi</genre>
                <genre class="bg-warning font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">sci-Fi</genre>
            </genres>
            <ScrollArea
                gradient_mask={true}
                parent_class="md:max-h-[4vw]"
                class="text-surface-50 md:text-[0.8vw] md:leading-[1vw]"
            >
                Azur Lane, a combination of all the different Camps in the world, was once successful in repelling the underwater menace, the Siren. Now splintered, they must face a new threat in Red Axis, former allies who crave to wield this otherworldly Siren technology for their own nefarious desires! Who will be victorious in the never-ending war between these battleship girls!? Akagami no
                Shirayuki-hime depicts Shirayuki's journey toward a new life at the royal palace of Clarines, as well as Zen's endeavor to become a prince worthy of his title. As loyal friendships are forged and deadly enemies formed, Shirayuki and Zen slowly learn to support each other as they walk their own paths.
            </ScrollArea>
            <div class="divider md:m-0 md:before:h-[0.15vw] md:after:h-[0.15vw]"></div>
            <options class="flex items-center md:gap-[0.5vw]">
                <a
                    href="/anime/mal/1/episode/4"
                    class="btn btn-primary h-[2.75vw] min-h-full flex-1 leading-none text-accent md:rounded-[0.5vw]"
                >
                    <!-- {% include "icons/play.html" with class="md:w-[0.9vw]" %} -->
                    <span class="font-semibold md:text-[0.9vw]">
                        Continue Ep
                        {{ anime_current_episodes }}
                    </span>
                </a>
                <a
                    href="/anime/mal/1"
                    class="btn btn-square h-[2.75vw] min-h-full p-0 leading-none md:rounded-[0.5vw]"
                >
                    <!-- {% include "icons/info.html" with class="md:w-[1.2vw]" %} -->
                </a>
            </options>
        </div>
    </button>
</div>
