<script lang="ts">
	export let rating: number;
	export let gap: number;
	export let size: number;
	export let color: string;

	// icons
	import Star from '$icons/Star.svelte';
</script>

<div class="flex gap-{gap ?? 1}">
	{#each Array(Math.floor(rating)) as _}
		<Star variation="solid" size={size ?? 18} class="{color ?? 'text-white'}" />
	{/each}
	{#each Array(5 - Math.floor(rating)) as _}
		<Star variation="outline" size={size ?? 18} class="{color ?? 'text-white'}" />
	{/each}
</div>