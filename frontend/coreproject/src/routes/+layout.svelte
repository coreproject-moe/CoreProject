<script lang="ts">
	// Your custom Skeleton theme:
	import '../theme.scss';

	// This contains the bulk of Skeletons required styles:
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.scss';
	import { AppShell, Avatar } from '@skeletonlabs/skeleton';
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
	let active_button: string;

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
			<div class="h-24 flex justify-between">
				<Logo height="48" width="33.6" class="mt-10 mx-10" />

				<AnimeCore width="168" height="33.6" class="self-center" />

				<div class="h-16 w-16 mr-16 self-center">
					<Avatar rounded="rounded-md" src="https://i.pravatar.cc/?img=48" initials="JD" />
				</div>
			</div>
		</svelte:fragment>
		<svelte:fragment slot="sidebarLeft">
			<div class="w-28 h-full flex flex-col justify-between">
				<div class="flex mt-3 flex-col gap-5 items-center">
					{#each icon_mapping.top as item}
						<button type="button" class="btn-icon bg-warning-400 rounded-md p-0">
							<svelte:component
								this={item.icon.component}
								height={item.icon.height}
								width={item.icon.width}
								color={item.icon.color}
							/>
						</button>
					{/each}
				</div>

				<div class="flex flex-col gap-9 items-center">
					{#each icon_mapping.middle as item}
						<button
							type="button"
							class="btn-icon w-16 h-16 bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
							on:click={() => {
								active_button = item.name;
							}}
						>
							<svelte:component
								this={item.icon.component}
								height={item.icon.height}
								width={item.icon.width}
								color={item.icon.color}
							/>
							<p class="capitalize !m-0">{item.name}</p>
						</button>
					{/each}
				</div>

				<div class="flex flex-col gap-9 items-center mb-9">
					{#each icon_mapping.bottom as item}
						<button
							type="button"
							class="btn-icon w-16 h-16 bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
						>
							<svelte:component
								this={item.icon.component}
								height={item.icon.height}
								width={item.icon.width}
								color={item.icon.color}
							/>
							<p class="capitalize !m-0">{item.name}</p>
						</button>
					{/each}
				</div>
			</div>
		</svelte:fragment>

		<!-- Page contents go here  -->
		<slot />
	</AppShell>
</div>
