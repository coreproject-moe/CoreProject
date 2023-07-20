import xss from "xss";

export function sanitize(text: string) {
    return xss(text, {
        whiteList: {
            del: ["class"],
            p: ["class"],
            strong: ["class"],
            em: ["class"],
            b: ["class"],
            a: ["href", "class"],
            u: ["class"],
            i: ["class"],
            img: ["src", "alt"],
            code: ["class"],
            pre: ["class"],
            span: ["class"],
            h1: ["class"],
            h2: ["class"],
            h3: ["class"],
            h4: ["class"],
            h5: ["class"]
        }
    });
}
