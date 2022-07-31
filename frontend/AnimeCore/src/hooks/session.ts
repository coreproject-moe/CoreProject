import type { GetSession } from "@sveltejs/kit";

export const getSession: GetSession = ({ request }) => {
    // Hack from : https://github.com/django/django/pull/15791#discussion_r906362318
    const csrftoken = new URLSearchParams(
        request?.headers.get("cookie")?.replaceAll("&", "%26").replaceAll("; ", "&")
    ).get("csrftoken");

    try {
        if (csrftoken) {
            return {
                authenticated: true
            };
        }
    } catch (error) {
        console.log(error);
    }

    // By default, the user is not authenticated
    return {
        authenticated: false
    };
};
