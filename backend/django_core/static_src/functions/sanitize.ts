// Synced with : https://github.com/Ultimate-Hosts-Blacklist/whitelist/blob/e5a171243f9a418cc88d836c5eaf8a08198b0fb6/domains.list
const whitelisted_domain = [`https://www.google.com/`, "https://github.com", "https://reddit.com", `https://github.com`];

export async function sanitize(_text: string | undefined | Promise<string | undefined>): Promise<string> {
    const text = await _text;
    const xss = await import("xss");

    return xss.filterXSS(text ?? "", {
        whiteList: {
            blockquote: ["class"],
            del: ["class"],
            p: ["class"],
            strong: ["class"],
            em: ["class"],
            b: ["class"],
            a: ["href", "class"],
            u: ["class"],
            i: ["class"],
            img: ["src", "alt", "class"],
            code: ["class"],
            pre: ["class"],
            span: ["class"],
            h1: ["class"],
            h2: ["class"],
            h3: ["class"],
            h4: ["class"],
            h5: ["class"]
        },
        onTagAttr(tag, name, value, isWhiteAttr) {
            // Whitelist links
            if (tag === "a" && name === "href" && isWhiteAttr) {
                if (
                    whitelisted_domain.some((domain) => {
                        const check = domain.toLocaleLowerCase().includes(value.toLowerCase());
                        return !check;
                    })
                ) {
                    return "";
                }
            }
        }
    });
}
