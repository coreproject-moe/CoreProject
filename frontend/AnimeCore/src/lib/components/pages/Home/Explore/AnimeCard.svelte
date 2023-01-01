<script lang="ts">
    export let animeName: string;
    export let animeCoverBackgroundImage: string;
    export let animeCardBackgroundImage: string;
    export let animeTags: string[];
    export let animeEpisodeCount: string | number;
    export let animeAirTime: string | number;
    export let animeSummary: string;

    import voca from "voca";
</script>

<div class="inline-grid h-52 w-96 ">
    <background-hero-image
        class="h-full bg-no-repeat bg-cover bg-center rounded-2xl"
        style="
            grid-area: 1 / 1 / 2 / 2;
            background-image:url('{animeCardBackgroundImage ?? ''}')
        "
    />
    <background-hero-image-gradient
        class="h-full rounded-2xl"
        style="grid-area: 1 / 1 / 2 / 2;"
    />
    <background-hero-content
        class="h-full"
        style="grid-area: 1 / 1 / 2 / 2;"
    >
        <div class="rounded-2xl bg-no-repeat bg-cover bg-center">
            <div class="flex flex-row">
                <!-- Anime image cards  -->
                <div class="inline-grid h-52">
                    <background-image
                        class="w-[135px] bg-no-repeat bg-cover bg-center h-full rounded-2xl"
                        style="
                            background-image:url('{animeCoverBackgroundImage ?? ''}');
                            grid-area: 1 / 1 / 2 / 2;
                        "
                    />
                    <background-image-gradient
                        class="w-[135px] rounded-2xl"
                        style="grid-area: 1 / 1 / 2 / 2;"
                    />
                    <background-image-text
                        class="w-[135px] flex items-center"
                        style="grid-area: 1 / 1 / 2 / 2;"
                    >
                        <p class="px-4 text-center text-white">
                            {animeName}
                        </p>
                    </background-image-text>
                </div>

                <!-- Anime Card Informations  -->
                <div class="p-3">
                    <!-- Anime Information  -->
                    <p class="text-sm">
                        <span class="items font-thin">TV</span>
                        <span class="items font-thin">{String(animeEpisodeCount)} eps</span>
                        <span class="items font-thin">{animeAirTime}</span>
                    </p>

                    <!-- Tags  -->
                    <div class="mt-2 flex gap-2">
                        {#each animeTags as tag}
                            <div
                                class="badge badge-warning !rounded-md w-12 text-xs font-bold !p-0"
                            >
                                {tag}
                            </div>
                        {/each}
                    </div>

                    <!-- Anime Summary  -->
                    <div class="text-sm">
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
            content: " ▪ ";
        }
    }
</style>
