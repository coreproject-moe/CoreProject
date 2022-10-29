<script lang="ts">
	let CHOICES = [
		'https://images.unsplash.com/photo-1666688090267-4858c2075629',
		'https://placeimg.com/1000/800/arch'
	];
	var index = Math.floor(Math.random() * CHOICES.length);

	let CHOICE_NUMBER = 1;

	setInterval(() => {
		CHOICE_NUMBER = index;
	}, 1000);
</script>

<div class="grid h-screen w-screen">
	<!-- Background Image Container -->
	<div style="grid-area: 1 / 1 / 2 / 2">
		{#each CHOICES as item}
			{#if CHOICES.indexOf(item) == CHOICE_NUMBER}
				<div
					class="h-screen w-screen bg-no-repeat bg-center bg-cover"
					style="background-image:url('{item}')"
				/>
			{/if}
		{/each}
	</div>

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
