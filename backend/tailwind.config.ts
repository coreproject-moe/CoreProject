/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        // '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        "./components/**/*.html",
        "./django_core/templates/**/*.html",

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        // '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',
        "./components/**/*.js",
        "./django_core/**/*.ts",

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        "./components/**/*.py",
        "./**/*.py",

        /**
         * Svelte
         */
        "./**/*.svelte"
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ["Kokoro", "sans-serif"]
            },
            keyframes: {
                floating: {
                    "0%": { transform: "translate(0, 0px)" },
                    "50%": { transform: "translate(0, 1rem)" },
                    "100%": { transform: "translate(0, -0px)" }
                }
            }
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
        require("@tailwindcss/aspect-ratio"),
        require("tailwind-scrollbar"),
        require("daisyui")
    ],
    daisyui: {
        themes: [
            {
                kokoro: {
                    primary: "#7569E1",
                    secondary: "#03020C",
                    accent: "#FFF7F8",
                    neutral: "#1E2036",
                    "base-100": "#070519",
                    info: "#DCD9F7",
                    success: "#6FCF97",
                    warning: "#EDD68D",
                    error: "#EB5757"
                }
            }
        ]
    }
};
