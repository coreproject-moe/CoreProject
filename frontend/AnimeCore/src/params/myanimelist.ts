import type { ParamMatcher } from "@sveltejs/kit";

export const match: ParamMatcher = function (param) {
    return /^mal|myanimelist+$/gm.test(param);
};
