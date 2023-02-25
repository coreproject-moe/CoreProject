<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";
    type $$Props = SVGAttributes<SVGElement>;
</script>

<svg
    viewBox="0 0 24 25"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...$$props}
>
    <g filter="url(#filter0_d_1917_2487)">
        <path
            d="M12 1.5L14.3175 6.195L19.5 6.9525L15.75 10.605L16.635 15.765L12 13.3275L7.365 15.765L8.25 10.605L4.5 6.9525L9.6825 6.195L12 1.5Z"
            fill="#DCD9F7"
            stroke="#DCD9F7"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
    </g>
    <defs>
        <filter
            id="filter0_d_1917_2487"
            x="-1"
            y="0"
            width="26"
            height="26"
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
                result="effect1_dropShadow_1917_2487"
            />
            <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect1_dropShadow_1917_2487"
                result="shape"
            />
        </filter>
    </defs>
</svg>
