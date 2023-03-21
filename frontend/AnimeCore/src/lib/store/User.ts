import Cookies from "js-cookie";
import { writable } from "svelte/store";

import { browser } from "$app/environment";
import { UrlMaps } from "$data/urls";

export const user_is_logged_in = writable<boolean | undefined>(undefined, function start(set) {
    if (!browser) {
        return;
    }

    if (Cookies.get("token")) {
        set(true);
    } else {
        set(false);
    }
});

user_is_logged_in.subscribe((value) => {
    if (value) {
        (async () => {
            const token = Cookies.get("token");
            const backend_mapping = new UrlMaps();
            const res = await fetch(backend_mapping.user_info(), {
                headers: { Authorization: `Bearer ${token}` }
            });

            if (res.ok) {
                const data: {
                    id: number;
                    last_login: string;
                    is_superuser: boolean;
                    username: string;
                    first_name: string;
                    last_name: string;
                    email: string;
                    is_staff: boolean;
                    is_active: boolean;
                    discriminator: number;
                    avatar_provider: string;
                    date_joined: string;
                    groups: number[];
                    user_permissions: number[];
                    avatar: string;
                } = await res.json(); // dont call await here
                user_information.set(data);
            } else {
                console.error(`Cannot Fetch to backend user endpoint | Reason ${res.text}`);
            }
        })();
    }
});

export const user_information = writable<
    | {
          id: number;
          last_login: string;
          is_superuser: boolean;
          username: string;
          first_name: string;
          last_name: string;
          email: string;
          is_staff: boolean;
          is_active: boolean;
          discriminator: number;
          avatar_provider: string;
          date_joined: string;
          groups: number[];
          user_permissions: number[];
          avatar: string;
      }
    | undefined
>(undefined);
