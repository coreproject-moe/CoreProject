<script lang="ts">
    import { formatTime } from "$functions/formatTime";

    export let backend_anime_number: number;
    export let episode_card_background_image: string;
    export let episode_name: string;
    export let episode_duration: number;
    export let episode_number: number;

    const formated_date = new formatTime(episode_duration);
</script>

<a href="../backend/{backend_anime_number}/episodes/{episode_number}">
    <episode-card-container
        class="flex transform flex-col items-center gap-4 transition-transform active:scale-95"
    >
        <episode-card class="relative flex h-52 w-80 rounded-2xl">
            <episode-card-background-image
                class="absolute inset-0 z-0 h-52 w-80 rounded-2xl"
                style="background-image:url({episode_card_background_image})"
            />
            <episode-card-background-gradient class="absolute inset-0 z-10 h-52 w-80 rounded-2xl" />
            <episode-card-info
                class="absolute inset-0 z-20 h-52 w-80 rounded-2xl font-bold text-white"
            >
                <p class="absolute inset-x-0 bottom-3 text-center text-xs">{episode_number}</p>
                <p class="absolute bottom-3 right-3 text-xs">
                    {formated_date.formatSecondsToTimeStampDuration}
                </p>
            </episode-card-info>
        </episode-card>
        <episode-name class="text-center text-zinc-200">{episode_name}</episode-name>
    </episode-card-container>
</a>

<style lang="scss">
    episode-card-background-gradient {
        background: linear-gradient(180deg, rgba(7, 5, 25, 0) 0%, #070519 100%);
    }
</style>
