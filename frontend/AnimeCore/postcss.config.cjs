const cssnano = require("cssnano");
const postcss_preset_env = require("postcss-preset-env");
const tailwindcss = require("tailwindcss");
const autoprefixer = require("autoprefixer");
const tailwindNesting = require("@tailwindcss/nesting/index");
const purgecss = require("@fullhuman/postcss-purgecss");

const dev = process.env.NODE_ENV === "development";

const config = {
    plugins: [
        tailwindcss({}),
        tailwindNesting({}),
        autoprefixer({}),
        postcss_preset_env({
            stage: 0,
            autoprefixer: {
                grid: true
            },
            features: { "nesting-rules": false }
        }),
        cssnano({
            autoprefixer: false,
            preset: ["default"]
        })
        // !dev &&
        //     purgecss({
        //         content: ["./src/**/**/*.{svelte,html,js,ts}"],
        //         defaultExtractor: (content) =>
        //             content.match(/[\w\-:.\/\[\]\#\,\(\)]+(?<!:)/g) || [],
        //         safelist: {
        //             deep: [],
        //             greedy: [/swiper/, /svelte/]
        //         }
        //     })
    ]
};

module.exports = config;
