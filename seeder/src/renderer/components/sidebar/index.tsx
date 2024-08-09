import { COMMANDS_MAPPING } from "@constants/shiinobi";
import { VERSION } from "@renderer/constants/version";
import { A } from "@solidjs/router";
import { Component, For } from "solid-js";

const Sidebar: Component = () => {
	return (
		<div class="flex flex-col md:w-44 md:gap-1">
			<div class="flex h-full flex-col md:gap-1">
				<A
					href="/"
					class="btn h-max min-h-max w-full justify-start rounded border-none font-normal outline-none transition-none hover:bg-primary hover:bg-primary/10 md:gap-1 md:p-2"
					activeClass="!bg-primary text-accent"
					inactiveClass="bg-transparent"
					end
				>
					<span class="text-xs font-bold text-warning">&sol;</span>
					Home
				</A>
				<For each={Object.entries(COMMANDS_MAPPING)}>
					{([command_cat, commands_obj]) => (
						<details class="collapse collapse-arrow rounded-none border-none !outline-none" open>
							<summary class="collapse-title min-h-max p-0 text-sm text-info after:!right-1 after:!top-1/2 after:!size-1.5">
								{command_cat}
							</summary>
							<div class="collapse-content pl-0 pr-0 pt-1">
								<For each={Object.entries(commands_obj)}>
									{([command_title, command]) => (
										<A
											href={command}
											class="btn h-max min-h-max w-full justify-start rounded border-none bg-transparent font-normal outline-none transition-none hover:bg-primary/10 md:gap-1 md:p-2"
											activeClass="!bg-primary text-accent"
										>
											<span class="text-xs font-bold text-warning">&sol;</span>
											{command_title.replaceAll("-", " ")}
										</A>
									)}
								</For>
							</div>
						</details>
					)}
				</For>
			</div>
			<span class="md:text-xs">version: {VERSION}</span>
		</div>
	);
};

export default Sidebar;
