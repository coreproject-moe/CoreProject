import { cloneBlob } from "$functions/cloneBlob";

export const deepCloneBlobUrl = async (blob_url: string) => {
    const urlToBlob = await fetch(blob_url).then((r) => r.blob());
    return URL.createObjectURL(await cloneBlob(urlToBlob));
};
