<script lang="ts">
	import { onMount } from 'svelte';
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
	}, 1000);
</script>

<svelte:head>
	{#each CHOICES as image}
		<link rel="preload" as="image" href={image} />
	{/each}
</svelte:head>

<div class="grid h-screen w-screen" style="grid-area: 1 / 1 / 2 / 2">
	<!-- Background Image Container -->
	{#each CHOICES as item}
		{#if CHOICES.indexOf(item) == CHOICE_NUMBER}
			<div transition:blur|local style="grid-area: 1 / 1 / 2 / 2">
				<div
					class="h-screen w-screen bg-no-repeat bg-center bg-cover"
					style="background-image:url('{item}')"
				/>
			</div>
		{/if}
	{/each}

	<!-- Login card  -->
	<div style="grid-area: 1 / 1 / 2 / 2" class="inline-grid justify-center content-center">
		<div class="card w-96 bg-base-100 shadow-xl">
			<figure><img src="https://placeimg.com/400/225/arch" alt="Shoes" /></figure>
			<div class="card-body">
				<h2 class="card-title">Shoes!</h2>
				<p>If a dog chews shoes whose shoes does he choose?</p>
				<div class="card-actions justify-end">
					<button class="btn btn-primary">Buy Now</button>
				</div>
			</div>
		</div>
	</div>
</div>
