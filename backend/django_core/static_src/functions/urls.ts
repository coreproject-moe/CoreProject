const urls = window.urls;

export function reverse(view: string, ...args: Array<string | number>) {
    const url = urls.get(view);
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
