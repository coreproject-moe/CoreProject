<script lang="ts">
	// Your custom Skeleton theme:
	import '../theme.scss';

	// This contains the bulk of Skeletons required styles:
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.scss';
	import { AppShell, Avatar } from '@skeletonlabs/skeleton';

	import { blur } from 'svelte/transition';

	// import icons
	import AnimeCore from '$icons/AnimeCore.svelte';
	import Logo from '$icons/Logo.svelte';
	import Search from '$icons/Search.svelte';
	import Home from '$icons/Home.svelte';
	import Explore from '$icons/Explore.svelte';
	import List from '$icons/List.svelte';
	import Schedule from '$icons/Schedule.svelte';
	import Forum from '$icons/Forum.svelte';
	import Settings from '$icons/Settings.svelte';
	import Misc from '$icons/Misc.svelte';

	// Local
	let active_button:
		| keyof typeof icon_mapping.top
		| keyof typeof icon_mapping.middle
		| keyof typeof icon_mapping.bottom = 'home';


	const icon_mapping = {
		top: {
			search: {
				icon: {
					component: Search,
					width: 18,
					height: 18,
					color: 'black'
				}
			}
		},
		middle: {
			home: {
				icon: {
					component: Home,
					width: 18,
					height: 18,
					color: 'white'
				}
			},

			discover: {
				icon: {
					component: Explore,
					width: 18,
					height: 18,
					color: 'white'
				}
			},
			list: {
				icon: {
					component: List,
					width: 25,
					height: 25,
					color: 'white'
				}
			},
			schedule: {
				icon: {
					component: Schedule,
					width: 18,
					height: 18,
					color: 'white'
				}
			},
			forum: {
				icon: {
					component: Forum,
					width: 18,
					height: 18,
					color: 'white'
				}
			}
		},
		bottom: {
			settings: {
				icon: {
					component: Settings,
					width: 18,
					height: 18,
					color: 'white'
				}
			},
			'misc.': {
				icon: {
					component: Misc,
					width: 18,
					height: 18,
					color: 'white'
				}
			}
		}
	};

	async function middle_section_click(item: string) {
		active_button = item as typeof active_button;
	}
</script>

<div class="h-screen">
	<AppShell>
		<svelte:fragment slot="header">
			<div class="md:h-18 flex justify-between items-center md:mx-6 md:my-3 2xl:my-0 2xl:mx-10 2xl:h-24">
				<Logo width="33.6" height="48" />

				<AnimeCore width="168" height="33.6" />

				<div class="md:h-10 md:w-10 2xl:h-16 2xl:w-16">
					<Avatar
						rounded="rounded-md"
						width="w-full"
						cursor="cursor-pointer"
						src="https://i.pravatar.cc/?img=48"
						initials="JD"
					/>
				</div>
			</div>
		</svelte:fragment>
		<svelte:fragment slot="sidebarLeft">
			<div class="flex flex-col md:w-[6.25vw]">
				<div class="mt-3 flex flex-col items-center gap-5">
					{#each Object.entries(icon_mapping.top) as item}
						{@const item_icon = item[1].icon}
						<button type="button" class="btn-icon md:rounded-[0.375vw] bg-warning-400 p-0 md:w-[2.5vw]">
							<svelte:component
								this={item_icon.component}
								height={item_icon.height}
								width={item_icon.width}
								color={item_icon.color}
							/>
						</button>
					{/each}
				</div>

				<div class="md:mt-10 flex flex-col items-center md:gap-5 2xl:gap-9">
					{#each Object.entries(icon_mapping.middle) as item}
						{@const item_name = item[0]}
						{@const item_icon = item[1].icon}

						{@const component = item_icon.component}
						{@const component_width = item_icon.width}
						{@const component_height = item_icon.height}

						{@const is_active = active_button === item_name}

						<button
							type="button"
							class="{is_active
								? 'relative bg-secondary-100 before:absolute before:-left-0.5 before:z-10 before:h-[0.875vw] before:w-[0.25vw] before:rounded-lg before:bg-primary-500'
								: 'bg-initial'} btn-icon relative rounded-lg p-0 md:w-[3.375vw]"
							on:click={() => middle_section_click(item_name)}
						>
							<div class="inline-grid">
								{#if !is_active}
									<div
										class="absolute inset-0 flex flex-col items-center justify-center md:gap-[0.75vw]"
										transition:blur|local
									>
										<svelte:component
											this={component}
											height={component_height}
											width={component_width}
											color={item_icon.color}
										/>
										<span class="capitalize md:text-[0.875vw] md:leading-[1.05vw]">{item_name}</span>
									</div>
								{:else}
									<div
										class="absolute inset-0 flex items-center justify-center"
										transition:blur|local
									>
										<svelte:component
											this={component}
											height={component_height}
											width={component_width}
											color="black"
										/>
									</div>
								{/if}
							</div>
						</button>
					{/each}
				</div>

				<div class="md:mt-10 2xl:mt-20 flex flex-col-reverse items-center md:gap-5 2xl:gap-9">
					{#each Object.entries(icon_mapping.bottom) as item}
						{@const item_name = item[0]}
						{@const item_icon = item[1].icon}
						<button
							type="button"
							class="bg-initial btn-icon flex-col justify-center p-0 text-sm md:w-[3.375vw] md:gap-[0.75vw]"
						>
							<svelte:component
								this={item_icon.component}
								height={item_icon.height}
								width={item_icon.width}
								color={item_icon.color}
							/>
							<span class="!m-0 capitalize md:text-[0.875vw] md:leading-[1.05vw]">{item_name}</span>
  						</button>
					{/each}
				</div>
			</div>
		</svelte:fragment>

		<!-- Page contents go here  -->
		<slot />
	</AppShell>
</div>
