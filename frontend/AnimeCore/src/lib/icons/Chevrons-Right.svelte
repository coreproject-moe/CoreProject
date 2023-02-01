<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";
    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    {...$$props}
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
>
    <path
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="3"
        d="M13 17L18 12L13 7"
    />
    <path
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="3"
        d="M6 17L11 12L6 7"
    />
</svg>
