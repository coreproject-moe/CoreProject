import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';
const STATIC_SRC = resolve('./django_core/static_src');

const JS_DIRECTORY = join(STATIC_SRC, 'js');
const CSS_DIRECTORY = join(STATIC_SRC, 'css');
const IMAGE_DIRECTORY = join(STATIC_SRC, 'images');

export default defineConfig({
    root: resolve('./django_core/static_src'),
    base: '/static/',
    // assetsInclude: ['**/*.svg'],
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
            input: [
                // Vendor packages
                join(JS_DIRECTORY, 'vendor', 'htmx.ts'),
                join(JS_DIRECTORY, 'vendor', 'hyperscript.ts'),

                // Tailwind.css
                join(CSS_DIRECTORY, 'index.postcss'),

                // Textarea
                join(JS_DIRECTORY, 'textarea.ts'),
                // Easytimer
                join(JS_DIRECTORY, 'easytimer.ts'),
                // Register Page
                join(JS_DIRECTORY, 'register.ts'),
                // Register Page
                join(JS_DIRECTORY, 'favicon.js'),

                // join(IMAGE_DIRECTORY, 'favicon', 'favicon.svg'),
            ],
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
