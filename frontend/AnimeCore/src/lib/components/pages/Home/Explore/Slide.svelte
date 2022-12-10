<script lang="ts">
    let selectionChoice: String = "popular";
</script>

<div class="hero min-h-[60vh] md:min-h-screen w-screen bg-center bg-no-repeat">
    <div class="flex gap-3 md:gap-32 self-start pt-16">
        {#each ["popular", "trending", "top rated", "upcoming"] as item}
            <button
                class="btn {selectionChoice.toLowerCase() === item.toLowerCase() &&
                    'btn-active'} btn-ghost text-white capitalize font-bold text-lg"
                on:click={() => {
                    selectionChoice = item.toLowerCase();
                }}
            >
                {item}
            </button>
        {/each}
    </div>
</div>
