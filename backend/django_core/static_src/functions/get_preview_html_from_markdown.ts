import { reverse } from "$functions/urls";

export async function get_preview_html_from_markdown(text: string) {
    const res = await fetch(reverse("partial_markdown_endpoint"), {
        method: "POST",
        credentials: "same-origin",
        body: text,
        headers: {
            "X-CSRFToken": window.csrfmiddlewaretoken
        }
    });
    const html = await res.text();

    // guard clause
    if (res.ok) {
        return html;
    } else {
        throw new Error(await res.text());
    }
}
