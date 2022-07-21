<script lang="ts">
    import AutoComplete from "$components/Genre/AutoComplete.svelte";

    const badgeData = [
        { name: "Action", color: "theme.colors.blue[4]" },
        { name: "Adventure", color: "theme.colors.red[4]" },
        { name: "Comedy", color: "theme.colors.yellow[6]" },
        { name: "Drama", color: "theme.colors.green[5]" },
        { name: "Ecchi", color: "theme.colors.green[5]" },
        { name: "Fantasy", color: "theme.colors.blue[4]" },
        { name: "Horror", color: "theme.colors.red[4]" },
        { name: "Mahou Shoujo", color: "theme.colors.red[3]" },
        { name: "Mecha", color: "theme.colors.orange[3]" },
        { name: "Music", color: "theme.colors.cyan[5]" },
        { name: "Mystery", color: "theme.colors.yellow[5]" },
        { name: "Psychological", color: "theme.colors.red[6]" },
        { name: "Romance", color: "theme.colors.red[5]" },
        { name: "Sci-Fi", color: "theme.colors.green[5]" },
        { name: "Slice of Life", color: "theme.colors.yellow[5]" },
        { name: "Sports", color: "theme.colors.red[8]" },
        { name: "Supernatural", color: "theme.colors.cyan[8]" },
        { name: "Thriller", color: "theme.colors.green[5]" }
    ];
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center">
        <div>
            <AutoComplete />
            <p class="py-6">
                Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi
                exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.
            </p>
            <button class="btn btn-primary">Get Started</button>
        </div>
    </div>
</div>
