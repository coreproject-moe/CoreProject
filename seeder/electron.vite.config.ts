import { defineConfig, externalizeDepsPlugin } from "electron-vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

export default defineConfig({
	main: {
		plugins: [externalizeDepsPlugin()]
	},
	preload: {
		plugins: [externalizeDepsPlugin()]
	},
	renderer: {
		resolve: {
			alias: {
				/// Main
				"@constants": path.resolve(__dirname, "./src/main/constants"),
				/// Renderer
				"@": path.resolve(__dirname, "./src/renderer"),
				"@assets": path.resolve(__dirname, "./src/renderer/assets"),
				"@components": path.resolve(__dirname, "./src/renderer/components"),
				"@routes": path.resolve(__dirname, "./src/renderer/routes"),
				"@layouts": path.resolve(__dirname, "./src/renderer/layouts")
			}
		},
		plugins: [svelte()]
	}
});
