import svelteRetag from "svelte-retag";

const mappings = [
    { tagname: "markdown", component: await import("./Markdown/Index.svelte") },
    { tagname: "scroll-area", component: await import("./ScrollArea/Index.svelte") },
    { tagname: "comment", component: await import("./Comment/Index.svelte") },
    { tagname: "hover-expand", component: await import("./HoverExpand/Index.svelte") },
    { tagname: "sidebar", component: await import("./SideBar/Index.svelte") },
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
