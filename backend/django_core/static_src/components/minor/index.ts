import svelteRetag from "svelte-retag";

const mappings = [
    { tagname: "markdown", component: await import("$components/minor/Markdown/Index.svelte") },
    { tagname: "scroll-area", component: await import("$components/minor/ScrollArea/Index.svelte") },
    { tagname: "comment", component: await import("$components/minor/Comment/Index.svelte") }
];

mappings.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-${item.tagname}`,
        attributes: true,
        shadow: false, // Use the light DOM
        hydratable: false
    });
});
