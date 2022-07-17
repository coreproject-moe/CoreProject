<script lang="ts">
    import Navbar from "$components/common/Navbar.svelte";

    export let animeTitle: string;
    export let animeSummary: string;
    export let animeEpisodeCount: number;
    export let animeStudio: string;
    export let animeAirTime: string;
    export let backgroundImage: string;
    export let backgroundBanner: string;
    export let tags: string[];
</script>

<div
    class="hero min-h-[60vh] md:min-h-screen bg-center bg-no-repeat"
    style="background-image: url('{backgroundImage}');"
>
    <div class="hero-overlay bg-opacity-60 bg-gradient-to-t from-base-100">
        <div class="pt-8 pr-[72px] pl-[48px] pb-0">
            <Navbar />
        </div>
    </div>
    <div class="pl-[48px] hero-content text-neutral-content text-white justify-self-start">
        <div class="max-w-prose">
            <div class="text-secondary text-lg font-bold pb-2">
                Featured
                <span>
                    <span
                    style="display: inline-block; width: 60px; border-top: 4px solid; border-radius: 10px;"
                />
                </span>
            </div>
            <h1 class="mb-5 text-5xl font-bold">{animeTitle}</h1>
            <h1 class='font-bold py-8 hidden md:flex'>
                <span class="items pr-2">TV</span><span
                    class="items pr-2">{animeEpisodeCount} eps</span
                ><span class="items pr-2">Completed</span><span
                    class="items pr-2">{animeAirTime}</span
                ><span>{animeStudio}</span>

            </h1>
            <div class="mb-5 max-h-24 text-ellipsis overflow-y-auto">
                <div class="pr-3 font-normal text-gray-400">{animeSummary}</div>
            </div>
            {#each tags as tag}
            <span class="badge mr-5 bg-base-100 badge-lg">{tag}</span>
            {/each}
        </div>
    </div>
</div>


<style lang="scss">
    .items {
        &::after {
            content:" ▪ "
        }
    }

</style>
