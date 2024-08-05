<script lang="ts">
  import type { Snippet } from 'svelte'
  import Navbar from '@components/navbar/Index.svelte'

  const {
    children
  }: {
    children: Snippet
  } = $props()
</script>

<div class="h-screen w-screen flex flex-col">
  <Navbar />
  <div class="flex-1 flex">
    <div class="md:w-1/4"></div>
    <div class="w-full overflow-y-scroll">
      {@render children()}
    </div>
  </div>
</div>
