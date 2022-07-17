const cssnano = require("cssnano");
const postcss_preset_env = require("postcss-preset-env");
const tailwindcss = require("tailwindcss");
const autoprefixer = require("autoprefixer");
const dev = process.env.NODE_ENV === "development";

const config = {
    plugins: [
        postcss_preset_env({
            stage: 0,
            autoprefixer: {
                grid: true
            }
        }),
        cssnano({
            autoprefixer: false,
            preset: ["default"]
        }),
        tailwindcss({}),
        autoprefixer({})
    ]
};

module.exports = config;
