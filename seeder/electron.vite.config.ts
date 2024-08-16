import { resolve } from "path";
import { defineConfig, swcPlugin, externalizeDepsPlugin } from "electron-vite";
import solid from "vite-plugin-solid";
import svg from "vite-plugin-solid-svg";

const alias_mappinh = {
	// Node
	$constants: resolve(__dirname, "./src/main/constants"),
	$interfaces: resolve(__dirname, "./src/main/interfaces"),
	$backend: resolve(__dirname, "./src/main/backend"),
	$workers: resolve(__dirname, "./src/main/workers"),
	$utils: resolve(__dirname, "./src/main/utils"),
	$database: resolve(__dirname, "./src/main/database"),
	// Web
	"@renderer": resolve(__dirname, "./src/renderer"),
	"@assets": resolve(__dirname, "./src/renderer/assets"),
	"@components": resolve(__dirname, "./src/renderer/components"),
	"@routes": resolve(__dirname, "./src/renderer/routes"),
	"@layouts": resolve(__dirname, "./src/renderer/layouts"),
	"@constants": resolve(__dirname, "./src/renderer/constants"),
	"@utils": resolve(__dirname, "./src/renderer/utils"),
	"@stores": resolve(__dirname, "./src/renderer/stores")
};

export default defineConfig({
	main: {
		plugins: [externalizeDepsPlugin(), swcPlugin()],
		esbuild: {
			target: "esnext",
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: undefined,
			minify: "terser",
			rollupOptions: {
				output: {
					format: "es"
				}
			}
		},
		resolve: {
			alias: alias_mappinh
		}
	},
	preload: {
		plugins: [externalizeDepsPlugin()],
		esbuild: {
			target: "esnext",
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: undefined,
			minify: "terser",
			rollupOptions: {
				output: {
					format: "es"
				}
			}
		},
		resolve: {
			alias: alias_mappinh
		}
	},
	renderer: {
		esbuild: {
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: 2048,
			target: "es2022",
			cssTarget: "esnext"
			//minify: "terser"
		},
		resolve: {
			alias: alias_mappinh
		},
		plugins: [solid(), svg()]
	}
});
