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

        // Create a dictionary to quickly access nodes by their path
        const nodeDictionary: { [path: string]: Comment } = {};

        // First pass: Create nodes and populate the dictionary
        data.forEach((node: Comment) => {
            const newNode: Comment = { ...node, child: [] };
            nodeDictionary[node.path] = newNode;

            // If the node is a root-level node, add it to the tree
            if (!node.path.includes(".")) {
                tree.push(newNode);
            }
        });

        // Second pass: Connect child nodes to their parent nodes
        data.forEach((node: Comment) => {
            const path_segments = node.path.split(".");
            const parentPath = path_segments.slice(0, -1).join(".");
            const parentNode = nodeDictionary[parentPath];

            if (parentNode) {
                parentNode.child.push(nodeDictionary[node.path]);
            }
        });
        return tree;
    }

    public build() {
        return this.#json;
    }
}
