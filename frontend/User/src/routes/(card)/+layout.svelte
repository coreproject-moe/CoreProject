<script lang="ts">

	import { blur } from 'svelte/transition';
	import { browser } from '$app/environment';

	let CHOICE_NUMBER = 1;

	let CHOICES = browser ? window.IMAGE_CHOICES : [];

	setInterval(() => {
		const index = Math.floor(Math.random() * CHOICES.length);
		CHOICE_NUMBER = index;
		console.log(index);
	}, 5000);
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
					class="h-screen w-screen bg-no-repeat bg-center bg-cover brightness-50"
					style="background-image:url('{item}')"
				/>
			</div>
		{/if}
	{/each}

	<slot />
</div>
