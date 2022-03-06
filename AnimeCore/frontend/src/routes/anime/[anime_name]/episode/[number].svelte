<!-- <script context="module" lang="ts">
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
			props: {
				backendVimeVolume: 0
			}
		};
	}
</script> -->
<script lang="ts">
	export let backendVimeVolume: number;
	$: {
		if (backendVimeVolume !== 0 && backendVimeVolume) {
			browser && localStorage.setItem("vimejs-volume", JSON.stringify(~~backendVimeVolume));
		}
	}

	import videojs from "video.js";
	import "video.js/dist/video-js.css";

	import { onDestroy } from "svelte";

	import { browser } from "$app/env";
	import { page } from "$app/stores";

	import { responsiveMode } from "$lib/store/responsive";
	import { projectName } from "$lib/constants/frontend/projectName";
	import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";
	import { captureEndpoint } from "$lib/constants/backend/urls/restEndpoints";
	import { isUserAuthenticated, userToken } from "$lib/store/users";

	$: episode_number = parseInt($page.params.number);
	$: anime_name = snakeCaseToTitleCase($page.params.anime_name);

	let videoElement: HTMLVideoElement & { dispose?: () => void };

	const onVolumeChange = async () => {};

	$: {
		if (videoElement) {
			videojs(videoElement, {}, () => {
				console.log("player is ready");
			});
		}
	}
	onDestroy(async () => {
		if (videoElement) {
			videoElement.dispose();
		}
	});
</script>

<svelte:head>
	<title>{anime_name} | Episode : {episode_number} | {projectName}</title>
</svelte:head>

<div class="container pt-5">
	<!-- svelte-ignore a11y-media-has-caption -->
	<video controls preload="auto" bind:this={videoElement} class="video-js vjs-big-play-centered">
		<source src="//vjs.zencdn.net/v/oceans.mp4" type="video/mp4" />
		<source src="//vjs.zencdn.net/v/oceans.webm" type="video/webm" />
	</video>
</div>
<div class="container pt-5">
	<!-- Main container -->
	<nav class="level is-mobile">
		<!-- Left side -->
		<div class={`level-left ${$responsiveMode === "mobile" ? "is-size-6" : "is-size-4"}`}>
			<div class="level-item">
				<a
					href={`/anime/${$page.params.anime_name}/episode/${episode_number - 1}`}
					sveltekit:prefetch
					sveltekit:noscroll
				>
					<ion-icon name="arrow-back-outline" class="has-text-white" />
				</a>
			</div>
		</div>

		<!-- Middle side -->
		<div class="level-item">
			<p class={`has-text-white ${$responsiveMode === "mobile" ? "is-size-6" : "is-size-4"}`}>
				Anime Name : {anime_name} | Episode :
				{episode_number}
			</p>
		</div>

		<!-- Right side -->
		<div class={`level-right ${$responsiveMode === "mobile" ? "is-size-6" : "is-size-4"}`}>
			<p class="level-item">
				<a
					href={`/anime/${$page.params.anime_name}/episode/${episode_number + 1}`}
					sveltekit:prefetch
					sveltekit:noscroll
				>
					<ion-icon name="arrow-forward-outline" class="has-text-white" />
				</a>
			</p>
		</div>
	</nav>
</div>
