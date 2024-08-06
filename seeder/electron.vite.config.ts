import { defineConfig, externalizeDepsPlugin } from "electron-vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

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
      chunkSizeWarningLimit: undefined
      //minify: "terser"
    },
    resolve: {
      alias: {
        $constants: path.resolve(__dirname, "./src/main/constants"),
        $interfaces: path.resolve(__dirname, "./src/main/interfaces")
      }
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
      chunkSizeWarningLimit: undefined
      //minify: "terser"
    }
  },

  renderer: {
    esbuild: {
      target: "esnext",
      legalComments: "external"
    },
    build: {
      commonjsOptions: {
        transformMixedEsModules: true
      },
      chunkSizeWarningLimit: 2048,
      target: "esnext",
      cssTarget: "esnext"
      //minify: "terser"
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src/renderer"),
        "@assets": path.resolve(__dirname, "./src/renderer/assets"),
        "@components": path.resolve(__dirname, "./src/renderer/components"),
        "@routes": path.resolve(__dirname, "./src/renderer/routes"),
        "@layouts": path.resolve(__dirname, "./src/renderer/layouts"),
        "@constants": path.resolve(__dirname, "./src/renderer/constants"),
        "@utils": path.resolve(__dirname, "./src/renderer/utils")
      }
    },
    plugins: [svelte()]
  }
});
