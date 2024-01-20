import { writable } from "@macfja/svelte-persistent-store";

// `url` regex pattern to clear `commentbox_value`
const whitelisted_regexs = [/^\/anime\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+/gm];

export const commentbox_value = writable<string>("commentbox", "");

export function clear_commentbox_if_needed() {
    const matches_string = whitelisted_regexs.some((regex) => {
        return regex.test(window.location.pathname);
    });

    if (!matches_string) {
        commentbox_value.set("");
    }
}
clear_commentbox_if_needed();
