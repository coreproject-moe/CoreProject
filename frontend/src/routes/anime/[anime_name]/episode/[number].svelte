<script lang="ts">
	import { onMount } from "svelte";
	import { get } from "svelte/store";

	import { browser } from "$app/env";
	import { page } from "$app/stores";

	import { useEffect } from "$hooks/useEffect";
	import { responsiveMode } from "$lib/store/responsive";
	import { projectName } from "$lib/constants/frontend/projectName";
	import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";
	import { captureEndpoint } from "$lib/constants/backend/urls/restEndpoints";
	import { isUserAuthenticated, userToken } from "$lib/store/users";

	$: episode_number = parseInt($page.params.number);
	$: anime_name = snakeCaseToTitleCase($page.params.anime_name);

	let showPlayer = false;
	let player: HTMLVmPlayerElement;

	onMount(async () => {
		const { defineCustomElements } = await import("@vime/core");
		await import("@vime/core/themes/default.css");

		defineCustomElements();
		showPlayer = true;
	});

	useEffect(
		() => {
			const localStorageVideoVolume =
				parseInt(browser && localStorage.getItem("vimejs-volume")) || 100;
			player.volume = localStorageVideoVolume;
		},
		() => [player]
	);

	const onVolumeChange = async () => {
		if (browser && $isUserAuthenticated) {
			localStorage.setItem("vimejs-volume", JSON.stringify(player?.volume));

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
	};
</script>

<svelte:head>
	<title>{anime_name} | Episode : {episode_number} | {projectName}</title>
</svelte:head>

<div class="container pt-5">
	{#if showPlayer}
		<vm-player autoplay bind:this={player} on:vmVolumeChange={onVolumeChange}>
			<vm-video poster="https://media.vimejs.com/poster.png" cross-origin>
				<source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
				<track default kind="subtitles" src="/media/subs/en.vtt" srclang="en" label="English" />
			</vm-video>
			<vm-default-ui />
		</vm-player>
	{/if}
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
