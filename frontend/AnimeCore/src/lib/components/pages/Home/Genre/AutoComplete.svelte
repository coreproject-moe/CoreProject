<script lang="ts">
    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";
    import { UrlMaps } from "$data/urls";
    import _ from "lodash";

    const backend_mapping = new UrlMaps();

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropDownElement: Partial<HTMLDivElement> | undefined = undefined;
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

    const onFocus = () => {
        dropDownElement?.classList?.add("dropdown-open");
    };

    const onBlur = () => {
        dropDownElement?.classList?.remove("dropdown-open");
    };

    const onInput = async (e: Event) => {
        const target = e.target as HTMLInputElement;
        const value = target.value;
        if (value) {
            const res = await fetch(backend_mapping.anime({ name: value }));
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

<div
    class="dropdown"
    bind:this={dropDownElement}
>
    <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
    <div
        tabindex="0"
        class="m-1"
    >
        <div class="relative text-gray-600 focus-within:text-gray-400">
            <span class="absolute flex h-full w-16 items-center justify-center">
                <Search
                    color="red"
                    height={mobile ? 22 : 36}
                    width={mobile ? 22 : 36}
                />
            </span>
            <input
                on:focus={onFocus}
                on:blur={onBlur}
                on:input={onInput}
                type="Search"
                class="h-12 w-[65vw] rounded-[8px] bg-white py-2 pl-16 text-sm text-gray-900 placeholder-gray-600 outline-none focus:border-4 focus:border-red-400 md:h-20 md:w-[40vw] md:rounded-[16px] md:text-xl"
                placeholder="Search for anything"
                autocomplete="off"
            />
        </div>
    </div>
    <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
    <ul
        tabindex="0"
        class="dropdown-content menu rounded-box inset-x-0 mx-auto w-52 items-center bg-base-100 p-2 pt-6 shadow"
    >
        {#if search_data.length !== 0}
            {#each search_data as item}
                <li>
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
                </li>
            {/each}
        {:else}
            <li>Nothing came up</li>
        {/if}
    </ul>
</div>
