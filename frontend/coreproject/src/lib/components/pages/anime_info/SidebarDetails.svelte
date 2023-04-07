<script lang="ts">
	export let anime: any;

	// icons
	import SettingsOutline from '$icons/SettingsOutline.svelte';
	import TrendingUp from '$icons/Trending-Up.svelte';
	import Star from '$icons/Star.svelte';
	import Edit from '$icons/Edit.svelte';
	import ExternalLink from '$icons/ExternalLink.svelte';
</script>

<div>
	<div class="flex items-center gap-4">
		<h4 class="font-semibold 2xl:!text-4xl">Ratings</h4>
		<SettingsOutline width="15" height="15" class="opacity-75" />
	</div>

	<div class="md:mt-4 2xl:mt-5">
		<div>
			<span class="md:text-3xl 2xl:text-5xl font-bold underline decoration-white/25 underline-offset-[15px]"
				>{Math.ceil((anime.rating / 5) * 100)}%</span
			>
			<span class="md:text-xs 2xl:text-lg">| {anime.totalResponse} Ratings</span>
		</div>

		<div class="md:mt-3 2xl:mt-5">
			{#each anime.milestones as milestone}
				<div class="flex items-center md:gap-2 2xl:gap-4 2xl:mt-1">
					<span class="2xl:text-xl">#{milestone.value}</span>
					<span class="md:text-xs 2xl:text-lg opacity-80">{milestone.title}</span>
				</div>
			{/each}
		</div>

		<button
			class="btn md:btn-sm 2xl:btn-lg md:mt-3 gap-2 rounded bg-secondary-100 px-2 md:py-1 2xl:px-5 text-xs text-surface-500"
		>
			<TrendingUp width="15" height="15" />
			Detailed Distribution
		</button>

		<div class="rating md:mt-2 xl:mt-4">
			<span class="md:text-xs 2xl:text-lg">Your rating</span>

			<div class="ratings flex items-center gap-3">
				<div class="flex gap-2">
					{#each Array(Math.floor(anime.rating)) as _}
						<Star variation="solid" size="18" class="text-white" />
					{/each}
					{#each Array(5 - Math.floor(anime.rating)) as _}
						<Star variation="outline" size="18" class="text-white" />
					{/each}
				</div>
				<span class="md:text-xs xl:text-lg font-bold">{Math.ceil((anime.rating / 5) * 100)}%</span>
				<button class="btn-icon 2xl:btn-icon-sm rounded bg-secondary-100 p-1 text-surface-500">
					<Edit
						width="13"
						height="13"
						variant="without_underline_around_pencil"
						color="bg-surface-500"
					/>
				</button>
			</div>
		</div>

		<button class="review btn btn-sm mt-2 flex items-center gap-2 p-0 md:text-xs 2xl:text-lg">
			Add a review
			<ExternalLink width="15" height="15" />
		</button>
	</div>
</div>
