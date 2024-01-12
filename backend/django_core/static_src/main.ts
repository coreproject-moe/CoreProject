// import css
import "./css/index.postcss";

// Configure hyperscript

import _hyperscript from "hyperscript.org";

_hyperscript.browserInit();
_hyperscript.processNode(document.body);
window._hyperscript = _hyperscript;

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
const components = import.meta.glob("./components/**/*/index.ts", {
    eager: true
});
if (import.meta.env.DEV) {
    console.log(`Registered : ${Object.keys(components).length} web-components`);
}

// Register event listeners
const events = import.meta.glob("./event/**/*.ts", {
    eager: true
});
if (import.meta.env.DEV) {
    console.log(`Registered : ${Object.keys(events).length}`);
}
