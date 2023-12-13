/**
 * @author yorris
 *  @see https://gist.github.com/yoriiis/3bfd3833d5aaaa454c682f782b1e3a23
 */
export function get_transition_duration_as_ms({ element, ms = false }: { element: HTMLElement; ms?: boolean }) {
    return parseFloat(window.getComputedStyle(element).transitionDuration) * (ms ? 1000 : 1);
}
