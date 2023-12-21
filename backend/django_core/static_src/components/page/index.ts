// @ts-ignore
import svelteRetag from "svelte-retag";

// Pages
const mapping = [
    { tagname: `explore`, component: await import("./explore/Index.svelte") },
]

mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-page-${item.tagname}`,
        attributes: false,
        shadow: false,
        hydratable: true
    });
});
