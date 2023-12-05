export type Comment = {
    user: {
        username: string;
        first_name: string;
        last_name: string;
        avatar: null | string;
        avatar_url: string;
    };
    text: string;
    path: string;
    created_at: string;
    children: number;
    child: Comment[];
};
