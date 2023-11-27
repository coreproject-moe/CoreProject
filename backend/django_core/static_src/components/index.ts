import ScrollArea from './ScrollArea.svelte';

// @ts-ignore
import svelteRetag from 'svelte-retag';

svelteRetag({
    component: ScrollArea,
    tagname: 'scroll-area',
    attributes: ['parent_class', 'offset_scrollbar', 'gradient_mask', 'class'], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM]
    hydratable: true,
});
