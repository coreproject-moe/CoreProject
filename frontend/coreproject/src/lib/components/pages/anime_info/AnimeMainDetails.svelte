<script lang="ts">
	export let anime: any;

	import ScrollArea from '$components/shared/ScrollArea.svelte';
	import SidebarDetails from '$components/pages/anime_info/SidebarDetails.svelte';

	// icons
	import PlayCircle from '$icons/PlayCircle.svelte';
	import Read from '$icons/Read.svelte';
	import Listen from '$icons/Listen.svelte';
	import Video from '$icons/Video.svelte';
	import Download from '$icons/Download.svelte';
	import Share from '$icons/Share.svelte';
	import SettingsOutline from '$icons/SettingsOutline.svelte';
	import Edit from '$icons/Edit.svelte';
</script>

<div class="grid grid-cols-12 items-start">
	<div class="col-span-10 grid grid-cols-12 items-end">
		<div class="col-span-7 flex items-end gap-10">
			<img class="md:w-1/3 2xl:w-2/5 md:rounded-xl 2xl:rounded-3xl" src={anime.cardBackgroundImage} alt={anime.titles.eng} />
			<div>
				<h2 class="font-bold 2xl:!text-6xl">{anime.titles.eng}</h2>

				<div class="anime_titles mt-3 flex items-center gap-2 md:text-xs 2xl:!text-lg font-medium opacity-80">
					<span>{anime.titles.japanese}</span>
					<span>-</span>
					<span>{anime.titles.eng}</span>
					<span>-</span>
					<span>{anime.titles.others}</span>
				</div>

				<div
					class="anime_basic_details mt-2 flex flex-wrap items-center gap-2 pr-5 md:text-xs 2xl:!text-lg 2xl:!leading-none font-semibold opacity-100"
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

				<div class="md:mt-5 2xl:mt-10 flex items-center gap-5">
					<button
						type="button"
						class="btn 2xl:btn-lg md:h-16 2xl:h-24 justify-start md:rounded-lg 2xl:rounded-xl bg-primary-500 md:text-xs 2xl:text-xl font-bold text-white"
					>
						<PlayCircle width="30" height="30" color="white" />
						<div class="flex flex-col items-start">
							<span class="leading-5">Watch</span>
							<span class="md:text-[0.6rem] 2xl:text-lg font-normal leading-none opacity-70">Ep 01</span>
						</div>
					</button>

					<button
						type="button"
						class="btn md:h-16 2xl:h-24 2xl:w-24 flex-col gap-1 md:rounded-lg 2xl:rounded-xl bg-secondary-100 md:text-xs 2xl:text-xl md:font-bold 2xl:font-semibold text-surface-500"
					>
						<Read width="22" height="22" color="bg-surface-500" />
						Read
					</button>

					<button
						type="button"
						class="btn md:h-16 2xl:h-24 2xl:w-24 flex-col gap-1 md:rounded-lg 2xl:rounded-xl bg-secondary-100 md:text-xs 2xl:text-xl md:font-bold 2xl:font-semibold text-surface-500"
					>
						<Listen width="22" height="22" color="bg-surface-500" />
						Listen
					</button>
				</div>

				<div class="user_options mt-5 flex md:gap-2 2xl:gap-3">
					<button
						type="button"
						class="btn-icon md:btn-icon-sm 2xl:btn-icon-lg md:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Video width="20" />
					</button>

					<button
						type="button"
						class="btn-icon md:btn-icon-sm 2xl:btn-icon-lg md:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Edit width="20" variant="with_underline_around_pencil" />
					</button>

					<button
						type="button"
						class="btn-icon md:btn-icon-sm 2xl:btn-icon-lg md:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Download width="20" />
					</button>

					<button
						type="button"
						class="btn-icon md:btn-icon-sm 2xl:btn-icon-lg md:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Share width="20" />
					</button>
				</div>
			</div>
		</div>

		<div class="col-span-5 pr-8">
			<div class="flex items-center gap-4">
				<h4 class="font-semibold 2xl:!text-4xl">
					Synopsis
				</h4>
				<SettingsOutline width="15" height="15" class="opacity-75" />
			</div>

			<ScrollArea
				offsetScrollbar
				parentClass="mt-5"
				class="md:max-h-36 2xl:max-h-52 text-justify md:!text-xs 2xl:!text-lg 2xl:!leading-normal"
			>
				{anime.description}
			</ScrollArea>

			<div class="md:mt-3 2xl:mt-5 flex gap-2">
				{#each anime.generes as genere}
					<div class="rounded bg-surface-500 p-1 px-3 md:text-xs 2xl:!text-lg text-white">
						{genere}
					</div>
				{/each}
			</div>

			<div class="mt-3 flex w-max items-center gap-2 rounded bg-white/20 p-1 px-3 md:text-[10px] 2xl:!text-[15px]">
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
	</div>

	<div class="col-span-2 mt-10">
		<SidebarDetails {anime} />
	</div>
</div>
