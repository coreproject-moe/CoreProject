<script lang="ts">
    export let src: string;
    export let alt: string;
</script>

<anime-image-card class="card flex w-[200px] h-[300px]">
    <img
        class="rounded-lg object-contain"
        width={200}
        height={300}
        {src}
        {alt}
    />
</anime-image-card>
