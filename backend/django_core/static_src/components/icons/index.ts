// @ts-ignore
import svelteRetag from "svelte-retag";

const mapping = [
    { tagname: `arrow`, component: await import("./Arrow/Index.svelte"), attributes: ["class", "style", "variant"] },
    { tagname: `arrow-up-right`, component: await import("./ArrowUpRight/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `animecore`, component: await import("./AnimeCore/index.svelte"), attributes: ["class", "style"] },
    { tagname: `bold`, component: await import("./Bold/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `book`, component: await import("./Book/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `calender`, component: await import("./Calender/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `chat`, component: await import("./Chat/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `chevron`, component: await import("./Chevron/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `circle`, component: await import("./Circle/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `code`, component: await import("./Code/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `compass`, component: await import("./Compass/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `core-text`, component: await import("./CoreText/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `cross`, component: await import("./Cross/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `coreproject-text`, component: await import("./CoreProjectText/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `coreproject`, component: await import("./CoreProject/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `delete`, component: await import("./Delete/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `double-arrow`, component: await import("./DoubleArrow/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `download`, component: await import("./Download/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `dot`, component: await import("./Dot/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `edit`, component: await import("./Edit/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `empty`, component: await import("./Empty/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `filter`, component: await import("./Filter/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `headphone`, component: await import("./Headphone/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `home`, component: await import("./Home/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `hyperlink`, component: await import("./Hyperlink/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `info`, component: await import("./Info/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `italic`, component: await import("./Italic/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `language`, component: await import("./Language/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `like`, component: await import("./Like/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `list`, component: await import("./List/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `misc`, component: await import("./Misc/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `moon`, component: await import("./Moon/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `notification`, component: await import("./Notification/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `play`, component: await import("./Play/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `preference`, component: await import("./Preference/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `recent`, component: await import("./Recent/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `record`, component: await import("./Record/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `refresh`, component: await import("./Refresh/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `search`, component: await import("./Star/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `star`, component: await import("./Star/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `share`, component: await import("./Share/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `settings`, component: await import("./Settings/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `strike`, component: await import("./Strike/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `tick`, component: await import("./Tick/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `trending-arrow`, component: await import("./TrendingArrow/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `underline`, component: await import("./Underline/Index.svelte"), attributes: ["class", "style"] },
    { tagname: `upload`, component: await import("./Upload/Index.svelte"), attributes: ["class", "style"] }
];

// Register Icons
mapping.forEach((item) => {
    svelteRetag({
        component: item.component.default,
        tagname: `coreproject-icon-${item.tagname}`.toLowerCase(),
        attributes: item.attributes,
        shadow: false,
        hydratable: false
    });
});
