<script context="module" lang="ts">
	export async function load({ fetch }) {
		if (browser && get(isUserAuthenticated)) {
			try {
				const res = await fetch(captureEndpoint, {
					method: "GET",
					headers: new Headers({
						Accept: "application/json",
						"Content-Type": "application/json",
						Authorization: `Bearer ${get(userToken).access}`
					})
				});
				const data = await res.json();
				return {
					props: {
						backendVimeVolume: data.video_volume
					}
				};
			} catch (err) {
				if (err instanceof Error) {
					userToken.set({ refresh: "", access: "" });
					console.error(`Can't fetch from backend | Flushing Tokens | Reason : ${err.message}`);
				}
			}
		}
		return {
			props: {}
		};
	}
</script>

<script lang="ts">
	export let backendVimeVolume: number;

	import anime from "animejs";
	import { onMount } from "svelte";
	import { get } from "svelte/store";

	import { browser } from "$app/env";
	import { page } from "$app/stores";

	import { captureEndpoint } from "$urls/restEndpoints";
	import { responsiveMode } from "$store/responsive";
	import { projectName } from "$lib/constants/frontend/projectName";
	import { isUserAuthenticated, userToken } from "$store/users";
	import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";

	$: episode_number = parseInt($page.params.number);
	$: anime_name = snakeCaseToTitleCase($page.params.anime_name);

	let player: HTMLVmPlayerElement;
	let showPlayer = false;
	let captionEnabled = true;

	onMount(async () => {
		const { defineCustomElements } = await import("@vime/core");
		defineCustomElements();
		showPlayer = true;
	});

	$: {
		if (browser) {
			const volume =
				backendVimeVolume ?? parseInt(localStorage.getItem("vimejs-volume") ?? JSON.stringify(100));

			// Set to localstorage
			localStorage.setItem("vimejs-volume", JSON.stringify(~~volume));

			// Set player volume
			if (player) {
				player.volume = volume;
			}
		}
	}

	const onVolumeChange = async () => {
		if (browser) {
			localStorage.setItem("vimejs-volume", JSON.stringify(~~player?.volume));

			if ($isUserAuthenticated) {
				try {
					fetch(captureEndpoint, {
						method: "PATCH",
						headers: {
							Accept: "application/json",
							"Content-Type": "application/json",
							Authorization: `Bearer ${get(userToken).access}`
						},
						body: JSON.stringify({
							video_volume: ~~player?.volume
						})
					});
				} catch {
					console.error(`POST to ${captureEndpoint} Failed`);
				}
			}
		}
	};

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
				player?.muted ? player?.removeAttribute("muted") : player?.setAttribute("muted", "");
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
	let textContent = "";
	let showMore = false;
	let chevronOne: HTMLElement;
	let chevronTwo: HTMLElement;

	let textContentParagraph: HTMLParagraphElement;
	let textContentParagraphHeight = 0;

	$: {
		let height = textContentParagraph?.clientHeight;
		if (height > textContentParagraphHeight) {
			textContentParagraphHeight = height;
		}
	}

	$: switch (showMore) {
		case true:
			if (browser && chevronOne && chevronTwo && textContentParagraph) {
				anime({
					targets: [chevronOne],
					rotate: [0, 180],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [chevronTwo],
					rotate: [0, -180],
					easing: "easeOutSine",
					duration: 500
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
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [chevronTwo],
					rotate: [-180, 0],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [textContentParagraph],
					height: 100,
					duration: 500,
					easing: "linear"
				});
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

		<!-- Middle side -->
		<div class="level-item">
			<p class="has-text-white {$responsiveMode === 'mobile' ? 'is-size-6' : 'is-size-4'}">
				Anime Name : {anime_name} | Episode :
				{episode_number}
			</p>
		</div>

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
			<p bind:this={textContentParagraph} class="is-clipped has-text-justified">
				{textContent}
			</p>
			{#if textContent?.length > 950}
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
