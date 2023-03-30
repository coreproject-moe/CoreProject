<script lang="ts">
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import ChevronUpDown from "$icons/Chevron-Up-Down.svelte";
    import { modals } from "$store/Modal";
    import { responsiveMode } from "$store/Responsive";

    import AutoComplete from "./AutoComplete.svelte";

    const badgeData = [
        { name: "Action", class: "bg-indigo-700 hover:bg-indigo-900" },
        { name: "Adventure", class: "bg-red-500 hover:bg-red-700" },
        { name: "Comedy", class: "bg-amber-300 hover:bg-amber-500" },
        { name: "Drama", class: "bg-green-500 hover:bg-green-700" },
        { name: "Ecchi", class: "bg-green-400 hover:bg-green-600" },
        { name: "Fantasy", class: "bg-indigo-400 hover:bg-indigo-600" },
        { name: "Horror", class: "bg-red-400 hover:bg-red-600" },
        { name: "Mahou Shoujo", class: "bg-red-300 hover:bg-red-500" },
        { name: "Mecha", class: "bg-orange-300 hover:bg-orange-500" },
        { name: "Music", class: "bg-cyan-500 hover:bg-cyan-700" },
        { name: "Mystery", class: "bg-amber-300 hover:bg-amber-500" },
        { name: "Psychological", class: "bg-red-500 hover:bg-red-700" },
        { name: "Romance", class: "bg-red-300 hover:bg-red-500" },
        { name: "Sci-Fi", class: "bg-green-400 hover:bg-green-600" },
        { name: "Slice of Life", class: "bg-amber-300 hover:bg-amber-500" },
        { name: "Sports", class: "bg-red-500 hover:bg-red-700" },
        { name: "Supernatural", class: "bg-cyan-500 hover:bg-cyan-700" },
        { name: "Thriller", class: "bg-green-400 hover:bg-green-600" }
    ];

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

<div class="hero mt-10 min-h-[184px] bg-base-100 md:mt-0 md:min-h-screen">
    <div class="hero-content p-0 text-center">
        <div class="block flex-col">
            <AutoComplete />
            {#if mobile}
                <div class="mt-10">
                    <label
                        for={$modals.genre}
                        class="modal-button btn flex gap-5"
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
                <div class="divider mx-auto mb-6 mt-12 w-80 before:bg-white after:bg-white">
                    or search by genres
                </div>
                <div class="grid grid-cols-6 justify-items-center gap-x-0 gap-y-5 lg:gap-x-5">
                    {#each badgeData as item}
                        <div class="btn w-fit whitespace-nowrap font-bold text-black {item.class}">
                            {item.name}
                        </div>
                    {/each}
                </div>
                <div class="mt-24 flex flex-col items-center">
                    <div class="w-[500px]">
                        <h1 class="mb-2 text-3xl font-bold">Choose your preferences</h1>
                        <p>
                            Choose some options to customize your experience. You can change them
                            anytime by clicking the profile icon and going to Settings
                        </p>
                    </div>
                </div>
                <div class="mt-8 flex w-full flex-row justify-center">
                    <div class="align-center flex flex-row">
                        Romaji Naming
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="align-center flex flex-row">
                        10 point scoring system
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="align-center flex flex-row">
                        2 trackers added
                        <ChevronDown
                            color="white"
                            height={30}
                            width={30}
                        />
                    </div>
                    <div class="divider divider-horizontal before:bg-white after:bg-white" />
                    <div class="align-center flex flex-row">
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
