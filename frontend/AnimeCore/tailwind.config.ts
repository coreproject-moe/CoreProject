import type { Config } from "tailwindcss";

const config: Config = {
    darkMode: "class",
    content: ["./src/**/*.{html,js,svelte,ts}", require("path").join(require.resolve("@skeletonlabs/skeleton"), "../**/*.{html,js,svelte,ts}")],
    theme: {
        extend: {}
    },
    plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography"), require("tailwind-scrollbar"), ...require("@skeletonlabs/skeleton/tailwind/skeleton.cjs")()]
};

export default config;
