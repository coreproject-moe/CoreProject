import type { ComponentType } from "svelte";

// @ts-ignore
import svelteRetag from "svelte-retag";

const icon_map = {
    "arrow-up-right": await import("./ArrowUpRight/Index.svelte"),
    animecore: await import("./AnimeCore/index.svelte"),
    bold: await import("./Bold/Index.svelte"),
    book: await import("./Book/Index.svelte"),
    calender: await import("./Calender/Index.svelte"),
    chat: await import("./Chat/Index.svelte"),
    chevron: await import("./Chevron/Index.svelte"),
    circle: await import("./Circle/Index.svelte"),
    code: await import("./Code/Index.svelte"),
    compass: await import("./Compass/Index.svelte"),
    "core-text": await import("./CoreText/Index.svelte"),
    cross: await import("./Cross/Index.svelte"),
    "coreproject-text": await import("./CoreProjectText/Index.svelte"),
    coreproject: await import("./CoreProject/Index.svelte"),
    delete: await import("./Delete/Index.svelte"),
    "double-arrow": await import("./DoubleArrow/Index.svelte"),
    download: await import("./Download/Index.svelte"),
    dot: await import("./Dot/Index.svelte"),
    edit: await import("./Edit/Index.svelte"),
    empty: await import("./Empty/Index.svelte"),
    filter: await import("./Filter/Index.svelte"),
    headphone: await import("./Headphone/Index.svelte"),
    home: await import("./Home/Index.svelte"),
    hyperlink: await import("./Hyperlink/Index.svelte"),
    info: await import("./Info/Index.svelte"),
    italic: await import("./Italic/Index.svelte"),
    language: await import("./Language/Index.svelte"),
    like: await import("./Like/Index.svelte"),
    list: await import("./List/Index.svelte"),
    misc: await import("./Misc/Index.svelte"),
    moon: await import("./Moon/Index.svelte"),
    notification: await import("./Notification/Index.svelte"),
    play: await import("./Play/Index.svelte"),
    preference: await import("./Preference/Index.svelte"),
    recent: await import("./Recent/Index.svelte"),
    record: await import("./Record/Index.svelte"),
    refresh: await import("./Refresh/Index.svelte"),
    star: await import("./Star/Index.svelte"),
    share: await import("./Share/Index.svelte"),
    settings: await import("./Settings/Index.svelte"),
    strike: await import("./Strike/Index.svelte"),
    tick: await import("./Tick/Index.svelte"),
    "trending-arrow": await import("./TrendingArrow/Index.svelte"),
    underline: await import("./Underline/Index.svelte"),
    upload: await import("./Upload/Index.svelte")
};

// Register Icons
Object.entries(icon_map).forEach((item) => {
    svelteRetag({
        component: item[1],
        tagname: `coreproject-icon-${item[0]}`.toLowerCase(),
        attributes: ["class", "style"],
        shadow: false,
        hydratable: true
    });
});
