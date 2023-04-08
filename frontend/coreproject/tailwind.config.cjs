/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: [
        './src/**/*.{html,js,svelte,ts}',
        require('path').join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')
    ],
    theme: {
        extend: {
            screens: {
                '3xl': '1920px',
            },
        }
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        ...require('@skeletonlabs/skeleton/tailwind/skeleton.cjs')(),
        require('tailwind-scrollbar'),
    ]
};
