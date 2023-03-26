/* eslint-disable global-require */
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./App.{js,jsx,ts,tsx}', './screens/**/*.{js,jsx,ts,tsx}'],
    theme: {
        fontFamily: {
            sans: [`Kokoro`, 'sans-serif'],
        },

        extend: {},
    },

    // eslint-disable-next-line import/no-extraneous-dependencies
    plugins: [require('@tailwindcss/typography')],
};
