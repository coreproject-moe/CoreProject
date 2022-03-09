import { userToken } from "src/store/usersers";
import { tokenBlacklistUrl } from "$urls/restEndpoints";
import { get } from "svelte/store";

async function logoutUser() {
    const res = await fetch(tokenBlacklistUrl, {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            refresh: get(userToken).refresh
        })
    });
    if (res?.ok) {
        return {
            props: {
                logoutState: true
            }
        };
    }
}
