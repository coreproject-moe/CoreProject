import { browser } from "$app/env";
import { userToken } from "$store/users";
import { tokenBlacklistUrl } from "$urls/restEndpoints";
import { get } from "svelte/store";

export const logoutUser = async (href: string = "/user/login") => {
    try {
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
            userToken.set({ refresh: "", access: "" });
            browser && localStorage.removeItem("tokens");
            window.location.href = href;
        }
    } catch (err) {
        if (err instanceof Error) {
            console.error(`Cannot POST to ${tokenBlacklistUrl} | Reason : ${err}`);
        }
    }
};
