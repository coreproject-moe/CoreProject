import { sveltekit } from "@sveltejs/kit/vite";
import path from "path";

/** @type {import('vite').UserConfig} */
const config = {
    plugins: [sveltekit()],
    resolve: {
        alias: {
            // these are the aliases and paths to them
            $store: path.resolve("./src/lib/store"),
            $hooks: path.resolve("./src/hooks"),
            $components: path.resolve("./src/lib/components"),
            $functions: path.resolve("./src/lib/functions")
        }
    },
    esbuild: {
        legalComments: "none",
        charset: "utf8"
    },
    build: {
        // minify: "terser",
        // terserOptions: {
        //     format: {
        //         comments: false
        //     }
        // },
        rollupOptions: {
            output: {
                manualChunks: {
                    // md5: ["md5"],
                    // anime: ["animejs"],
                    // dayjs: ["dayjs"],
                    // swiper: ["swiper"],
                    // "tippy.js": ["tippy.js"],
                }
            }
        }
    }
};

export default config;
