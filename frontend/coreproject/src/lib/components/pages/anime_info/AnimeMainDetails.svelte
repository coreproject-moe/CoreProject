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
	<div class="col-span-10 grid grid-cols-12 items-end xl:gap-10">
		<div class="col-span-7 flex items-end gap-10">
			<img class="xl:w-60 2xl:w-96 xl:rounded-xl 2xl:rounded-3xl" src={anime.cardBackgroundImage} alt={anime.titles.eng} />
			<div>
				<h2 class="font-bold 2xl:!text-5xl 3xl:!text-6xl">{anime.titles.eng}</h2>

				<div class="pt-3 3xl:mt-5 flex items-center gap-2 xl:text-xs 2xl:text-sm 3xl:!text-[16px] font-medium text-surface-100">
					<span>{anime.titles.japanese}</span>
					<span>-</span>
					<span>{anime.titles.eng}</span>
					<span>-</span>
					<span>{anime.titles.others}</span>
				</div>

				<div
					class="pt-4 flex flex-wrap items-center gap-2 pr-5 xl:text-xs 2xl:text-sm 3xl:!text-[16px] 2xl:!leading-none font-semibold"
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

				<div class="xl:mt-5 2xl:mt-7 3xl:mt-12 flex items-center xl:gap-3 2xl:gap-5">
					<button
						type="button"
						class="btn 2xl:btn-md 3xl:btn-lg xl:h-16 2xl:h-20 justify-start xl:rounded-lg 2xl:rounded-xl bg-primary-500 xl:text-xs 2xl:text-xl font-bold text-white"
					>
						<PlayCircle width="30" height="30" color="white" />
						<div class="flex flex-col items-start">
							<span class="leading-5">Watch</span>
							<span class="xl:text-[0.6rem] 2xl:text-lg font-normal leading-none opacity-70">Ep 01</span>
						</div>
					</button>

					<button
						type="button"
						class="btn xl:h-16 2xl:h-20 2xl:w-20 3xl:w-24 flex-col gap-1 xl:rounded-lg 2xl:rounded-xl bg-secondary-100 xl:text-xs 2xl:text-base 3xl:text-xl xl:font-bold 2xl:font-semibold text-surface-500"
					>
						<Read width="22" height="22" color="bg-surface-500" />
						Read
					</button>

					<button
						type="button"
						class="btn xl:h-16 2xl:h-20 2xl:w-20 3xl:w-24 flex-col gap-1 xl:rounded-lg 2xl:rounded-xl bg-secondary-100 xl:text-xs 2xl:text-base 3xl:text-xl xl:font-bold 2xl:font-semibold text-surface-500"
					>
						<Listen width="22" height="22" color="bg-surface-500" />
						Listen
					</button>
				</div>

				<div class="user_options mt-5 flex xl:gap-2 2xl:gap-3">
					<button
						type="button"
						class="btn-icon xl:btn-icon-sm 3xl:btn-icon-lg 2xl:w-12 3xl:w-10 2xl:h-12 3xl:h-10 xl:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Video width="20" />
					</button>

					<button
						type="button"
						class="btn-icon xl:btn-icon-sm 2xl:btn-icon-lg 2xl:w-12 3xl:w-10 2xl:h-12 3xl:h-10 xl:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Edit width="20" variant="with_underline_around_pencil" />
					</button>

					<button
						type="button"
						class="btn-icon xl:btn-icon-sm 2xl:btn-icon-lg 2xl:w-12 3xl:w-10 2xl:h-12 3xl:h-10 xl:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Download width="20" />
					</button>

					<button
						type="button"
						class="btn-icon xl:btn-icon-sm 2xl:btn-icon-lg 2xl:w-12 3xl:w-10 2xl:h-12 3xl:h-10 xl:rounded 2xl:rounded-lg bg-warning-400 p-0 text-surface-500"
					>
						<Share width="20" />
					</button>
				</div>
			</div>
		</div>

		<div class="col-span-5 pr-8">
			<div class="flex items-center gap-4">
				<h4 class="font-semibold 2xl:!text-2xl 3xl:!text-3xl">
					Synopsis
				</h4>
				<SettingsOutline width="15" height="15" class="opacity-75" />
			</div>

			<ScrollArea
				offsetScrollbar
				parentClass="mt-4 2xl:mt-6 3xl:mt-8"
				class="xl:max-h-40 3xl:max-h-60 text-justify xl:!text-xs 2xl:!text-base 2xl:!leading-normal text-surface-50"
			>
				{anime.description}
			</ScrollArea>

			<div class="xl:mt-3 2xl:mt-5 3xl:mt-10 flex gap-2">
				{#each anime.generes as genere}
					<div class="rounded bg-surface-500 p-1 px-3 xl:text-xs 2xl:!text-base 3xl:!text-lg text-white">
						{genere}
					</div>
				{/each}
			</div>

			<div class="xl:mt-3 3xl:mt-6 flex w-max items-center gap-2 rounded bg-white/20 p-1 px-3 3xl:p-2 3xl:px-5 xl:text-[10px] 2xl:text-xs 3xl:!text-[15px]">
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

	<div class="col-span-2 xl:mt-10 2xl:mt-3 3xl:mt-10">
		<SidebarDetails {anime} />
	</div>
</div>