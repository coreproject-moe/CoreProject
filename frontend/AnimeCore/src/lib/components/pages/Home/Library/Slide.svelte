<script lang="ts">
    import Heart from "$icons/Heart.svelte";

    import ContinueWatching from "./ContinueWatching.svelte";
    import LatestEpisode from "./LatestEpisode.svelte";
    import MyList from "./MyList.svelte";
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center flex-col md:flex-row">
        <div class="flex flex-col gap-3 pt-12 md:pt-0">
            <LatestEpisode />
        </div>
        <div class="divider lg:divider-horizontal hidden md:flex before:bg-white after:bg-white" />
        <div class="flex flex-col">
            <ContinueWatching />
            <div class="divider hidden md:flex before:bg-white after:bg-white" />
            <MyList />

            <div class="gap-8 mt-16 hidden md:flex">
                <div
                    class="flex flex-col items-center w-32 h-20 justify-center rounded-lg bg-[#42424240]"
                >
                    <rectangle
                        style="width: 20px;height: 20px;background: #DCD9F7;border-radius: 2px;"
                    />
                    <div class="w-32 mt-2.5">Placeholder</div>
                </div>

                <div class="text-start">
                    <p class="font-bold text-xl">Characters, Seiyuus, Studios and lots more!</p>
                    <p>
                        Did you know that you can search for characters, voice actors/actresses,
                        studios and anime staff here? You can also
                        <Heart
                            height={12}
                            width={12}
                            class="inline-block"
                            color="#FFABB6"
                        />
                        your favorite ones. If you have a tracker account added, they will also be synced
                        to your profile.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
