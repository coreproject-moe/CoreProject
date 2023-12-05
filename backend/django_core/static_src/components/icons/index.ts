import type { SvelteComponent } from "svelte";

// @ts-ignore
import svelteRetag from "svelte-retag";

const icon_map: Record<string, typeof SvelteComponent<{}>> = {
    arrow: (await import("./Arrow/Index.svelte")).default,
    "arrow-up-right": (await import("./ArrowUpRight/Index.svelte")).default,
    animecore: (await import("./AnimeCore/index.svelte")).default,
    bold: (await import("./Bold/Index.svelte")).default,
    book: (await import("./Book/Index.svelte")).default,
    calender: (await import("./Calender/Index.svelte")).default,
    chat: (await import("./Chat/Index.svelte")).default,
    chevron: (await import("./Chevron/Index.svelte")).default,
    circle: (await import("./Circle/Index.svelte")).default,
    code: (await import("./Code/Index.svelte")).default,
    compass: (await import("./Compass/Index.svelte")).default,
    "core-text": (await import("./CoreText/Index.svelte")).default,
    cross: (await import("./Cross/Index.svelte")).default,
    "coreproject-text": (await import("./CoreProjectText/Index.svelte")).default,
    coreproject: (await import("./CoreProject/Index.svelte")).default,
    delete: (await import("./Delete/Index.svelte")).default,
    "double-arrow": (await import("./DoubleArrow/Index.svelte")).default,
    download: (await import("./Download/Index.svelte")).default,
    dot: (await import("./Dot/Index.svelte")).default,
    edit: (await import("./Edit/Index.svelte")).default,
    empty: (await import("./Empty/Index.svelte")).default,
    filter: (await import("./Filter/Index.svelte")).default,
    headphone: (await import("./Headphone/Index.svelte")).default,
    home: (await import("./Home/Index.svelte")).default,
    hyperlink: (await import("./Hyperlink/Index.svelte")).default,
    info: (await import("./Info/Index.svelte")).default,
    italic: (await import("./Italic/Index.svelte")).default,
    language: (await import("./Language/Index.svelte")).default,
    like: (await import("./Like/Index.svelte")).default,
    list: (await import("./List/Index.svelte")).default,
    misc: (await import("./Misc/Index.svelte")).default,
    moon: (await import("./Moon/Index.svelte")).default,
    notification: (await import("./Notification/Index.svelte")).default,
    play: (await import("./Play/Index.svelte")).default,
    preference: (await import("./Preference/Index.svelte")).default,
    recent: (await import("./Recent/Index.svelte")).default,
    record: (await import("./Record/Index.svelte")).default,
    refresh: (await import("./Refresh/Index.svelte")).default,
    star: (await import("./Star/Index.svelte")).default,
    share: (await import("./Share/Index.svelte")).default,
    settings: (await import("./Settings/Index.svelte")).default,
    strike: (await import("./Strike/Index.svelte")).default,
    tick: (await import("./Tick/Index.svelte")).default,
    "trending-arrow": (await import("./TrendingArrow/Index.svelte")).default,
    underline: (await import("./Underline/Index.svelte")).default,
    upload: (await import("./Upload/Index.svelte")).default
};

// Register Icons
Object.entries(icon_map).forEach((item) => {
    svelteRetag({
        component: item[1],
        tagname: `coreproject-icon-${item[0]}`.toLowerCase(),
        attributes: ["class", "style"],
        shadow: false,
        hydratable: false
    });
});
