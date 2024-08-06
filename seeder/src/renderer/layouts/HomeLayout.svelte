<script lang="ts">
	import type { Snippet } from "svelte";
	import Navbar from "@components/navbar/Index.svelte";
	import { COMMANDS } from "@constants/commands";
	import { Link } from "svelte-routing";
	import { cn } from "@utils/cn";

	const {
		children
	}: {
		children: Snippet;
	} = $props();

	console.log(window.location.pathname);
</script>

<div class="flex h-screen w-screen flex-col">
	<Navbar />
	<div class="flex flex-1 md:gap-3 md:p-3">
		<div class="flex flex-col md:w-60 md:gap-1">
			<Link to="/" let:active
				><button
					class={cn(
						active && "!bg-primary text-accent",
						"btn h-max min-h-max w-full justify-start rounded border-none bg-transparent font-normal transition-none hover:bg-primary hover:bg-primary/10 md:p-2"
					)}><span class="text-xs font-semibold uppercase text-warning">//</span>Home</button
				></Link
			>
			{#each Object.entries(COMMANDS) as item}
				{@const command_cat = item[0]}
				{@const commands = item[1]}

				<details class="collapse rounded-none border-none outline-none" open>
					<summary class="collapse-title min-h-max p-0 text-sm text-info">{command_cat}</summary>
					<div class="collapse-content pl-2 pr-0 pt-1">
						{#each commands as command}
							<Link to={command} let:active
								><button
									class={cn(
										active && "!bg-primary text-accent",
										"btn h-max min-h-max w-full justify-start rounded border-none bg-transparent font-normal transition-none hover:bg-primary/10 md:p-2"
									)}
									><span class="text-xs font-semibold uppercase text-warning">get</span>{command
										.replaceAll("-", " ")
										.replace("get ", "")}</button
								></Link
							>
						{/each}
					</div>
				</details>
			{/each}
		</div>
		<div class="w-full overflow-y-scroll">
			{@render children()}
		</div>
	</div>
</div>
