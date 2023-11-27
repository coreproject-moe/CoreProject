import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
const STATIC_SRC = resolve('./django_core/static_src');

const COMPONENT_DIRECTORY = join(STATIC_SRC, 'components');
const JS_DIRECTORY = join(STATIC_SRC, 'js');
const CSS_DIRECTORY = join(STATIC_SRC, 'css');

export default defineConfig({
    root: resolve('./django_core/static_src'),
    base: '/static/',

    plugins: [
        svelte({
            compilerOptions: {
                customElement: true,
            },
        }),
    ],
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
                join(JS_DIRECTORY, 'vendor', 'easytimer.ts'),

                // Tailwind.css
                join(CSS_DIRECTORY, 'index.postcss'),

                // Textarea
                join(JS_DIRECTORY, 'textarea.ts'),

                // Register Page
                join(JS_DIRECTORY, 'register.ts'),
                // join(IMAGE_DIRECTORY, 'favicon', 'favicon.svg'),
                // Components
                join(COMPONENT_DIRECTORY, 'index.ts'),
            ],
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
