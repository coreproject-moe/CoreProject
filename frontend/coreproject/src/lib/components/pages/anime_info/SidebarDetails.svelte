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
		<h4 class="font-semibold 2xl:!text-2xl 3xl:!text-3xl">Ratings</h4>
		<SettingsOutline width="15" height="15" class="opacity-75" />
	</div>

	<div class="xl:mt-4 2xl:mt-8">
		<div>
			<span class="xl:text-3xl 2xl:text-4xl 3xl:text-5xl font-bold underline decoration-white/25 underline-offset-[15px]"
				>{Math.ceil((anime.rating / 5) * 100)}%</span
			>
			<span class="xl:text-xs 2xl:text-base 3xl:text-lg">| {anime.totalResponse} Ratings</span>
		</div>

		<div class="xl:mt-3 2xl:mt-5 3xl:mt-7">
			{#each anime.milestones as milestone}
				<div class="flex items-center xl:gap-2 2xl:gap-4 2xl:mt-1">
					<span class="2xl:text-lg 3xl:text-xl">#{milestone.value}</span>
					<span class="xl:text-xs 2xl:text-sm 3xl:text-lg text-surface-50">{milestone.title}</span>
				</div>
			{/each}
		</div>

		<button
			class="btn xl:btn-sm 3xl:btn-lg xl:mt-3 gap-2 rounded bg-secondary-100 px-2 xl:py-1 2xl:px-3 3xl:px-5 text-xs text-surface-500"
		>
			<TrendingUp width="15" height="15" />
			Detailed Distribution
		</button>

		<div class="rating xl:mt-2 2xl:mt-3 3xl:mt-10">
			<span class="xl:text-xs 2xl:text-lg">Your rating</span>

			<div class="ratings flex items-center gap-3">
				<div class="flex gap-2">
					{#each Array(Math.floor(anime.rating)) as _}
						<Star variation="solid" size="18" class="text-white" />
					{/each}
					{#each Array(5 - Math.floor(anime.rating)) as _}
						<Star variation="outline" size="18" class="text-white" />
					{/each}
				</div>
				<span class="xl:text-xs 2xl:text-lg font-bold">{Math.ceil((anime.rating / 5) * 100)}%</span>
				<button class="btn-icon xl:btn-icon-sm rounded bg-secondary-100 p-1 text-surface-500">
					<Edit
						width="13"
						height="13"
						variant="without_underline_around_pencil"
						color="bg-surface-500"
					/>
				</button>
			</div>
		</div>

		<button class="review btn btn-sm mt-2 flex items-center gap-2 p-0 xl:text-xs 2xl:text-lg">
			Add a review
			<ExternalLink width="15" height="15" />
		</button>
	</div>
</div>