export function vw(vw: number) {
    return (vw * globalThis.window?.innerWidth) / 100;
}
