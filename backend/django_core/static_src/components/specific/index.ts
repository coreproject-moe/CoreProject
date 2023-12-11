// @ts-ignore
import svelteRetag from "svelte-retag";

// Specific Components
const mapping = [
    { tagname: "specific-commentbox", component: await import("$components/specific/CommentBox/Index.svelte") },
    { tagname: "specific-my-anime-list", component: await import("$components/specific/MyAnime/Index.svelte") },
    { tagname: "specific-search-modal", component: await import("$components/specific/SearchModal/Index.svelte") },
    { tagname: "specific-latest-episode", component: await import("$components/specific/LatestEpisode/Index.svelte") },
    // Modals
    /* item */ { tagname: "specific-search-modal", component: await import("$components/specific/SearchModal/Index.svelte") },
    /* Trigger */ { tagname: "specific-search-modal-trigger", component: await import("./SearchModal/Trigger.svelte") }
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
