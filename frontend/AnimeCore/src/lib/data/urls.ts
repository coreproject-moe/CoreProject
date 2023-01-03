import { get } from "svelte/store";

import { page } from "$app/stores";

export class MAL {
    private BASE_URL = `https://api.jikan.moe/v4/anime`;

    public id = (id: number | string) => {
        return `${this.BASE_URL}/${id}/full`;
    };
}

export class Kitsu {
    private BASE_URL = ``;

    public id = () => {
        return;
    };
}

export class Anilist {
    private BASE_URL = ``;

    public id = () => {
        return;
    };
}

export class UrlMaps {
    public get media_url() {
        return process.env.NODE_ENV === "development" ? get(page).url.origin : "/media";
    }
}
