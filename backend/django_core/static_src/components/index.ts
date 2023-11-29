// @ts-ignore
import svelteRetag from "svelte-retag";

import CommentBox from "$components/specific/CommentBox.svelte";
import ScrollArea from "$components/minor/ScrollArea.svelte";
import MyAnime from "$components/specific/MyAnime.svelte";

import "../css/tippy.scss";

svelteRetag({
    component: ScrollArea,
    tagname: `scroll-area`,
    attributes: [`parent_class`, `offset_scrollbar`, `gradient_mask`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: CommentBox,
    tagname: `coreproject-commentbox`,
    attributes: [`submit_url`],
    shadow: false,
    hydratable: true
});
svelteRetag({
    component: MyAnime,
    tagname: `coreproject-my-anime-list`,
    attributes: [`anime_name`, `anime_status`, `anime_image`, `anime_current_episodes`, `anime_total_episodes`, `dropdown_class`, `anime_description`],
    shadow: false,
    hydratable: true
});
