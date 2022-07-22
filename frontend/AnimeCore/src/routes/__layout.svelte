<script lang="ts">
import { onMount } from "svelte";

    import "../app.scss";

    onMount(()=>{
        document?.querySelectorAll("#loader").forEach(e=>e.remove())
    })
</script>

<slot />
