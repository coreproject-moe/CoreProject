<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";

    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    {...$$props}
    viewBox="0 0 28 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <g filter="url(#filter0_d_1329_1599)">
        <rect
            x="4"
            width="8"
            height="8"
            rx="2"
            fill="currentColor"
        />
        <rect
            x="16"
            width="8"
            height="8"
            rx="2"
            fill="currentColor"
        />
        <rect
            x="16"
            y="12"
            width="8"
            height="8"
            rx="2"
            fill="currentColor"
        />
        <rect
            x="4"
            y="12"
            width="8"
            height="8"
            rx="2"
            fill="currentColor"
        />
    </g>
    <defs>
        <filter
            id="filter0_d_1329_1599"
            x="0"
            y="0"
            width="28"
            height="28"
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
                result="effect1_dropShadow_1329_1599"
            />
            <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect1_dropShadow_1329_1599"
                result="shape"
            />
        </filter>
    </defs>
</svg>
