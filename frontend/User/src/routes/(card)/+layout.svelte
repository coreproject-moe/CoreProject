<script lang="ts">
	import { blur } from 'svelte/transition';
	import { onMount } from 'svelte';

	let CHOICE_NUMBER = 1;
	let CHOICES: typeof window.DJANGO.IMAGE_CHOICES = [];

	onMount(() => {
		CHOICES = window.DJANGO.IMAGE_CHOICES;

		setInterval(() => {
			const index = Math.floor(Math.random() * CHOICES.length);
			CHOICE_NUMBER = index;
			console.log(index);
		}, 5000);
	});

	const formatType = (input: string) => {};
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
		<slot />
	</div>
</div>

<style lang="scss">
</style>
