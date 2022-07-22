<script lang="ts">
    import "../app.scss";

import { onMount } from "svelte";

    onMount(()=>{
        document?.querySelectorAll("#loader").forEach(e=>e.remove())
    })
</script>

<slot />
