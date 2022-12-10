<script lang="ts">
    import emblaCarouselSvelte, { type EmblaOptionsType } from "embla-carousel-svelte";
    import voca from "voca";

    import latestEpisodes from "$data/mock/latest_episode.json";
    import Play from "$icons/Play.svelte";
    import { responsiveMode } from "$store/Responsive";

    const emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            breakpoints: {
                "(max-width: 768px)": { axis: "x", align: "center" },
                "(min-width: 769px)": { axis: "y", align: "start" }
            }
        },
        plugins: []
    };

    // We might control it in future :D
    let lastestEpisodeNameWordCount: number;
    $: {
        switch (true) {
            case $responsiveMode === "mobile":
                lastestEpisodeNameWordCount = 25;
                break;
            case $responsiveMode === "tablet":
                lastestEpisodeNameWordCount = 16;
                break;
            case $responsiveMode === "desktop":
                lastestEpisodeNameWordCount = 19;
                break;
            case $responsiveMode === "widescreen":
                lastestEpisodeNameWordCount = 21;
                break;
            case $responsiveMode === "fullhd":
                lastestEpisodeNameWordCount = 22;
                break;
        }
    }
</script>

<embla
    class="overflow-hidden overscroll-auto lg:overscroll-contain overflow-y-hidden"
    use:emblaCarouselSvelte={emblaConfig}
>
    <embla-container class="h-28 md:h-[530px] w-96 md:w-80 gap-6 flex flex-row md:flex-col">
        {#each latestEpisodes as item}
            <embla-slide
                class="cursor-grab select-none w-10/12 md:w-64 carousel-item bg-center rounded-xl bg-no-repeat bg-cover flex items-center justify-between p-8"
                style="
                                    background-image:
                                        linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                                        linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                                        url('{item.background_image.trim()}');
                                    "
            >
                <div class="flex flex-col items-start">
                    <p
                        class="font-bold"
                        style="display: block ruby"
                    >
                        {voca
                            .chain(item.name)
                            .trim()
                            .truncate(lastestEpisodeNameWordCount + 3, " ...")}
                    </p>
                    <p>
                        Ep {voca.chain(String(item.episode)).padLeft(2, String(0))}
                    </p>
                </div>

                <button
                    class="btn btn-circle btn-md btn-warning"
                    aria-label="play"
                >
                    <Play
                        width={20}
                        height={20}
                    />
                </button>
            </embla-slide>
        {/each}
    </embla-container>
</embla>
