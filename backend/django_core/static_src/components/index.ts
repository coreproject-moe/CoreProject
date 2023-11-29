// @ts-ignore
import svelteRetag from "svelte-retag";

import CommentBox from "$components/specific/CommentBox.svelte";
import ScrollArea from "$components//minor/ScrollArea.svelte";

import Comment from "$components/minor/Comment/Index.svelte";

svelteRetag({
    component: ScrollArea,
    tagname: "scroll-area",
    attributes: ["parent_class", "offset_scrollbar", "gradient_mask", "class"], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: Comment,
    tagname: `coreproject-comment`,
    attributes: [`api_url`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
// Specific Components
svelteRetag({
    component: CommentBox,
    tagname: "coreproject-commentbox",
    attributes: ["submit_url"],
    shadow: false,
    hydratable: true
});
