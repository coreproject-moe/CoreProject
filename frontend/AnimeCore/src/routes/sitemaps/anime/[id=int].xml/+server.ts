import { error } from "@sveltejs/kit";

import { NUMBER_OF_ENTRIES_IN_A_SINGLE_SITEMAP_XML } from "$data/constraints";
import { UrlMaps } from "$data/urls";

export async function GET({ url, params }) {
    const backend_mapping = new UrlMaps();
    const anime_res = await fetch(backend_mapping?.anime_feed());
    const anime_json: {
        data: number[];
    } = await anime_res.json();

    const anime_data = anime_json["data"].sort((a, b) => a - b);

    const last_element = Number(anime_data[anime_data.length - 1]);
    const page_number = Number(params.id);

    if (
        !isNaN(last_element) &&
        !isNaN(page_number) &&
        // Formula for this
        // (n-1)*50_000 < last_element <= n*50_000
        (page_number - 1) * NUMBER_OF_ENTRIES_IN_A_SINGLE_SITEMAP_XML < last_element &&
        page_number * NUMBER_OF_ENTRIES_IN_A_SINGLE_SITEMAP_XML >= last_element
    ) {
        const xml = `
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
            ${anime_data
                .map((item) => {
                    return `
                        <url>
                            <loc>https://${url.host}/anime/backend/${item}</loc>
                        </url>
                    `;
                })
                .join("")
                .trim()}
        </urlset>
        `.trim();

        return new Response(xml, {
            headers: {
                "content-type": "text/xml"
            }
        });
    } else {
        throw error(404, {
            message: `No such entry exist`
        });
    }
}
