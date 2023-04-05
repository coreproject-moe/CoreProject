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
					<button type="button" class="btn-icon bg-warning-400 rounded-md p-0">
						<Search color="black" width="18" height="18" />
					</button>
				</div>

				<div class="flex flex-col gap-9">
					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Home width="18" height="18" />
						Home
					</button>
					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Explore width="18" height="18" />
						Discover
					</button>

					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<List width="25" height="25" />
						List
					</button>

					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Schedule width="18" height="18" />
						Schedule
					</button>

					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Forum width="18" height="18" />
						Forum
					</button>
				</div>

				<div class="flex flex-col gap-9 items-center mb-9">
					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Settings width="18" height="18" />
						Settings
					</button>

					<button
						type="button"
						class="btn bg-initial rounded-lg p-0 flex-col gap-1 justify-center text-sm"
					>
						<Misc width="18" height="18" />
						Misc.
					</button>
				</div>
			</div>
		</svelte:fragment>

		<!-- Page contents go here  -->
		<slot />
	</AppShell>
</div>
