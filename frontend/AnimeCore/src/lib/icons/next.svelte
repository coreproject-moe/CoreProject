<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";

    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    {...$$props}
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
>
    <g
        fill="none"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
    >
        <path d="M0 0h24v24H0z" />
        <path
            fill="currentColor"
            d="M2 5v14c0 .86 1.012 1.318 1.659.753l8-7a1 1 0 0 0 0-1.506l-8-7C3.012 3.682 2 4.141 2 5zm11 0v14c0 .86 1.012 1.318 1.659.753l8-7a1 1 0 0 0 0-1.506l-8-7C14.012 3.682 13 4.141 13 5z"
        />
    </g>
</svg>
