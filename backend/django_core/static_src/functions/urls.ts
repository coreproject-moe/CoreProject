import htmx from "htmx.org";

export function reverse(view: string, ...args: Array<string | number>) {
    const url = window.urls.get(view);
    if (!url) {
        throw new Error(`No Match found for ${view}`);
    }

    // Matches the following patterns
    // <str:pk> | <int:pk>
    const match_pattern = /\<(int|str):(\w+)>?/g;
    const matches = url?.match(match_pattern) ?? [];

    if (matches?.length === 0) {
        return url;
    } else if (matches?.length !== args.length) {
        throw new Error("`args` doesnot match with `urlpattern`");
    }

    const replacements: Record<string, string> = matches.reduce((obj, k, i) => ({ ...obj, [k]: args[i] }), {});

    // Create a regular expression pattern to match all occurrences of the keys in replacements
    const pattern = new RegExp(Object.keys(replacements).join("|"), "g");

    const final_url = url.replace(pattern, function (match: string) {
        return replacements[match];
    });

    return final_url;
}

export async function goto({ url, verb, target }: { url: string; verb?: "GET" | "POST"; target: string }): Promise<void> {
    // WHAT KIND OF FUCKERY IS THIS
    // FUCK HTMX
    // related : https://github.com/bigskysoftware/htmx/discussions/2116
    // related : https://www.reddit.com/r/htmx/comments/18np8pk/how_to_make_ajax_update_the_history_cache/
    const btn = document.createElement("button");
    btn.setAttribute(`hx-${verb?.toLowerCase()}`, url);
    btn.setAttribute("hx-push-url", url);
    btn.setAttribute("hx-target", target);
    // Hide Button
    btn.style.display = "hidden";
    // Add `htmx` listener
    htmx.process(btn);
    document.body.appendChild(btn);
    btn.click();
}
