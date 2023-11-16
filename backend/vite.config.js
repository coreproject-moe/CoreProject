import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';

const STATIC_SRC = resolve('./django_core/static_src');

const JS_DIRECTORY = join(STATIC_SRC, 'js');
const CSS_DIRECTORY = join(STATIC_SRC, 'css');

export default defineConfig({
    root: resolve('./django_core/static_src'),
    base: '/static/',
    // css: {
    //     devSourcemap: true,
    // },
    build: {
        outDir: join(process.cwd(), 'django_core', 'static'),
        manifest: true,
        emptyOutDir: true,
        target: 'esnext',
        sourcemap: true,
        rollupOptions: {
            input: {
                // Vendor packages
                htmx: join(JS_DIRECTORY, 'vendor', 'htmx.ts'),
                hyperscript: join(JS_DIRECTORY, 'vendor', 'hyperscript.ts'),

                // Tailwind.css
                tailwind: join(CSS_DIRECTORY, 'index.postcss'),

                // Textarea
                textarea: join(JS_DIRECTORY, 'textarea.ts'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
