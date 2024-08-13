import { PLATFORMS } from "@renderer/constants/shiinobi";
import { Component, createSignal, For } from "solid-js";

const CommandInitializer: Component = () => {
  const [platform, setPlatform] = createSignal<typeof PLATFORMS[0]>("myanimelist")

  return (
    <div>
      <div class="flex items-center gap-2">
        <span class="text-sm">Select Platform: </span>
        <div class="dropdown">
          <div tabindex="0" role="button" class="text-warning">{platform()}</div>
          <ul tabindex="0" class="dropdown-content bg-neutral p-1 mt-1 rounded min-w-full">
            <For each={PLATFORMS.filter((pl) => pl !== platform())}>
              {(pl) => <li onClick={() => setPlatform(pl)} class="text-sm hover:bg-primary px-2 py-0.5 cursor-pointer rounded hover:text-accent">{pl}</li>}
            </For>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default CommandInitializer
