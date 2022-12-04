export const fetchImage = async (url: string) => {
    console.log(url);
    const response = await fetch(url, {
        method: "GET",
        // https://stackoverflow.com/questions/41030425/disabling-cors-using-js-fetch
        mode: "no-cors"
    });
    const blob = await response.blob();

    return URL.createObjectURL(blob);
};
