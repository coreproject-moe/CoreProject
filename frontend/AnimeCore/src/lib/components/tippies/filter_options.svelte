<script lang="ts">
    import ScrollArea from "$components/shared/scroll_area.svelte";
    import Tick from "$icons/tick.svelte";
    import { createEventDispatcher } from "svelte";

	export let items: Record<string, string> | undefined;
	export let selected_items: Array<[string, string]>;

	const dispatch = createEventDispatcher();

	function handle_select(item: [string, string]) {
	  	dispatch("select", item);
	}
</script>

<div class="w-[8.5rem] rounded-lg md:w-[11vw] bg-surface-900 md:rounded-[0.5vw] overflow-x-hidden">
	{#if items}
		<ScrollArea
			class="md:p-[0.5vw] flex flex-col"
			parentClass="md:max-h-[30vw] bg-surface-400/75"
		>
			{#each Object.entries(items) as item}
				{@const key = item[0]}
				{@const value = item[1]}

				{@const is_selected = selected_items.some(selected_item => selected_item[0] === key)}

				<button
					on:click={() => handle_select(item)}
					class="btn leading-none flex justify-between items-center hover:bg-surface-400 md:rounded-[0.35vw] p-3 text-sm md:px-[1vw] md:py-[0.75vw] md:text-[0.9vw] text-surface-50">
					{value}

					{#if is_selected}
						<tick class="rounded-full bg-primary-500 text-white p-1 md:p-[0.3vw]">
							<Tick class="w-2 md:w-[0.5vw]" />
						</tick>
					{/if}
				</button>
			{/each}
		</ScrollArea>
	{/if}
</div>