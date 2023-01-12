import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

export default defineConfig({
    plugins: [sveltekit()],
    esbuild: {
        legalComments: "none"
    },
    build: {
        target: "esnext",
        sourcemap: true
    }
});
