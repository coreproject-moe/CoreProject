export function autofocus(node: HTMLElement) {
    const input_first_el: HTMLInputElement | null = node.querySelector("input:not([disabled])");
    if (!input_first_el) return;

    input_first_el.focus();
};