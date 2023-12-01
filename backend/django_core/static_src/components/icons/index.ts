import type { ComponentType } from "svelte";

// @ts-ignore
import svelteRetag from "svelte-retag";

import AnimeCore from "./AnimeCore/index.svelte";
import ArrowUpRight from "./ArrowUpRight/Index.svelte";
import Bold from "./Bold/Index.svelte";
import Book from "./Book/Index.svelte";
import Calender from "./Calender/Index.svelte";
import Chat from "./Chat/Index.svelte";
import Chevron from "./Chevron/Index.svelte";
import Compass from "./Compass/Index.svelte";
import CoreText from "./CoreText/Index.svelte";
import CoreProjectText from "./CoreProjectText/Index.svelte";
import CoreProject from "./CoreProject/Index.svelte";
import Cross from "./Cross/Index.svelte";
import Circle from "./Circle/Index.svelte";
import Code from "./Code/Index.svelte";
import Delete from "./Delete/Index.svelte";
import DoubleArrow from "./DoubleArrow/Index.svelte";
import Download from "./Download/Index.svelte";
import Dot from "./Dot/Index.svelte";
import Edit from "./Edit/Index.svelte";
import Empty from "./Empty/Index.svelte";
import Filter from "./Filter/Index.svelte";
import Headphone from "./Headphone/Index.svelte";
import Home from "./Home/Index.svelte";
import Hyperlink from "./Hyperlink/Index.svelte";
import Info from "./Info/Index.svelte";
import Italic from "./Italic/Index.svelte";
import Language from "./Language/Index.svelte";
import Like from "./Like/Index.svelte";
import List from "./List/Index.svelte";
import Misc from "./Misc/Index.svelte";
import Moon from "./Moon/Index.svelte";
import Notification from "./Notification/Index.svelte";
import Play from "./Play/Index.svelte";
import Preference from "./Preference/Index.svelte";
import Recent from "./Recent/Index.svelte";
import Record from "./Record/Index.svelte";
import Refresh from "./Refresh/Index.svelte";
import Star from "./Star/Index.svelte";
import Strike from "./Strike/Index.svelte";
import Tick from "./Tick/Index.svelte";
import TrendingArrow from "./TrendingArrow/Index.svelte";
import Settings from "./Settings/Index.svelte";
import Share from "./Share/Index.svelte";
import Underline from "./Underline/Index.svelte";
import Upload from "./Upload/Index.svelte";

const icon_map = {
    "arrow-up-right": ArrowUpRight,
    animecore: AnimeCore,
    bold: Bold,
    book: Book,
    calender: Calender,
    chat: Chat,
    chevron: Chevron,
    circle: Circle,
    code: Code,
    compass: Compass,
    "core-text": CoreText,
    cross: Cross,
    "coreproject-text": CoreProjectText,
    coreproject: CoreProject,
    delete: Delete,
    "double-arrow": DoubleArrow,
    download: Download,
    dot: Dot,
    edit: Edit,
    empty: Empty,
    filter: Filter,
    headphone: Headphone,
    home: Home,
    hyperlink: Hyperlink,
    info: Info,
    italic: Italic,
    language: Language,
    like: Like,
    list: List,
    misc: Misc,
    moon: Moon,
    notification: Notification,
    play: Play,
    preference: Preference,
    recent: Recent,
    record: Record,
    refresh: Refresh,
    star: Star,
    share: Share,
    settings: Settings,
    strike: Strike,
    tick: Tick,
    "trending-arrow": TrendingArrow,
    underline: Underline,
    upload: Upload
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
