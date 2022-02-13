<script lang="ts">
	import { browser } from '$app/env';
	import { page } from '$app/stores';
	import { projectName } from '$lib/constants/frontend/projectName';
	import { snakeCaseToTitleCase } from '$lib/functions/snakeCaseToTitleCase';

	import { useEffect } from '$lib/hooks/useEffect';
	import { onMount } from 'svelte';

	const episode_number = $page.params.number;
	const anime_name = $page.params.anime_name;

	let showPlayer = false;
	let player: HTMLVmPlayerElement;

	onMount(async () => {
		const { defineCustomElements } = await import('@vime/core');
		defineCustomElements();
		showPlayer = true;
	});

	useEffect(
		() => {
			const localStorageVideoVolume =
				parseInt(browser && localStorage.getItem('vimejs-volume')) || 100;
			player.volume = localStorageVideoVolume;
		},
		() => [player]
	);

	const onVolumeChange = () => {
		browser && localStorage.setItem('vimejs-volume', JSON.stringify(player?.volume));
	};
</script>

<svelte:head>
	<title>{snakeCaseToTitleCase(anime_name)} | Episode : {episode_number} | {projectName}</title>
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

<nav class="level is-mobile pt-5">
	<div class="level-item has-text-centered">
		<div />
	</div>
	<div class="level-item has-text-centered">
		<div>
			<p class="title has-text-white">{`<--`} Episode : {episode_number} {`-->`}</p>
		</div>
	</div>

	<div class="level-item has-text-centered">
		<div />
	</div>
</nav>

<style lang="scss">
	@import url('https://cdn.jsdelivr.net/npm/@vime/core@^5/themes/default.css');
</style>
