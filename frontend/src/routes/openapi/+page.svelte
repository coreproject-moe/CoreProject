<script lang="ts">
    import { onMount } from "svelte";
    import "@stoplight/elements/styles.min.css";

    onMount(async () => {
        // @ts-ignore
        await import("@stoplight/elements/web-components.min.js");
    });
</script>

<elements-api
    class="w-screen"
    apiDescriptionUrl="/openapi/schema.yaml"
    router="hash"
    layout="sidebar"
/>
