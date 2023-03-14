import { UrlMaps } from "$data/urls";

export async function GET() {
    const backend_mapping = new UrlMaps();
    const res = await fetch(backend_mapping.anime());
    const data = await res.json();

    const total = data["count"];
    console.log(total);
    const BASE_URL = "https://coreproject.moe";

    return new Response(
        `
        <?xml version="1.0" encoding="UTF-8" ?>
            <urlset
                xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xhtml="https://www.w3.org/1999/xhtml"
                xmlns:mobile="https://www.google.com/schemas/sitemap-mobile/1.0"
                xmlns:news="https://www.google.com/schemas/sitemap-news/0.9"
                xmlns:image="https://www.google.com/schemas/sitemap-image/1.1"
                xmlns:video="https://www.google.com/schemas/sitemap-video/1.1"
            >
            ${Array(total)
                .fill(0)
                .map((_, index) => {
                    return `
                    <url>
                        <loc>${BASE_URL + "/backend/" + (index + 1)}
                    </loc>
                </url>`;
                })}
            </urlset>`.trim(),
        {
            headers: {
                "Content-Type": "application/xml"
            }
        }
    );
}
