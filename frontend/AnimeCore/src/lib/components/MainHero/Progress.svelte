<script lang="ts">
    import { onMount,onDestroy } from "svelte";
    import { createEventDispatcher } from 'svelte';
    import Timer from "easytimer.js";
 
	const dispatch = createEventDispatcher();

    let progressValue = 0

    let timer = new Timer({
        target:{
            seconds: 10
        },
        precision:'secondTenths',
    });
    
    timer.on('targetAchieved',()=>{
        dispatch('targetAchieved')
    })

    onMount(()=>{
        timer.start({
            callback:()=>{
                progressValue = progressValue += 1
            }
        })
    })

    onDestroy(()=>{
        timer.stop()
    })
</script>

<progress class="progress progress-secondary w-50 transition-[width] delay-1000" value={progressValue} max="100"/>