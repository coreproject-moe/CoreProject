import _ from "lodash-es";
import { reverse } from "$functions/urls";

let upload_url: null | string;

async function get_api_url(api_key: string) {
    const res = await fetch(reverse("doodstream-provider-endpoint"), {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ api_key: api_key })
    });

    if (!res.ok) {
        throw new Error(`Got error from Backend. Error: ${res.text}`);
    }
    const json = await res.json();
    const result = json["url"];

    if (_.isUndefined(result)) throw new Error("doodstream url is undefined");
    return result;
}

export async function upload_file_to_doodstream({ api_key, file }: { api_key: string; file: File }) {
    upload_url = await get_api_url(api_key);

    const formData = new FormData();
    formData.append("api_key", api_key);
    formData.append("file", file);

    const res = await fetch(`${upload_url}?api_key=${api_key}`, {
        method: "POST",
        body: formData
    });

    if (res.ok) {
        console.log(res.json());
    }
}
