// @ts-ignore

import { register } from "$functions/resgister";

// Specific Components
const mapping = [
    { tagname: "commentbox", component: await import("./CommentBox/Index.svelte") },
    { tagname: "my-anime-list", component: await import("./MyAnime/Index.svelte") },
    { tagname: "latest-episodes", component: await import("./LatestEpisodes/Index.svelte") },
    { tagname: "bottom-navigation", component: await import("./BottomNavigation/Index.svelte") },
    // Modals
    /* item */ {
        tagname: "search-modal",
        component: await import("./SearchModal/Index.svelte")
    },
    /* Trigger */ {
        tagname: "search-modal-trigger",
        component: await import("./SearchModal/Trigger.svelte")
    }
];

mapping.forEach((item) => {
    register({
        component: item.component.default,
        tagname: `coreproject-specific-${item.tagname}`
    });
});
