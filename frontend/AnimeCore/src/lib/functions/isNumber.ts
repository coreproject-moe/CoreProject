export function isNumber(n: string | undefined) {
    return /^-?[\d.]+(?:e-?\d+)?$/.test(n ?? "");
}
