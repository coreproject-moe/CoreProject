import { browser } from "$app/env";
import { get, writable } from "svelte/store";
import { jwtRefresh } from "$lib/constants/backend/jwt/refresh";
import { tokenRefreshUrl, userInfoUrl } from "$urls/restEndpoints";

export const userToken = writable(
    browser && JSON.parse(localStorage.getItem("tokens") ?? '{ "refresh": "", "access": "" }')
);

export const isUserAuthenticated = writable(get(userToken).access);

// Monitor changes and set it to localStorage
userToken.subscribe((change: { access: string; refresh: string }) => {
    browser && localStorage.setItem("tokens", JSON.stringify(change));
});

// Custom function to refresh tokens
browser && // Is browser
    get(isUserAuthenticated) && // User is authenticated
    localStorage.getItem("tokens") && // Item exists
    setInterval(async () => {
        const res = await fetch(tokenRefreshUrl, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                refresh: get(userToken).refresh
            })
        });
        const data = await res.json();
        userToken.set({ refresh: get(userToken).refresh, access: data?.access });
    }, jwtRefresh);

    
// User Info Store
export const userInfo = writable(
    {
        id: 0,
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        user_permission: [],
        date_joined: "",
        last_login: "",
        is_superuser: false,
        is_staff: false,
        avatar: ""
    },
    function start(set) {
        // Async Callback to fetch data
        (async (__set) => {
            if (get(isUserAuthenticated)) {
                try {
                    const res = await fetch(userInfoUrl, {
                        method: "GET",
                        headers: new Headers({
                            Accept: "application/json",
                            "Content-Type": "application/json",
                            Authorization: `Bearer ${get(userToken).access}`
                        })
                    });
                    const data = await res.json();
                    __set(data);
                } catch (e) {
                    if (e instanceof Error) {
                        console.log(`Cannot get user data | Reason : ${e?.message}`);
                        browser && localStorage.removeItem("tokens"); // Clear the database
                    }
                }
            }
        })(set);
    }
);
