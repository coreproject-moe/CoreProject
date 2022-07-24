<script lang="ts">
    import "../app.scss";

    import { afterUpdate } from "svelte";

    afterUpdate(() => {
        setTimeout(() => {
            document?.querySelectorAll("#loader").forEach((e) => e.remove());
            const root = document.querySelector<HTMLElement>(".root");
            if (root) {
                root.style.display = "block";
            }
        }, 1000);
    });
</script>

<slot />
