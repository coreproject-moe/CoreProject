import svelteRetag from "svelte-retag";
import { Newable } from "svelte-retag";

export function register({ component, tagname }: { component: Newable; tagname: string }) {
    svelteRetag({
        component: component,
        tagname: tagname,

        shadow: false,
        hydratable: false
    });
}
