import type { Comment } from "../../../types/comment";

export class JSONToTree {
    #json: Comment[] = new Array<Comment>();

    constructor({ json, old_json }: { json: Comment[]; old_json?: Comment[] }) {
        if (old_json) {
            // DO NOT DEEP MERGE
            const new_arr = this.convert_to_tree_given_path(json);
            this.#json = old_json.concat(new_arr);
        } else {
            this.#json = this.convert_to_tree_given_path(json);
        }
    }

    private convert_to_tree_given_path(data: Comment[]): Comment[] {
        const tree: Comment[] = [];
        data.forEach((node: Comment) => {
            const path_segments = node.path.split(".");
            let current_node: Comment[] = tree;

            path_segments.forEach((segment, index) => {
                const existing_node = current_node.find((n) => n.path === segment);

                if (existing_node) {
                    current_node = existing_node.child;
                } else {
                    let new_node: any = { path: segment, child: [] };

                    if (index === path_segments.length - 1) {
                        // Copy values
                        const { child, path, ...rest } = node;
                        Object.assign(new_node, rest);
                    }

                    current_node.push(new_node);
                    current_node = new_node.child;
                }
            });
        });
        return tree;
    }

    public build() {
        return this.#json;
    }
}
