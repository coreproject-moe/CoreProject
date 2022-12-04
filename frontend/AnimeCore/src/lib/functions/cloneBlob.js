export const cloneBlob = (b) =>
    new Promise((resolve, reject) => {
        const r = new FileReader();
        r.readAsArrayBuffer(b);

        r.addEventListener("load", (_) => {
            resolve(new Blob([r.result], { type: b.type }));
        });

        r.addEventListener("error", (_) => {
            reject();
        });
    });
