<script lang="ts">
    import "../app.scss";

import { onMount } from "svelte";

    onMount(()=>{
        document?.querySelectorAll("#loader").forEach(e=>e.remove())
        const root =  document.querySelector<HTMLElement>('.root')
        if (root){
            root.style.display = 'block'
        }
    })
</script>

<slot />
