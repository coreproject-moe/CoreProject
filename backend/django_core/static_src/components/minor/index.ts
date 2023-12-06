// @ts-ignore
import svelteRetag from "svelte-retag";

const mappings = [
    { tagname: "markdown", component: await import("$components/minor/Markdown/Index.svelte"), attributes: [`markdown`, `class`] },
    { tagname: "scroll-area", component: await import("$components/minor/ScrollArea/Index.svelte"), attributes: [`parent_class`, `offset_scrollbar`, `gradient_mask`, `class`] },
    { tagname: "comment", component: await import("$components/minor/Comment/Index.svelte"), attributes: [`api_url`] }
];

mappings.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-${item.tagname}`,
        attributes: item.attributes, // Changes to these attributes will be reactively forwarded to your component
        shadow: false, // Use the light DOM
        hydratable: false
    });
});
