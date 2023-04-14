<script lang="ts">
	export let anime: any;

	import ScrollArea from '$components/shared/ScrollArea.svelte';
	import SidebarDetails from '$components/pages/anime_info/SidebarDetails.svelte';
	import type { SvelteComponentDev } from 'svelte/internal';
	// icons
	import PlayCircle from '$icons/PlayCircle.svelte';
	import Read from '$icons/Read.svelte';
	import Listen from '$icons/Listen.svelte';
	import Video from '$icons/Video.svelte';
	import Download from '$icons/Download.svelte';
	import Share from '$icons/Share.svelte';
	import SettingsOutline from '$icons/SettingsOutline.svelte';
	import Edit from '$icons/Edit.svelte';
	import ChevronDown from '$icons/Chevron-Down.svelte';

	const icon_mapping: {
		anime_options: {
			read: {
				icon: {
					component: typeof SvelteComponentDev;
					width: number;
					height: number;
					color?: string;
				};
			};
			listen: {
				icon: {
					component: typeof SvelteComponentDev;
					width: number;
					height: number;
					color?: string;
				};
			};
		};
		user_options_icons: {
			video: {
				icon: {
					component: typeof SvelteComponentDev;
					variant?: string | boolean;
					width: number;
					height: number;
				};
			};
			edit: {
				icon: {
					component: typeof SvelteComponentDev;
					variant?: string | boolean;
					width: number;
					height: number;
				};
			};
			download: {
				icon: {
					component: typeof SvelteComponentDev;
					variant?: 'with_underline_around_pencil' | 'without_underline_around_pencil';
					width: number;
					height: number;
				};
			};
			share: {
				icon: {
					component: typeof SvelteComponentDev;
					variant?: string | boolean;
					width: number;
					height: number;
				};
			};
		};
	} = {
		anime_options: {
			read: {
				icon: {
					component: Read,
					width: 18,
					height: 18,
					color: 'bg-surface-500'
				}
			},
			listen: {
				icon: {
					component: Listen,
					width: 18,
					height: 18,
					color: 'bg-surface-500'
				}
			}
		},
		user_options_icons: {
			video: {
				icon: {
					component: Video,
					variant: false,
					width: 15,
					height: 15
				}
			},
			edit: {
				icon: {
					component: Edit,
					variant: 'with_underline_around_pencil',
					width: 15,
					height: 15
				}
			},
			download: {
				icon: {
					component: Download,
					width: 15,
					height: 15
				}
			},
			share: {
				icon: {
					component: Share,
					width: 15,
					height: 15
				}
			}
		}
	};


	// scroll top
	let scroll_top = 0;
	let scrollbar_type: string = '';

	$: {
		if (scroll_top > 90 && scroll_top <= 100) {
			scrollbar_type = 'scroll-top';
		} else if (scroll_top >= 10 && scroll_top <= 90) {
			scrollbar_type = 'scroll-middle';
		} else {
			scrollbar_type = 'scroll-bottom';
		}
	}

</script>

<div class="grid grid-cols-12 items-start">
	<div class="col-span-10 grid grid-cols-12 items-end justify-between">
		<div class="col-span-7 flex items-end md:gap-[3.125vw]">
			<img
				class="md:w-[12.5vw] md:rounded-[1vw]"
				src={anime.cardBackgroundImage}
				alt={anime.titles.eng}
			/>
			<div>
				<span class="font-bold md:text-[2.5vw] md:leading-[3vw]">{anime.titles.eng}</span>

				<p class="flex items-center gap-2 text-surface-100 md:pt-[0.625vw]">
					{#each Object.entries(anime.titles) as anime_title}
						{#if anime_title[0] !== 'eng'}
							<span
								class="font-medium md:text-[0.75vw] md:leading-[0.9vw] [&:not(:last-child)]:after:ml-2 [&:not(:last-child)]:after:content-['▪']"
								>{anime_title[1]}</span
							>
						{/if}
					{/each}
				</p>

				<p class="flex flex-wrap items-center gap-2 md:pt-[1vw]">
					{#each Object.entries(anime.basic_details) as anime_detail}
						<span
							class="font-semibold md:text-[0.625vw] md:leading-[0.75vw] [&:not(:last-child)]:after:ml-1 [&:not(:last-child)]:after:content-['▪']"
						>
							{anime_detail[1]}
							{anime_detail[0] === 'episodes' ? 'eps' : ''}
						</span>
					{/each}
				</p>

				<div class="flex items-center md:mt-[2.25vw] md:gap-[1.15vw]">
					<button
						type="button"
						class="btn bg-primary-500 font-bold text-white md:h-[4.3vw] md:w-[6.75vw] md:rounded-[0.625vw] md:text-[0.87vw]"
					>
						<div class="flex items-center justify-center md:gap-[0.7vw]">
							<PlayCircle width="25" height="25" color="white" />
							<div class="flex flex-col items-start">
								<span class="md:leading-5">Watch</span>
								<span class="font-normal leading-none text-surface-100 md:text-[0.625vw]"
									>Ep 01</span
								>
							</div>
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
							class="btn bg-secondary-100 capitalize text-surface-500 md:h-[4.3vw] md:w-[4.3vw] md:rounded-[0.625vw]
					       md:text-[0.87vw] md:font-semibold"
						>
							<div class="flex flex-col items-center justify-center md:gap-[0.68vw]">
								<svelte:component
									this={component}
									width={component_width}
									height={component_height}
									color={component_color}
								/>
								<span class="md:leading-[1vw]">{item_name}</span>
							</div>
						</button>
					{/each}
				</div>

				<div class="flex md:mt-[1.25vw] md:gap-[0.625vw]">
					{#each Object.entries(icon_mapping.user_options_icons) as item}
						{@const item_icon = item[1].icon}

						{@const component = item_icon.component}
						{@const component_width = item_icon.width}
						{@const component_height = item_icon.height}
						{@const component_variant = item_icon.variant}

						<button
							type="button"
							class="btn-icon bg-warning-400 p-0 text-surface-500 md:w-[1.875vw] md:rounded-[0.25vw]"
						>
							<svelte:component
								this={component}
								width={component_width}
								height={component_height}
								variant={component_variant}
							/>
						</button>
					{/each}
				</div>
			</div>
		</div>

		<div class="col-span-5 pr-8 md:w-[26.625vw]">
			<div class="flex items-center gap-4">
				<span class="font-semibold md:text-[1.25vw] md:leading-[1.5vw]"> Synopsis </span>
				<SettingsOutline width="11" height="11" class="opacity-75" />
			</div>

			<ScrollArea
				bind:scroll_top
				offsetScrollbar
				parentClass="mt-5 {scrollbar_type} transition duration-500"
				class=" text-justify md:max-h-[9.5vw] md:text-[0.75vw] md:leading-[1vw]"
			>
				{anime.description}
			</ScrollArea>

			<div class="flex gap-2 md:mt-3">
				{#each anime.generes as genere}
					<div
						class="rounded bg-surface-500 px-[0.95vw] text-white md:py-[0.375vw] md:text-[0.75vw] md:leading-[0.9vw]"
					>
						{genere}
					</div>
				{/each}
			</div>

			<div
				class="flex w-max items-center gap-2 rounded bg-white/20 md:mt-3 md:px-[0.75vw] md:py-[0.375vw] md:text-[0.625vw] md:leading-[0.75vw]"
			>
				<div class="flex items-center gap-1">
					Score:
					<span class="text-warning-400">{anime.score}</span>
				</div>
				<div class="flex items-center gap-1">
					Status:
					<span class="text-warning-400">Watching</span>
					<ChevronDown width="9" color="warning-400" />
				</div>
				<div class="flex items-center gap-1">
					Episode:
					<span class="text-warning-400">0/{anime.basic_details.episodes}</span>
				</div>
				<div class="flex items-center gap-1">
					Your Score:
					<span class="text-warning-400">Not Rated</span>
					<ChevronDown width="9" color="warning-400" />
				</div>
			</div>
		</div>
	</div>

	<div class="col-span-2">
		<SidebarDetails {anime} />
	</div>
</div>
