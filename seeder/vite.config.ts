import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
    esbuild: {
        target: 'esnext',
        legalComments: 'external'
    },
    css: {
        devSourcemap: true,
        // Switch to lightning.css when tailwind supports it
        transformer: 'postcss'
    },
    build: {
        commonjsOptions: {
            transformMixedEsModules: true
        },
        chunkSizeWarningLimit: 2048,
        emptyOutDir: true,
        target: 'esnext',
        cssTarget: 'esnext',
        minify: 'terser'
        //sourcemap: true
    },
    worker: {
        format: 'es'
    },

    plugins: [sveltekit()],

    test: {
        include: ['src/**/*.{test,spec}.{js,ts}']
    }
});
