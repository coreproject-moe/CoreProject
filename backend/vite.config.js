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
                // Vendor packages
                htmx: resolve('./django_core/static_src/js/htmx.ts'),
                hyperscript: resolve(
                    './django_core/static_src/js/hyperscript.ts'
                ),

                // Tailwind.css
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
