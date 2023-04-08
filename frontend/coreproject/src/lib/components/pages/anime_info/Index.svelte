<script lang="ts">
  import { page } from '$app/stores';

	import { anime_list } from '$data/mock/anime_list.ts';
	import AnimeMainDetails from './AnimeMainDetails.svelte';

  let anime_id = Number($page.params.id);

	let anime = anime_list?.find((anime: any) => anime.id === anime_id);
</script>

<div class="anime_info">
	<div
		class="relative h-screen bg-cover rounded-tl-3xl"
		style="background-image: url({anime?.bannerBackgroundImage ?? ''});"
	>
		<div
			class="gradient absolute h-full w-full bg-gradient-to-t from-surface-500 to-surface-500/50"
		/>
		<div class="absolute h-full w-full xl:p-16 2xl:p-18 3xl:p-28">
			<AnimeMainDetails {anime} />
		</div>
	</div>
</div>
