import node_adapter from "@sveltejs/adapter-node";
import static_adapter from "@sveltejs/adapter-static";
import vercel from "@sveltejs/adapter-vercel";
import { vitePreprocess } from "@sveltejs/kit/vite";
import path from "path";

const is_static = process.env.BUILD_STATIC_ENV ?? false;
const is_node = process.env.BUILD_NODE_ENV ?? false;

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://kit.svelte.dev/docs/integrations#preprocessors
    // for more information about preprocessors
    preprocess: vitePreprocess({}),

    kit: {
        // adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
        // If your environment is not supported or you settled on a specific environment, switch out the adapter.
        // See https://kit.svelte.dev/docs/adapters for more information about adapters.
        adapter: is_static
            ? static_adapter({
                  fallback: "app.html",
                  // precompress: true,
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
            $modals: path.resolve("./src/lib/components/modals"),
            $skeletons: path.resolve("./src/lib/skeletons"),
            $home: path.resolve("./")
        }
    }
};

export default config;
