<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";
    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    xmlns="http://www.w3.org/2000/svg"
    {...$$props}
    fill="none"
    viewBox="0 0 24 24"
>
    <path
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="4"
        d="M15 18L9 12L15 6"
    />
</svg>
