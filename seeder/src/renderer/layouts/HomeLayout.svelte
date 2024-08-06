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
    <div class="md:w-80 flex flex-col md:gap-1">
      {#each COMMANDS.common as command}
        <a
          href={command}
          class="btn !bg-transparent border-none md:p-2 h-max min-h-max justify-start rounded hover:!bg-primary font-normal hover:text-accent transition-none"
          ><span class="text-warning font-semibold uppercase">get</span>{command
            .replaceAll('-', ' ')
            .replace('get ', '')}</a
        >
      {/each}
    </div>
    <div class="w-full overflow-y-scroll">
      {@render children()}
    </div>
  </div>
</div>
