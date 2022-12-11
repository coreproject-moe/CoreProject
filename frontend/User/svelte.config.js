import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import path from 'path';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [vitePreprocess()],
	kit: {
		appDir: 'svelte__user',
		adapter: adapter({ fallback: 'app.html' }),
		alias: {
			$hooks: path.resolve('./src/hooks'),
			$components: path.resolve('./src/lib/components'),
			$icons: path.resolve('./src/lib/icons'),
			$kaomoji: path.resolve('./src/lib/kaomoji'),
			$error: path.resolve('./src/lib/components/errors')
		}
	}
};

export default config;
