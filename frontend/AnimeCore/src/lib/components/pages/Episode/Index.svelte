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

<div class="grid h-screen relative">
    <div class="h-screen grid w-screen absolute inset-0">
        <div class="hero">
            <div class="grid h-full w-full">
                <div class="pt-8 md:pr-[72px] pl-6 md:pl-20 pb-0">
                    <Navbar />
                </div>
                <div class="flex flex-col mt-0 mx-6 md:mx-20 items-center">
                    <iframe
                        class="h-[80vh] w-[80vw]"
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
