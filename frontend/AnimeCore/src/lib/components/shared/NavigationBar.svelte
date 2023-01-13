<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import { cubicOut } from "svelte/easing";
    import { tweened } from "svelte/motion";

    import navigationState from "$store/Navigation_State";

    const progress = tweened(0, {
        duration: 3500,
        easing: cubicOut
    });

    const unsubscribe = navigationState.subscribe((state) => {
        if (state === "loaded") {
            progress.set(1, { duration: 1000 });
        }
    });
    onMount(() => {
        progress.set(0.7);
    });
    onDestroy(() => {
        unsubscribe();
    });
</script>

<progress-div>
    <progress-actual style={`--width: ${$progress * 100}%`} />
</progress-div>

<style lang="scss">
    progress-div {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 0.5rem;

        progress-actual {
            width: var(--width);
            background-color: #f8485e;
            height: 100%;
        }
    }
</style>
