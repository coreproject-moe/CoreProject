// @ts-ignore
import svelteRetag from "svelte-retag";
import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
import Comment from "$components/minor/Comment/Index.svelte";
import Markdown from "$components/minor/Markdown/Index.svelte";

svelteRetag({
    component: Markdown,
    tagname: `coreproject-markdown`,
    attributes: [`markdown`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: ScrollArea,
    tagname: `coreproject-scroll-area`,
    attributes: [`parent_class`, `offset_scrollbar`, `gradient_mask`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: Comment,
    tagname: `coreproject-comment`,
    attributes: [`api_url`],
    shadow: false, // Use the light DOM
    hydratable: true
});
