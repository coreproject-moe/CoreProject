import adapter from "@sveltejs/adapter-node";
import path from "path";
import preprocess from "svelte-preprocess";

const dev = process.env.NODE_ENV === "development";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://github.com/sveltejs/svelte-preprocess
    // for more information about preprocessors
    preprocess: [
        preprocess({
            style: "postcss",
            postcss: true
        })
    ],

    kit: {
        adapter: adapter({
            // precompress: 'br',
            fallback: "app.html"
        }),
        // appDir: "static", // Defaults to _app
        // paths: {
        // 	base: dev ? '' : '/static'
        // }
        vite: {
            resolve: {
                alias: {
                    // these are the aliases and paths to them
                    $store: path.resolve("./src/lib/store"),
                    $hooks: path.resolve("./src/hooks"),
                    $components: path.resolve("./src/lib/components"),
                    $urls: path.resolve("./src/lib/constants/backend/urls"),
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
        }
    }
};

export default config;
