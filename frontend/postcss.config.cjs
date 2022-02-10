const cssnano = require('cssnano');
const autoprefixer = require('autoprefixer');
const purgecss = require('@fullhuman/postcss-purgecss');

const mode = process.env.NODE_ENV;
const dev = mode === 'development';

const config = {
	plugins: [
		autoprefixer(),
		// Run on buld
		!dev &&
			purgecss({
				content: ['./src/**/**/*.{svelte,html,js,ts}'],
				defaultExtractor: (content) => content.match(/[A-Za-z0-9-_:/]+/g) || [],
				safelist: {
					deep: [/svelte-/, /swiper-/]
				}
			}),
		!dev &&
			cssnano({
				preset: 'default'
			})
	]
};

module.exports = config;
