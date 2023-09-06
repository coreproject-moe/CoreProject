import { JSONToTree } from "$functions/json_to_tree";

import { expect, test } from "vitest";

test("format date function", () => {
    const tree = new JSONToTree([
        {
            user: 1,
            text: "fasd",
            path: "fsad.test.fa"
        },
        {
            user: 1,
            text: "fdsafdsa",
            path: "fsad.test.fa.0000"
        },
        {
            user: 1,
            text: "fdsafdsa",
            path: "fsad.test.fa.0001"
        },
        {
            user: 1,
            text: "hea",
            path: "fsad.test.fa1.0000"
        }
    ]).to_tree();

    expect(tree).toStrictEqual({
        fsad: {
            test: {
                fa: {
                    user: 1,
                    text: "fasd",
                    path: "fsad.test.fa",
                    "0000": {
                        user: 1,
                        text: "fdsafdsa",
                        path: "fsad.test.fa.0000"
                    },
                    "0001": {
                        user: 1,
                        text: "fdsafdsa",
                        path: "fsad.test.fa.0001"
                    }
                },

                fa1: {
                    "0000": {
                        user: 1,
                        text: "hea",
                        path: "fsad.test.fa1.0000"
                    }
                }
            }
        }
    });
});
