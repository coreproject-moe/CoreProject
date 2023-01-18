/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./src/**/*.{html,js,svelte,ts,json}'],
    theme: {
        fontFamily: {
            sans: [`Kokoro`, 'sans-serif']
        },

        extend: {}
    },

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
                    error: '#EB5757'
                }
            }
        ]
    }
};
