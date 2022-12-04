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
    private django = window?.django;

    private is_django_used_for_rendering() {
        if (this.django.DEBUG == `{{ debug|yesno:'true,false' }}`) {
            return false;
        } else if (this.django.DEBUG == "true" || this.django.DEBUG == "false") {
            return true;
        } else {
            return null;
        }
    }

    public get media_url() {
        return process.env.NODE_ENV === "development" && !this.is_django_used_for_rendering()
            ? get(page).url.origin
            : this.django.MEDIA_URL;
    }
}
