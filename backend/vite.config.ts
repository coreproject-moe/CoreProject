import { join, resolve } from "path";
import process from "process";
import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import topLevelAwait from "vite-plugin-top-level-await";
const STATIC_SRC = resolve("./django_core/static_src");

const COMPONENT_DIRECTORY = join(STATIC_SRC, "components");
const JS_DIRECTORY = join(STATIC_SRC, "js");
const CSS_DIRECTORY = join(STATIC_SRC, "css");

export default defineConfig({
    root: resolve("./django_core/static_src"),
    base: "/static/",
    resolve: {
        alias: {
            $functions: join(STATIC_SRC, "functions"),
            $components: join(STATIC_SRC, "components"),
            $icons: join(STATIC_SRC, "components", "icons")
        }
    },
    plugins: [
        topLevelAwait({
            // The export name of top-level await promise for each chunk module
            promiseExportName: "__coreproject__",
            // The function to generate import names of top-level await promise in each chunk module
            promiseImportName: (i) => `__coreproject__${i}`
        }),
        svelte({
            compilerOptions: {
                customElement: true
            },
            configFile: join(process.cwd(), "svelte.config.js")
        })
    ],
    css: {
        devSourcemap: true,
        // Switch to lightning.css when tailwind supports it
        transformer: "postcss"
    },
    esbuild: {
        legalComments: "external"
    },
    build: {
        outDir: join(process.cwd(), "django_core", "static"),
        manifest: true,
        chunkSizeWarningLimit: 2048,
        emptyOutDir: true,
        target: "es2015",
        cssTarget: "esnext",
        minify: "terser",
        // sourcemap: true,
        rollupOptions: {
            input: [
                // Vendor packages
                join(JS_DIRECTORY, "vendor", "htmx.ts"),
                join(JS_DIRECTORY, "vendor", "hyperscript.ts"),
                join(JS_DIRECTORY, "vendor", "easytimer.ts"),

                // Tailwind.css
                join(CSS_DIRECTORY, "index.postcss"),

                // Register Page
                join(JS_DIRECTORY, "register.ts"),
                // join(IMAGE_DIRECTORY, 'favicon', 'favicon.svg'),
                // Components
                join(COMPONENT_DIRECTORY, "index.ts")
            ],
            output: {
                manualChunks: undefined,
                entryFileNames: `coreproject.entry.[name].[hash].js`,
                chunkFileNames: `coreproject.chunk.[name].[hash].js`,
                assetFileNames: `coreproject.asset.[name].[hash].[ext]`
            }
        }
    }
});
