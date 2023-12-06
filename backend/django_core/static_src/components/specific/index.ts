// @ts-ignore
import svelteRetag from "svelte-retag";

const mapping = [
    { tagname: "coreproject-specific-commentbox", component: await import("$components/specific/CommentBox/Index.svelte"), attributes: [`submit_url`] },
    { tagname: "coreproject-specific-my-anime-list", component: await import("$components/specific/MyAnime/Index.svelte"), attributes: [`anime_name`, `anime_status`, `anime_image`, `anime_current_episodes`, `anime_total_episodes`, `dropdown_class`, `anime_description`, `anime_studio`, `anime_genres`] }
];
// Specific Components
mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: item.tagname,
        attributes: item.attributes,
        shadow: false,
        hydratable: true
    });
});
