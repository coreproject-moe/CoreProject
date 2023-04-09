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
		<span class="font-semibold md:text-[1.6vw]">Ratings</span>
		<SettingsOutline width="15" height="15" class="opacity-75" />
	</div>

	<div class="md:mt-3">
		<div class="divide-x flex items-end gap-3">
			<span class="md:text-[2.5vw] font-bold underline decoration-white/25 underline-offset-[2vh]"
				>{Math.ceil((anime.rating / 5) * 100)}%</span
			>
			<span class="md:text-[0.8vw] pl-2">{anime.totalResponse} Ratings</span>
		</div>

		<div class="md:mt-3">
			{#each anime.milestones as milestone}
				<div class="flex items-center md:gap-2">
					<span class="md:text-[1.3vw]">#{milestone.value}</span>
					<span class="md:text-[1vw] text-surface-50">{milestone.title}</span>
				</div>
			{/each}
		</div>

		<button
			class="btn md:mt-3 gap-2 rounded bg-secondary-100 md:w-[12vw] md:h-[3vh] p-0 md:text-[1vw] text-surface-500"
		>
			<TrendingUp width="15" height="15" />
			Detailed Distribution
		</button>

		<div class="md:mt-3">
			<span class="md:text-[1vw]">Your rating</span>

			<div class="flex items-center gap-3">
				<div class="flex gap-2">
					{#each Array(Math.floor(anime.rating)) as _}
						<Star variation="solid" size="18" class="text-white" />
					{/each}
					{#each Array(5 - Math.floor(anime.rating)) as _}
						<Star variation="outline" size="18" class="text-white" />
					{/each}
				</div>
				<span class="md:text-[1.3vw] font-bold">{Math.ceil((anime.rating / 5) * 100)}%</span>
				<button class="btn-icon rounded bg-secondary-100 p-1 text-surface-500">
					<Edit
						width="13"
						height="13"
						variant="without_underline_around_pencil"
						color="bg-surface-500"
					/>
				</button>
			</div>
		</div>

		<button class="btn btn-sm mt-2 flex items-center gap-2 p-0 md:text-[1vw]">
			Add a review
			<ExternalLink width="15" height="15" />
		</button>
	</div>
</div>
