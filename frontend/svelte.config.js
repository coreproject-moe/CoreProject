import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [
		preprocess({
			style: 'postcss',
			postcss: true
		})
	],
	kit: {
		adapter: adapter({
			fallback: 'app.html'
		}),

		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte'
	}
};

export default config;
