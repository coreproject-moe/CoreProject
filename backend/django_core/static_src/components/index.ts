// @ts-ignore
import svelteRetag from "svelte-retag";

import CommentBox from "$components/specific/CommentBox.svelte";
import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
import MyAnime from "$components/specific/MyAnime.svelte";
import Comment from "$components/minor/Comment/Index.svelte";
import Markdown from "$components/minor/Markdown/Index.svelte";

svelteRetag({
    component: Markdown,
    tagname: `markdown`,
    attributes: [`markdown`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: ScrollArea,
    tagname: `scroll-area`,
    attributes: [`parent_class`, `offset_scrollbar`, `gradient_mask`, `class`], // Changes to these attributes will be reactively forwarded to your component
    shadow: false, // Use the light DOM
    hydratable: true
});
svelteRetag({
    component: Comment,
    tagname: `coreproject-comment`,
    attributes: [`api_url`],
    shadow: false, // Use the light DOM
    hydratable: true
});

// Specific Components
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
    attributes: [`anime_name`, `anime_status`, `anime_image`, `anime_current_episodes`, `anime_total_episodes`, `dropdown_class`, `anime_description`, `anime_studio`, `anime_genres`],
    shadow: false,
    hydratable: true
});
