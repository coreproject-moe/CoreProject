<script lang="ts">
	import { page } from '$app/stores';

	import { anime_list } from '$data/mock/anime_list';
	import AnimeMainDetails from './AnimeMainDetails.svelte';

	let anime_id = Number($page.params.id);

	let anime = anime_list?.find((anime: any) => anime.id === anime_id);
</script>

<div class="anime_info">
	<div
		class="relative h-screen rounded-tl-3xl bg-cover"
		style="background-image: url({anime?.bannerBackgroundImage ?? ''});"
	>
		<div
			class="gradient absolute h-full w-full bg-gradient-to-t from-surface-900 to-surface-900/50"
		/>
		<div class="absolute h-full w-full md:p-[5vw]">
			<AnimeMainDetails {anime} />
		</div>
	</div>
</div>
