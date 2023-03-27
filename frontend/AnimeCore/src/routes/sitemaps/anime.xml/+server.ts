import { UrlMaps } from "$data/urls";

export async function GET({ url }) {
    const backend_mapping = new UrlMaps();
    const anime_res = await fetch(backend_mapping?.anime_feed());
    const anime_json: {
        data: number[];
    } = await anime_res.json();

    const anime_data = anime_json["data"];
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
}
