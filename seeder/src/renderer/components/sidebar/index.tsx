import { COMMANDS_MAPPING } from "@constants/shiinobi";
import { VERSION } from "@renderer/constants/version";
import { A } from "@solidjs/router";
import { Component, For } from "solid-js";

const Sidebar: Component = () => {
	return (
		<div class="flex h-full w-40 flex-col gap-1">
			<div class="flex h-full flex-col gap-1">
				<A
					href="/"
					class="btn h-max min-h-max w-full justify-start rounded border-none p-2 font-normal outline-none transition-none hover:bg-primary hover:bg-primary/10"
					activeClass="!bg-primary text-accent"
					inactiveClass="bg-transparent"
					end
				>
					{/*
					// @ts-ignore: solid-js doesn't support web-component with typescript */}
					<coreproject-shape-home class="size-3 text-warning" />
					Home
				</A>
				<For each={Object.entries(COMMANDS_MAPPING)}>
					{([command_cat, commands_obj]) => (
						<details
							class="collapse collapse-arrow rounded-none border-none !outline-none"
							open
						>
							<summary class="collapse-title min-h-max p-0 text-sm text-info after:!right-1 after:!top-1/2 after:!size-1.5">
								{command_cat}
							</summary>
							<div class="collapse-content pl-0 pr-0 pt-1">
								<For each={Object.entries(commands_obj)}>
									{([command_title, obj]) => (
										<A
											href={obj.command}
											class="btn h-max min-h-max w-full justify-start rounded border-none bg-transparent p-2 font-normal outline-none transition-none hover:bg-primary/10"
											activeClass="!bg-primary text-accent"
										>
											<span innerHTML={obj.icon} class="text-warning" />
											{command_title.replaceAll("-", " ")}
										</A>
									)}
								</For>
							</div>
						</details>
					)}
				</For>
			</div>
			<span class="text-xs">version: {VERSION}</span>
		</div>
	);
};

export default Sidebar;
