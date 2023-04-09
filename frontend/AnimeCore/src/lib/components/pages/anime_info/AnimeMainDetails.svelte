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

	const icon_mapping = {
		anime_options: {
			read: {
				icon: {
					component: Read,
					width: 22,
					height: 22,
					color: "bg-surface-500"
				}
			},
			listen: {
				icon: {
					component: Listen,
					width: 22,
					height: 22,
					color: "bg-surface-500"
				}
			},
		},
		user_options_icons : {
			video: {
				icon: {
					component: Video,
					variant: false,
					width: 20,
					height: 20
				}
			},
			edit: {
				icon: {
					component: Edit,
					variant: "with_underline_around_pencil",
					width: 20,
					height: 20
				}
			},
			download: {
				icon: {
					component: Download,
					variant: false,
					width: 20,
					height: 20
				}
			},
			share: {
				icon: {
					component: Share,
					variant: false,
					width: 20,
					height: 20
				}
			}
		}
	}
</script>

<div class="grid grid-cols-12 items-start">
	<div class="col-span-10 grid grid-cols-12 items-end md:gap-10">
		<div class="col-span-7 flex items-end gap-10">
			<img class="md:w-[15vw] md:rounded-xl" src={anime.cardBackgroundImage} alt={anime.titles.eng} />
			<div>
				<span class="font-bold md:text-[3vw]">{anime.titles.eng}</span>

				<p class="flex items-center gap-2 text-surface-100">
					<span class="md:text-[0.8vw] font-medium after:content-['▪'] after:ml-1">{anime.titles.japanese}</span>
					<span class="md:text-[0.8vw] font-medium after:content-['▪'] after:ml-1">{anime.titles.eng}</span>
					<span class="md:text-[0.8vw] font-medium">{anime.titles.others}</span>
				</p>

				<p class="pt-2 flex flex-wrap items-center gap-2 pr-5">
					<span class="md:text-[0.9vw] md:leading-none font-semibold after:content-['▪'] after:ml-1">
						{anime.type}
					</span>
					<span class="md:text-[0.9vw] md:leading-none font-semibold after:content-['▪'] after:ml-1">
						{anime.episodes} eps
					</span>
					<span class="md:text-[0.9vw] md:leading-none font-semibold after:content-['▪'] after:ml-1">
						{anime.status}</span>
					<span class="md:text-[0.9vw] md:leading-none font-semibold after:content-['▪'] after:ml-1">
						{anime.premiered}
					</span>
					<span class="md:text-[0.9vw] md:leading-none font-semibold">{anime.studio}</span>
				</p>

				<div class="md:mt-10 flex items-center md:gap-4">
					<button
						type="button"
						class="btn md:h-[8vh] md:w-[8vw] justify-center md:rounded-lg bg-primary-500 md:text-[1vw] font-bold text-white"
					>
						<PlayCircle width="30" height="30" color="white" />
						<div class="flex flex-col items-start">
							<span class="md:leading-5">Watch</span>
							<span class="md:text-[0.8vw] font-normal leading-none text-surface-100">Ep 01</span>
						</div>
					</button>

					{#each Object.entries(icon_mapping.anime_options) as item}
						{@const item_name = item[0]}
						{@const item_icon = item[1].icon}

						{@const component = item_icon.component}
						{@const component_width = item_icon.width}
						{@const component_height = item_icon.height}
						{@const component_color = item_icon.color}

						<button
						type="button"
						class="btn md:h-[8vh] md:w-[5vw] flex-col gap-1 md:rounded-lg bg-secondary-100 md:text-[1vw] md:font-semibold text-surface-500 capitalize"
						>
							<svelte:component 
								this={component}
								width={component_width}
								height={component_height}
								color={component_color}
							/>
							{item_name}
						</button>
					{/each}
				</div>

				<div class="mt-5 flex md:gap-2">
					{#each Object.entries(icon_mapping.user_options_icons) as item}
						{@const item_icon = item[1].icon}

						{@const component = item_icon.component}
						{@const component_width = item_icon.width}
						{@const component_height = item_icon.height}
						{@const component_variant = item_icon.variant}

						<button
							type="button"
							class="btn-icon md:w-[2.5vw] md:rounded-lg bg-warning-400 p-0 text-surface-500"
						>
							<svelte:component
								this = {component}
								width = {component_width}
								height = {component_height}
								variant = {component_variant}
							 />
						</button>
					{/each}
				</div>
			</div>
		</div>

		<div class="col-span-5 pr-8">
			<div class="flex items-center gap-4">
				<span class="font-semibold md:text-[1.6vw]">
					Synopsis
				</span>
				<SettingsOutline width="15" height="15" class="opacity-75" />
			</div>

			<ScrollArea
				offsetScrollbar
				parentClass="mt-5"
				class="md:max-h-36 text-justify md:text-[1vw] md:leading-tight text-surface-50"
			>
				{anime.description}
			</ScrollArea>

			<div class="md:mt-3 flex gap-2">
				{#each anime.generes as genere}
					<div class="rounded bg-surface-500 p-1 px-3 md:text-[0.8vw] text-white">
						{genere}
					</div>
				{/each}
			</div>

			<div class="md:mt-3 flex w-max items-center gap-2 rounded bg-white/20 p-1 px-3 md:text-[0.7vw]">
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

	<div class="col-span-2 md:mt-7">
		<SidebarDetails {anime} />
	</div>
</div>
