import node_adapter from "@sveltejs/adapter-node";
import static_adapter from "@sveltejs/adapter-static";
import vercel from "@sveltejs/adapter-vercel";
import path from "path";
import preprocess from "svelte-preprocess";

const is_static = process.env.BUILD_STATIC_ENV ?? false;
const is_node = process.env.BUILD_NODE_ENV ?? false;

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
        appDir: "svelte__animecore",
        // adapter: adapter({ fallback: "app.html" }),
        adapter: is_static
        ? static_adapter({
            fallback: "app.html",
            precompress: true,
            strict: true
        })
        : is_node
        ? node_adapter({
            precompress: false
        })
        : vercel({
            // an array of dependencies that esbuild should treat
            // as external when bundling functions
            external: []
        }),

        alias: {
            $store: path.resolve("./src/lib/store"),
            $hooks: path.resolve("./src/hooks"),
            $components: path.resolve("./src/lib/components"),
            $icons: path.resolve("./src/lib/icons"),
            $data: path.resolve("./src/lib/data"),
            $kaomoji: path.resolve("./src/lib/kaomoji"),
            $error: path.resolve("./src/lib/components/errors"),
            $functions: path.resolve("./src/lib/functions"),
            $modals: path.resolve("./src/lib/components/modals")
        }
    }
};

export default config;
