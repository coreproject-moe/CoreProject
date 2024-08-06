import { resolve } from 'path'
import { defineConfig, externalizeDepsPlugin } from 'electron-vite'
import solid from 'vite-plugin-solid'

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
        "@main": resolve(__dirname, "./src/main"),
        "@constants": resolve(__dirname, "./src/main/constants"),
        "@interfaces": resolve(__dirname, "./src/main/interfaces")
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
        "@renderer": resolve(__dirname, "./src/renderer"),
        "@assets": resolve(__dirname, "./src/renderer/assets"),
        "@components": resolve(__dirname, "./src/renderer/components"),
        "@routes": resolve(__dirname, "./src/renderer/routes"),
        "@layouts": resolve(__dirname, "./src/renderer/layouts"),
        "@constants": resolve(__dirname, "./src/renderer/constants"),
        "@utils": resolve(__dirname, "./src/renderer/utils")
      }
    },
    plugins: [solid()]
  }
});
