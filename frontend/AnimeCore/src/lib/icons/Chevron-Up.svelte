<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";
    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    xmlns="http://www.w3.org/2000/svg"
    {...$$props}
    fill="none"
    viewBox="0 0 24 25"
>
    <g filter="url(#filter0_d_664_61)">
        <path
            stroke="#fff"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="3.5"
            d="M18 15L12 9L6 15"
        />
    </g>
    <defs>
        <filter
            id="filter0_d_664_61"
            width="32"
            height="32"
            x="-4"
            y="0"
            color-interpolation-filters="sRGB"
            filterUnits="userSpaceOnUse"
        >
            <feFlood
                flood-opacity="0"
                result="BackgroundImageFix"
            />
            <feColorMatrix
                in="SourceAlpha"
                result="hardAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
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
                in2="BackgroundImageFix"
                mode="normal"
                result="effect1_dropShadow_664_61"
            />
            <feBlend
                in="SourceGraphic"
                in2="effect1_dropShadow_664_61"
                mode="normal"
                result="shape"
            />
        </filter>
    </defs>
</svg>
