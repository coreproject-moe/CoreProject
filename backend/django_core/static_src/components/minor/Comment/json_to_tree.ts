import type { Comment } from "$types/comment";
import * as _ from "lodash-es";
export class JSONToTree {
    #json: Comment[] = new Array<Comment>();

    constructor({ json, old_json }: { json: Comment[]; old_json?: Comment[] }) {
        if (old_json) {
            // DO NOT DEEP MERGE
            const new_arr = this.convert_to_tree_given_path(json);
            this.#json = _.concat(old_json, new_arr);
        } else {
            this.#json = this.convert_to_tree_given_path(json);
        }
    }

    private convert_to_tree_given_path(data: Comment[]): Comment[] {
        const tree: Comment[] = [];

        // Create a dictionary to quickly access nodes by their path
        const node_dictionary: { [path: string]: Comment } = {};

        // First pass: Create nodes and populate the dictionary
        data.forEach((node: Comment) => {
            const new_node: Comment = { ...node, child: [] };
            node_dictionary[node.path] = new_node;

            // If the node is a root-level node, add it to the tree
            if (!node.path.includes(".")) {
                tree.push(new_node);
            }
        });

        // Second pass: Connect child nodes to their parent nodes
        data.forEach((node: Comment) => {
            const path_segments = node.path.split(".");
            const parent_path = path_segments.slice(0, -1).join(".");
            const parent_node = node_dictionary[parent_path];

            if (parent_node) {
                parent_node.child.push(node_dictionary[node.path]);
            }
        });
        return tree;
    }

    public build() {
        return this.#json;
    }
}
