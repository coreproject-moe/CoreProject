<script lang="ts">
    let textContent = "";
    import anime from "animejs";
    import { onMount, beforeUpdate } from "svelte";

    import { browser } from "$app/env";
    import { page } from "$app/stores";

    import { vimeJSVolume } from "$store/vimeJs";
    import { responsiveMode } from "$store/responsive";

    import { projectName } from "$lib/constants/frontend/project";
    import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";
    import { goto } from "$app/navigation";

    $: episode_number = parseInt($page.params.number);
    $: anime_name = snakeCaseToTitleCase($page.params.anime_name);

    let player: HTMLVmPlayerElement;
    let showPlayer = false;
    let captionEnabled = true;

    // Get height before dom is updated
    beforeUpdate(async () => {
        if (textContentParagraph?.clientHeight > textContentParagraphHeight) {
            textContentParagraphHeight = textContentParagraph?.clientHeight;
        }
    });

    onMount(async () => {
        const { defineCustomElements } = await import("@vime/core");
        defineCustomElements();
        showPlayer = true;
    });

    const onVolumeChange = async () => {
        $vimeJSVolume = player?.volume;
    };

    // First book for player
    $: {
        if (player) {
            player.volume = $vimeJSVolume;
        }
    }

    const handleKeydown = async (event: KeyboardEvent) => {
        /*
			Maps Keys to vimejs control

				* Space | K 	= 	Play / Pause
				* M 			= 	Mute / Unmute
				* C				= 	Captions
				* ArrowRight 	= 	Seek Forward 5 sec
				* ArrowLeft 	= 	Seek Backward 5 sec
				* F				= 	Enter / Exit FullScreen
		
		*/

        switch (event?.key?.toLowerCase()) {
            case " ":
            case "k": {
                player?.paused ? player?.play() : player?.pause();
                break;
            }
            case "m": {
                player?.muted
                    ? player?.removeAttribute("muted")
                    : player?.setAttribute("muted", "");
                break;
            }
            case "c": {
                switch (captionEnabled) {
                    case true: {
                        await player?.setTextTrackVisibility(false);
                        captionEnabled = false;
                        break;
                    }
                    case false: {
                        await player?.setTextTrackVisibility(true);
                        captionEnabled = true;
                        break;
                    }
                }
                break;
            }
            case "arrowright": {
                player.currentTime += 5;
                break;
            }
            case "arrowleft": {
                player.currentTime -= 5;
                break;
            }
            case "f": {
                player?.isFullscreenActive ? player?.exitFullscreen() : player?.enterFullscreen();
                break;
            }
        }
    };
    let showMore = false;
    let chevronOne: HTMLElement;
    let chevronTwo: HTMLElement;

    let textContentParagraph: HTMLParagraphElement;
    let textContentParagraphHeight = 0;

    $: switch (showMore) {
        case true:
            if (browser && chevronOne && chevronTwo && textContentParagraph) {
                anime({
                    targets: [chevronOne],
                    rotate: [0, 180],
                    easing: "linear",
                    duration: 250
                });

                anime({
                    targets: [chevronTwo],
                    rotate: [0, -180],
                    easing: "linear",
                    duration: 250
                });

                anime({
                    targets: [textContentParagraph],
                    height: ~~textContentParagraphHeight,
                    duration: 500,
                    easing: "linear"
                });
            }
            break;
        case false:
            if (browser && chevronOne && chevronTwo && textContentParagraph) {
                anime({
                    targets: [chevronOne, chevronTwo],
                    rotate: [180, 0],
                    easing: "linear",
                    duration: 250
                });

                anime({
                    targets: [chevronTwo],
                    rotate: [-180, 0],
                    easing: "linear",
                    duration: 250
                });

                anime({
                    targets: [textContentParagraph],
                    height: 100,
                    duration: 500,
                    easing: "linear"
                });
            }
    }
    let episodeSelectOption: HTMLSelectElement;

    $: {
        if (episodeSelectOption) {
            episodeSelectOption.value = `Episode ${episode_number}`;
        }
    }
</script>

<svelte:window on:keydown={handleKeydown} />

<svelte:head>
    <title>{anime_name} | Episode : {episode_number} | {projectName}</title>
</svelte:head>

<div class="container pt-5">
    {#if showPlayer}
        <vm-player autoplay bind:this={player} on:vmVolumeChange={onVolumeChange}>
            <vm-video poster="https://media.vimejs.com/poster.png" cross-origin>
                <source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
                <track
                    default
                    kind="subtitles"
                    src="https://media.vimejs.com/subs/english.vtt"
                    srclang="en"
                    label="English"
                />
            </vm-video>
            <vm-ui>
                <vm-click-to-play />
                <vm-dbl-click-fullscreen />
                <vm-captions />
                <vm-poster />
                <vm-spinner />
                <vm-loading-screen />
                <vm-default-controls />
                <vm-default-settings pin="bottomRight" />
            </vm-ui>
        </vm-player>
    {:else}
        <section class="hero is-large">
            <div class="hero-body">
                <div class="has-text-centered">
                    <button class="button is-ghost is-loading is-size-2" />
                </div>
            </div>
        </section>
    {/if}
</div>
<div class="container pt-5">
    <!-- Main container -->
    <nav class="level is-mobile">
        {#if episode_number > 0}
            <!-- Left side -->
            <div
                class="level-left {$responsiveMode === 'mobile'
                    ? 'is-size-6'
                    : 'is-size-4'} {$responsiveMode === 'mobile' ? 'pl-4' : ''}"
            >
                <div class="level-item">
                    <a
                        href="/anime/{$page.params.anime_name}/episode/{episode_number - 1}"
                        sveltekit:prefetch
                        sveltekit:noscroll
                    >
                        <ion-icon name="arrow-back-outline" class="has-text-white" />
                    </a>
                </div>
            </div>
        {/if}

        <!-- Middle side -->
        <div class="level-item">
            <div class="has-text-white {$responsiveMode === 'mobile' ? 'is-size-6' : 'is-size-4'}">
                Anime Name : {anime_name} | Episode :

                <div class="select is-small mt-1">
                    <select class="select-items" bind:this={episodeSelectOption}>
                        {#each Array(100) as _, i}
                            <option
                                class="pd-2"
                                on:click={async () => {
                                    goto(`/anime/${$page.params.anime_name}/episode/${i}`, {
                                        replaceState: true
                                    });
                                }}>Episode {i}</option
                            >
                        {/each}
                    </select>
                </div>
            </div>
        </div>

        {#if episode_number < 99}
            <!-- Right side -->
            <div
                class="level-right {$responsiveMode === 'mobile'
                    ? 'is-size-6'
                    : 'is-size-4'} {$responsiveMode === 'mobile' ? 'pr-4' : ''}"
            >
                <p class="level-item">
                    <a
                        href="/anime/{$page.params.anime_name}/episode/{episode_number + 1}"
                        sveltekit:prefetch
                        sveltekit:noscroll
                    >
                        <ion-icon name="arrow-forward-outline" class="has-text-white" />
                    </a>
                </p>
            </div>
        {/if}
    </nav>
</div>
<div class="container">
    <div
        class="column is-flex {$responsiveMode === 'desktop' ||
        $responsiveMode === 'widescreen' ||
        $responsiveMode === 'fullhd'
            ? ''
            : 'is-align-self-center'}"
    >
        <div class="content has-text-white">
            <h1 class="has-text-white pt-3">Synopsis :</h1>
            <p
                bind:this={textContentParagraph}
                style={textContentParagraphHeight >= 100 ? "height:100px" : ""}
                class="is-clipped has-text-justified"
            >
                {textContent}
            </p>
            {#if textContentParagraphHeight > 100}
                <!-- Main container -->
                <nav class="level is-mobile">
                    <!-- Middle side -->
                    <div class="level-item">
                        <div
                            class="has-text-white is-clickable"
                            on:click={() => {
                                showMore = !showMore;
                            }}
                        >
                            <ion-icon bind:this={chevronOne} name="chevron-down-outline" />
                            <span class="pb-5 is-size-5"> Show More </span>
                            <ion-icon bind:this={chevronTwo} name="chevron-down-outline" />
                        </div>
                    </div>
                </nav>
            {/if}
        </div>
    </div>
</div>

<style lang="scss">
    .select {
        &::after {
            border-color: #ffffffd1 !important;
        }
        &:hover {
            &::after {
                border-color: white !important;
            }
        }
        .select-items {
            background-color: black !important;
            color: white !important;
            border-color: var(--button-border-color) !important;
            scrollbar-width: thin;

            &:hover {
                border-color: #b5b5b5 !important;
            }

            option {
                appearance: none;
            }
        }
    }
</style>
