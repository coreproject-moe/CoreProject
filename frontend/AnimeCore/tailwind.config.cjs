/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		fontFamily: {
			sans: [`Kokoro`, 'sans-serif']
		},
		extend: {}
	},
	plugins: [require('@tailwindcss/typography'), require('daisyui')]
};
