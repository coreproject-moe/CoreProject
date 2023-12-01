// @ts-ignore
import svelteRetag from "svelte-retag";

import CommentBox from "$components/specific/CommentBox/Index.svelte";
import MyAnime from "$components/specific/MyAnime/Index.svelte";

// Specific Components
svelteRetag({
    component: CommentBox,
    tagname: `coreproject-specific-commentbox`,
    attributes: [`submit_url`],
    shadow: false,
    hydratable: true
});
svelteRetag({
    component: MyAnime,
    tagname: `coreproject-specific-my-anime-list`,
    attributes: [`anime_name`, `anime_status`, `anime_image`, `anime_current_episodes`, `anime_total_episodes`, `dropdown_class`, `anime_description`, `anime_studio`, `anime_genres`],
    shadow: false,
    hydratable: true
});