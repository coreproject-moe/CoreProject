// @ts-ignore
import svelteRetag from "svelte-retag";

// Pages
const mapping = [
    { tagname: `explore`, component: await import("./Explore/Index.svelte") },
    { tagname: `anime-info`, component: await import("./Anime/Info/Index.svelte") }
];

mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-page-${item.tagname}`,
        attributes: false,
        shadow: false,
        hydratable: true
    });
});
