<script lang="ts">
    let dropDownElement:HTMLDivElement;
    let data = [];

    const onFocus = () => {
        dropDownElement.classList.add('dropdown-open')
    };

    const onBlur = () => {
        dropDownElement.classList.remove('dropdown-open')
    }
</script>

<div class="dropdown" bind:this={dropDownElement}>
    <div tabindex="0" class="m-1">
        <div class="relative text-gray-600 focus-within:text-gray-400">
            <span class="absolute inset-y-0 left-0 flex items-center pl-2">
                <!-- Icon goes here -->
            </span>
            <input
                on:focus="{onFocus}"
                on:blur={onBlur}
                type="Search"
                class="py-2 text-sm text-gray-900 bg-white rounded-[16px] pl-10 h-20 w-[40vh] md:w-[75vh]"
                placeholder="Search..."
                autocomplete="off"
            />
        </div>
    </div>
    <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 items-center inset-x-0 mx-auto">
        {#if data.length !== 0}
            {#each data as item}
                <li>{item}</li>
            {/each}
        {:else}
            <li> Nothing came up</li>
        {/if}
    </ul>
</div>

<style global>
</style>
