import { PLATFORMS } from "@renderer/constants/shiinobi";
import { Component, createSignal, For } from "solid-js";
import { createEventDispatcher } from "@solid-primitives/event-dispatcher";

type Props = {
	title: string;
	onFetchClick: (e: CustomEvent<string>) => void;
};

const CommandInitializer: Component<Props> = (props) => {
	const [platform, setPlatform] = createSignal<(typeof PLATFORMS)[0]>("myanimelist");

	const dispatch = createEventDispatcher(props);

	const handleFetchClick = () => {
		dispatch("fetchClick", platform());
	};

	return (
		<div class="flex items-center gap-2">
			<h2 class="text-lg font-bold">{props.title}</h2>
			<div class="ml-auto flex items-center gap-2">
				<span class="text-sm">Select Platform: </span>
				<div class="dropdown dropdown-end">
					<div tabindex="0" role="button" class="flex items-center gap-1 text-warning">
						{platform()}
						{/*
					// @ts-ignore: solid-js doesn't support web-component with typescript */}
						<coreproject-shape-chevron class="size-3"></coreproject-shape-chevron>
					</div>
					<ul tabindex="0" class="dropdown-content mt-1 min-w-full rounded bg-neutral p-1">
						<For each={PLATFORMS.filter((pl) => pl !== platform())}>
							{(pl) => (
								<li
									onClick={() => setPlatform(pl)}
									class="cursor-pointer rounded px-2 py-0.5 text-sm hover:bg-primary hover:text-accent"
								>
									{pl}
								</li>
							)}
						</For>
					</ul>
				</div>
			</div>
			<button
				onClick={handleFetchClick}
				class="btn btn-primary h-max min-h-full rounded px-4 py-2 text-accent outline-none"
			>
				Fetch
				{/*
					// @ts-ignore: solid-js doesn't support web-component with typescript */}
				<coreproject-shape-upload class="size-3"></coreproject-shape-upload>
			</button>
		</div>
	);
};

export default CommandInitializer;
