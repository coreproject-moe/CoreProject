<script lang="ts">
	import { browser } from '$app/env';
	import { page } from '$app/stores';

	import { useEffect } from '$lib/hooks/useEffect';
	import { projectName } from '$lib/constants/frontend/projectName';
	import { snakeCaseToTitleCase } from '$lib/functions/snakeCaseToTitleCase';

	import { onMount } from 'svelte';
	import { captureEndpoint } from '$lib/constants/backend/urls/restEndpoints';

	import { userToken } from '$lib/store/users';
	import { get } from 'svelte/store';
	import anime from 'animejs';

	$: episode_number = $page.params.number;
	$: anime_name = snakeCaseToTitleCase($page.params.anime_name);

	let showPlayer = false;
	let player: HTMLVmPlayerElement;

	onMount(async () => {
		const { defineCustomElements } = await import('@vime/core');
		defineCustomElements();
		showPlayer = true;

		// Icon control

		anime({
			targets: '.animejs__arrow__forward',
			color: '#FFFFFF'
		});
	});

	useEffect(
		() => {
			const localStorageVideoVolume =
				parseInt(browser && localStorage.getItem('vimejs-volume')) || 100;
			player.volume = localStorageVideoVolume;
		},
		() => [player]
	);

	const onVolumeChange = async () => {
		if (browser) {
			localStorage.setItem('vimejs-volume', JSON.stringify(player?.volume));

			try {
				fetch(captureEndpoint, {
					method: 'PATCH',
					headers: {
						Accept: 'application/json',
						'Content-Type': 'application/json',
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
	<!-- VimeJS import -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@vime/core@^5/themes/default.css" />
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
		<div class="level-left">
			<div class="level-item">
				<p class="subtitle is-5">
					<strong>123</strong> posts
				</p>
			</div>
		</div>

		<!-- Middle side -->
		<div class="level-item">
			<p class="has-text-white is-size-4">
				Anime Name : {anime_name} | Episode :
				{episode_number}
			</p>
		</div>

		<!-- Right side -->
		<div class="level-right">
			<p class="level-item">
				<a href={`/anime/${$page.params.anime_name}/episode/${episode_number + 1}`}>
					<ion-icon name="arrow-forward-outline" class="animejs__arrow__forward" />
				</a>
			</p>
		</div>
	</nav>
</div>
