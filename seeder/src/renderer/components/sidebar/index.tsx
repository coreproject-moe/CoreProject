import { COMMANDS } from "@constants/commands";
import { A } from "@solidjs/router";
import { Component, For } from "solid-js";

const Sidebar: Component = () => {
  return (
    <div class="flex flex-col md:w-60 md:gap-1">
      <A
        href="/"
        class="btn h-max min-h-max w-full justify-start rounded border-none bg-transparent font-normal transition-none hover:bg-primary hover:bg-primary/10 md:p-2"
        activeClass="!bg-primary text-accent"
        end
      >
        <span class="text-xs font-semibold uppercase text-warning">&#47;&#47;</span>Home
      </A>
      <For each={Object.entries(COMMANDS)}>
        {([command_cat, commands]) => (
          <details class="collapse rounded-none border-none outline-none" open>
            <summary class="collapse-title min-h-max p-0 text-sm text-info">{command_cat}</summary>
            <div class="collapse-content pl-2 pr-0 pt-1">
              <For each={commands}>
                {(command) => (
                  <A
                    href={command}
                    activeClass="!bg-primary text-accent"
                    class="btn h-max min-h-max w-full justify-start rounded border-none bg-transparent font-normal transition-none hover:bg-primary/10 md:p-2"
                  >
                    <span class="text-xs font-semibold uppercase text-warning">get</span>
                    {command.replaceAll("-", " ").replace("get ", "")}
                  </A>
                )}
              </For>
            </div>
          </details>
        )}
      </For>
    </div>
  );
};

export default Sidebar;
