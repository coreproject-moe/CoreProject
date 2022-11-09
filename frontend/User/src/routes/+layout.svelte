<script lang="ts">
	import '../app.scss';

	import { blur } from 'svelte/transition';
	let CHOICES = [
		'https://images.unsplash.com/photo-1666688090267-4858c2075629',
		'https://images.unsplash.com/photo-1666756272254-724e9ed61321',
		'https://images.unsplash.com/photo-1666845266582-7885e3485303'
	];

	let CHOICE_NUMBER = 1;

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

<div class="grid bg-black">
	<!-- Background Image Container -->
	{#each CHOICES as item}
		{#if CHOICES.indexOf(item) == CHOICE_NUMBER}
			<div transition:blur|local style="grid-area: 1 / 1 / 2 / 2">
				<div
					class="h-screen w-screen bg-no-repeat bg-center bg-cover brightness-50"
					style="background-image:url('{item}')"
				/>
			</div>
		{/if}
	{/each}

	<slot />
</div>
