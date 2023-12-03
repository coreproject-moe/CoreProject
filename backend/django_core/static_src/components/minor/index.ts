// @ts-ignore
import svelteRetag from "svelte-retag";

svelteRetag({
    component: (await import("$components/minor/Markdown/Index.svelte")).default,
    tagname: `coreproject-markdown`,
    attributes: [`markdown`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: false
});
svelteRetag({
    component: (await import("$components/minor/ScrollArea/Index.svelte")).default,
    tagname: `coreproject-scroll-area`,
    attributes: [`parent_class`, `offset_scrollbar`, `gradient_mask`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: false
});
svelteRetag({
    component: (await import("$components/minor/Comment/Index.svelte")).default,
    tagname: `coreproject-comment`,
    attributes: [`api_url`],
    shadow: false, // Use the light DOM
    hydratable: false
});
