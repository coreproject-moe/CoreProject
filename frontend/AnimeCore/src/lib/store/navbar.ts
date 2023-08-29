import { page } from "$app/stores";
import { derived } from "svelte/store";

type ILogo = "logo" | "form";

function get_logo_variant(pathname: string): ILogo {
    let logo_type: ILogo;

    if (pathname.match(/user/gm)) {
        logo_type = "logo";
    } else {
        logo_type = "form";
    }

    return logo_type;
}

export const navbar_middle_section_variant = derived(page, ($page) => get_logo_variant($page.url.pathname));
