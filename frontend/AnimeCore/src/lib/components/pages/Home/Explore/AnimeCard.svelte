<script lang="ts">
    export let animeName: string;
    export let animeCoverBackgroundImage: string;
    export let animeCardBackgroundImage: string;
    export let animeTags: string[];
    export let animeEpisodeCount: string | number;
    export let animeAirTime: string | number;
    export let animeSummary: string;

    import voca from"voca";
</script>

<div class="inline-grid h-36 w-96 md:h-52">
    <background-hero-image
        class="h-full w-96 rounded-2xl bg-cover bg-center bg-no-repeat"
        style="grid-area: 1 / 1 / 2 / 2; background-image:url('{animeCardBackgroundImage ?? ''}')"
    />
    <background-hero-image-gradient
        class="h-full w-96 rounded-2xl"
        style="grid-area: 1 / 1 / 2 / 2;"
    />
    <background-hero-content
        class="h-full w-96"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div class="rounded-2xl bg-cover bg-center bg-no-repeat">
            <div class="flex flex-row">
                <!-- Anime image cards  -->
                <div class="inline-grid h-36 md:h-52">
                    <background-image
                        class="h-full w-[87px] rounded-2xl bg-cover bg-center bg-no-repeat md:w-[135px]"
                        style="background-image:url('{animeCoverBackgroundImage ??
                            ''}');grid-area: 1 / 1 / 2 / 2;"
                    />
                    <background-image-gradient
                        class="w-[87px] rounded-2xl md:w-[135px]"
                        style="grid-area: 1 / 1 / 2 / 2;"
                    />
                    <background-image-text
                        class="hidden w-[87px] items-center md:flex md:w-[135px]"
                        style="grid-area: 1 / 1 / 2 / 2;"
                    >
                        <p class="px-4 text-center text-white">
                            {animeName}
                        </p>
                    </background-image-text>
                </div>

                <!-- Anime Card Informations | Only on mobile  -->
                <div class="flex flex-col items-center justify-center pl-5 md:hidden">
                    <p class="w-full text-left text-sm font-bold leading-3 text-white">
                        {animeName}
                    </p>
                    <p class="w-full pt-4 text-xs leading-3">
                        <span class="items font-thin">TV</span>
                        <span class="items font-thin">{String(animeEpisodeCount)} eps</span>
                        <span class="items font-thin">{animeAirTime}</span>
                    </p>
                    <p class="w-full pt-3 text-xs font-thin">
                        <span class="items !text-warning">Studio</span>
                        <span class="items !text-green-500">85%</span>
                    </p>

                    <div class="flex w-full gap-2 overflow-y-scroll pt-3 scrollbar-hide">
                        {#each animeTags as tag}
                            <div
                                class="badge-warning badge !rounded-md !p-0 text-xs font-bold !lowercase"
                            >
                                <span class="mx-[6px] my-[3px]">{tag}</span>
                            </div>
                        {/each}
                    </div>
                </div>
                <!-- Anime Card Informations | Only on desktop  -->
                <div class="hidden w-[250px] p-3 md:block">
                    <!-- Anime Information  -->
                    <p class="text-sm">
                        <span class="items font-thin">TV</span>
                        <span class="items font-thin">{String(animeEpisodeCount)} eps</span>
                        <span class="items font-thin">{animeAirTime}</span>
                    </p>

                    <!-- Tags  -->
                    <div class="mt-2 flex gap-2 overflow-x-scroll scrollbar-hide">
                        {#each animeTags as tag}
                            <div
                                class="badge-warning badge !rounded-md !p-0 text-xs font-bold !lowercase"
                            >
                                <span class="mx-2 my-1">{tag}</span>
                            </div>
                        {/each}
                    </div>

                    <!-- Anime Summary  -->
                    <div class="mt-4 text-sm">
                        {voca.chain(animeSummary).truncate(170)}
                    </div>
                </div>
            </div>
        </div>
    </background-hero-content>
</div>

<style lang="scss">
    background-hero-image-gradient {
        background: linear-gradient(90deg, #070519 -1.41%, rgba(7, 5, 25, 0) 100%),
            linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgba(7, 5, 25, 0.9) 95.81%);
    }
    background-image-gradient {
        background: linear-gradient(90deg, rgba(7, 5, 25, 0.5) 0%, rgba(7, 5, 25, 0) 99.75%),
            linear-gradient(179.94deg, rgba(7, 5, 25, 0) 0.05%, rgba(7, 5, 25, 0.8) 98.74%);
    }
    .items {
        color: #d8d8d8;

        &:not(:last-child)::after {
            content:" ▪";
        }
    }
</style>
