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
	let active_button: string = 'home';

	const icon_mapping = {
		top: [
			{
				icon: {
					component: Search,
					width: 18,
					height: 18,
					color: 'black'
				},
				name: ''
			}
		],
		middle: [
			{
				icon: {
					component: Home,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'home'
			},
			{
				icon: {
					component: Explore,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'discover'
			},
			{
				icon: {
					component: List,
					width: 25,
					height: 25,
					color: 'white'
				},
				name: 'list'
			},
			{
				icon: {
					component: Schedule,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'schedule'
			},
			{
				icon: {
					component: Forum,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'forum'
			}
		],
		bottom: [
			{
				icon: {
					component: Settings,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'settings'
			},
			{
				icon: {
					component: Misc,
					width: 18,
					height: 18,
					color: 'white'
				},
				name: 'misc.'
			}
		]
	};

	$: console.log(active_button);
</script>

<div class="h-screen overflow-hidden">
	<AppShell>
		<svelte:fragment slot="header">
			<div class="flex h-24 justify-between">
				<Logo height="48" width="33.6" class="mx-10 mt-10" />

				<AnimeCore width="168" height="33.6" class="self-center" />

				<div class="mr-16 h-16 w-16 self-center">
					<Avatar rounded="rounded-md" src="https://i.pravatar.cc/?img=48" initials="JD" />
				</div>
			</div>
		</svelte:fragment>
		<svelte:fragment slot="sidebarLeft">
			<div class="flex h-full w-28 flex-col justify-between">
				<div class="mt-3 flex flex-col items-center gap-5">
					{#each icon_mapping.top as item}
						<button type="button" class="btn-icon rounded-md bg-warning-400 p-0">
							<svelte:component
								this={item.icon.component}
								height={item.icon.height}
								width={item.icon.width}
								color={item.icon.color}
							/>
						</button>
					{/each}
				</div>

				<div class="flex flex-col items-center gap-9">
					{#each icon_mapping.middle as item}
						{@const is_active = active_button === item.name}
						<button
							type="button"
							class="{is_active
								? 'relative bg-secondary-100 before:absolute before:-left-0.5 before:z-10 before:h-4 before:w-1 before:rounded-lg before:bg-primary-500'
								: 'bg-initial'} btn-icon relative h-16 w-16 rounded-lg p-0"
							on:click={() => {
								active_button = item.name;
							}}
						>
							<div class="inline-grid">
								{#if !is_active}
									<div
										class="absolute inset-0 flex flex-col items-center justify-center gap-2"
										transition:blur|local
									>
										<svelte:component
											this={item.icon.component}
											height={item.icon.height}
											width={item.icon.width}
											color={item.icon.color}
										/>
										<p class="!m-0 text-sm capitalize">{item.name}</p>
									</div>
								{:else}
									<div
										class="absolute inset-0 flex items-center justify-center"
										transition:blur|local
									>
										<svelte:component
											this={item.icon.component}
											height={item.icon.height}
											width={item.icon.width}
											color="black"
										/>
									</div>
								{/if}
							</div>
						</button>
					{/each}
				</div>

				<div class="mb-9 flex flex-col items-center gap-9">
					{#each icon_mapping.bottom as item}
						<button
							type="button"
							class="bg-initial btn-icon h-16 w-16 flex-col justify-center gap-1 rounded-lg p-0 text-sm"
						>
							<svelte:component
								this={item.icon.component}
								height={item.icon.height}
								width={item.icon.width}
								color={item.icon.color}
							/>
							<p class="!m-0 capitalize">{item.name}</p>
						</button>
					{/each}
				</div>
			</div>
		</svelte:fragment>

		<!-- Page contents go here  -->
		<slot />
	</AppShell>
</div>
