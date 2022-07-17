import { sveltekit } from "@sveltejs/kit/vite";
import path from "path";

/** @type {import('vite').UserConfig} */
const config = {
    plugins: [sveltekit()],
    optimizeDeps: {
        exclude: ["swiper"]
    },
    resolve: {
        alias: {
            // these are the aliases and paths to them
            $store: path.resolve("./src/lib/store"),
            $hooks: path.resolve("./src/hooks"),
            $components: path.resolve("./src/lib/components"),
            $functions: path.resolve("./src/lib/functions")
        }
    }
};

export default config;
