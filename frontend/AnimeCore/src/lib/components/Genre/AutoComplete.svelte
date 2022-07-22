<script lang="ts">
    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropDownElement: HTMLDivElement;
    let data = [];

    const onFocus = () => {
        dropDownElement.classList.add("dropdown-open");
    };

    const onBlur = () => {
        dropDownElement.classList.remove("dropdown-open");
    };
</script>

<div class="dropdown" bind:this={dropDownElement}>
    <div tabindex="0" class="m-1">
        <div class="relative text-gray-600 focus-within:text-gray-400">
            <span class="absolute w-16 h-full flex justify-center items-center">
                <Search color="red" height={mobile ? 22 : 36} width={mobile ? 22 : 36} />
            </span>
            <input
                on:focus={onFocus}
                on:blur={onBlur}
                type="Search"
                class="py-2 text-gray-900 placeholder-gray-600 bg-white rounded-[8px] md:rounded-[16px] pl-16 h-12 md:h-20 w-[65vw] md:w-[40vw] text-sm md:text-xl outline-none focus:border-4 focus:border-red-400"
                placeholder="Search for anything"
                autocomplete="off"
            />
        </div>
    </div>
    <ul
        tabindex="0"
        class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 items-center inset-x-0 mx-auto pt-6"
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

<style global>
</style>
