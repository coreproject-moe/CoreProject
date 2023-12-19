<script lang="ts">
    import { search_modal_state } from "./store";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import { string_to_boolean } from "$functions/string_to_bool";
    import { reverse } from "$functions/urls";
    import { Anime } from "../../../types/anime";
    import { FormatDate } from "$functions/format_date";

    // Icon imports
    import Search from "$icons/Search/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";

    let active_index = 0,
        active_core: "anime" | "manga" | "sound" = "anime",
        search_query = "",
        // search variables
        results: Anime[] = new Array<Anime>();

    // Bindings
    let dialog_element: HTMLDialogElement | null = null;

    const handle_search_key_down = async (e: KeyboardEvent) => {
            if (!dialog_element?.open) return;
        },
        handle_core_mouse_enter = async (core: typeof active_core, index: number) => {
            active_index = index;
            active_core = core;
        },
        handle_input = async () => {
            search_promise = get_anime_with_serach_parameters();
        },
        handle_global_input = async (e: KeyboardEvent) => {
            switch (e.key.toLowerCase()) {
                case "arrowdown":
                    active_index = (active_index + 1) % results.length;
                    break;
                case "arrowup":
                    active_index = (active_index - 1 + results.length) % results.length;
                    break;
                // do tab logic of switching core
                // case "tab":
                //     break;
                default:
                    break;
            }
        };

    const get_anime_with_serach_parameters = async () => {
        const headers: { [key: string]: string } = {};

        if (string_to_boolean(window.user_authenticated)) {
            headers["X-CSRFToken"] = window.csrfmiddlewaretoken;
        }
        const res = await fetch(reverse(`anime-list`) + "?" + new URLSearchParams({ name: search_query }), {
            method: "GET",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            }
        });
        const json = await res.json();
        if (res.ok) {
            return json["results"] as Array<Anime>;
        } else {
            throw new Error("Something is wrong from the backend");
        }
    };
    let search_promise: Promise<Anime[]> | null = null;

    search_modal_state.subscribe((val) => {
        if (val) {
            dialog_element?.showModal();
            search_modal_state.set(false);
        }
    });
</script>

<svelte:window
    on:keyup={(event) => {
        if (dialog_element?.open) handle_global_input(event);
    }}
/>
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
                on:input={handle_input}
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
                    {#if search_promise}
                        {#await search_promise}
                            <div class="grid h-full place-items-center">
                                <span class="loading loading-ring loading-lg"></span>
                            </div>
                        {:then results}
                            {#if results.length !== 0}
                                {#each results as item, index}
                                    {@const is_active = active_core === "anime" && active_index === index}
                                    {@const mapping = [
                                        {
                                            value: item.name,
                                            class: "text-[1.1vw] font-semibold leading-none text-white"
                                        },
                                        {
                                            value: item.name_japanese,
                                            class: "text-surface-200 text-[0.7vw] font-medium uppercase leading-[1.5vw]"
                                        }
                                    ]}
                                    {@const nested_mapping = [
                                        { value: item.aired_from ? new FormatDate(item.aired_from).format_to_human_readable_form : null },
                                        { value: `TV` },
                                        { value: item.episode_count ? item.episode_count : null }
                                    ]}
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
                                            {#each mapping as item}
                                                {#if item.value}
                                                    <span class={item.class}>{item.value}</span>
                                                {/if}
                                            {/each}
                                            <!-- Do some css magic-->
                                            <div class="text-surface-200 flex items-center gap-[0.3vw] text-[0.7vw] leading-[1vw]">
                                                {#each nested_mapping as item}
                                                    {@const is_last = item === nested_mapping.at(-1)}
                                                    {#if item.value}
                                                        <span>
                                                            {item.value}
                                                        </span>
                                                        {#if !is_last}
                                                            <Circle style="width: 0.2vw;" />
                                                        {/if}
                                                    {/if}
                                                {/each}
                                            </div>
                                        </div>
                                    </a>
                                {/each}
                            {:else}
                                <div class="grid h-full place-items-center">No match found</div>
                            {/if}
                        {:catch error}
                            Oh no, something is wrong {@html error}
                        {/await}
                    {:else}
                        <div class="grid h-full place-items-center">Search Away</div>
                    {/if}
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
