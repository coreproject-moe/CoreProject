<script>
    import { goto, reverse } from "$functions/urls";

    // Icons
    import Home from "$icons/Home/Index.svelte";
    import Compass from "$icons/Compass/Index.svelte";

    const mapping = [
        {
            icon: Home,
            url: reverse("anime_home_view"),
            name: "Home"
        },
        {
            icon: Compass,
            url: reverse("anime_explore_view"),
            name: "Explore"
        }
    ];
</script>

<div class="flex items-start justify-center gap-4">
    {#each mapping as item}
        <button
            on:click={() => {
                goto({ target: "#page", verb: "GET", url: item.url });
            }}
            type="button"
            class="flex flex-col items-center gap-[0.5vh]"
        >
            <div class="btn btn-primary mask mask-squircle h-max min-h-max rounded-xl p-5">
                <svelte:component this={item.icon} />
            </div>
            <span class="text-sm font-bold capitalize">{item.name}</span>
        </button>
    {/each}
</div>
