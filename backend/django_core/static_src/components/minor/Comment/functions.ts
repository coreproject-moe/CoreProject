import { FETCH_TIMEOUT } from "$constants/fetch";
import { get_csrf_token } from "$functions/get_csrf_token";
import { Comment } from "$types/comment";

export interface CommentResponse {
    detail?: string;
    count: number;
    next: null | string;
    previous: null | string;
    results: Comment[];
}

export const fetch_comments = async (url: string) => {
    const res = await fetch(url, {
        method: "GET",
        headers: {
            "X-CSRFToken": get_csrf_token()
        },
        signal: AbortSignal.timeout(FETCH_TIMEOUT)
    });
    const value = (await res.json()) as CommentResponse;

    switch (res.status) {
        case 200:
            return value;

        case 404:
            // No comment exists
            // Return empty array
            if (!value?.detail?.toLowerCase().includes("not found")) {
                throw new Error(`Data fetched from backend contains error`);
            }
            // return new Array<Comment>();
            value.results = new Array<Comment>();
            return value;

        default:
            throw new Error(await res.text());
    };
};