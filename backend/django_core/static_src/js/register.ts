const zxcvbnTscore = await import('@zxcvbn-ts/core');
// Language import
const zxcvbnCommonPackage = await import('@zxcvbn-ts/language-common');
const zxcvbnEnPackage = await import('@zxcvbn-ts/language-en');
const options = {
    translations: zxcvbnEnPackage.translations,
    graphs: zxcvbnCommonPackage.adjacencyGraphs,
    dictionary: {
        ...zxcvbnCommonPackage.dictionary,
        ...zxcvbnEnPackage.dictionary,
        ...(await import('@zxcvbn-ts/language-fr')).dictionary,
        ...(await import('@zxcvbn-ts/language-de')).dictionary,
        ...(await import('@zxcvbn-ts/language-it')).dictionary,
        ...(await import('@zxcvbn-ts/language-nl-be')).dictionary,
        ...(await import('@zxcvbn-ts/language-es-es')).dictionary,
        ...(await import('@zxcvbn-ts/language-pt-br')).dictionary,
        ...(await import('@zxcvbn-ts/language-ja')).dictionary,
        ...(await import('@zxcvbn-ts/language-fi')).dictionary,
        ...(await import('@zxcvbn-ts/language-pl')).dictionary,
        ...(await import('@zxcvbn-ts/language-cs')).dictionary,
        ...(await import('@zxcvbn-ts/language-id')).dictionary,
        ...(await import('@zxcvbn-ts/language-ar')).dictionary,
    },
};
zxcvbnTscore.zxcvbnOptions.setOptions(options);

function get_password_strength(password: string) {
    return zxcvbnTscore.zxcvbn(password);
}

// @ts-ignore
window.get_password_strength = get_password_strength;
