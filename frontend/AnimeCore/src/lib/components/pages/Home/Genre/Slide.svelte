<script lang="ts">
    import GenreModal from "$components/modals/Genre.svelte";
    import badgeData from "$data/components/badge_data.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import ChevronUpDown from "$icons/Chevron-Up-Down.svelte";
    import { modals } from "$store/Modal";
    import { responsiveMode } from "$store/Responsive";

    import AutoComplete from "./AutoComplete.svelte";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

<!-- Modals  -->
<svelte:component this={GenreModal} />

<div class="hero min-h-[184px] mt-10 md:mt-0 md:min-h-screen bg-base-100">
    <div class="hero-content text-center p-0">
        <div class="block flex-col">
            <AutoComplete />
            {#if mobile}
                <div class="mt-10">
                    <label
                        for={$modals.genre}
                        class="btn modal-button flex gap-5"
                    >
                        <span class="text-white">or search by genres</span>
                        <ChevronUpDown
                            color="#D8D8D8"
                            height={18}
                            width={18}
                        />
                    </label>
                </div>
            {:else}
                <div class="divider w-80 mx-auto mt-12 mb-6 before:bg-white after:bg-white">
                    or search by genres
                </div>
                <div class="grid grid-cols-6 gap-x-0 lg:gap-x-5 gap-y-5 justify-items-center">
                    {#each badgeData as item}
                        <div class="btn font-bold text-black w-fit whitespace-nowrap {item.class}">
                            {item.name}
                        </div>
                    {/each}
                </div>
                <div class="mt-24 flex flex-col items-center">
                    <div class="w-[500px]">
                        <h1 class="font-bold text-3xl mb-2">Choose your preferences</h1>
                        <p>
                            Choose some options to customize your experience. You can change them
                            anytime by clicking the profile icon and going to Settings
                        </p>
                    </div>
                </div>
                <div class="flex w-full flex-row justify-center mt-8">
                    <div class="flex flex-row align-center">
                        Romaji Naming
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        10 point scoring system
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        2 trackers added
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        Show 18+ content
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                </div>
            {/if}
        </div>
    </div>
</div>
