<script lang="ts">
    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropDownElement: Partial<HTMLDivElement> | undefined = undefined;
    let data = [];

    const onFocus = () => {
        dropDownElement?.classList?.add("dropdown-open");
    };

    const onBlur = () => {
        dropDownElement?.classList?.remove("dropdown-open");
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
        {#if data.length !== 0}
            {#each Array(10) as item}
                <li>{item}</li>
            {/each}
        {:else}
            <li>Nothing came up</li>
        {/if}
    </ul>
</div>
