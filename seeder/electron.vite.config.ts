import { resolve } from "path";
import { defineConfig, externalizeDepsPlugin } from "electron-vite";
import solid from "vite-plugin-solid";
import svg from "vite-plugin-solid-svg";

const node_alias = {
	$constants: resolve(__dirname, "./src/main/constants"),
	$interfaces: resolve(__dirname, "./src/main/interfaces"),
	$backend: resolve(__dirname, "./src/main/backend"),
	$workers: resolve(__dirname, "./src/main/workers"),
	$utils: resolve(__dirname, "./src/main/utils"),
	$database: resolve(__dirname, "./src/main/database")
};

export default defineConfig({
	main: {
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
			alias: node_alias
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
			alias: node_alias
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
			alias: {
				"@renderer": resolve(__dirname, "./src/renderer"),
				"@assets": resolve(__dirname, "./src/renderer/assets"),
				"@components": resolve(__dirname, "./src/renderer/components"),
				"@routes": resolve(__dirname, "./src/renderer/routes"),
				"@layouts": resolve(__dirname, "./src/renderer/layouts"),
				"@constants": resolve(__dirname, "./src/renderer/constants"),
				"@utils": resolve(__dirname, "./src/renderer/utils"),
				"@stores": resolve(__dirname, "./src/renderer/stores")
			}
		},
		plugins: [solid(), svg()]
	}
});
