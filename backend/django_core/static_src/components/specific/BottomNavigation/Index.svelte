<script>
    import { goto, reverse } from "$functions/urls";
    import { url } from "$stores/url";

    // Icons
    import Home from "$icons/Home/Index.svelte";
    import Compass from "$icons/Compass/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";

    const mapping = [
        {
            icon: Home,
            name: "home",
            href: "/anime/",
            url: reverse("anime_home_view")
        },
        {
            icon: Compass,
            name: "explore",
            href: "/anime/explore/",
            url: reverse("anime_explore_view")
        },
        {
            icon: Chat,
            name: "forum",
            href: "/forum",
            url: reverse("anime_home_view"),
        }
    ];
</script>

<footer class="flex gap-3 h-24 items-center justify-center md:hidden">
    {#each mapping as item}
        {@const is_active = item.href === $url}

        <button
            on:click={() => {
                goto({ target: "#page", verb: "GET", url: item.url });
            }}
            type="button"
            class="flex flex-col items-center gap-[0.5vh] leading-none"
        >
            <div
                class="btn text-accent h-max min-h-max rounded-xl w-20 h-[3.25rem]"
                class:btn-primary={is_active}
                class:btn-secondary={!is_active}
            >
                <svelte:component class="w-5" this={item.icon} />
            </div>
            <span class="text-sm font-bold capitalize">{item.name}</span>
        </button>
    {/each}
</footer>
