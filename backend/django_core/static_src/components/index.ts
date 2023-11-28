// @ts-ignore
import svelteRetag from "svelte-retag";

import CommentBox from "./specific/CommentBox.svelte";
import ScrollArea from "./minor/ScrollArea.svelte";

import "../css/tippy.scss";

svelteRetag({
    component: ScrollArea,
    tagname: "scroll-area",
    attributes: ["parent_class", "offset_scrollbar", "gradient_mask", "class"], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: CommentBox,
    tagname: "coreproject-commentbox",
    attributes: [],
    shadow: false,
    hydratable: true
});
