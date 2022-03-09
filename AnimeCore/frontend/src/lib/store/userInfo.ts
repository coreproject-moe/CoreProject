import { get, writable } from "svelte/store";

import { browser } from "$app/env";
import { userInfoUrl } from "$urls/restEndpoints";
import { userToken } from "./users";

export const userInfo = writable({
    first_name: "",
    last_name: "",
    email: "",
    date_joined: "",
    username: "",
    id: 0,
    last_login: "",
    avatar: ""
});

browser && // Is browser
    (async () => {
        const res = await fetch(userInfoUrl, {
            method: "GET",
            headers: new Headers({
                Accept: "application/json",
                "Content-Type": "application/json",
                Authorization: `Bearer ${get(userToken).access}`
            })
        });
        const data = await res.json();
        userInfo.set(data);
    })();
