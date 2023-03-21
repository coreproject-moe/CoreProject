<script lang="ts">
    export let src: string;
    export let alt: string;
</script>

<anime-image-card class="card flex h-[150px] w-[100px] md:h-[300px] md:w-[200px]">
    <img
        class="rounded-lg object-contain"
        width={200}
        height={300}
        {src}
        {alt}
    />
</anime-image-card>
