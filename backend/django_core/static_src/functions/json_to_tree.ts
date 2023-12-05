import set from "lodash/set";

export class JSONToTree {
    #json = {};

    constructor(json: object[]) {
        json.forEach((item) => {
            this.convert_to_tree_given_path(item as unknown as { user: string; text: string; path: string });
        });
    }

    public convert_to_tree_given_path({ user, text, path }: { user: string; text: string; path: string }) {
        set(this.#json, path, { path, user, text });
    }

    public to_tree() {
        return this.#json;
    }
}