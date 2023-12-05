import set from "lodash/set";

type Comment = { user: string; text: string; path: string; created_at: string; children: number; child: Comment[] };

export class JSONToTree {
    #json: Comment[] = new Array<Comment>();

    constructor(json: object[]) {
        this.#json = this.convert_to_tree_given_path(json);
    }

    private convert_to_tree_given_path(data: Comment): Comment {
        const tree: Comment[] = [];

        data.forEach((node) => {
            const pathSegments = node.path.split(".");
            let currentNode = tree;

            pathSegments.forEach((segment, index) => {
                const existingNode = currentNode.find((n) => n.child === segment);

                if (existingNode) {
                    currentNode = existingNode.children;
                } else {
                    const newNode = { segment, children: [] };

                    if (index === pathSegments.length - 1) {
                        newNode.data = node;
                    }

                    currentNode.push(newNode);
                    currentNode = newNode.children;
                }
            });
        });

        return tree;
    }

    public to_tree() {
        return this.#json;
    }
}
