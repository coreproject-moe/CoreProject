<script lang="ts">
	let promise = $state();

	async function get_staff_list() {
		try {
			const res = await window.api.get_staff_urls();
			return Object.entries(res);
		} catch (err) {
			console.error(err);
			throw new Error(err);
		}
	}

	function handle_click() {
		promise = get_staff_list();
	}
</script>

<div style="display: flex; flex-direction: column;">
	<button onclick={handle_click}>Get Staff List</button>

	{#if promise}
		{#await promise}
			<span>loading...</span>
		{:then data}
			{#each data as item}
				<span>{item[0]}: {item[1]}</span>
			{/each}
		{:catch err}
			<span>{err.message}</span>
		{/await}
	{/if}
</div>
