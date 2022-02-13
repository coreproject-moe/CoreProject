<script lang="ts">
	import { browser } from '$app/env';

	import { useEffect } from '$lib/hooks/useEffect';
	import { onMount } from 'svelte';

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

	const onVolumeChange = (e) => {
		console.log(typeof e);
	};
</script>

<svelte:head
	><!-- Default theme. ~960B -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@vime/core@^5/themes/default.css" />

	<!-- Optional light theme (extends default). ~400B -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@vime/core@^5/themes/light.css" />
</svelte:head>

<div class="container pt-5">
	{#if showPlayer}
		<vm-player autoplay muted bind:this={player} on:vmVolumeChange={onVolumeChange}>
			<vm-video poster="https://media.vimejs.com/poster.png" cross-origin>
				<source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
				<track default kind="subtitles" src="/media/subs/en.vtt" srclang="en" label="English" />
			</vm-video>
			<vm-default-ui />
		</vm-player>
	{/if}
</div>
