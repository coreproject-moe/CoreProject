import { Change } from "diff";
import { Component, For } from "solid-js";

type Props = {
	diff: Change[];
	options: {
		type: "add" | "remove";
	};
};

const RenderDiff: Component<Props> = (props) => {
	return (
		<span>
			<For
				each={props.diff.filter((part) =>
					props.options.type === "add" ? !part.removed : !part.added
				)}
			>
				{(part) => (
					<span
						classList={{
							"text-accent w-max leading-none p-0.5 rounded":
								part.removed || part.added,
							"bg-error/50": part.removed,
							"bg-success/50": part.added
						}}
					>
						{part.value}
					</span>
				)}
			</For>
		</span>
	);
};

export default RenderDiff;
