import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';

export default defineConfig({
    root: resolve('./django_core/static_src'),
    base: '/static/',
    build: {
        outDir: join(process.cwd(), 'django_core', 'static'),
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                htmx: resolve('./django_core/static_src/js/htmx.js'),
                hyperscript: resolve(
                    './django_core/static_src/js/hyperscript.js'
                ),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
