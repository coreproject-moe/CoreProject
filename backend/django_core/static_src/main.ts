// import css
import "./css/index.postcss";

// configure nprogress
import nProgress from "nprogress";

// Global Configuration
nProgress.configure({
    // Full list: https://github.com/rstacruz/nprogress#configuration
    showSpinner: false,
    minimum: 0.16
});

// Register web components
import.meta.glob("./components/**/*/index.ts", {
    eager: true
});

// Register event listeners
import.meta.glob("./events/**/*.ts");
