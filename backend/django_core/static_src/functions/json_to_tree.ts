import set from "lodash/set";

export class JSONToTree {
    #json = {};

    constructor(json: object[]) {
        json.forEach((item) => {
            this.convert_to_tree_given_path(item as unknown as { user: string; text: string; path: string, created_at: string, children: number });
        });
    }

    public convert_to_tree_given_path({ user, text, path, created_at, children }: { user: string; text: string; path: string, created_at: string, children: number }) {
        set(this.#json, path, { path, user, text, created_at, children });
    }

    public to_tree() {
        return this.#json;
    }
}
