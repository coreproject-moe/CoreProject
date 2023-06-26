<script lang="ts">
    import type { SVGAttributes } from "svelte/elements";

    interface $$Props extends SVGAttributes<SVGElement> {
        variant: "with_underline_around_pencil" | "without_underline_around_pencil";
    }
    const { variant, ...props } = $$props as $$Props;
</script>

{#if variant === "with_underline_around_pencil"}
    <svg
        viewBox="0 0 18 18"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        {...props}
    >
        <path
            d="M9 15H15.75"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
        <path
            d="M12.375 2.62517C12.6734 2.3268 13.078 2.15918 13.5 2.15918C13.7089 2.15918 13.9158 2.20033 14.1088 2.28029C14.3019 2.36024 14.4773 2.47743 14.625 2.62517C14.7727 2.77291 14.8899 2.9483 14.9699 3.14132C15.0498 3.33435 15.091 3.54124 15.091 3.75017C15.091 3.9591 15.0498 4.16599 14.9699 4.35902C14.8899 4.55204 14.7727 4.72743 14.625 4.87517L5.25 14.2502L2.25 15.0002L3 12.0002L12.375 2.62517Z"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
    </svg>
{:else if variant === "without_underline_around_pencil"}
    <svg
        {...props}
        viewBox="0 0 12 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
    >
        <g clip-path="url(#clip0_1917_2501)">
            <path
                d="M8.5 1.50015C8.63132 1.36883 8.78722 1.26466 8.9588 1.19359C9.13038 1.12252 9.31428 1.08594 9.5 1.08594C9.68572 1.08594 9.86962 1.12252 10.0412 1.19359C10.2128 1.26466 10.3687 1.36883 10.5 1.50015C10.6313 1.63147 10.7355 1.78737 10.8066 1.95895C10.8776 2.13054 10.9142 2.31443 10.9142 2.50015C10.9142 2.68587 10.8776 2.86977 10.8066 3.04135C10.7355 3.21293 10.6313 3.36883 10.5 3.50015L3.75 10.2502L1 11.0002L1.75 8.25015L8.5 1.50015Z"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
            />
        </g>
        <defs>
            <clipPath id="clip0_1917_2501">
                <rect
                    width="12"
                    height="12"
                    fill="white"
                />
            </clipPath>
        </defs>
    </svg>
{/if}
