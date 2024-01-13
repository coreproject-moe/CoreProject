const apiUrl = "https://jo283m.video-delivery.net/upload/01";

export async function upload_file_to_doodstream({ api_key, file }: { api_key: string; file: File }) {
    const formData = new FormData();
    formData.append("api_key", api_key);
    formData.append("file", file);

    const res = await fetch(`${apiUrl}?api_key=${api_key}`, {
        method: "POST",
        body: formData
    });

    if (res.ok) {
        console.log(res.json());
    }
}
