// @ts-ignore
import { register } from "$functions/resgister";
import svelteRetag from "svelte-retag";

// Pages
const mapping = [
    { tagname: `explore`, component: await import("./explore/Index.svelte") },
    { tagname: `anime-info`, component: await import("./anime/info/Index.svelte") }
];

mapping.forEach((item) => {
    register({
        component: item.component.default,
        tagname: `coreproject-page-${item.tagname}`
    });
});
