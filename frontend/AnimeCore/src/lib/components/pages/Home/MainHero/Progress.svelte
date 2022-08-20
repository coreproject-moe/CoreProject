<script lang="ts">
    let klass = "";
    export { klass as class };

    // This is the first time i had to rename imports
    import { Timer as EasyTimer } from "easytimer.js";
    import { createEventDispatcher, onDestroy } from "svelte";

    import { timer as timerStore } from "$store/Timer";

    const SWIPER_DELAY = 10;
    const dispatch = createEventDispatcher();

    let progressValue = 0;

    let timer = new EasyTimer({
        target: {
            seconds: SWIPER_DELAY
        },
        precision: "secondTenths"
    });

    timer.on("targetAchieved", () => {
        dispatch("targetAchieved");
    });

    timer.on("secondTenthsUpdated", () => {
        const time = timer.getTotalTimeValues().secondTenths;
        const value = (100 / SWIPER_DELAY) * (time / 10);
        progressValue = value;
    });

    $: {
        switch ($timerStore) {
            case "start":
                timer?.start();
                break;
            case "pause":
                timer?.pause();
                break;
            case "reset":
                timer?.reset();
                break;
        }
    }
    onDestroy(() => {
        timer.reset();
        timer.stop();
    });
</script>

<progress class="progress progress-secondary {klass}" value={progressValue} max="100" />
