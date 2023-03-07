<script lang="ts">
    import { formatNumberToDuration } from "$functions/formatNumberToDuration";

    export let episode_card_background_image: string;
    export let episode_name: string;
    export let episode_duration: number;
    export let episode_number: number;

    import { page } from "$app/stores";
</script>

<a href="{$page.url.href}/episodes/{episode_number}">
    <episode-card-container
        class="flex flex-col gap-4 active:scale-95 transform transition-transform"
    >
        <episode-card class="grid w-80 h-52 rounded-2xl relative">
            <episode-card-background-image
                class="w-80 h-52 rounded-2xl absolute inset-0 z-0"
                style="background-image:url({episode_card_background_image})"
            />
            <episode-card-background-gradient class="w-80 h-52 rounded-2xl absolute inset-0 z-10" />
            <episode-card-info
                class="w-80 h-52 rounded-2xl absolute inset-0 z-20 text-white font-bold"
            >
                <p class="absolute inset-x-0 bottom-3 text-center text-xs">{episode_number}</p>
                <p class="absolute bottom-3 right-3 text-xs">
                    {formatNumberToDuration(episode_duration)}
                </p>
            </episode-card-info>
        </episode-card>
        <episode-name class="text-zinc-200 text-center">{episode_name}</episode-name>
    </episode-card-container>
</a>

<style lang="scss">
    episode-card-background-gradient {
        background: linear-gradient(180deg, rgba(7, 5, 25, 0) 0%, #070519 100%);
    }
</style>
