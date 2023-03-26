import { UrlMaps } from "$data/urls";
export async function GET() {
    const backend_mapping = new UrlMaps();

    const xml = ``;

    return new Response(xml, {
        headers: {
            "content-type": "text/xml"
        }
    });
}
