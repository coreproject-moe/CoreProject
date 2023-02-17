<script lang="ts">
	import { onMount } from 'svelte';
	import { blur } from 'svelte/transition';

	import AnimeCore from '$icons/AnimeCore.svelte';

	let CHOICE_NUMBER: number;
	let CHOICES: Array<{
		type: string;
		name: string;
		image: string;
		credit?: string;
	}> = [
		{
			type: 'anime',
			name: 'Demon Slayer',
			image: '/posters/demon-slayer.webp',
			credit: 'https://www.reddit.com/r/DemonSlayerAnime/comments/tpgpid/demon_slayer_4k_wallpaper/'
		},
		{
			type: 'anime',
			name: 'Attack on Titan',
			image: '/posters/attack-on-titan.jpg'
		},
		{
			type: 'anime',
			name: 'Comic Girls',
			image: '/posters/Comic-Girls-Image.png'
		}
	];

	onMount(() => {
		setInterval(() => {
			const index = Math.floor(Math.random() * CHOICES.length);
			CHOICE_NUMBER = index;
			console.log(index);
		}, 5000);
	});
</script>

<svelte:head>
	{#each CHOICES as item}
		<link rel="preload" as="image" href={item.image} />
	{/each}
</svelte:head>

<div class="grid h-screen">
	<!-- Background Image Container -->
	{#each CHOICES as item}
		{#if CHOICES.indexOf(item) == CHOICE_NUMBER}
			{@const type = () => {
				switch (item.type) {
					case 'anime':
						return 'the anime';
					case 'pixiv':
						return 'the artist';
				}
			}}

			<div transition:blur|local class="bg-black h-screen fixed" style="grid-area: 1 / 1 / 2 / 2;">
				<div
					class="h-screen w-screen bg-no-repeat bg-center bg-cover brightness-90"
					style="background-image:url('{item.image}')"
				/>
				<div
					class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
				/>

				<!-- Top animecore logo div  -->
				<div class="absolute top-8 left-8">
					<AnimeCore width="164" height="25" />
				</div>
				<!-- Background from anime div  -->
				<div class="absolute bottom-8 left-8">
					<div class="flex flex-col">
						<div class="text-secondary">Background from {type()}</div>
						<div class="text-white">{item.name}</div>
					</div>
				</div>
			</div>
		{/if}
	{/each}
	<div class="h-screen grid absolute inset-0">
		<div
			style="grid-area: 1 / 1 / 2 / 2"
			class="inline-grid justify-center md:justify-end content-center"
		>
			<div
				class="card w-96 bg-base-100 shadow-xl mr-0 md:mr-6 bg-transparent from-base-100 bg-gradient-to-t"
			>
				<div class="card-body rounded-2xl">
					<slot />
				</div>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	$border-width: 3px;

	.card {
		border-image: linear-gradient(
				to top,
				transparent 0.1%,
				white 15%,
				transparent,
				rgba(0, 0, 0, 0)
			)
			1 100%;
		border-image-width: $border-width;

		&::before {
			content: '';
			position: absolute;
			bottom: 10.5px;
			right: 0;
			border-left: $border-width solid white;
			border-radius: 9999px;
			width: 1px;
			height: 100px;
			background-color: white;
		}
		&::after {
			content: '';
			position: absolute;
			bottom: 10.5px;
			left: 0;
			border-left: $border-width solid white;
			border-radius: 9999px;
			width: 1px;
			height: 100px;
			background-color: white;
		}
	}
	.card-body {
		z-index: 1;

		&::after {
			position: absolute;
			top: 0px;
			bottom: 0px;
			left: 0px;
			right: 0px;
			z-index: -1;
			box-shadow: inset 0 $border-width * -1 0 0 rgba(250, 250, 250, 0.9);
			content: '';
			border-radius: 16px;
		}
	}
</style>
