import { Action } from "svelte/action";
import { goto } from "$functions/urls";

export const enhance_anchor: Action<HTMLAnchorElement, { verb: "GET" | "POST" | "DELETE" | "PUT"; anchor?: HTMLElement; target: string }> = (node, { verb, anchor, target }) => {
    const handle_click = (event: Event) => {
        event.preventDefault();

        const href = node.getAttribute("href") ?? "";

        if (verb === "GET") {
            goto({ target: target, url: href, verb: verb, anchor: anchor });
        }
    };

    node.addEventListener("click", handle_click);

    return {
        destroy() {
            node.removeEventListener("click", handle_click);
        }
    };
};
