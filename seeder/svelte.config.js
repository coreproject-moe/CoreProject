import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://svelte.dev/docs/kit/integrations
    // for more information about preprocessors
    preprocess: vitePreprocess(),
    compilerOptions: {
        runes: true
    },

    kit: {
        adapter: adapter({
            pages: 'dist-front',
            strict: true,
            fallback: '404.html'
        }),
        paths: {
            assets: 'http://<REPLACEME>',
            relative: true
        },
        router: {
            type: 'hash'
        }
    }
};

export default config;
