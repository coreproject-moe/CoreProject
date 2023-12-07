export type Comment = {
    pk: number;
    user: {
        username: string;
        first_name: string;
        last_name: string;
        avatar: null | string;
        avatar_url: string;
    };
    ratio: number;
    text: string;
    path: string;
    created_at: string;
    childrens: number;
    user_reaction: "upvoted" | "downvoted" | null;
    child: Comment[];
};
