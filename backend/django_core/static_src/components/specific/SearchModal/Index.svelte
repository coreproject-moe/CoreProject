<script lang="ts">
    import Search from "../../icons/Search/Index.svelte";
    import Circle from "../../icons/Circle/Index.svelte";
    import Cross from "../../icons/Cross/Index.svelte";
    import { search_modal_state } from "./store";
    import ScrollArea from "../../minor/ScrollArea/Index.svelte";

    // demo variables
    const ARR_MAX_LENGTH = 6;

    let active_index = 0,
        active_core: "anime" | "manga" | "sound" = "anime",
        search_query = "";

    // Bindings
    let dialog_element: HTMLDialogElement | null = null;

    const handle_search_key_down = async (e: KeyboardEvent) => {
            switch (e.key.toLowerCase()) {
                case "arrowdown":
                    active_index = (active_index + 1) % ARR_MAX_LENGTH;
                    break;
                case "arrowup":
                    active_index = (active_index - 1 + ARR_MAX_LENGTH) % ARR_MAX_LENGTH;
                    break;
                case "tab":
                    // do tab logic of switching core
                    console.log("Tab clicked");
                    break;
                default:
                    break;
            }
        },
        handle_core_mouse_enter = async (core: typeof active_core, index: number) => {
            active_index = index;
            active_core = core;
        };

    search_modal_state.subscribe((val) => {
        if (val) {
            dialog_element?.showModal();
            search_modal_state.set(false);
        }
    });
</script>

<dialog
    class="modal"
    bind:this={dialog_element}
>
    <div class="modal-box flex !max-w-fit flex-col items-center bg-secondary md:px-[2vw] md:py-[1vw]">
        <form class="relative flex h-[3.5vw] w-[40vw] items-center">
            <button
                class="btn absolute left-[1.25vw] min-h-max border-none !bg-transparent p-0"
                aria-label="Search"
            >
                <Search style="width: 1.25vw;" />
            </button>
            <input
                bind:value={search_query}
                on:keydown={handle_search_key_down}
                on:keypress={() => (active_index = 0)}
                type="text"
                placeholder="Search for animes, mangas and musics"
                class="h-full w-full rounded-[0.625vw] border-none bg-neutral pl-[3.50vw] text-[1.1vw] font-semibold text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-accent/75"
            />

            <button
                type="button"
                aria-label="Clear"
                class="btn absolute right-[1.25vw] min-h-max border-none !bg-transparent p-0"
                on:click={() => (search_query = "")}
            >
                <Cross style="width: 1.5vw; opacity: 0.7;" />
            </button>
        </form>

        <div class="mt-[1.5vw] flex gap-[4vw]">
            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">anime</span>
                <ScrollArea
                    offset_scrollbar
                    gradient_mask
                    parent_class="md:mt-[0.2vw] md:h-[30vw] md:w-[20vw]"
                    class="w-full"
                >
                    {#each Array(ARR_MAX_LENGTH) as _, index}
                        {@const is_active = active_core === "anime" && active_index === index}
                        <a
                            on:mouseenter={() => handle_core_mouse_enter("anime", index)}
                            href="/mal/"
                            class:bg-neutral={is_active}
                            class="flex w-full items-center gap-[1vw] rounded-[0.7vw] p-[0.8vw] transition duration-200 hover:bg-neutral"
                        >
                            <img
                                src="https://static1.cbrimages.com/wordpress/wp-content/uploads/2021/03/demon-slayer-banner.jpg"
                                alt={search_query}
                                class="h-[3.5vw] w-[3.5vw] rounded-[0.5vw] object-cover"
                            />
                            <div class="flex w-full flex-col">
                                <span class="text-[1.1vw] font-semibold leading-none text-white">Kimetsu no Yaiba</span>
                                <span class="text-surface-200 text-[0.7vw] font-medium uppercase leading-[1.5vw]">Demon slayer</span>
                                <div class="text-surface-200 flex items-center gap-[0.3vw] text-[0.7vw] leading-[1vw]">
                                    <span>2006</span>
                                    <span>TV</span>
                                    <Circle style="width: 0.2vw;" />
                                    <span>26 eps</span>
                                </div>
                            </div>
                        </a>
                    {/each}
                </ScrollArea>
            </div>

            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">manga</span>
                <div class="bg-surface-400 mt-[0.2vw] h-[28.25vw] w-[21.875vw] rounded-[0.75vw] shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">mangacore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>

            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">music</span>
                <div class="bg-surface-400 mt-[0.2vw] h-[28.25vw] w-[21.875vw] rounded-[0.75vw] shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">soundcore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>
        </div>

        <p class="mt-[2vw] text-[0.8vw]">
            <b>Note:</b>
            Navigate through animes, mangas and sounds with
            <b>Up Down</b>
            and
            <b>Tab</b>
            keys.
        </p>
    </div>
    <form
        method="dialog"
        class="modal-backdrop"
    >
        <button>close</button>
    </form>
</dialog>
