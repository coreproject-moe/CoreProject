import { join, resolve } from 'path';
import process from 'process';
import { defineConfig } from 'vite';

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
                htmx: resolve('./django_core/static_src/js/htmx.ts'),
                hyperscript: resolve(
                    './django_core/static_src/js/hyperscript.ts'
                ),

                // Tailwind.css
                tailwind: resolve('./django_core/static_src/css/index.css'),

                // Textarea
                textarea: resolve('./django_core/static_src/js/textarea.ts'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
