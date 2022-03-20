import { browser } from "$app/env";
import { captureVolumeEndpoint } from "$urls/restEndpoints";
import { get, writable } from "svelte/store";
import { isUserAuthenticated, userToken } from "./users";

export const vimeJSVolume = writable(null || 0, function start(set) {
    (async () => {
        if (get(isUserAuthenticated)) {
            try {
                const res = await fetch(captureVolumeEndpoint, {
                    method: "GET",
                    headers: new Headers({
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${get(userToken).access}`
                    })
                });
                const data = await res.json();
                set(data?.video_volume);
            } catch (err) {
                if (err instanceof Error) {
                    console.error(`Can't GET from backend |  Reason : ${err?.message}`);
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
    })();
});

// On change update the backend and localstorage.
vimeJSVolume.subscribe((change: number) => {
    // Localstorage update
    browser && localStorage.setItem("vimejs-volume", JSON.stringify(~~change));

    // Backend update
    if (get(isUserAuthenticated)) {
        try {
            fetch(captureVolumeEndpoint, {
                method: "POST",
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
            console.error(`POST to ${captureVolumeEndpoint} Failed`);
        }
    }
});
