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
    plugins: [require('@tailwindcss/typography'), require('daisyui')],
    daisyui: {
        themes: [
            {
                kokoro: {
                    primary: '#7569E1',
                    secondary: '#E3BD49',
                    accent: '#FFF7F8',
                    neutral: '#1E2036',
                    'base-100': '#070519',
                    info: '#DCD9F7',
                    success: '#6FCF97',
                    warning: '#EDD68D',
                    error: '#EB5757',
                },
            },
        ],
    },
};
