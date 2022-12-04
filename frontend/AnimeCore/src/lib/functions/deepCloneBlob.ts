export const deepCloneBlobUrl = async (blob_url: string) => {
    const urlToBlob = await fetch(blob_url).then((r) => r.blob());
    return URL.createObjectURL(new Blob([urlToBlob]));
};
