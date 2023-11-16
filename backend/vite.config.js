import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';

export default defineConfig({
    root: resolve('./django_core/'),
    base: '/static/',
    build: {
        outDir: './static',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                htmx: resolve('./django_core/static_src/js/htmx.js'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
