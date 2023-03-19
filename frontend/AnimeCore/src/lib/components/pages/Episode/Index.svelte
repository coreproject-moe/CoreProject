<script lang="ts">
    import Navbar from "$components/shared/Navbar.svelte";
    export let data: {
        id: number;
        episode_number: number;
        episode_name: string;
        episode_thumbnail: string;
        episode_summary: string;
        episode_length: number;
        providers: { streamsb: string };
        episode_comments: Array<string>;
        episode_timestamps: Array<string>;
    };
</script>

<div class="relative grid h-screen">
    <div class="absolute inset-0 grid h-screen w-screen">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 pl-6 pb-0 md:pr-[72px] md:pl-20">
                    <Navbar />
                </div>
                <div class="mx-6 mt-0 flex flex-col items-center md:mx-20">
                    <iframe
                        class="h-[200px] w-[80vw] md:h-[80vh]"
                        title="anime"
                        src="https://sbbrisk.com/e/{data?.providers?.streamsb}.html"
                        frameborder="0"
                        marginwidth="0"
                        marginheight="0"
                        scrolling="NO"
                        allowfullscreen
                    />
                </div>
            </div>
        </div>
    </div>
</div>
