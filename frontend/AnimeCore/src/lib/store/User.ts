import Cookies from "js-cookie";
import { readable, writable } from "svelte/store";

import { browser } from "$app/environment";

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

export const user_token = readable<string | undefined>(undefined, function start(set) {
    if (!browser) {
        return;
    }

    const token = Cookies.get("token");
    if (token !== undefined) {
        set(token);
    }
});
