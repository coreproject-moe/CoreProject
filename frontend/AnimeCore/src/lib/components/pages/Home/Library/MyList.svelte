<script lang="ts">
    import emblaCarouselSvelte, { type EmblaOptionsType } from "embla-carousel-svelte";
    import voca from "voca";

    import ChevronDown from "$icons/Chevron-Down.svelte";
    import Settings from "$icons/Settings.svelte";
    const emblaConfig: { options: EmblaOptionsType; plugins: any } = {
        options: {
            loop: false,
            axis: "x",
            align: "start"
        },
        plugins: []
    };
    import myList from "$data/mock/my_list.json";

    let mylistAnimeNameWordCount: number;
    mylistAnimeNameWordCount ??= 25;
</script>

<div class="flex justify-between pb-3 gap-2 mt-10 mb-3 md:my-0">
    <div class="flex items-center flex-col md:flex-row gap-5 md:gap-0">
        <p class="font-bold text-3xl items-start">My List</p>
        <p class="text-3xl hidden md:block">•</p>
        <p class="text-sm md:text-xl">
            Watching
            <ChevronDown
                class="inline-block"
                color="white"
                height="24"
                width="24"
            />
        </p>
    </div>
    <div class="flex items-center">
        <Settings
            color="white"
            height="24"
            width="24"
        />
    </div>
</div>

<embla
    class="overflow-hidden"
    use:emblaCarouselSvelte={emblaConfig}
>
    <embla-container
        class="w-96 md:w-[60vw] gap-6 overscroll-auto lg:overscroll-contain flex flex-row"
    >
        {#each myList as item}
            <embla-slide
                class="select-none cursor-grab carousel-item card w-36 h-52 bg-base-100 image-full before:!opacity-60"
            >
                <figure>
                    <img
                        src={item.background_image}
                        alt={item.name}
                    />
                </figure>
                <div class="card-body justify-between items-center !text-white">
                    <h2 class="card-title text-sm">
                        {voca.chain(item.name).truncate(mylistAnimeNameWordCount + 3)}
                    </h2>
                    <div class="card-actions">{item.current}/{item.total}</div>
                </div>
            </embla-slide>
        {/each}
    </embla-container>
</embla>
