import { join } from 'path';
import process from 'process';
import { defineConfig } from 'vite';

const DJANGO_DIRECTORY = process.cwd();
const DJANGO_STATIC_DIRECTORY = join(DJANGO_DIRECTORY, '/static/');

const STATIC_DIRECTORY = join(DJANGO_DIRECTORY, '/static_src/');

export default defineConfig({
    base: '/static/',
    build: {
        outDir: DJANGO_STATIC_DIRECTORY,
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                htmx: join(STATIC_DIRECTORY, 'js', 'htmx.js'),
            },
        },
    },
});
