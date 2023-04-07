<script lang="ts">
	export let anime: any;

	// icons
	import PlayCircle from '$icons/PlayCircle.svelte';
	import Read from '$icons/Read.svelte';
	import Listen from '$icons/Listen.svelte';
	import Video from '$icons/Video.svelte';
	import Download from '$icons/Download.svelte';
	import Share from '$icons/Share.svelte';
	import SettingsOutline from '$icons/SettingsOutline.svelte';
	import TrendingUp from '$icons/Trending-Up.svelte';
	import Star from '$icons/Star.svelte';
	import Edit from '$icons/Edit.svelte';
	import ExternalLink from '$icons/ExternalLink.svelte';

	const roundedRating = Math.floor(anime.rating);
	const grayStars = 5 - roundedRating;

	const ratingPercentage = Math.ceil((anime.rating / 5) * 100);

	const k_formatter = (total_rating: number) => {
		return Math.abs(total_rating) > 999
			? Math.sign(total_rating) * Number((Math.abs(total_rating) / 1000).toFixed(1)) + 'k'
			: Math.sign(total_rating) * Math.abs(total_rating);
	};
</script>

<div class="grid grid-cols-12 items-end">
	<div class="col-span-6 flex items-end gap-10">
		<img class="w-1/3 rounded-xl" src={anime.cardBackgroundImage} alt={anime.titles.eng} />
		<div>
			<h2 class="font-bold">{anime.titles.eng}</h2>

			<div class="anime_titles mt-3 flex items-center gap-2 text-xs font-medium opacity-80">
				<span>{anime.titles.japanese}</span>
				<span>-</span>
				<span>{anime.titles.eng}</span>
				<span>-</span>
				<span>{anime.titles.others}</span>
			</div>

			<div
				class="anime_basic_details mt-2 flex flex-wrap items-center gap-2 pr-5 text-xs font-semibold opacity-100"
			>
				<span>{anime.type}</span>
				<span>-</span>
				<span>{anime.episodes} eps</span>
				<span>-</span>
				<span>{anime.status}</span>
				<span>-</span>
				<span>{anime.premiered}</span>
				<span>-</span>
				<span>{anime.studio}</span>
			</div>

			<div class="mt-5 flex items-center gap-5">
				<button
					type="button"
					class="btn h-16 justify-start rounded-lg bg-primary-500 py-3 pl-4 text-xs font-bold text-white"
				>
					<PlayCircle width="30" height="30" color="white" />
					<div class="flex flex-col items-start">
						<span class="leading-5">Watch</span>
						<span class="text-[0.6rem] font-normal leading-none opacity-70">Ep 01</span>
					</div>
				</button>

				<button
					type="button"
					class="btn h-16 flex-col gap-1 rounded-lg bg-secondary-100 text-xs font-bold text-surface-500"
				>
					<Read width="22" height="22" color="bg-surface-500" />
					Read
				</button>

				<button
					type="button"
					class="btn h-16 flex-col gap-1 rounded-lg bg-secondary-100 text-xs font-bold text-surface-500"
				>
					<Listen width="22" height="22" color="bg-surface-500" />
					Listen
				</button>
			</div>

			<div class="user_options mt-5 flex gap-2">
				<button
					type="button"
					class="btn-icon btn-icon-sm rounded bg-warning-400 p-0 text-surface-500"
				>
					<Video width="20" />
				</button>

				<button
					type="button"
					class="btn-icon btn-icon-sm rounded bg-warning-400 p-0 text-surface-500"
				>
					<Edit width="20" variant="with_underline_around_pencil" />
				</button>

				<button
					type="button"
					class="btn-icon btn-icon-sm rounded bg-warning-400 p-0 text-surface-500"
				>
					<Download width="20" />
				</button>

				<button
					type="button"
					class="btn-icon btn-icon-sm rounded bg-warning-400 p-0 text-surface-500"
				>
					<Share width="20" />
				</button>
			</div>
		</div>
	</div>

	<div class="col-span-4 pr-8">
		<div class="flex items-center gap-4">
			<h4 class="font-semibold">Synopsis</h4>
			<SettingsOutline width="15" height="15" class="opacity-75" />
		</div>
		<div
			class="mt-5 h-36 overflow-hidden pr-3 scrollbar scrollbar-track-white scrollbar-thumb-surface-200 scrollbar-track-rounded-xl scrollbar-thumb-rounded-xl scrollbar-w-1 hover:overflow-y-scroll hover:pr-2"
		>
			<p class="text-justify !text-xs opacity-80">
				{anime.description}
			</p>
		</div>

		<div class="mt-3 flex gap-2">
			{#each anime.generes as genere}
				<div class="rounded bg-surface-500 p-1 px-3 text-xs text-white">
					{genere}
				</div>
			{/each}
		</div>

		<div class="mt-3 flex w-max items-center gap-2 rounded bg-white/20 p-1 px-3 text-[10px]">
			<div class="flex items-center gap-1">
				Score:
				<span class="text-warning-400">{anime.score}</span>
			</div>
			<div class="flex items-center gap-1">
				Status:
				<span class="text-warning-400">{anime.status}</span>
			</div>
			<div class="flex items-center gap-1">
				Episode:
				<span class="text-warning-400">0/{anime.episodes}</span>
			</div>
			<div class="flex items-center gap-1">
				Your Score:
				<span class="text-warning-400">Not Rated</span>
			</div>
		</div>
	</div>

	<div class="col-span-2">
		<div class="flex items-center gap-4">
			<h4 class="font-semibold">Ratings</h4>
			<SettingsOutline width="15" height="15" class="opacity-75" />
		</div>

		<div class="mt-4">
			<div>
				<span class="text-3xl font-bold underline decoration-white/25 underline-offset-[15px]"
					>{ratingPercentage}%</span
				>
				<span class="text-xs">| {k_formatter(anime.totalResponse)} Ratings</span>
			</div>

			<div class="mt-3">
				{#each anime.milestones as milestone}
					<div class="flex items-center gap-2">
						<span>#{milestone.value}</span>
						<span class="text-xs opacity-80">{milestone.title}</span>
					</div>
				{/each}
			</div>

			<button class="btn btn-sm mt-3 gap-2 rounded bg-secondary-100 px-2 py-1 text-xs text-surface-500">
				<TrendingUp width="15" height="15" />
				Detailed Distribution
			</button>

			<div class="rating mt-2">
				<span class="text-xs">Your rating</span>

				<div class="ratings flex items-center gap-3">
					<div class="flex gap-2">
						<!-- <Star width="15" height="15" fill="fill-white" />
						<Star width="15" height="15" fill="fill-white" />
						<Star width="15" height="15" fill="fill-white" />
						<Star width="15" height="15" fill="fill-white" />
						<Star width="15" height="15" /> -->
						{#each Array(roundedRating) as _}
							<Star variation="solid" size="15" class="text-white" />
						{/each}
						{#each Array(grayStars) as _}
							<Star variation="outline" size="15" class="text-white" />
						{/each}
					</div>
					<span class="text-xs font-bold">{ratingPercentage}%</span>
					<button class="btn-icon w-6 h-6 rounded bg-secondary-100 p-0 text-surface-500">
						<Edit
							width="13"
							height="13"
							variant="without_underline_around_pencil"
							color="bg-surface-500"
						/>
					</button>
				</div>
			</div>

			<button class="review btn btn-sm mt-2 flex items-center gap-2 p-0 text-xs">
				Add a review
				<ExternalLink width="15" height="15" />
			</button>
		</div>
	</div>
</div>
