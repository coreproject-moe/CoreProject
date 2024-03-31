export type Comment = {
    pk: number;
    user: {
        username: string;
        first_name: string;
        last_name: string;
        avatar: null | string;
        avatar_url: string;
    } | null;
    ratio: number;
    text: string;
    path: string;
    created_at: string;
    childrens: number;
    user_reaction: "upvoted" | "downvoted" | null;
    child: Comment[];
    deleted: boolean;
    collapse: boolean;
    depth: number;
};

export interface CommentResponse {
    detail?: string;
    count: number;
    next: null | string;
    previous: null | string;
    results: Comment[];
}