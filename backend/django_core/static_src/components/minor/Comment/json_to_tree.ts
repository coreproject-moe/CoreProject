import type { Comment } from "$types/comment";
import * as _ from "lodash-es";

export class JSONToTree {
    #json: Comment[] = new Array<Comment>();
    #root_path: string | undefined | null = null;

    constructor({ json, old_json, root_path }: { json: Comment[]; old_json?: Comment[]; root_path?: string }) {
        this.#root_path = root_path;

        if (old_json) {
            // DO NOT DEEP MERGE
            const new_arr = this.convert_to_tree_given_path(json);
            this.#json = _.merge(old_json, new_arr);
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
            const new_node: Comment = {
                ...node,
                child: [],
                depth: node.path.split(".").length,
                collapse: (node.depth > 1 && node.ratio < 0) || node.ratio < 0 && this.#root_path !== node.path,
            };
            node_dictionary[node.path] = new_node;

            // If the node is a root-level node, add it to the tree
            if (!node.path.includes(".") || node.path === this.#root_path) {
                tree.push(new_node);
            };
        });

        console.log("tree", tree);

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
