// vite.config.ts
import { join, resolve } from "path";
import process from "process";
import { defineConfig } from "file:///home/sssuneeth/Desktop/CoreProject-Fork/backend/node_modules/vite/dist/node/index.js";
import { svelte } from "file:///home/sssuneeth/Desktop/CoreProject-Fork/backend/node_modules/@sveltejs/vite-plugin-svelte/src/index.js";
var STATIC_SRC = resolve("./django_core/static_src");
var COMPONENT_DIRECTORY = join(STATIC_SRC, "components");
var JS_DIRECTORY = join(STATIC_SRC, "js");
var CSS_DIRECTORY = join(STATIC_SRC, "css");
var vite_config_default = defineConfig({
  root: resolve("./django_core/static_src"),
  base: "/static/",
  resolve: {
    alias: {
      $stores: join(STATIC_SRC, "stores"),
      $functions: join(STATIC_SRC, "functions"),
      $components: join(STATIC_SRC, "components"),
      $icons: join(STATIC_SRC, "components", "icons"),
      $skeleton: join(STATIC_SRC, "skeleton"),
      $types: join(STATIC_SRC, "types"),
      $constants: join(STATIC_SRC, "constants")
    }
  },
  plugins: [
    svelte({
      compilerOptions: {
        customElement: true
      },
      configFile: join(process.cwd(), "svelte.config.js")
    })
  ],
  css: {
    devSourcemap: true,
    // Switch to lightning.css when tailwind supports it
    transformer: "postcss"
  },
  esbuild: {
    // legalComments: "external"
  },
  build: {
    outDir: join(process.cwd(), "django_core", "static"),
    manifest: true,
    chunkSizeWarningLimit: 2048,
    emptyOutDir: true,
    target: "es2022",
    cssTarget: "es2015",
    minify: "terser",
    // sourcemap: true,
    rollupOptions: {
      input: [
        // Vendor packages
        join(JS_DIRECTORY, "vendor", "easytimer.ts"),
        // Tailwind.css
        join(CSS_DIRECTORY, "index.postcss"),
        // join(IMAGE_DIRECTORY, 'favicon', 'favicon.svg'),
        // Components
        join(STATIC_SRC, "main.ts")
      ],
      output: {
        manualChunks: void 0,
        entryFileNames: `coreproject.entry.[name].[hash].js`,
        chunkFileNames: `coreproject.chunk.[name].[hash].js`,
        assetFileNames: `coreproject.asset.[name].[hash].[ext]`
      }
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvaG9tZS9zc3N1bmVldGgvRGVza3RvcC9Db3JlUHJvamVjdC1Gb3JrL2JhY2tlbmRcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIi9ob21lL3Nzc3VuZWV0aC9EZXNrdG9wL0NvcmVQcm9qZWN0LUZvcmsvYmFja2VuZC92aXRlLmNvbmZpZy50c1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vaG9tZS9zc3N1bmVldGgvRGVza3RvcC9Db3JlUHJvamVjdC1Gb3JrL2JhY2tlbmQvdml0ZS5jb25maWcudHNcIjtpbXBvcnQgeyBqb2luLCByZXNvbHZlIH0gZnJvbSBcInBhdGhcIjtcbmltcG9ydCBwcm9jZXNzIGZyb20gXCJwcm9jZXNzXCI7XG5pbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tIFwidml0ZVwiO1xuaW1wb3J0IHsgc3ZlbHRlIH0gZnJvbSBcIkBzdmVsdGVqcy92aXRlLXBsdWdpbi1zdmVsdGVcIjtcbmNvbnN0IFNUQVRJQ19TUkMgPSByZXNvbHZlKFwiLi9kamFuZ29fY29yZS9zdGF0aWNfc3JjXCIpO1xuXG5jb25zdCBDT01QT05FTlRfRElSRUNUT1JZID0gam9pbihTVEFUSUNfU1JDLCBcImNvbXBvbmVudHNcIik7XG5jb25zdCBKU19ESVJFQ1RPUlkgPSBqb2luKFNUQVRJQ19TUkMsIFwianNcIik7XG5jb25zdCBDU1NfRElSRUNUT1JZID0gam9pbihTVEFUSUNfU1JDLCBcImNzc1wiKTtcblxuZXhwb3J0IGRlZmF1bHQgZGVmaW5lQ29uZmlnKHtcbiAgICByb290OiByZXNvbHZlKFwiLi9kamFuZ29fY29yZS9zdGF0aWNfc3JjXCIpLFxuICAgIGJhc2U6IFwiL3N0YXRpYy9cIixcbiAgICByZXNvbHZlOiB7XG4gICAgICAgIGFsaWFzOiB7XG4gICAgICAgICAgICAkc3RvcmVzOiBqb2luKFNUQVRJQ19TUkMsIFwic3RvcmVzXCIpLFxuICAgICAgICAgICAgJGZ1bmN0aW9uczogam9pbihTVEFUSUNfU1JDLCBcImZ1bmN0aW9uc1wiKSxcbiAgICAgICAgICAgICRjb21wb25lbnRzOiBqb2luKFNUQVRJQ19TUkMsIFwiY29tcG9uZW50c1wiKSxcbiAgICAgICAgICAgICRpY29uczogam9pbihTVEFUSUNfU1JDLCBcImNvbXBvbmVudHNcIiwgXCJpY29uc1wiKSxcbiAgICAgICAgICAgICRza2VsZXRvbjogam9pbihTVEFUSUNfU1JDLCBcInNrZWxldG9uXCIpLFxuICAgICAgICAgICAgJHR5cGVzOiBqb2luKFNUQVRJQ19TUkMsIFwidHlwZXNcIiksXG4gICAgICAgICAgICAkY29uc3RhbnRzOiBqb2luKFNUQVRJQ19TUkMsIFwiY29uc3RhbnRzXCIpXG4gICAgICAgIH1cbiAgICB9LFxuICAgIHBsdWdpbnM6IFtcbiAgICAgICAgc3ZlbHRlKHtcbiAgICAgICAgICAgIGNvbXBpbGVyT3B0aW9uczoge1xuICAgICAgICAgICAgICAgIGN1c3RvbUVsZW1lbnQ6IHRydWVcbiAgICAgICAgICAgIH0sXG4gICAgICAgICAgICBjb25maWdGaWxlOiBqb2luKHByb2Nlc3MuY3dkKCksIFwic3ZlbHRlLmNvbmZpZy5qc1wiKVxuICAgICAgICB9KVxuICAgIF0sXG4gICAgY3NzOiB7XG4gICAgICAgIGRldlNvdXJjZW1hcDogdHJ1ZSxcbiAgICAgICAgLy8gU3dpdGNoIHRvIGxpZ2h0bmluZy5jc3Mgd2hlbiB0YWlsd2luZCBzdXBwb3J0cyBpdFxuICAgICAgICB0cmFuc2Zvcm1lcjogXCJwb3N0Y3NzXCJcbiAgICB9LFxuICAgIGVzYnVpbGQ6IHtcbiAgICAgICAgLy8gbGVnYWxDb21tZW50czogXCJleHRlcm5hbFwiXG4gICAgfSxcbiAgICBidWlsZDoge1xuICAgICAgICBvdXREaXI6IGpvaW4ocHJvY2Vzcy5jd2QoKSwgXCJkamFuZ29fY29yZVwiLCBcInN0YXRpY1wiKSxcbiAgICAgICAgbWFuaWZlc3Q6IHRydWUsXG4gICAgICAgIGNodW5rU2l6ZVdhcm5pbmdMaW1pdDogMjA0OCxcbiAgICAgICAgZW1wdHlPdXREaXI6IHRydWUsXG4gICAgICAgIHRhcmdldDogXCJlczIwMjJcIixcbiAgICAgICAgY3NzVGFyZ2V0OiBcImVzMjAxNVwiLFxuICAgICAgICBtaW5pZnk6IFwidGVyc2VyXCIsXG4gICAgICAgIC8vIHNvdXJjZW1hcDogdHJ1ZSxcbiAgICAgICAgcm9sbHVwT3B0aW9uczoge1xuICAgICAgICAgICAgaW5wdXQ6IFtcbiAgICAgICAgICAgICAgICAvLyBWZW5kb3IgcGFja2FnZXNcbiAgICAgICAgICAgICAgICBqb2luKEpTX0RJUkVDVE9SWSwgXCJ2ZW5kb3JcIiwgXCJlYXN5dGltZXIudHNcIiksXG5cbiAgICAgICAgICAgICAgICAvLyBUYWlsd2luZC5jc3NcbiAgICAgICAgICAgICAgICBqb2luKENTU19ESVJFQ1RPUlksIFwiaW5kZXgucG9zdGNzc1wiKSxcblxuICAgICAgICAgICAgICAgIC8vIGpvaW4oSU1BR0VfRElSRUNUT1JZLCAnZmF2aWNvbicsICdmYXZpY29uLnN2ZycpLFxuICAgICAgICAgICAgICAgIC8vIENvbXBvbmVudHNcbiAgICAgICAgICAgICAgICBqb2luKFNUQVRJQ19TUkMsIFwibWFpbi50c1wiKVxuICAgICAgICAgICAgXSxcbiAgICAgICAgICAgIG91dHB1dDoge1xuICAgICAgICAgICAgICAgIG1hbnVhbENodW5rczogdW5kZWZpbmVkLFxuICAgICAgICAgICAgICAgIGVudHJ5RmlsZU5hbWVzOiBgY29yZXByb2plY3QuZW50cnkuW25hbWVdLltoYXNoXS5qc2AsXG4gICAgICAgICAgICAgICAgY2h1bmtGaWxlTmFtZXM6IGBjb3JlcHJvamVjdC5jaHVuay5bbmFtZV0uW2hhc2hdLmpzYCxcbiAgICAgICAgICAgICAgICBhc3NldEZpbGVOYW1lczogYGNvcmVwcm9qZWN0LmFzc2V0LltuYW1lXS5baGFzaF0uW2V4dF1gXG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9XG59KTtcbiJdLAogICJtYXBwaW5ncyI6ICI7QUFBa1UsU0FBUyxNQUFNLGVBQWU7QUFDaFcsT0FBTyxhQUFhO0FBQ3BCLFNBQVMsb0JBQW9CO0FBQzdCLFNBQVMsY0FBYztBQUN2QixJQUFNLGFBQWEsUUFBUSwwQkFBMEI7QUFFckQsSUFBTSxzQkFBc0IsS0FBSyxZQUFZLFlBQVk7QUFDekQsSUFBTSxlQUFlLEtBQUssWUFBWSxJQUFJO0FBQzFDLElBQU0sZ0JBQWdCLEtBQUssWUFBWSxLQUFLO0FBRTVDLElBQU8sc0JBQVEsYUFBYTtBQUFBLEVBQ3hCLE1BQU0sUUFBUSwwQkFBMEI7QUFBQSxFQUN4QyxNQUFNO0FBQUEsRUFDTixTQUFTO0FBQUEsSUFDTCxPQUFPO0FBQUEsTUFDSCxTQUFTLEtBQUssWUFBWSxRQUFRO0FBQUEsTUFDbEMsWUFBWSxLQUFLLFlBQVksV0FBVztBQUFBLE1BQ3hDLGFBQWEsS0FBSyxZQUFZLFlBQVk7QUFBQSxNQUMxQyxRQUFRLEtBQUssWUFBWSxjQUFjLE9BQU87QUFBQSxNQUM5QyxXQUFXLEtBQUssWUFBWSxVQUFVO0FBQUEsTUFDdEMsUUFBUSxLQUFLLFlBQVksT0FBTztBQUFBLE1BQ2hDLFlBQVksS0FBSyxZQUFZLFdBQVc7QUFBQSxJQUM1QztBQUFBLEVBQ0o7QUFBQSxFQUNBLFNBQVM7QUFBQSxJQUNMLE9BQU87QUFBQSxNQUNILGlCQUFpQjtBQUFBLFFBQ2IsZUFBZTtBQUFBLE1BQ25CO0FBQUEsTUFDQSxZQUFZLEtBQUssUUFBUSxJQUFJLEdBQUcsa0JBQWtCO0FBQUEsSUFDdEQsQ0FBQztBQUFBLEVBQ0w7QUFBQSxFQUNBLEtBQUs7QUFBQSxJQUNELGNBQWM7QUFBQTtBQUFBLElBRWQsYUFBYTtBQUFBLEVBQ2pCO0FBQUEsRUFDQSxTQUFTO0FBQUE7QUFBQSxFQUVUO0FBQUEsRUFDQSxPQUFPO0FBQUEsSUFDSCxRQUFRLEtBQUssUUFBUSxJQUFJLEdBQUcsZUFBZSxRQUFRO0FBQUEsSUFDbkQsVUFBVTtBQUFBLElBQ1YsdUJBQXVCO0FBQUEsSUFDdkIsYUFBYTtBQUFBLElBQ2IsUUFBUTtBQUFBLElBQ1IsV0FBVztBQUFBLElBQ1gsUUFBUTtBQUFBO0FBQUEsSUFFUixlQUFlO0FBQUEsTUFDWCxPQUFPO0FBQUE7QUFBQSxRQUVILEtBQUssY0FBYyxVQUFVLGNBQWM7QUFBQTtBQUFBLFFBRzNDLEtBQUssZUFBZSxlQUFlO0FBQUE7QUFBQTtBQUFBLFFBSW5DLEtBQUssWUFBWSxTQUFTO0FBQUEsTUFDOUI7QUFBQSxNQUNBLFFBQVE7QUFBQSxRQUNKLGNBQWM7QUFBQSxRQUNkLGdCQUFnQjtBQUFBLFFBQ2hCLGdCQUFnQjtBQUFBLFFBQ2hCLGdCQUFnQjtBQUFBLE1BQ3BCO0FBQUEsSUFDSjtBQUFBLEVBQ0o7QUFDSixDQUFDOyIsCiAgIm5hbWVzIjogW10KfQo=
