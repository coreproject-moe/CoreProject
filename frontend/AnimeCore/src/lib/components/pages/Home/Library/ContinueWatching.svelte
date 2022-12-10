<script lang="ts">
    import emblaCarouselSvelte, { type EmblaOptionsType } from "embla-carousel-svelte";
    import voca from "voca";

    import continueWatching from "$data/mock/continue_watching.json";
    import Play from "$icons/Play.svelte";
    
    const emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            axis: "x",
            align: "start"
        },
        plugins: []
    };
</script>

<p class="font-bold text-3xl items-start flex pb-4 mt-10 mb-6 md:my-0">Continue Watching</p>
<embla
    class="overflow-hidden overscroll-auto lg:overscroll-contain overflow-y-hidden"
    use:emblaCarouselSvelte={emblaConfig}
>
    <embla-container class="h-28 md:h-[200px] w-96 md:w-[640px] flex flex-row gap-6">
        {#each continueWatching as item}
            <embla-slide
                class="select-none cursor-grab carousel-item w-96 md:w-[640px] rounded-xl flex items-center justify-around"
                style="
                    background-image:
                        linear-gradient(90deg, rgb(7 5 25 / 92%) -1.41%, rgba(7, 5, 25, 0.1) 100%),
                        linear-gradient(180deg, rgba(7, 5, 25, 0) -16%, rgb(7 5 25 / 90%) 95.81%),
                        url('{item.background_image}');
                "
            >
                <div class="md:self-start flex flex-col items-start gap-2 md:pt-5">
                    <p class="font-bold">{item.name}</p>
                    <p>
                        continue from Ep {voca
                            .chain(String(item.current_episode))
                            .padLeft(2, String(0))}
                    </p>
                    <p class="text-justify text-sm hidden md:block">
                        {voca.chain(item.about).truncate(60)}
                    </p>
                </div>

                <div class="md:self-end md:pb-5">
                    <button
                        class="btn btn-circle btn-md btn-warning"
                        aria-label="play"
                    >
                        <Play
                            width={20}
                            height={20}
                        />
                    </button>
                </div>
            </embla-slide>
        {/each}
    </embla-container>
</embla>
