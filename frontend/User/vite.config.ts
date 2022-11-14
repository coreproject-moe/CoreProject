import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	esbuild: {
		legalComments: 'none'
	},
	build: {
		target: 'esnext',
		sourcemap: true
	}
};

export default config;
