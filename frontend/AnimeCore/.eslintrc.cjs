module.exports = {
    root: true,
    parser: "@typescript-eslint/parser",
    extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended", "prettier"],
    plugins: ["svelte3", "@typescript-eslint", "simple-import-sort", "unused-imports"],
    ignorePatterns: ["*.cjs"],
    overrides: [{ files: ["*.svelte"], processor: "svelte3/svelte3" }],
    settings: {
        "svelte3/typescript": () => require("typescript")
    },
    parserOptions: {
        sourceType: "module",
        ecmaVersion: 2020
    },
    globals: { svelte: true },
    rules: {
        /** Sort imports */
        "simple-import-sort/imports": "warn",
        "simple-import-sort/exports": "warn",
        /** Remove unused code */
        "unused-imports/no-unused-imports": "warn",
        "unused-imports/no-unused-vars": [
            "warn",
            {
                vars: "all",
                varsIgnorePattern: "\\$\\$Props",
                args: "after-used",
                argsIgnorePattern: "^_"
            }
        ]
    },
    env: {
        browser: true,
        es2022: true,
        node: true
    }
};
