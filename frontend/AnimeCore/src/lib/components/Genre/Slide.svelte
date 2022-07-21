<script lang="ts">
    import AutoComplete from "$components/Genre/AutoComplete.svelte";

    const badgeData = [
        { name: "Action", class:'bg-indigo-700 hover:bg-indigo-900' },
        { name: "Adventure", class: "bg-red-500 hover:bg-red-700" },
        { name: "Comedy", class: "bg-amber-300 hover:bg-amber-500" },
        { name: "Drama", class: "bg-green-500 hover:bg-green-700" },
        { name: "Ecchi", class: "bg-green-400 hover:bg-green-600" },
        { name: "Fantasy", class: "bg-indigo-400 hover:bg-indigo-600" },
        { name: "Horror", class: "bg-red-400 hover:bg-red-600" },
        { name: "Mahou Shoujo", class: "bg-red-300 hover:bg-red-500" },
        { name: "Mecha", class: "theme.colors.orange[3]" },
        { name: "Music", class: "theme.colors.cyan[5]" },
        { name: "Mystery", class: "theme.colors.yellow[5]" },
        { name: "Psychological", class: "theme.colors.red[6]" },
        { name: "Romance", class: "theme.colors.red[5]" },
        { name: "Sci-Fi", class: "theme.colors.green[5]" },
        { name: "Slice of Life", class: "theme.colors.yellow[5]" },
        { name: "Sports", class: "theme.colors.red[8]" },
        { name: "Supernatural", class: "theme.colors.cyan[8]" },
        { name: "Thriller", class: "theme.colors.green[5]" }
    ];
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center pt-8 px-24">
        <div>
            <AutoComplete />
            <div class="divider w-80 mx-auto mt-12">or search by genres</div>
            <div class='grid grid-cols-6 gap-10'>
                {#each badgeData as item}
                    <div class='btn font-bold text-black {item.class}'>{item.name}</div>
                {/each}
            </div>
            <button class="btn btn-primary">Get Started</button>
        </div>
    </div>
</div>
