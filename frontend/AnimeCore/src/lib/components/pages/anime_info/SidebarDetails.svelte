<script lang="ts">
	export let anime: any;

	import StarRating from 'svelte-star-rating';

	// icons
	import SettingsOutline from '$icons/SettingsOutline.svelte';
	import TrendingUp from '$icons/Trending-Up.svelte';
	import Edit from '$icons/Edit.svelte';
	import ExternalLink from '$icons/ExternalLink.svelte';
</script>

<div>
	<div class="flex items-center gap-4">
		<span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Ratings</span>
		<SettingsOutline width="15" height="15" class="opacity-75" />
	</div>

	<div class="md:mt-[1.56vw]">
		<div class="flex items-end md:gap-[0.3vw]">
			<span class="md:text-[2vw] md:leading-[1.5vw] font-bold underline decoration-white/25 underline-offset-8"
				>{Math.ceil((anime.rating / 5) * 100)}%</span
			>
			<span class="md:text-[0.75vw] md:leading-[0.9vw] md:pl-2 divider-vertical !border-white/25">{anime.totalResponse} Ratings</span>
		</div>

		<div class="md:mt-[1.125vw]">
			{#each anime.milestones as milestone}
				<div class="flex items-center md:gap-[0.25vw]">
					<span class="md:text-[1vw] md:leading-[1.5vw]">#{milestone.value}</span>
					<span class="md:text-[0.625vw] md:leading-[0.75vw] text-surface-50">{milestone.title}</span>
				</div>
			{/each}
		</div>

		<button
			class="btn md:mt-[1.125vw] md:rounded-[0.18vw] bg-secondary-100 md:w-[9.125vw] md:h-[2vh] md:text-[0.75vw] md:leading-[0.9vw] text-surface-500"
		>
			<div class="flex items-center justify-center gap-1">
				<TrendingUp width="15" height="15" />
				Detailed Distribution
			</div>
		</button>

		<div class="md:mt-[0.4vw]">
			<span class="md:text-[0.75vw] md:leading-[0.9vw] font-semibold">Your rating</span>
			<div class="flex items-center gap-3 md:mt-[0.375vw]">
				<StarRating rating={anime.rating} config={{size: 18}} style={"margin: 0;"} />
				<span class="md:text-[0.95vw] md:leading-[1.125vw] font-bold">{Math.ceil((anime.rating / 5) * 100)}%</span>
				<button class="btn-icon md:w-[1.375vw] md:rounded-[0.19vw] bg-secondary-100 p-1 text-surface-500">
					<Edit
						width="13"
						height="13"
						variant="without_underline_around_pencil"
						color="bg-surface-500"
					/>
				</button>
			</div>
		</div>

		<button class="btn btn-sm md:mt-[1.25vw] flex items-center gap-2 p-0 md:text-[0.75vw] md:leading-[0.9vw]">
			Add a review
			<ExternalLink width="11" height="11" />
		</button>
	</div>
</div>
