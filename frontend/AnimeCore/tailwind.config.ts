import { join } from "path";
import type { Config } from "tailwindcss";
import forms from "@tailwindcss/forms";
import typography from "@tailwindcss/typography";
import scrollbar from "tailwind-scrollbar";
// 1. Import the Skeleton plugin
import { skeleton } from "@skeletonlabs/tw-plugin";
import { kokoroTheme } from "./src/lib/themes/kokoro";

const config = {
    // 2. Opt for dark mode to be handled via the class method
    darkMode: "class",
    content: [
        "./src/**/*.{html,js,svelte,ts}",
        // 3. Append the path to the Skeleton package
        join(require.resolve("@skeletonlabs/skeleton"), "../**/*.{html,js,svelte,ts}")
    ],
    theme: {
        extend: {}
    },
    plugins: [
        // 4. Append the Skeleton plugin (after other plugins)
        typography,
        forms,
        scrollbar,
        skeleton({
            themes: {
                custom: [kokoroTheme]
            }
        })
    ]
} satisfies Config;

export default config;
