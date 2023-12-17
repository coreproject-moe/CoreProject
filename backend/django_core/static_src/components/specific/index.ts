// @ts-ignore
import svelteRetag from "svelte-retag";

// Specific Components
const mapping = [
  { tagname: "specific-commentbox", component: await import("./CommentBox/Index.svelte") },
  { tagname: "specific-my-anime-list", component: await import("./MyAnime/Index.svelte") },
  { tagname: "specific-latest-episodes", component: await import("./LatestEpisodes/Index.svelte") },
    // Modals
    /* item */ {
    tagname: "specific-search-modal",
    component: await import("./SearchModal/Index.svelte")
  },
    /* Trigger */ {
    tagname: "specific-search-modal-trigger",
    component: await import("./SearchModal/Trigger.svelte")
  }
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
