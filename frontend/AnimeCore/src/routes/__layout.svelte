<script lang="ts">
import { onMount } from "svelte";

    import "../app.scss";

    onMount(()=>{
        document?.querySelectorAll("#loader").forEach(e=>e.remove())
        const root =  document.querySelector<HTMLElement>('.root')
        if (root){
            root.style.display = 'block'
        }
    })
</script>

<slot />
