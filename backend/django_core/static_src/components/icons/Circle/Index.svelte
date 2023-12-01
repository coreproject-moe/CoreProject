<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";

    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    {...$$props}
    class="opacity-50 md:w-[0.25vw]"
    viewBox="0 0 10 10"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <circle
        cx="5"
        cy="5"
        r="5"
        fill="currentColor"
    ></circle>
</svg>
