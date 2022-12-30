<script lang="ts">
    export let animeName: string;
    export let animeCoverBackgroundImage: string;
</script>

<div class="h-52 w-96 bg-base-100 rounded-2xl">
    <div class="flex flex-row">
        <div class="inline-grid w-[135px] h-[200px]">
            <background-image
                class="bg-no-repeat bg-cover bg-center h-full rounded-2xl"
                style="
                    background-image:url('{animeCoverBackgroundImage ?? ''}');
                    grid-area: 1 / 1 / 2 / 2;
                "
            />
            <background-image-gradient
                class="h-full"
                style="grid-area: 1 / 1 / 2 / 2;"
            />
            <background-image-text
                class="h-full flex items-center"
                style="grid-area: 1 / 1 / 2 / 2;"
            >
                <p class="px-4 text-center text-white">
                    {animeName}
                </p>
            </background-image-text>
        </div>

        <p>helo</p>
    </div>
</div>

<style>
    background-image-gradient {
        background: linear-gradient(90deg, rgba(7, 5, 25, 0.5) 0%, rgba(7, 5, 25, 0) 99.75%),
            linear-gradient(179.94deg, rgba(7, 5, 25, 0) 0.05%, rgba(7, 5, 25, 0.8) 98.74%);
    }
</style>
