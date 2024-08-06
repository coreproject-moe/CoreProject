<script lang="ts">
  import type { Snippet } from 'svelte'
  import Navbar from '@components/navbar/Index.svelte'
  import { COMMANDS } from '../constants/commands'

  const {
    children
  }: {
    children: Snippet
  } = $props()
</script>

<div class="h-screen w-screen flex flex-col">
  <Navbar />
  <div class="flex-1 flex md:p-3 md:gap-3">
    <div class="md:w-60 flex flex-col md:gap-1">
      {#each Object.entries(COMMANDS) as item}
        {@const command_cat = item[0]}
        {@const commands = item[1]}

        <details class="collapse outline-none border-none rounded-none" open>
          <summary class="collapse-title min-h-max p-0 text-info">{command_cat}</summary>
          <div class="collapse-content pl-2 pt-1 pr-0">
            {#each commands as command}
              <a
                href={command}
                class="btn w-full !bg-transparent border-none md:p-2 h-max min-h-max justify-start rounded hover:!bg-primary font-normal hover:text-accent transition-none"
                ><span class="text-warning font-semibold uppercase">get</span>{command
                  .replaceAll('-', ' ')
                  .replace('get ', '')}</a
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
