<script lang="ts">
	export let anime_id: number;

	import { anime_list } from '$data/mock/anime_list';
	import AnimeMainDetails from './AnimeMainDetails.svelte';

	let anime = anime_list?.find((anime) => anime.id == anime_id);
</script>

<div class="anime_info rounded-tl-3xl overflow-hidden">
	<div class="anime_basic_details h-screen relative bg-[url({anime?.bannerBackgroundImage})] bg-cover">
		<div class="gradient absolute w-full h-full bg-gradient-to-t from-surface-500 to-surface-500/50" />
		<div class="absolute w-full h-full p-16">
      
      <AnimeMainDetails {anime} />
    </div>
	</div>
</div>
