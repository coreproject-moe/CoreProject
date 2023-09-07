import pickBy from "lodash/pickBy";

export class UrlMaps {
    #domain: string;

    constructor({ domain }: { domain?: string }) {
        if (domain) {
            this.#domain = domain;
        } else {
            this.#domain = "https://backend.coreproject.moe";
        }
    }

    public get DOMAIN() {
        return this.#domain;
    }
    private BASE_URL = this.DOMAIN + "/api/v1";

    // Url Declaration
    public id = (id: number | string) => {
        return new URL(`${this.BASE_URL}/anime/${id}`);
    };

    public episode = (id: number | string) => {
        return new URL(`${this.BASE_URL}/anime/${id}/episodes`);
    };

    public episode_number = (anime_id: number | string, episode_number: number | string) => {
        return new URL(`${this.BASE_URL}/anime/${anime_id}/episodes/${episode_number}`);
    };

    public get media_url() {
        // return process.env.NODE_ENV === "development" ? get(page).url.origin : "/media";
        return "";
    }

    public user_info = () => {
        return new URL(`${this.BASE_URL}/user/`);
    };

    public signup = () => {
        return new URL(`${this.BASE_URL}/user/signup`);
    };

    public login = () => {
        return new URL(`${this.BASE_URL}/user/login`);
    };

    public username_validity = () => {
        return new URL(`${this.BASE_URL}/user/username_validity`);
    };

    // Searchable endpoints
    public anime = ({ mal_id, kitsu_id, anilist_id, name, genres, themes, studios, producers, characters, staffs }: { mal_id?: number; kitsu_id?: number; anilist_id?: number; name?: string; genres?: string; themes?: string; studios?: string; producers?: string; characters?: string; staffs?: string }) => {
        const url = new URL(`${this.BASE_URL}/anime`);
        const searchObject = pickBy({
            mal_id: mal_id ?? 0,
            kitsu_id: kitsu_id ?? 0,
            anilist_id: anilist_id ?? 0,
            name: name ?? "",
            genres: genres ?? "",
            themes: themes ?? "",
            studios: studios ?? "",
            producers: producers ?? "",
            characters: characters ?? "",
            staffs: staffs ?? ""
        });
        for (const key in searchObject) url.searchParams.append(key, searchObject[key] as string);
        return url;
    };

    public genre = ({ name, mal_id }: { name?: string; mal_id?: string }) => {
        const url = new URL(`${this.BASE_URL}/anime/genres`);
        const searchObject = pickBy({
            name: name ?? "",
            mal_id: mal_id ?? 0
        });
        for (const key in searchObject) url.searchParams.append(key, searchObject[key] as string);
        return url;
    };

    public theme = ({ name, mal_id }: { name?: string; mal_id?: string }) => {
        const url = new URL(`${this.BASE_URL}/anime/themes`);
        const searchObject = pickBy({
            name: name ?? "",
            mal_id: mal_id ?? 0
        });
        for (const key in searchObject) url.searchParams.append(key, searchObject[key] as string);
        return url;
    };

    // Feeds
    public anime_feed = () => {
        return new URL(`${this.DOMAIN}/feed/anime/`);
    };
    public character_feed = () => {
        return new URL(`${this.DOMAIN}/feed/character/`);
    };
    public staff_feed = () => {
        return new URL(`${this.DOMAIN}/feed/staff/`);
    };
    public producer_feed = () => {
        return new URL(`${this.DOMAIN}/feed/producer/`);
    };
}
