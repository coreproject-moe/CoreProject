import { Change } from "diff";
import { Component, For } from "solid-js";

type Props = {
  diff: {
    [key: string]: Change[];
  };
  field: string;
  type: "old" | "new";
}

const RenderDiffField: Component<Props> = (props) => {
  return (
    <div class="flex flex-col gap-1">
      <For each={props.diff[props.field].filter((part) => props.type === "old" ? !part.added : !part.removed)}>
        {(part) => (
          <span classList={{
            "text-accent w-max leading-none p-1 rounded whitespace-pre-line break-words": part.removed || part.added,
            "bg-error/35": part.removed,
            "bg-success/25": part.added,
          }}>
            {part.removed ? "-" : part.added ? "+" : ""} {part.value}
          </span>
        )}
      </For>
    </div>
  )
};

export default RenderDiffField;
