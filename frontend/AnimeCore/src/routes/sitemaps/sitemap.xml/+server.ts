import { NUMBER_OF_ENTRIES_IN_A_SINGLE_SITEMAP_XML } from "$data/constraints";
import { UrlMaps } from "$data/urls";

export async function GET({ url }) {
    const backend_mapping = new UrlMaps();

    const anime_res = await fetch(backend_mapping?.anime_feed());
    const anime_json: {
        data: number[];
    } = await anime_res.json();

    const anime_data = anime_json["data"].sort((a, b) => a - b);
    const last_element = Number(anime_data[anime_data.length - 1]);

    const xml = `
    <?xml version="1.0" encoding="UTF-8"?>
    <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        ${Array(Math.ceil(last_element / NUMBER_OF_ENTRIES_IN_A_SINGLE_SITEMAP_XML))
            .fill(0)
            .map((_, index) => {
                return `
                <sitemap>
                    <loc>https://${url.host}/sitemaps/anime/${index + 1}.xml</loc>
                </sitemap>`.trim();
            })}
    </sitemapindex>
    `.trim();

    return new Response(xml, {
        headers: {
            "content-type": "text/xml"
        }
    });
}
