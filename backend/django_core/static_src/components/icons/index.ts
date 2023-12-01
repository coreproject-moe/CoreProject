// @ts-ignore
import svelteRetag from "svelte-retag";

import Bold from "./Bold/Index.svelte";
import Circle from "./Circle/Index.svelte";
import Code from "./Code/Index.svelte";
import Dot from "./Dot/Index.svelte";
import Hyperlink from "./Hyperlink/Index.svelte";
import Info from "./Info/Index.svelte";
import Italic from "./Italic/Index.svelte";
import Play from "./Play/Index.svelte";
import Star from "./Star/Index.svelte";
import Strike from "./Strike/Index.svelte";
import Underline from "./Underline/Index.svelte";

const icon_array = [Bold, Circle, Code, Dot, Hyperlink, Info, Italic, Play, Star, Strike, Underline];

// Register Icons
icon_array.forEach((item) => {
    svelteRetag({
        component: item,
        tagname: `coreproject-icon-${String(item)}`,
        attributes: ["class", "style"],
        shadow: false,
        hydratable: true
    });
});
