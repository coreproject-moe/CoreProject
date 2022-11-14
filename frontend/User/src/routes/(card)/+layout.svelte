<script lang="ts">
	import { blur } from 'svelte/transition';
	import { onMount } from 'svelte';

	let CHOICE_NUMBER = 1;
	let CHOICES: string[] = [];

	onMount(() => {
		CHOICES = window.IMAGE_CHOICES;

		setInterval(() => {
			const index = Math.floor(Math.random() * CHOICES.length);
			CHOICE_NUMBER = index;
			console.log(index);
		}, 5000);
	});
</script>

<svelte:head>
	{#each CHOICES as image}
		<link rel="preload" as="image" href={image} />
	{/each}
</svelte:head>

<div class="grid h-screen">
	<!-- Background Image Container -->
	{#each CHOICES as item}
		{#if CHOICES.indexOf(item) == CHOICE_NUMBER}
			<div transition:blur|local class="bg-black h-screen fixed" style="grid-area: 1 / 1 / 2 / 2;">
				<div
					class="h-screen w-screen bg-no-repeat bg-center bg-cover brightness-90"
					style="background-image:url('{item}')"
				/>
				<div
					class="absolute inset-0 bg-gradient-to-t from-base-100 via-base-100/[.8] md:via-base-100/[.0001]"
				/>
				<div class="absolute bottom-8 left-8">
					<div class="flex flex-col">
						<div class="text-secondary">Background from the anime</div>
						<div class="text-white">Comic Girls</div>
					</div>
				</div>
			</div>
		{/if}
	{/each}

	<slot />
</div>

<style lang="scss">
	.background {
		background-image: linear-gradient(to top, var(--tw-gradient-stops));

		@media screen and (min-width: 768px) {
			background-image: linear-gradient(to top, var(--tw-gradient-stops)),
				linear-gradient(to left, var(--tw-gradient-stops)),
				linear-gradient(to right, var(--tw-gradient-stops));
		}
	}
</style>
