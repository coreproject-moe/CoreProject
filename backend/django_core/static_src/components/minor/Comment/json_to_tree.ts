import type { Comment } from "$types/comment";
import * as _ from "lodash-es";

export class JSONToTree {
    #json: Comment[] = new Array<Comment>();

    constructor({ json, old_json, specific_path }:
        { json: Comment[]; old_json?: Comment[], specific_path?: string }
    ) {
        if (old_json && specific_path) {
            // DO NOT DEEP MERGE
            const new_arr = this.convert_to_tree_given_path(json, specific_path);
            this.#json = this.merge_tree_branches(new_arr, old_json);
        } else {
            this.#json = this.convert_to_tree_given_path(json, specific_path);
        };
    };

    private merge_tree_branches(new_branch: Comment[], old_branch: Comment[]) {
        function merge(branch: Comment, target: Comment[]) {
            const path = branch.path;
            const existing_branch_idx = target.findIndex((t) => t.path === path);
            // if branch found, then modify its reference arr
            if (existing_branch_idx !== -1) {
                target[existing_branch_idx] = branch;
                return;
            };

            // chcek for children
            for (let i = 0; i < target.length; i++) {
                const child_branch = target[i];
                if (child_branch.child && child_branch.child.length > 0) {
                    merge(branch, child_branch.child);
                };
            };
        };

        new_branch.forEach((branch) => {
            merge(branch, old_branch);
        });

        return old_branch;
    };

    private convert_to_tree_given_path(data: Comment[], specific_path?: string): Comment[] {
        const tree: Comment[] = [];

        // Create a dictionary to quickly access nodes by their path
        const node_dictionary: { [path: string]: Comment } = {};

        // First pass: Create nodes and populate the dictionary
        data.forEach((node: Comment) => {
            const new_node: Comment = {
                ...node,
                child: [],
                depth: node.path.split(".").length,
                collapse: node.depth > 1 && node.ratio < 0 || node.ratio < 0 && specific_path !== node.path,
            };
            node_dictionary[node.path] = new_node;

            // If the node is a root-level node or specific node, add it to the tree
            if (specific_path && specific_path === node.path || !node.path.includes(".")) {
                tree.push(new_node);
            };
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
    };

    public build() {
        return this.#json;
    };
};
