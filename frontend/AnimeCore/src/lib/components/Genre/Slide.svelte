<script lang="ts">
    import AutoComplete from "$components/Genre/AutoComplete.svelte";
    import ChevronDown from "$icons/Chevron-Down.svelte";

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
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center p-0">
        <div>
            <AutoComplete />
            <div class="divider w-80 mx-auto mt-12 mb-6">or search by genres</div>
            <div class="grid grid-cols-6 gap-x-10 gap-y-5 justify-items-center">
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
            <div class="flex flex-col w-full lg:flex-row justify-center mt-8">
                <div class="flex flex-row align-center">
                    Romaji Naming <ChevronDown height={30} width={30} />
                </div>
                <div class="divider lg:divider-horizontal" />
                <div class="flex flex-row align-center">
                    10 point scoring system <ChevronDown height={30} width={30} />
                </div>
                <div class="divider lg:divider-horizontal" />
                <div class="flex flex-row align-center">
                    2 trackers added <ChevronDown height={30} width={30} />
                </div>
                <div class="divider lg:divider-horizontal" />
                <div class="flex flex-row align-center">
                    Show 18+ content <ChevronDown height={30} width={30} />
                </div>
            </div>
        </div>
    </div>
</div>
