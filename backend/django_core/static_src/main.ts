// import css
import "./css/index.postcss";

// Import htmx
import "htmx.org";

// configure nprogress
import nProgress from "nprogress";

// Global Configuration
nProgress.configure({
    // Full list: https://github.com/rstacruz/nprogress#configuration
    showSpinner: false,
    minimum: 0.16
});

// Register web components
const components = import.meta.glob("./components/**/*/index.ts");

// Register event listeners
const events = import.meta.glob("./events/**/*.ts");

// Register
[components, events].forEach((item) => {
    // console.log(`Registered : ${Object.keys(item).length} ${String(item)}`);
    Object.values(item).forEach(async (module) => {
        await module();
    });
});
