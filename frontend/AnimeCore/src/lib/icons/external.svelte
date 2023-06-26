<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";

    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    {...$$props}
    viewBox="0 0 18 19"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <g filter="url(#filter0_d_1917_2504)">
        <path
            d="M12 6.5V9.5C12 9.76522 11.8946 10.0196 11.7071 10.2071C11.5196 10.3946 11.2652 10.5 11 10.5H5.5C5.23478 10.5 4.98043 10.3946 4.79289 10.2071C4.60536 10.0196 4.5 9.76522 4.5 9.5V4C4.5 3.73478 4.60536 3.48043 4.79289 3.29289C4.98043 3.10536 5.23478 3 5.5 3H8.5"
            stroke="white"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
        <path
            d="M10.5 1.5H13.5V4.5"
            stroke="white"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
        <path
            d="M8 7L13.5 1.5"
            stroke="white"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
    </g>
    <defs>
        <filter
            id="filter0_d_1917_2504"
            x="-1"
            y="0"
            width="20"
            height="20"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
        >
            <feFlood
                flood-opacity="0"
                result="BackgroundImageFix"
            />
            <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
            />
            <feOffset dy="4" />
            <feGaussianBlur stdDeviation="2" />
            <feComposite
                in2="hardAlpha"
                operator="out"
            />
            <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"
            />
            <feBlend
                mode="normal"
                in2="BackgroundImageFix"
                result="effect1_dropShadow_1917_2504"
            />
            <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect1_dropShadow_1917_2504"
                result="shape"
            />
        </filter>
    </defs>
</svg>
