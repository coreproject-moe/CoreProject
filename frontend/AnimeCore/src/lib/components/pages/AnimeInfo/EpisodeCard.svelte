<script lang="ts">
    export let episode_card_background_image: string;
</script>

<episode-card
    class="w-80 h-52 bg-no-repeat bg-cover bg-center rounded-2xl"
    style="background-image:url({episode_card_background_image})"
>
    pass
</episode-card>

<style lang="scss">
    episode-card {
        background: linear-gradient(180deg, rgba(7, 5, 25, 0) 0%, #070519 100%);
    }
</style>
