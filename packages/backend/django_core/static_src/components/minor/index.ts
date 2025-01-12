import { register } from "$functions/register";

const mappings = [
    { tagname: "markdown", component: await import("./Markdown/Index.svelte") },
    { tagname: "scroll-area", component: await import("./ScrollArea/Index.svelte") },
    { tagname: "comment", component: await import("./Comment/Index.svelte") },
    { tagname: "hover-expand", component: await import("./HoverExpand/Index.svelte") },
    { tagname: "sidebar", component: await import("./SideBar/Index.svelte") }
];

mappings.forEach((item) => {
    register({
        component: item.component.default,
        tagname: `coreproject-${item.tagname}`
    });
});
