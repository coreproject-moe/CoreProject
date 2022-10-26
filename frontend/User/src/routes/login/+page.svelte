<script lang="ts">
	let background_image = 'https://placeimg.com/1000/800/arch';

	let CHOICES = [
		'https://images.unsplash.com/photo-1666688090267-4858c2075629?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=600&q=60',
		'https://placeimg.com/1000/800/arch'
	];
	var index = Math.floor(Math.random() * CHOICES.length);

	setInterval(() => {
		background_image = CHOICES[index];
	}, 5000);
</script>

<div class="grid h-screen justify-center content-center">
	<div style="grid-area: 1 / 1 / 2 / 2">
		<div>Hello</div>
	</div>
	<div style="grid-area: 1 / 1 / 2 / 2">
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
