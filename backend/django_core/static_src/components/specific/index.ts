// @ts-ignore
import svelteRetag from "svelte-retag";

// Specific Components
const mapping = [
    { tagname: "specific-commentbox", component: await import("$components/specific/CommentBox/Index.svelte") },
    { tagname: "specific-my-anime-list", component: await import("$components/specific/MyAnime/Index.svelte") }
];

mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-${item.tagname}`,
        attributes: true,
        shadow: false,
        hydratable: true
    });
});
