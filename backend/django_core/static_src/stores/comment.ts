import { writable } from "@macfja/svelte-persistent-store";

// `url` regex pattern to clear `commentbox_value`
const whitelisted_regexs = [/^anime\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+\/$/];

export const commentbox_value = writable<string>("commentbox", "");

export function clear_commentbox_if_needed() {
    const matches_string = whitelisted_regexs.some((regex) => regex.test(window.location.pathname));
    console.log(matches_string);
    if (!matches_string) {
        // commentbox_value.set("");
    }
}
