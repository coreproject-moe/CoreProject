<script lang="ts">
    import { beforeUpdate } from "svelte";

    beforeUpdate(async () => {
        // @ts-ignore
        await import("@stoplight/elements/web-components.min.js");
        await import("@stoplight/elements/styles.min.css");
    });
</script>

<elements-api
    data-theme="dark"
    class="w-screen"
    apiDescriptionUrl="/openapi/schema.yaml"
    router="hash"
    layout="sidebar"
/>
