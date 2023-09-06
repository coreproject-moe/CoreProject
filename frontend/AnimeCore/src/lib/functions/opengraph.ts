import { encode } from "html-entities";

type ISiteName = "CoreProject" | "AnimeCore" | "MangaCore";

type ILocale =
    | "af_ZA"
    | "af_NA"
    | "ak_GH"
    | "am_ET"
    | "ar_AR"
    | "as_IN"
    | "ay_BO"
    | "az_AZ"
    | "be_BY"
    | "bg_BG"
    | "bm_ML"
    | "bn_IN"
    | "bo_CN"
    | "bo_IN"
    | "br_FR"
    | "bs_BA"
    | "ca_ES"
    | "cgg_UG"
    | "chr_US"
    | "cs_CZ"
    | "cy_GB"
    | "da_DK"
    | "de_DE"
    | "de_AT"
    | "de_CH"
    | "de_LI"
    | "el_GR"
    | "en_US"
    | "en_GB"
    | "en_AU"
    | "en_CA"
    | "en_IN"
    | "en_SG"
    | "en_ZA"
    | "eo_EO"
    | "es_ES"
    | "es_LA"
    | "et_EE"
    | "eu_ES"
    | "fa_IR"
    | "ff_SN"
    | "fi_FI"
    | "fil_PH"
    | "fo_FO"
    | "fr_FR"
    | "fr_BE"
    | "fr_CA"
    | "fr_CH"
    | "fr_LU"
    | "fur_IT"
    | "ga_IE"
    | "gl_ES"
    | "gn_PY"
    | "gu_IN"
    | "gun_FR"
    | "ha_NG"
    | "he_IL"
    | "hi_IN"
    | "hr_HR"
    | "ht_HT"
    | "hu_HU"
    | "hy_AM"
    | "id_ID"
    | "ig_NG"
    | "ii_CN"
    | "is_IS"
    | "it_IT"
    | "it_CH"
    | "iu_CA"
    | "ja_JP"
    | "jv_ID"
    | "ka_GE"
    | "kk_KZ"
    | "km_KH"
    | "kn_IN"
    | "ko_KR"
    | "kok_IN"
    | "ks_IN"
    | "ku_TR"
    | "ky_KG"
    | "la_VA"
    | "lb_LU"
    | "lo_LA"
    | "lt_LT"
    | "lv_LV"
    | "mi_NZ"
    | "mk_MK"
    | "ml_IN"
    | "mn_MN"
    | "mo_RO"
    | "mr_IN"
    | "ms_MY"
    | "mt_MT"
    | "my_MM"
    | "nb_NO"
    | "nd_ZW"
    | "ne_NP"
    | "nl_NL"
    | "nl_BE"
    | "nn_NO"
    | "nso_ZA"
    | "oc_FR"
    | "om_ET"
    | "or_IN"
    | "pa_IN"
    | "pl_PL"
    | "ps_AF"
    | "pt_PT"
    | "pt_BR"
    | "qu_PE"
    | "rm_CH"
    | "ro_RO"
    | "ru_RU"
    | "rw_RW"
    | "sa_IN"
    | "se_NO"
    | "si_LK"
    | "sk_SK"
    | "sl_SI"
    | "sq_AL"
    | "sr_RS"
    | "sv_SE"
    | "sw_KE"
    | "syr_SY"
    | "ta_IN"
    | "te_IN"
    | "tg_TJ"
    | "th_TH"
    | "ti_ER"
    | "tk_TM"
    | "tl_PH"
    | "tn_ZA"
    | "tr_TR"
    | "ts_ZA"
    | "tt_RU"
    | "ug_CN"
    | "uk_UA"
    | "ur_PK"
    | "uz_UZ"
    | "vi_VN"
    | "wo_SN"
    | "xh_ZA"
    | "yo_NG"
    | "zh_CN"
    | "zh_HK"
    | "zh_MO"
    | "zh_SG"
    | "zh_TW"
    | "zu_ZA";

export class OpengraphGenerator {
    #title: string;
    #url: string;
    #description: string;
    #site_name: ISiteName;
    #locale: ILocale;
    #audio?: string;
    #image?: string;
    #video?: {
        url: string;
        type: string;
        title: string;
        description: string;
        secure_url: string;
        tag: string;
        duration?: string;
        release_date?: string;
        width?: number;
        height?: number;
    };
    #keywords?: string[];

    constructor({
        title,
        url,
        description,
        site_name,
        locale,
        audio,
        image_url,
        video,
        keywords
    }: {
        title: string;
        url: string;
        description: string;
        site_name: ISiteName;
        locale: ILocale;
        audio?: string;
        image_url?: string;
        video?: {
            url: string;
            type: string;
            title: string;
            description: string;
            secure_url: string;
            tag: string;
            duration?: string;
            release_date?: string;
            width?: number;
            height?: number;
        };
        keywords?: string[];
    }) {
        this.#title = encode(title);
        this.#url = url;
        this.#description = encode(description);
        this.#site_name = site_name;
        this.#locale = locale;

        if (audio) {
            this.#audio = audio;
        }
        if (image_url) {
            this.#image = image_url;
        }
        if (video) {
            this.#video = video;
        }
        if (keywords) {
            this.#keywords = keywords;
        }
    }

    private get title() {
        let title = `<title>${this.#title}</title>`;

        // Handle opengraph
        title += `<meta property="og:title" content="${this.#title}">`;
        // Handle Twitter
        title += `<meta name="twitter:title" content="${this.#title}" />`;

        return title;
    }
    private get url() {
        return `<meta property="og:url" content="${this.#url}">`;
    }
    private get description() {
        let description = `<meta name="description" content="${this.#description}">`;
        description += `<meta property="og:description" content="${this.#description}">`;
        description += `<meta name="twitter:description" content="${this.#description}" />`;

        return description;
    }
    private get site_name() {
        return `<meta property="og:site_name" content="${this.#site_name}">`;
    }
    private get locale() {
        return `<meta property="og:locale" content="${this.#locale}">`;
    }
    private get audio() {
        return `<meta property="og:audio" content="${this.#audio}">`;
    }
    private get image() {
        let image = "";

        image += `<meta property="og:image" content="${this.#image}">`;
        image += `<meta name="twitter:image" content="${this.#image}" />`;

        return image;
    }
    public get video() {
        let video_opengraph_text = "";
        if (this.#video?.url) {
            video_opengraph_text += `<meta property="og:video" content="${this.#video.url}">`;
        }
        if (this.#video?.title) {
            video_opengraph_text += `<meta property="og:video:title" content="${this.#video?.title}">`;
        }
        if (this.#video?.type) {
            video_opengraph_text += `<meta property="og:video:type" content="${this.#video.type}">`;
        }
        if (this.#video?.height) {
            video_opengraph_text += `<meta property="og:video:height" content="${this.#video.height}">`;
        }
        if (this.#video?.width) {
            video_opengraph_text += `<meta property="og:video:width" content="${this.#video.width}">`;
        }
        if (this.#video?.description) {
            video_opengraph_text += `<meta property="og:video:description" content="${this.#video.description}">`;
        }
        if (this.#video?.secure_url) {
            video_opengraph_text += `<meta property="og:video:secure_url" content="${this.#video.secure_url}">`;
        }
        if (this.#video?.tag) {
            video_opengraph_text += `<meta property="og:video:tag" content="Video Tag">`;
        }
        if (this.#video?.duration) {
            video_opengraph_text += `<meta property="og:video:duration" content="${this.#video.duration}">`;
        }
        if (this.#video?.release_date) {
            video_opengraph_text += `<meta property="og:video:release_date" content="${this.#video.release_date}">`;
        }

        return video_opengraph_text;
    }

    private get keywords() {
        return `<meta name="keywords" content="${this.#keywords?.join(", ")}"/>`;
    }

    public generate_opengraph() {
        let opengraph_html = `<meta property="og:type" content="website">`;
        opengraph_html += this.site_name;
        opengraph_html += this.locale;
        opengraph_html += this.title;
        opengraph_html += this.url;
        opengraph_html += this.description;

        if (this.#audio) {
            opengraph_html += this.audio;
        }
        if (this.#image) {
            opengraph_html += this.image;
            opengraph_html += `<meta name="twitter:card" content="summary_large_image" />`;
        }
        if (this.#video) {
            opengraph_html += this.video;
        }
        if (this.#keywords) {
            opengraph_html += this.keywords;
        }

        return opengraph_html;
    }
}
