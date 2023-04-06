<script lang="ts">
	export let anime: any;

	import { truncate_str } from '$lib/helpers/truncate_str';
	// icons
	import PlayCircle from '$icons/PlayCircle.svelte';
	import Book from '$icons/Book.svelte';
	import HeadPhones from '$icons/HeadPhones.svelte';
	import Video from '$icons/Video.svelte';
	import Edit3 from '$icons/Edit3.svelte';
	import Download from '$icons/Download.svelte';
	import Share from '$icons/Share.svelte';
  import SettingsOutline from '$icons/SettingsOutline.svelte';
  import TrendingUp from '$icons/Trending-Up.svelte';
	import Star from '$icons/Star.svelte';
  import Edit from '$icons/Edit.svelte';
  import ExternalLink from '$icons/ExternalLink.svelte';
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
				class="anime_basic_details mt-2 flex flex-wrap items-center gap-2 text-xs font-semibold opacity-100 pr-5"
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
					<Book width="22" height="22" color="bg-surface-500" />
					Read
				</button>

				<button
					type="button"
					class="btn h-16 flex-col gap-1 rounded-lg bg-secondary-100 text-xs font-bold text-surface-500"
				>
					<HeadPhones width="22" height="22" color="bg-surface-500" />
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
					<Edit3 width="20" />
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

	<div class="col-span-4 pr-10">
		<div class="flex items-center gap-4">
      <h4 class="font-semibold">Synopsis</h4>
      <SettingsOutline width="15" height="15" class="opacity-75" />
    </div>
		<p class="mt-5 text-justify !text-xs opacity-80">
			{truncate_str(anime.description, 500)}
		</p>

		<div class="flex gap-2 mt-3">
			{#each anime.generes as genere}
				<div class="bg-surface-500 p-1 px-3 text-xs text-white rounded">
					{genere}
				</div>
			{/each}
		</div>

    <div class="bg-white/20 rounded mt-3 p-1 px-3 w-max flex items-center gap-2 text-[10px]">
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
        <span class="font-bold text-3xl underline underline-offset-[15px] decoration-white/25">79%</span>
        <span class="text-xs">| 2.8k Ratings</span>
      </div>

      <div class="mt-3">
        <div class="flex items-center gap-2">
          <span>#86</span>
          <span class="text-xs opacity-80">Most popular all time</span>
        </div>
        <div class="flex items-center gap-2">
          <span>#260</span>
          <span class="text-xs opacity-80">Highest rated all time</span>
        </div>
      </div>

      <button class="btn btn-sm bg-secondary-100 text-surface-500 rounded py-1 px-2 text-xs mt-3">
        <TrendingUp width="15" height="15" />
        Detailed Distribution
      </button>

      <div class="rating mt-2">
        <span class="text-xs">Your rating</span>

        <div class="ratings flex items-center gap-3">
            <div class="flex gap-2">
              <Star width="15" height="15" fill="fill-white" />
              <Star width="15" height="15" fill="fill-white" />
              <Star width="15" height="15" fill="fill-white" />
              <Star width="15" height="15" fill="fill-white" />
              <Star width="15" height="15" />
            </div>
            <span class="text-xs font-bold">100%</span>
            <button class="btn-icon btn-icon-sm bg-secondary-100 text-surface-500 rounded p-0">
              <Edit width="10" height="10" color="bg-surface-500" />
            </button>
        </div>
      </div>

      <button class="review btn btn-sm flex items-center gap-2 p-0 text-xs mt-2">
        Add a review
        <ExternalLink width="15" height="15" />
      </button>
    </div>
  </div>
</div>
