import { browser } from "$app/env";
import { captureEndpoint } from "$urls/restEndpoints";
import { get, writable } from "svelte/store";
import { isUserAuthenticated, userToken } from "./users";

export const vimeJSVolume = writable(100, function start(set) {
    (async (__set) => {
        if (get(isUserAuthenticated)) {
            try {
                const res = await fetch(captureEndpoint, {
                    method: "GET",
                    headers: new Headers({
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${get(userToken).access}`
                    })
                });
                const data = await res.json();
                __set(data?.video_volume);
            } catch (err) {
                if (err instanceof Error) {
                    console.error(
                        `Can't fetch from backend | Flushing Tokens | Reason : ${err?.message}`
                    );
                }
            }
        } else {
            if (browser) {
                const volume = parseInt(
                    localStorage.getItem("vimejs-volume") ?? JSON.stringify(100)
                );
                set(volume);
            }
        }
    })(set);
});

// On change update the backend and localstorage.
vimeJSVolume.subscribe((change: number) => {
    // Localstorage update
    browser && localStorage.setItem("vimejs-volume", JSON.stringify(~~change));

    // Backend update
    if (get(isUserAuthenticated)) {
        try {
            fetch(captureEndpoint, {
                method: "PATCH",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${get(userToken).access}`
                },
                body: JSON.stringify({
                    video_volume: ~~change
                })
            });
        } catch {
            console.error(`POST to ${captureEndpoint} Failed`);
        }
    }
});
