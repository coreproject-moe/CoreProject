<script lang="ts">
    import _ from "lodash";
    import { modals } from "$store/Modal";
    import { timer as timerStore } from "$store/Timer";
    let value: boolean;

    $: switch (value) {
        case true:
            $timerStore = "pause";
            break;
        case false:
            $timerStore = "start";
            break;
    }

    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";
    import { UrlMaps } from "$data/urls";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    const backend_mapping = new UrlMaps();

    let search_data: Array<{
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
        updated: string;
        name_synonyms: string[];
    }> = [];

    const onInput = async (e: Event) => {
        const target = e.target as HTMLInputElement;
        const value = target.value;
        if (value) {
            const res = await fetch(
                `${backend_mapping.anime()}?` +
                    new URLSearchParams({
                        name: value
                    })
            );
            if (res.ok) {
                const data = await res.json();
                const item = data["items"][0];

                search_data = [];
                search_data.push(item);
                search_data = _.uniqBy(search_data, "id");
            } else {
                search_data = [];
            }
        } else {
            search_data = [];
        }
    };
</script>

<input
    bind:checked={value}
    type="checkbox"
    id={$modals.search}
    class="modal-toggle"
/>
<label
    for={$modals.search}
    class="modal cursor-pointer"
>
    <label
        for=""
        class="flex flex-col gap-24"
    >
        <div class="relative w-96 self-center text-gray-600 focus-within:text-gray-400">
            <span class="absolute flex h-full w-16 items-center justify-center">
                <Search
                    color="white"
                    height={15}
                    width={15}
                />
            </span>
            <input
                type="Search"
                class="input w-full pl-16"
                placeholder="Search for anything"
                autocomplete="off"
                on:input={onInput}
            />
        </div>
        <div class="flex flex-row gap-24 text-white">
            <div>
                <p class="pl-3 font-bold">Anime</p>
                <div class="modal-box relative flex h-96 w-72 flex-col gap-4">
                    {#if search_data.length === 0}
                        <p class="self-center">Search away</p>
                    {:else}
                        {#each search_data as item}
                            <a
                                class="flex gap-2"
                                href="/anime/backend/{item.id}"
                            >
                                <img
                                    class="h-16 w-16 rounded-lg"
                                    src={backend_mapping.DOMAIN + item.banner}
                                    alt="{item.name} banner"
                                />
                                <div>
                                    <p class="font-bold">{item.name}</p>
                                </div>
                            </a>
                        {/each}
                    {/if}
                </div>
            </div>
            <div>
                <p class="pl-3 font-bold">Manga</p>
                <div
                    class="modal-box relative flex h-96 w-72 items-center justify-center text-center"
                >
                    mangacore integration coming soon
                </div>
            </div>
            <div>
                <p class="pl-3 font-bold">music</p>
                <div
                    class="modal-box relative flex h-96 w-72 items-center justify-center text-center"
                >
                    soundcore integration coming soon
                </div>
            </div>
        </div>
    </label>
</label>
