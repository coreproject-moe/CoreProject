import { get } from "svelte/store";

import { page } from "$app/stores";

export class MAL {
    private BASE_URL = `https://api.jikan.moe/v4/anime`;

    public id = (id: number | string) => {
        return `${this.BASE_URL}/${id}/full`;
    };

    public pictures = (id: number | string) => {
        return `${this.BASE_URL}/${id}/pictures`;
    };
}

export class Anilist {
    private BASE_URL = ``;

    public id = () => {
        return;
    };
}

export class UrlMaps {
    public DOMAIN = "https://backend.coreproject.moe";
    private BASE_URL = this.DOMAIN + "/api/v1";

    public anime = () => {
        return `${this.BASE_URL}/anime`;
    };

    public id = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}`;
    };

    public mal_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?mal_id=${id}`;
    };

    public kitsu_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?kitsu_id=${id}`;
    };

    public anilist_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?anilist_id=${id}`;
    };

    public genre = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}/genres`;
    };

    public episode = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}/episodes`;
    };

    public episode_number = (anime_id: number | string, episode_number: number | string) => {
        return `${this.BASE_URL}/anime/${anime_id}/episodes/${episode_number}`;
    };

    public get media_url() {
        // return process.env.NODE_ENV === "development" ? get(page).url.origin : "/media";
        return get(page).url.origin;
    }

    public get signup_url() {
        return `${this.BASE_URL}/user/sign_up`;
    }

    public get login_url() {
        return `${this.BASE_URL}/user/login`;
    }

    public get username_validity_endpoint() {
        return `${this.BASE_URL}/user/username_validity`;
    }
}
