import ScrollArea from './ScrollArea.svelte';

// @ts-ignore
import svelteRetag from 'svelte-retag';

svelteRetag({
    component: ScrollArea,
    tagname: 'scroll-area',

    // Optional:
    attributes: ['parentClass', 'offsetScrollbar', 'gradientMask', 'class'], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
});
