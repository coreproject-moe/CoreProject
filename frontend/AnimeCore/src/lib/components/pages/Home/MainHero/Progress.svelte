<script lang="ts">
    import Timer from "easytimer.js";
    import { createEventDispatcher,onDestroy, onMount } from "svelte";

    const SWIPER_DELAY = 10;
    const dispatch = createEventDispatcher();

    let progressValue = 0;

    let timer = new Timer({
        target: {
            seconds: SWIPER_DELAY
        },
        precision: "secondTenths"
    });

    timer.on("targetAchieved", () => {
        dispatch("targetAchieved");
    });

    onMount(() => {
        timer.start({
            callback: () => {
                const time = timer.getTotalTimeValues().secondTenths;
                const value = (100 / SWIPER_DELAY) * (time / 10);
                progressValue = value;
            }
        });
    });

    onDestroy(() => {
        timer.reset();
        timer.stop();
    });

    export const pause = () => {
        timer.pause();
    };
    export const reset = () => {
        timer.reset();
    };
    export const start = () => {
        timer.start();
    };
</script>

<progress class="progress progress-secondary w-40" value={progressValue} max="100" />
