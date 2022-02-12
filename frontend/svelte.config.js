import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';

const dev = process.env.NODE_ENV === 'development';

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
			precompress: 'br',
			fallback: 'app.html'
		})
		// paths: {
		// 	base: dev ? '' : '/static'
		// }
	}
};

export default config;
