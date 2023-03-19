<script lang="ts">
    import Heart from "$icons/Heart.svelte";

    import ContinueWatching from "./ContinueWatching.svelte";
    import LatestEpisode from "./LatestEpisode.svelte";
    import MyList from "./MyList.svelte";
</script>

<div class="hero min-h-[20vh] bg-base-100 md:min-h-screen">
    <div class="hero-content flex-col text-center md:flex-row">
        <div class="flex flex-col gap-3 pt-12 md:pt-0">
            <LatestEpisode />
        </div>
        <div class="divider hidden lg:divider-horizontal before:bg-white after:bg-white md:flex" />
        <div class="flex flex-col">
            <ContinueWatching />
            <div class="divider hidden before:bg-white after:bg-white md:flex" />
            <MyList />

            <div class="mt-14 hidden gap-8 md:flex">
                <div
                    class="flex h-20 w-32 flex-col items-center justify-center rounded-lg bg-[#42424240]"
                >
                    <rectangle
                        style="width: 20px;height: 20px;background: #DCD9F7;border-radius: 2px;"
                    />
                    <div class="mt-2.5 w-32">Placeholder</div>
                </div>

                <div class="text-start">
                    <p class="text-xl font-bold">Characters, Seiyuus, Studios and lots more!</p>
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
