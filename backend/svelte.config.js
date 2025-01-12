import preprocess from "svelte-preprocess";

const config = {
    compilerOptions: {
        enableSourcemap: true
    },
    preprocess: preprocess({
        sourceMap: true
    })
};

export default config;
