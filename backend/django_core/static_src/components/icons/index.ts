// @ts-ignore
import svelteRetag from "svelte-retag";

const mapping = [
    { tagname: `arrow`, component: await import("./Arrow/Index.svelte") },
    { tagname: `arrow-up-right`, component: await import("./ArrowUpRight/Index.svelte") },
    { tagname: `animecore`, component: await import("./AnimeCore/index.svelte") },
    { tagname: `bold`, component: await import("./Bold/Index.svelte") },
    { tagname: `book`, component: await import("./Book/Index.svelte") },
    { tagname: `calender`, component: await import("./Calender/Index.svelte") },
    { tagname: `chat`, component: await import("./Chat/Index.svelte") },
    { tagname: `chevron`, component: await import("./Chevron/Index.svelte") },
    { tagname: `circle`, component: await import("./Circle/Index.svelte") },
    { tagname: `code`, component: await import("./Code/Index.svelte") },
    { tagname: `compass`, component: await import("./Compass/Index.svelte") },
    { tagname: `core-text`, component: await import("./CoreText/Index.svelte") },
    { tagname: `cross`, component: await import("./Cross/Index.svelte") },
    { tagname: `coreproject-text`, component: await import("./CoreProjectText/Index.svelte") },
    { tagname: `coreproject`, component: await import("./CoreProject/Index.svelte") },
    { tagname: `delete`, component: await import("./Delete/Index.svelte") },
    { tagname: `double-arrow`, component: await import("./DoubleArrow/Index.svelte") },
    { tagname: `download`, component: await import("./Download/Index.svelte") },
    { tagname: `dot`, component: await import("./Dot/Index.svelte") },
    { tagname: `edit`, component: await import("./Edit/Index.svelte") },
    { tagname: `empty`, component: await import("./Empty/Index.svelte") },
    { tagname: `filter`, component: await import("./Filter/Index.svelte") },
    { tagname: `headphone`, component: await import("./Headphone/Index.svelte") },
    { tagname: `home`, component: await import("./Home/Index.svelte") },
    { tagname: `hyperlink`, component: await import("./Hyperlink/Index.svelte") },
    { tagname: `info`, component: await import("./Info/Index.svelte") },
    { tagname: `italic`, component: await import("./Italic/Index.svelte") },
    { tagname: `language`, component: await import("./Language/Index.svelte") },
    { tagname: `like`, component: await import("./Like/Index.svelte") },
    { tagname: `list`, component: await import("./List/Index.svelte") },
    { tagname: `misc`, component: await import("./Misc/Index.svelte") },
    { tagname: `moon`, component: await import("./Moon/Index.svelte") },
    { tagname: `notification`, component: await import("./Notification/Index.svelte") },
    { tagname: `play`, component: await import("./Play/Index.svelte") },
    { tagname: `preference`, component: await import("./Preference/Index.svelte") },
    { tagname: `recent`, component: await import("./Recent/Index.svelte") },
    { tagname: `record`, component: await import("./Record/Index.svelte") },
    { tagname: `refresh`, component: await import("./Refresh/Index.svelte") },
    { tagname: `search`, component: await import("./Star/Index.svelte") },
    { tagname: `star`, component: await import("./Star/Index.svelte") },
    { tagname: `share`, component: await import("./Share/Index.svelte") },
    { tagname: `settings`, component: await import("./Settings/Index.svelte") },
    { tagname: `strike`, component: await import("./Strike/Index.svelte") },
    { tagname: `tick`, component: await import("./Tick/Index.svelte") },
    { tagname: `trending-arrow`, component: await import("./TrendingArrow/Index.svelte") },
    { tagname: `underline`, component: await import("./Underline/Index.svelte") },
    { tagname: `upload`, component: await import("./Upload/Index.svelte") },
    { tagname: `user`, component: await import("./User/Index.svelte") }
];

// Register Icons
mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-icon-${item.tagname}`.toLowerCase(),
        attributes: true,
        shadow: false,
        hydratable: false
    });
});
