<script lang="ts">
	import AnimeInfoPage from '$components/pages/anime_info/Index.svelte';
  export let data: { id: number};
</script>

<AnimeInfoPage anime_id={data.id} />
